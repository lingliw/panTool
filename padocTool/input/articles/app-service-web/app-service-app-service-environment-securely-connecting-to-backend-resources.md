<!-- not suitable for Mooncake -->

<properties 
	pageTitle="Securely Connecting to BackEnd Resources from an Azure Websites Environment" 
	description="Learn about how to securely connect to backend resources from an Azure Websites Environment." 
	services="app-service" 
	documentationCenter="" 
	authors="ccompy" 
	manager="wpickett" 
	editor=""/>

<tags
	ms.service="app-service"
	ms.date="09/11/2015"
	wacn.date=""/>	

# Securely Connecting to Backend Resources from an Azure Websites Environment #

## Overview ##
Since an Azure Websites Environment is always created in a subnet of a regional classic "v1" [virtual network][virtualnetwork], outbound connections from an Azure Websites Environment to other backend resources can flow exclusively over the virtual network.  

**Note:**  An Azure Websites Environment cannot be created in a "v2" virtual network.

For example, there may be a SQL Server running on a cluster of virtual machines with port 1433 locked down.  The endpoint may be ACLd to only allow access from other resources on the same virtual network.  

As another example, sensitive endpoints may run on-premises and be connected to Azure via either [Site-to-Site][SiteToSite] or [Azure ExpressRoute][ExpressRoute] connections.  As a result, only resources in virtual networks connected to the Site-to-Site or ExpressRoute tunnels will be able to access on-premises endpoints.

For all of these scenarios, apps running on an Azure Websites Environment will be able to securely connect to the various servers and resources.  Outbound traffic from apps running in an Azure Websites Environment to private endpoints in the same virtual network (or connected to the same virtual network), will only flow over the virtual network.  Outbound traffic to private endpoints will not flow over the public Internet.

[AZURE.INCLUDE [app-service-web-to-api-and-mobile](../includes/app-service-web-to-api-and-mobile.md)] 

## Outbound Connectivity and DNS Requirements ##
Note that for an Azure Websites Environment to function properly, it requires outbound access to Azure Storage worldwide, as well as connectivity to Sql Database in the same Azure region.  If outbound Internet access is blocked in the virtual network, Azure Websites Environments will not be able to access these Azure endpoints.

Customer may also have custom DNS servers configured in the virtual network.  Azure Websites Environments need to be able to resolve Azure endpoints under *.database.chinacloudapi.cn, *.file.core.chinacloudapi.cn and *.blob.core.chinacloudapi.cn.  

It is also recommended that any custom DNS servers on the virtual network be setup ahead of time prior to creating an Azure Websites Environment.  If a virtual network's DNS configuration is changed while an Azure Websites Environment is being created, that will result in the Azure Websites Environment creation process failing.  If a custom DNS server exists on the other end of a VPN gateway, and the DNS server is unreachable or unavailable, the Azure Websites Environment creation process will also fail. 

## Connecting to a SQL Server
A common SQL Server configuration has an endpoint listening on port 1433:

![SQL Server Endpoint][SqlServerEndpoint]

There are two approaches for restricting traffic to this endpoint:


- [Network Access Control Lists][NetworkAccessControlLists] (Network ACLs)

- [Network Security Groups][NetworkSecurityGroups]


## Restricting Access With a Network ACL

Port 1433 can be secured using a network access control list.  The example below whitelists client addresses originating from inside of a virtual network, and blocks access to all other clients.

![Network Access Control List Example][NetworkAccessControlListExample]

Any applications running in Azure Websites Environment in the same virtual network as the SQL Server will be able to connect to the SQL Server instance using the **VNet internal** IP address for the SQL Server virtual machine.  

The example connection string below references the SQL Server using its private IP address.

    Server=tcp:10.0.1.6;Database=MyDatabase;User ID=MyUser;Password=PasswordHere;provider=System.Data.SqlClient

Although the virtual machine has a public endpoint as well, connection attempts using the public IP address will be rejected because of the network ACL. 

## Restricting Access With a Network Security Group
An alternative approach for securing access is with a network security group.  Network security groups can be applied to individual virtual machines, or to a subnet containing virtual machines.

First a network security group needs to be created:

    New-AzureNetworkSecurityGroup -Name "testNSGexample" -Location "China East" -Label "Example network security group for an app service environment"

Restricting access to only VNet internal traffic is very simple with a network security group.  The default rules in a network security group only allow access from other network clients in the same virtual network.

As a result locking down access to SQL Server is as simple as applying a network security group with its default rules to either the virtual machines running SQL Server, or the subnet containing the virtual machines.

The sample below applies a network security group to the containing subnet:

    Get-AzureNetworkSecurityGroup -Name "testNSGExample" | Set-AzureNetworkSecurityGroupToSubnet -VirtualNetworkName 'testVNet' -SubnetName 'Subnet-1'
    
The end result is a set of security rules that block external access, while allowing VNet internal access:

![Default Network Security Rules][DefaultNetworkSecurityRules]


## Getting started

To get started with Azure Websites Environments, see [Introduction to Azure Websites Environment][IntroToAppServiceEnvironment]

For details around controlling inbound traffic to your Azure Websites Environment, see [Controlling inbound traffic to an Azure Websites Environment][ControlInboundASE]

For more information about the Azure Websites platform, see [Azure Websites][AzureAppService].

[AZURE.INCLUDE [app-service-web-whats-changed](../includes/app-service-web-whats-changed.md)]

[AZURE.INCLUDE [app-service-web-try-app-service](../includes/app-service-web-try-app-service.md)]
 

<!-- LINKS -->
[virtualnetwork]: /documentation/articles/virtual-networks-faq/
[ControlInboundTraffic]:  /documentation/articles/app-service-app-service-environment-control-inbound-traffic/
[SiteToSite]: /documentation/articles/vpn-gateway-site-to-site-create/
[ExpressRoute]: http://azure.microsoft.com/services/expressroute/
[NetworkAccessControlLists]: /documentation/articles/virtual-networks-acl/
[NetworkSecurityGroups]: /documentation/articles/virtual-networks-nsg/
[IntroToAppServiceEnvironment]:  /documentation/articles/app-service-app-service-environment-intro/
[AzureAppService]: /documentation/articles/app-service-value-prop-what-is/ 
[ControlInboundASE]:  /documentation/articles/app-service-app-service-environment-control-inbound-traffic/ 

<!-- IMAGES -->
[SqlServerEndpoint]: ./media/app-service-app-service-environment-securely-connecting-to-backend-resources/SqlServerEndpoint01.png
[NetworkAccessControlListExample]: ./media/app-service-app-service-environment-securely-connecting-to-backend-resources/NetworkAcl01.png
[DefaultNetworkSecurityRules]: ./media/app-service-app-service-environment-securely-connecting-to-backend-resources/DefaultNetworkSecurityRules01.png 
