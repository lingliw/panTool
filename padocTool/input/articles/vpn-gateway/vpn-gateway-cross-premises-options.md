<properties 
   pageTitle="About secure cross-premises connectivity for virtual networks | Azure"
   description="Learn about the types of secure cross-premises connections for virtual networks, including Site-to-Site, Point-to-Site, and ExpressRoute connections."
   services="vpn-gateway"
   documentationCenter="na"
   authors="cherylmc"
   manager="carmonm"
   editor="" />
<tags
	ms.service="vpn-gateway"
	ms.date="05/16/2016"
	wacn.date=""/>

# About secure cross-premises connectivity for virtual networks

This article discusses the different ways you can connect your on-premises site to an Azure virtual network. This article applies to both the Resource Manager and classic deployment models. If you are looking for VPN Gateway connection diagrams, see [Azure VPN Gateway connection topolgies](/documentation/articles/vpn-gateway-topology/).

There are three connection options available: Site-to-Site, Point-to-Site, and ExpressRoute. The option you choose can depend on a variety of considerations, such as:


- What kind of throughput does your solution require?
- Do you want to communicate over the public Internet via secure VPN, or over a private connection?
- Do you have a public IP address available to use?
- Are you planning to use a VPN device? If so, is it compatible?
- Are you connecting just a few computers, or do you want a persistent connection for your site?
- What type of VPN gateway is required for the solution you want to create?

The table below can help you decide the best connectivity option for your solution.

|                              | **Point-to-Site**                                                                            | **Site-to-Site**                                                                                        | **ExpressRoute**                                                                                                                     |
|------------------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **Azure Supported Services** | Cloud Services and Virtual Machines                                                          | Cloud Services and Virtual Machines                                                                     | [Services list](/documentation/articles/expressroute-faqs/#supported-services)                                                       |
| **Typical Bandwidths**       | Typically < 100 Mbps aggregate                                                               | Typically < 100 Mbps aggregate                                                                          | 50 Mbps, 100 Mbps, 200 Mbps, 500 Mbps, 1 Gbps, 2 Gbps, 5 Gbps, 10 Gbps                                                               |
| **Protocols Supported**      | Secure Sockets Tunneling Protocol (SSTP)                                                     | IPsec                                                | Direct connection over VLANs, NSP's VPN technologies (MPLS, VPLS,...)                                                                                                    |
| **Routing**                  | Route-based (dynamic)                                                                        | We support policy-based (static routing) and route-based (dynamic routing VPN)                 | BGP                                                                                                                                  |
| **Connection resiliency**    | active-passive                                                                               | active-passive                                                                                          | active-active                                                                                                                        |
| **Typical use case**         | Prototyping, dev / test / lab scenarios for cloud services and virtual machines              | Dev / test / lab scenarios and small scale production workloads for cloud services and virtual machines | Access to all Azure services (validated list), Enterprise-class and mission critical workloads, Backup, Big Data, Azure as a DR site |
| **SLA**                      | [SLA](/support/legal/sla)                                        | [SLA](/support/legal/sla)                                                   | [SLA](/support/legal/sla)                                                                                |
| **Pricing**                  | [Pricing](/home/features/vpn-gateway/pricing/)                           | [Pricing](/home/features/vpn-gateway/pricing/)                                      | [Pricing](/home/features/expressroute/pricing/)                                                                   |
| **Technical Documentation**  | [VPN Gateway Documentation](/documentation/services/vpn-gateway/) | [VPN Gateway Documentation](/documentation/services/vpn-gateway/)            | [ExpressRoute Documentation](/documentation/services/expressroute/)                                        |
| **FAQ**                     | [VPN Gateway FAQ](/documentation/articles/vpn-gateway-vpn-faq/)                                                    | [VPN Gateway FAQ](/documentation/articles/vpn-gateway-vpn-faq/)                                                               | [ExpressRoute FAQ](/documentation/articles/expressroute-faqs/)                                                                             |
                                                                    

## Site-to-Site connections

A Site-to-Site VPN allows you to create a secure connection between your on-premises site and your virtual network. To create a Site-to-Site connection, a VPN device that is located on your on-premises network is configured to create a secure connection with the Azure VPN Gateway. Once the connection is created, resources on your local network and resources located in your virtual network can communicate directly and securely. Site-to-Site connections do not require you to establish a separate connection for each client computer on your local network to access resources in the virtual network.

**Use a Site-to-Site connection when:**

- You want to create a hybrid solution.
- You want a connection between your on-premises location and your virtual network without requiring client-side configurations.
- You want a connection that is persistent. 

**Requirements**

- The on-premises VPN device must have an Internet-facing IPv4 IP address. This cannot be behind a NAT.
- You must have VPN device that is compatible. See [About VPN Devices](/documentation/articles/vpn-gateway-about-vpn-devices/). 
- The VPN device you use must be compatible with the gateway type that is required for your solution. See [About VPN Gateway](/documentation/articles/vpn-gateway-about-vpngateways/).
- The Gateway SKU will also impact aggregate throughput. See [Gateway SKUs](/documentation/articles/vpn-gateway-about-vpngateways/#gwsku) for more information. 

**Available deployment models and methods for S2S**

|  | **Classic Deployment**  | **Resource Manager Deployment** |
|----------------------------------------|--------------|----------------------|
| **Classic Management Portal**                     |[Article*](/documentation/articles/vpn-gateway-site-to-site-create/) |  Not Supported |
| **Azure Portal Preview**                       | Supported               | [Article](/documentation/articles/vpn-gateway-howto-site-to-site-resource-manager-portal/)|
| **PowerShell**               |[Article+](/documentation/articles/vpn-gateway-multi-site/)          | [Article](/documentation/articles/vpn-gateway-create-site-to-site-rm-powershell/)| 

(*) denotes that the Classic Management Portal can only support creating one S2S VPN connection.

(+) denotes that this article is written for multi-site connections.
 


## Point-to-Site connections

A Point-to-Site VPN also allows you to create a secure connection to your virtual network. In a Point-to-Site configuration, the connection is configured individually on each client computer that you want to connect to the virtual network. Point-to-Site connections do not require a VPN device. This type of connection uses a VPN client that you install on each client computer. The VPN is established by manually starting the connection from the on-premises client computer.

Point-to-Site and Site-to-Site configurations can exist concurrently, but unlike Site-to-Site connections, Point-to-Site connections cannot be configured concurrently with an ExpressRoute connection to the same virtual network.

**Use a Point-to-Site connection when:**

- You only want to configure a few clients to connect to a virtual network.

- You want to connect to your virtual network from a remote location. For example, connecting from a coffee shop or a conference venue.

- You have a Site-to-Site connection, but have some clients that need to connect from a remote location.

- You do not have access to a VPN device that meets the minimum requirements for a Site-to-Site connection.

- You do not have an Internet facing IPv4 IP address for your VPN device.

**Available deployment models and methods for P2S**

|  | **Classic Deployment**  |  **Resource Manager Deployment**  |
|----------------------------------------|--------------|------------------------|
| **Classic Management Portal** | [Article](/documentation/articles/vpn-gateway-point-to-site-create/) | Not Supported |
| **Azure Portal Preview** |  Not Supported  |  Not Supported  |
| **PowerShell** | Supported | [Article](/documentation/articles/vpn-gateway-howto-point-to-site-rm-ps/)|


 

## ExpressRoute connections

Azure ExpressRoute lets you create private connections between Azure datacenters and infrastructure that's on your premises or in a co-location environment. ExpressRoute connections do not go over the public Internet and offer more reliability, faster speeds, lower latencies and higher security than typical connections over the Internet.

In some cases, using ExpressRoute connections to transfer data between on-premises and Azure can also yield significant cost benefits. With ExpressRoute, you can establish connections to Azure at an ExpressRoute location (Exchange Provider facility) or directly connect to Azure from your existing WAN network (such as a MPLS VPN) provided by a network service provider.

For more information about ExpressRoute, see the ExpressRoute [Technical Overview](/documentation/articles/expressroute-introduction/).


## Next steps

- For more information about VPN Gateway, see [About VPN Gateway](/documentation/articles/vpn-gateway-about-vpngateways/), the 
VPN Gateway [FAQ](/documentation/articles/vpn-gateway-vpn-faq/), and the [Planning and Design](/documentation/articles/vpn-gateway-plan-design/) articles.

- For more information about ExpressRoute, see the ExpressRoute [Technical Overview](/documentation/articles/expressroute-introduction/), the [FAQ](/documentation/articles/expressroute-faqs/), and [Workflows](/documentation/articles/expressroute-workflows/).




