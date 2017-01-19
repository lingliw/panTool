<!-- to be customized -->

<properties 
   pageTitle="What is a Network Security Group (NSG)"
   description="Learn about Network Security Groups (NSG)"
   services="virtual-network"
   documentationCenter="na"
   authors="telmosampaio"
   manager="carmonm"
   editor="tysonn" />
<tags
	ms.service="virtual-network"
	ms.date="02/11/2016"
	wacn.date=""/>

# What is a Network Security Group (NSG)?

Network security group (NSG) contains a list of Access Control List (ACL) rules that allow or deny network traffic to your VM instances in a Virtual Network. NSGs can be associated with either subnets or individual VM instances within that subnet. When a NSG is associated with a subnet, the ACL rules apply to all the VM instances in that subnet. In addition, traffic to an individual VM can be restricted further by associating a NSG directly to that VM.

## NSG resource

NSGs contain the following properties.

|Property|Description|Constraints|Considerations|
|---|---|---|---|
|Name|Name for the NSG|Must be unique within the region<br/>Can contain letters, numbers, underscores, periods and hyphens<br/>Must start with a letter or number<br/>Must end with a letter, number, or underscore<br/>Can have up to 80 characters|Since you may need to create several NSGs, make sure you have a naming convention that makes it easy to identify the function of your NSGs|
|Rules|Rules that define what traffic is allowed, or denied||See [NSG rules](#Nsg-rules) below| 

>[AZURE.NOTE] Endpoint-based ACLs and network security groups are not supported on the same VM instance. If you want to use an NSG and have an endpoint ACL already in place, first remove the endpoint ACL. For information about how to do this, see [Managing Access Control Lists (ACLs) for Endpoints by using PowerShell](/documentation/articles/virtual-networks-acl-powershell).

### NSG rules

NSG rules contain the following properties.

|Property|Description|Constraints|Considerations|
|---|---|---|---|
|**Name**|Name for the rule|Must be unique within the region<br/>Can contain letters, numbers, underscores, periods and hyphens<br/>Must start with a letter or number<br/>Must end with a letter, number, or underscore<br/>Can have up to 80 characters|You may have several rules within an NSG, so make sure you follow a naming convention that allows you to identify the function of your rule|
|**Protocol**|Protocol to match for the rule|TCP, UDP, or \*|Using \* as a protocol includes ICMP (East-West traffic only), as well as UDP and TCP and may reduce the number of rules you need<br/>At the same time, using \* might be too broad an approach, so make sure you only use when really necessary|
|**Source port range**|Source port range to match for the rule|Single port number from 1 to 65535, port range (i.e. 100-2000), or \* (for all ports)|Try to use port ranges as much as possible to avoid the need for multiple rules|
|**Destination port range**|Destination port range to match for the rule|Single port number from 1 to 65535, port range (i.e. 100-2000), or \* (for all ports)|Try to use port ranges as much as possible to avoid the need for multiple rules|
|**Source address prefix**|Source address prefix or tag to match for the rule|Single IP address (i.e. 10.10.10.10), IP subnet (i.e. 192.168.1.0/24), [default tag](#Default-Tags), or * (for all addresses)|Consider using ranges, tags, and * to reduce the number of rules|
|**Destination address prefix**|Destination address prefix or tag to match for the rule|single IP address (i.e. 10.10.10.10), IP subnet (i.e. 192.168.1.0/24), [default tag](#Default-Tags), or * (for all addresses)|Consider using ranges, tags, and * to reduce the number of rules|
|**Direction**|Direction of traffic to match for the rule|inbound or outbound|Inbound and outbound rules are processed separately, based on direction|
|**Priority**|Rules are checked in the order of priority, once a rule applies, no more rules are tested for matching|Number between 100 and 65535|Consider creating rules jumping priorities by 100 for each rule, to leave space for new rules to come between existing rules|
|**Access**|Type of access to apply if the rule matches|allow or deny|Keep in mind that if an allow rule is not found for a packet, the packet is dropped|

NSGs contain two sets of rules: inbound and outbound. The priority for a rule must be unique within each set. 

![NSG rule processing](./media/virtual-network-nsg-overview/figure3.png) 

The figure above shows how NSG rules are processed.

### Default Tags

Default tags are system-provided identifiers to address a category of IP addresses. You can use default tags in the **source address prefix** and **destination address prefix** properties of any rule. There are three default tags you can use.

- **VIRTUAL_NETWORK:** This default tag denotes all of your network address space. It includes the virtual network address space (CIDR ranges defined in Azure) as well as all connected on-premises address spaces and connected Azure VNets (local networks).

- **AZURE_LOADBALANCER:** This default tag denotes Azure's Infrastructure load balancer. This will translate to an Azure datacenter IP where Azure's health probes originate.

- **INTERNET:** This default tag denotes the IP address space that is outside the virtual network and reachable by public Internet. This range includes [Azure owned public IP space](https://www.microsoft.com/download/details.aspx?id=41653) as well.

### Default Rules

All NSGs contain a set of default rules. The default rules cannot be deleted, but because they are assigned the lowest priority, they can be overridden by the rules that you create. 

As illustrated by the default rules below, traffic originating and ending in a VNet is allowed both in Inbound and Outbound directions. While connectivity to the Internet is allowed for Outbound direction, it is by default blocked for Inbound direction. There is a default rule to allow Azure's load balancer to probe the health of your VMs and role instances. You can override this rule if you are not using a load balanced set.

**Inbound default rules**

| Name                              | Priority | Source IP          | Source Port | Destination IP  | Destination Port | Protocol | Access |
|-----------------------------------|----------|--------------------|-------------|-----------------|------------------|----------|--------|
| ALLOW VNET INBOUND                | 65000    | VIRTUAL_NETWORK    | *           | VIRTUAL_NETWORK | *                | *        | ALLOW  |
| ALLOW AZURE LOAD BALANCER INBOUND | 65001    | AZURE_LOADBALANCER | *           | *               | *                | *        | ALLOW  |
| DENY ALL INBOUND                  | 65500    | *                  | *           | *               | *                | *        | DENY   |

**Outbound default rules**

| Name                    | Priority | Source IP       | Source Port | Destination IP  | Destination Port | Protocol | Access |
|-------------------------|----------|-----------------|-------------|-----------------|------------------|----------|--------|
| ALLOW VNET OUTBOUND     | 65000    | VIRTUAL_NETWORK | *           | VIRTUAL_NETWORK | *                | *        | ALLOW  |
| ALLOW INTERNET OUTBOUND | 65001    | *               | *           | INTERNET        | *                | *        | ALLOW  |
| DENY ALL OUTBOUND       | 65500    | *               | *           | *               | *                | *        | DENY   |

## Associating NSGs

You can associate an NSG to VMs, and subnets, depending on the deployment model you are using.

> [AZURE.NOTE] Azure has two different deployment models for creating and working with resources:  [Resource Manager and classic](/documentation/articles/resource-manager-deployment-model). This article covers using both models, but Microsoft recommends that most new deployments use the Resource Manager model. However, In Windows Azure China, Virtual Machines, Storage, and Virtual Network are not manageable with ARM.
 
- **Associating an NSG to a VM (classic deployments only).** When you associate an NSG to a VM, the network access rules in the NSG are applied to all traffic that destined and leaving the VM. 

- **Associating an NSG to a subnet (all deployments)**. When you associate an NSG to a subnet, the network access rules in the NSG are applied to all the IaaS and PaaS resources in the subnet. 

You can associate different NSGs to a VM and the subnet that a VM is bound to. When that happens, all network access rules are applied to the traffic in the following order:

- **Inbound traffic**
	1. NSG applied to subnet.
	2. NSG applied to VM (classic).
- **Outbound traffic**
	1. NSG applied to VM (classic).
	2. NSG applied to subnet.

![NSG ACLs](./media/virtual-network-nsg-overview/figure2.png)

>[AZURE.NOTE] Although you can only associate a single NSG to a subnet, VM; you can associate the same NSG to as many resources as you want.

## Implementation
You can implement NSGs in the classic using the different tools listed below.

|Deployment tool|Classic|
|---|---|---|
|Management Portal|![No][red]|
|PowerShell|<a href="/documentation/articles/virtual-networks-create-nsg-classic-ps">![Yes][green]</a>|
|Azure CLI|<a href="/documentation/articles/virtual-networks-create-nsg-classic-cli">![Yes][green]</a>|

|**Key**|![Yes][green] Supported. Click for article.|![No][red] Not Supported.|
|---|---|---|

## Planning

Before implementing NSGs, you need to answer the questions below:	

1. What types of resources do you want to filter traffic to or from (VM, VMs or other resources such as cloud services or application service environments connected to the same subnet, or between resources connected to different subnets)?

2. Are the resources you want to filter traffic to/from connected to subnets in existing VNets or will they be connected to new VNets or subnets?
 
For more information on planning for network security in Azure, read the [best practices for cloud services and network security](/documentation/articles/best-practices-network-security). 

## Design considerations

Once you know the answers to the questions in the [Planning](#Planning) section, review the following before defining your NSGs.

### Limits

You need to consider the following limits when designing your NSGs.

|**Description**|**Default Limit**|**Implications**|
|---|---|---|
|Number of NSGs you can associate to a subnet, VM|1|This means you cannot combine NSGs. Ensure all the rules needed for a given set of resources are included in a single NSG.|
|NSGs per region per subscription|100|By default, a new NSG is created for each VM you create in the Azure Management Portal. If you allow this default behavior, you will run out of NSGs quickly. Make sure you keep this limit in mind during your design, and separate your resources into multiple regions or subscriptions if necessary. |
|NSG rules per NSG|200|Use a broad range of IP and ports to ensure you do not go over this limit. |

>[AZURE.IMPORTANT] Make sure you view all the [limits related to networking services in Azure](/documentation/articles/azure-subscription-service-limits#networking-limits) before designing your solution. Some limits can be increased by opening a support ticket.

### VNet and subnet design

Since NSGs can be applied to subnets, you can minimize the number of NSGs by grouping your resources by subnet, and applying NSGs to subnets.  If you decide to apply NSGs to subnets, you may find that existing VNets and subnets you have were not defined with NSGs in mind. You may need to define new VNets and subnets to support your NSG design. And deploy your new resources to your new subnets. You could then define a migration strategy to move existing resources to the new subnets. 

### Special rules

You need to take into account the special rules listed below. Make sure you do not block traffic allowed by those rules, otherwise your infrastructure will not be able to communicate with essential Azure services.

- **Virtual IP of the Host Node:** Basic infrastructure services such as DHCP, DNS, and Health monitoring are provided through the virtualized host IP address 168.63.129.16. This public IP address belongs to Microsoft and will be the only virtualized IP address used in all regions for this purpose. This IP address maps to the physical IP address of the server machine (host node) hosting the virtual machine. The host node acts as the DHCP relay, the DNS recursive resolver, and the probe source for the load balancer health probe and the machine health probe. Communication to this IP address should not be considered as an attack.

- **Licensing (Key Management Service):** Windows images running in the virtual machines should be licensed. To do this, a licensing request is sent to the Key Management Service host servers that handle such queries. This will always be on outbound port 1688.

### ICMP traffic

The current NSG rules only allow for protocols *TCP* or *UDP*. There is not a specific tag for *ICMP*. However, ICMP traffic is allowed within a Virtual Network by default through the Inbound VNet rules that allow traffic from/to any port and protocol within the VNet.

### Subnets

- Consider the number of tiers your workload requires. Each tier can be isolated by using a subnet, with an NSG applied to the subnet. 
- If you need to implement a subnet for a VPN gateway, or ExpressRoute circuit, make sure you do **NOT** apply an NSG to that subnet. If you do so, your cross VNet or cross premises connectivity will not work.
- If you need to implement a virtual appliance, make sure you deploy the virtual appliance on its own subnet, so that your User Defined Routes (UDRs) can work correctly. You can implement a subnet level NSG to filter traffic in and out of this subnet. Learn more about [how to control traffic flow and use virtual appliances](/documentation/articles/virtual-networks-udr-overview).

### Other

- Endpoint-based ACLs and NSGs are not supported on the same VM instance. If you want to use an NSG and have an endpoint ACL already in place, first remove the endpoint ACL. For information about how to do this, see [Manage endpoint ACLs](/documentation/articles/virtual-networks-acl-powershell).
- Similar to the use of load balancers, when filtering traffic from other VNets, you must use the source address range of the remote computer, not the gateway connecting the VNets.
- Many Azure services cannot be connected to Azure Virtual Networks and therefore, traffic to and from them cannot be filtered with NSGs.  Read the documentation for the services you use to determine whether or not they can be connected to VNets.

## Sample deployment

To illustrate the application of the information in this article, we'll define NSGs to filter network traffic for a two tier workload solution with the following requirements:

1. Separation of traffic between front end (Windows web servers) and back end (SQL database servers).
2. Load balancing rules forwarding traffic to the load balancer to all web servers on port 80.
3. NAT rules forwarding traffic coming in port 50001 on load balancer to port 3389 on only one VM in the front end.
4. No access to the front end or back end VMs from the Internet, with exception of requirement number 1.
5. No access from the front end or back end to the Internet.
6. Access to port 3389 to any web server in the front end, for traffic coming from the front end subnet itself.
7. Access to port 3389 to all SQL Server VMs in the back end from the front end subnet only.
8. Access to port 1433 to all SQL Server VMs in the back end from the front end subnet only.

![NSGs](./media/virtual-network-nsg-overview/figure1.png)

As seen in the diagram above, the *Web1* and *Web2* VMs are connected to the *FrontEnd* subnet, and the *DB1* and *DB2* VMs are connected to the *BackEnd* subnet.  Both subnets are part of the *TestVNet* VNet. All resources are assigned to the *China North* Azure region.

Requirements 1-6 (with exception of 3) above are all confined to subnet spaces. To minimize the number of rules required for each NSG, and to make it easy to add additional VMs to the subnets running the same workload types as the existing VMs, we can implement the following subnet level NSGs.

### NSG for FrontEnd subnet

**Incoming rules**

|Rule|Access|Priority|Source address range|Source port|Destination address range|Destination port|Protocol|
|---|---|---|---|---|---|---|---|
|allow HTTP|Allow|100|INTERNET|\*|\*|80|TCP|
|allow RDP from FrontEnd|Allow|200|192.168.1.0/24|\*|\*|3389|TCP|
|deny anything from Internet|Deny|300|INTERNET|\*|\*|\*|TCP|

**Outgoing rules**

|Rule|Access|Priority|Source address range|Source port|Destination address range|Destination port|Protocol|
|---|---|---|---|---|---|---|---|
|deny Internet|Deny|100|\*|\*|INTERNET|\*|\*|

### NSG for BackEnd subnet

**Incoming rules**

|Rule|Access|Priority|Source address range|Source port|Destination address range|Destination port|Protocol|
|---|---|---|---|---|---|---|---|
|deny Internet|Deny|100|INTERNET|\*|\*|\*|\*|

**Outgoing rules**

|Rule|Access|Priority|Source address range|Source port|Destination address range|Destination port|Protocol|
|---|---|---|---|---|---|---|---|
|deny Internet|Deny|100|\*|\*|INTERNET|\*|\*|

### NSG for single VM in FrontEnd for RDP from Internet

**Incoming rules**

|Rule|Access|Priority|Source address range|Source port|Destination address range|Destination port|Protocol|
|---|---|---|---|---|---|---|---|
|allow RDP from Internet|Allow|100|INTERNET|*|\*|3389|TCP|

>[AZURE.NOTE] Notice how the source address range for this rule is **Internet**, and not the VIP for the load balancer; the source port is **\***, not 500001. Do not get confused between NAT rules/load balancing rules and NSG rules. The NSG rules are always related to the original source and final destination of traffic, **NOT** the load balancer between the two. 

## Next steps

- [Deploy NSGs in the classic deployment model](/documentation/articles/virtual-networks-create-nsg-classic-ps).
- [Manage NSG logs](/documentation/articles/virtual-network-nsg-manage-log).

[green]: ./media/virtual-network-nsg-overview/green.png
[yellow]: ./media/virtual-network-nsg-overview/yellow.png
[red]: ./media/virtual-network-nsg-overview/red.png