<properties 
   pageTitle="About VPN Gateway settings for virtual network gateways| Azure"
   description="Learn about VPN Gateway settings for Azure Virtual Network."
   services="vpn-gateway"
   documentationCenter="na"
   authors="cherylmc"
   manager="carmonm"
   editor=""
   tags="azure-resource-manager,azure-service-management"/>
<tags 
   ms.service="vpn-gateway"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="infrastructure-services"
   ms.date="10/06/2016"
   wacn.date=""
   ms.author="cherylmc" />

# About VPN Gateway settings

A VPN gateway connection solution relies on the configuration of multiple resources in order to send network traffic between virtual networks and on-premises locations. Each resource contains configurable settings. The combination of the resources and settings determines the connection outcome.

The sections in this article discuss the resources and settings that relate to a VPN gateway in the **Resource Manager** deployment model. You may find it helpful to view the available configurations by using connection topology diagrams. You can find the descriptions and topology diagrams for each connection solution in the [About VPN Gateway](/documentation/articles/vpn-gateway-about-vpngateways/) article. 

## <a name="gwtype"></a>Gateway types

Each virtual network can only have one virtual network gateway of each type. When you are creating a virtual network gateway, you must make sure that the gateway type is correct for your configuration.

The available values for -GatewayType are: 

- Vpn
- ExpressRoute

A VPN gateway requires the `-GatewayType` *Vpn*.  

Example:

	New-AzureRmVirtualNetworkGateway -Name vnetgw1 -ResourceGroupName testrg `
	-Location 'China North' -IpConfigurations $gwipconfig -GatewayType Vpn `
	-VpnType RouteBased
 

## <a name="gwsku"></a>Gateway SKUs


When you create a virtual network gateway, you need to specify the gateway SKU that you want to use. When you select a higher gateway SKU, more CPUs and network bandwidth are allocated to the gateway, and as a result, the gateway can support higher network throughput to the virtual network.

VPN Gateway can use the following SKUs:

- Basic
- Standard
- HighPerformance

When selecting a SKU, consider the following limitations:

- If you want to use a PolicyBased VPN type, you must use the Basic gateway SKU. PolicyBased VPNs (previously called Static Routing) are not supported on any other SKU.
- BGP is not supported on the Basic SKU.
- ExpressRoute-VPN Gateway coexist configurations are not supported on the Basic SKU.


**Specifying the gateway SKU in the Azure portal Preview**

If you use the Azure portal Preview to create a Resource Manager virtual network gateway, you can select the gateway SKU by using the dropdown. The options you are presented with correspond to the Gateway type and VPN type that you select.

For example, if you select the gateway type 'VPN' and the VPN type 'Policy-based', you see only the 'Basic' SKU because that is the only SKU available for PolicyBased VPNs. If you select 'Route-based', you can select from Basic, Standard, and HighPerformance SKUs. 


**Specifying the gateway SKU using PowerShell**


The following PowerShell example specifies the `-GatewaySku` as *Standard*.

	New-AzureRmVirtualNetworkGateway -Name vnetgw1 -ResourceGroupName testrg `
	-Location 'China North' -IpConfigurations $gwipconfig -GatewaySku Standard `
	-GatewayType Vpn -VpnType RouteBased

**Changing a gateway SKU**

If you want to upgrade your gateway SKU to a more powerful SKU (from Basic/Standard to HighPerformance) you can use the `Resize-AzureRmVirtualNetworkGateway` PowerShell cmdlet. You can also downgrade the gateway SKU size using this cmdlet.

The following PowerShell example shows a gateway SKU being resized to HighPerformance.

	$gw = Get-AzureRmVirtualNetworkGateway -Name vnetgw1 -ResourceGroupName testrg
	Resize-AzureRmVirtualNetworkGateway -VirtualNetworkGateway $gw -GatewaySku HighPerformance

<br>
The following table shows the gateway types and the estimated aggregate throughput. This table applies to both the Resource Manager and classic deployment models.

|    | **VPN Gateway throughput (1)** | **VPN Gateway max IPsec tunnels (2)** | **ExpressRoute Gateway throughput** | **VPN Gateway and ExpressRoute coexist**|
|--- |----------------------------|-----------------------------------|-------------------------------------|-----------------------------------------|
| **Basic SKU (3)**              |  100 Mbps | 10                         |  500 Mbps                           | No   |
| **Standard SKU (4)**           |  100 Mbps | 10                         | 1000 Mbps                           | Yes  |
| **High Performance SKU (4)**   | 200 Mbps  | 30                         | 2000 Mbps                           | Yes  |

- (1) The VPN throughput is a rough estimate based on the measurements between VNets in the same Azure region. It is not a guaranteed throughput for cross-premises connections across the Internet. It is the maximum possible throughput measurement.
- (2) The number of tunnels refer to RouteBased VPNs. A PolicyBased VPN can only support one Site-to-Site VPN tunnel.
- (3) BGP is not supported for the Basic SKU.
- (4) PolicyBased VPNs are not supported for this SKU. They are supported for the Basic SKU only. 


## <a name="connectiontype"></a>Connection types

In the Resource Manager deployment model, each configuration requires a specific virtual network gateway connection type. The available Resource Manager PowerShell values for `-ConnectionType` are:

- IPsec
- Vnet2Vnet
- ExpressRoute
- VPNClient

In the following PowerShell example, we create a S2S connection that requires the connection type *IPsec*.

	New-AzureRmVirtualNetworkGatewayConnection -Name localtovon -ResourceGroupName testrg `
	-Location 'China North' -VirtualNetworkGateway1 $gateway1 -LocalNetworkGateway2 $local `
	-ConnectionType IPsec -RoutingWeight 10 -SharedKey 'abc123'


## <a name="vpntype"></a>VPN types

When you create the virtual network gateway for a VPN gateway configuration, you must specify a VPN type. The VPN type that you choose depends on the connection topology that you want to create. For example, a P2S connection requires a RouteBased VPN type. A VPN type can also depend on the hardware that you will be using. S2S configurations require a VPN device. Some VPN devices only support a certain VPN type.

The VPN type you select must satisfy all the connection requirements for the solution you want to create. For example, if you want to create a S2S VPN gateway connection and a P2S VPN gateway connection for the same virtual network, you would use VPN type *RouteBased* because P2S requires a RouteBased VPN type. You would also need to verify that your VPN device supported a RouteBased VPN connection. 

Once a virtual network gateway has been created, you can't change the VPN type. You have to delete the virtual network gateway and create a new one. 
There are two VPN types:

- **PolicyBased:** PolicyBased VPNs were previously called static routing gateways in the classic deployment model. Policy-based VPNs encrypt and direct packets through IPsec tunnels based on the IPsec policies configured with the combinations of address prefixes between your on-premises network and the Azure VNet. The policy (or traffic selector) is usually defined as an access list in the VPN device configuration. The value for a PolicyBased VPN type is *PolicyBased*. When using a PolicyBased VPN, keep in mind the following limitations:

	- PolicyBased VPNs can **only** be used on the Basic gateway SKU. This VPN type is not compatible with other gateway SKUs.
	- You can have only 1 tunnel when using a PolicyBased VPN.
	- You can only use PolicyBased VPNs for S2S connections, and only for certain configurations. Most VPN Gateway configurations require a RouteBased VPN.

- **RouteBased**: RouteBased VPNs were previously called dynamic routing gateways in the classic deployment model. RouteBased VPNs use "routes" in the IP forwarding or routing table to direct packets into their corresponding tunnel interfaces. The tunnel interfaces then encrypt or decrypt the packets in and out of the tunnels. The policy (or traffic selector) for RouteBased VPNs are configured as any-to-any (or wild cards). The value for a RouteBased VPN type is *RouteBased*.



The following PowerShell example specifies the `-VpnType` as *RouteBased*. When you are creating a gateway, you must make sure that the -VpnType is correct for your configuration. 

	New-AzureRmVirtualNetworkGateway -Name vnetgw1 -ResourceGroupName testrg `
	-Location 'China North' -IpConfigurations $gwipconfig `
	-GatewayType Vpn -VpnType RouteBased

##  <a name="requirements"></a>Gateway requirements

The following table lists the requirements for PolicyBased and RouteBased VPN gateways. This table applies to both the Resource Manager and classic deployment models. For the classic model, PolicyBased VPN gateways are the same as Static gateways, and Route-based gateways are the same as Dynamic gateways.


|   | **PolicyBased Basic VPN Gateway** | **RouteBased Basic VPN Gateway** | **RouteBased Standard VPN Gateway**   | **RouteBased High Performance VPN Gateway** |
|---|---------------------------------------|---------------------------------------|----------------------------|----------------------------------|
|    **Site-to-Site connectivity   (S2S)**  | PolicyBased VPN configuration        | RouteBased VPN configuration  | RouteBased VPN configuration     | RouteBased VPN configuration    |
| **Point-to-Site connectivity (P2S**)      | Not supported   | Supported (Can coexist with S2S)  | Supported (Can coexist with S2S)  | Supported (Can coexist with S2S) |
| **Authentication method**                 |    Pre-shared key  | Pre-shared key for S2S connectivity, Certificates for P2S connectivity | Pre-shared key for S2S connectivity, Certificates for P2S connectivity | Pre-shared key for S2S connectivity, Certificates for P2S connectivity |
| **Maximum number of S2S connections**       | 1                              | 10                                                                    | 10                                | 30                               |
| **Maximum number of P2S connections**       | Not supported                  | 128                                                                   | 128                               | 128                              |
|**Active routing support (BGP)**           | Not supported                  | Not supported                                                         | Supported                     | Supported                   |
 
 


## <a name="gwsub"></a>Gateway subnet

To configure a virtual network gateway, you first need to create a gateway subnet for your VNet. The gateway subnet must be named *GatewaySubnet* to work properly. This name lets Azure know that this subnet should be used for the gateway.

The minimum size of your gateway subnet depends entirely on the configuration that you want to create. Although it is possible to create a gateway subnet as small as /29, we recommend that you create a gateway subnet of /28 or larger (/28, /27, /26, etc.). 

Creating a larger gateway size prevents you from running up against gateway size limitations. For example, you may have created a virtual network gateway with a gateway subnet size /29 for a S2S connection. You now want to configure a S2S/ExpressRoute coexist configuration. That configuration requires a gateway subnet minimum size /28. To create your configuration, you would have to modify the gateway subnet to accommodate the minimum requirement for the connection, which is /28.

The following Resource Manager PowerShell example shows a gateway subnet named GatewaySubnet. You can see the CIDR notation specifies a /27, which allows for enough IP addresses for most configurations that currently exist.

	Add-AzureRmVirtualNetworkSubnetConfig -Name 'GatewaySubnet' -AddressPrefix 10.0.3.0/27

>[AZURE.IMPORTANT] When working with gateway subnets, avoid associating a network security group (NSG) to the gateway subnet. Associating a network security group to this subnet may cause your VPN gateway to stop functioning as expected. For more information about network security groups, see [What is a network security group?](/documentation/articles/virtual-networks-nsg/)


 


## <a name="lng"></a>Local network gateways

When creating a VPN gateway configuration, the local network gateway often represents your on-premises location. In the classic deployment model, the local network gateway was referred to as a Local Site. 

You give the local network gateway a name, the public IP address of the on-premises VPN device, and specify the address prefixes that are located on the on-premises location. Azure looks at the destination address prefixes for network traffic, consults the configuration that you have specified for your local network gateway, and routes packets accordingly. You also specify local network gateways for VNet-to-VNet configurations that use a VPN gateway connection.

The following PowerShell example creates a new local network gateway:

	New-AzureRmLocalNetworkGateway -Name LocalSite -ResourceGroupName testrg `
	-Location 'China North' -GatewayIpAddress '23.99.221.164' -AddressPrefix '10.5.51.0/24'

Sometimes you need to modify the local network gateway settings. For example, when you add or modify the address range, or if the IP address of the VPN device changes. For a classic VNet, you can change these settings in the Classic Management Portal on the Local Networks page. For Resource Manager, see [Modify local network gateway settings using PowerShell](/documentation/articles/vpn-gateway-modify-local-network-gateway/).

## <a name="resources"></a>REST APIs and PowerShell cmdlets

For additional technical resources and specific syntax requirements when using REST APIs and PowerShell cmdlets for VPN Gateway configurations, see the following pages:

|**Classic** | **Resource Manager**|
|-----|----|
|[PowerShell](https://msdn.microsoft.com/zh-cn/library/mt270335.aspx)|[PowerShell](https://msdn.microsoft.com/zh-cn/library/mt163510.aspx)|
|[REST API](https://msdn.microsoft.com/zh-cn/library/jj154113.aspx)|[REST API](https://msdn.microsoft.com/zh-cn/library/mt163859.aspx)|


## Next steps

See [About VPN Gateway](/documentation/articles/vpn-gateway-about-vpngateways/) for more information about available connection configurations. 







 
