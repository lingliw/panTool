<properties
   pageTitle="How to add multiple VPN gateway Site-to-Site connections to a virtual network for the Resource Manager deployment model using the Azure portal Preview | Azure"
   description="Add multi-site S2S connections to a VPN gateway that has an existing connection"
   services="vpn-gateway"
   documentationCenter="na"
   authors="cherylmc"
   manager="carmonm"
   editor=""
   tags="azure-resource-manager"/>

<tags
   ms.service="vpn-gateway"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="infrastructure-services"
   ms.date="10/10/2016"
   wacn.date=""
   ms.author="cherylmc"/>



# Add a Site-to-Site connection to a VNet with an existing VPN gateway connection

> [AZURE.SELECTOR]
- [Resource Manager - Portal](/documentation/articles/vpn-gateway-howto-multi-site-to-site-resource-manager-portal/)
- [Classic - PowerShell](/documentation/articles/vpn-gateway-multi-site/)

This article walks you through using the Azure portal Preview to add Site-to-Site (S2S) connections to a VPN gateway that has an existing connection. This type of connection is often referred to as a "multi-site" configuration. 

You can use this article to add a S2S connection to a VNet that already has a S2S connection, Point-to-Site connection, or VNet-to-VNet connection. There are some limitations when adding connections. Check the [Before you begin](#before) section in this article to verify before you start your configuration. 

This article applies to VNets created using the Resource Manager deployment model that have a RouteBased VPN gateway. These steps do not apply to ExpressRoute/Site-to-Site coexisting connection configurations. See [ExpressRoute/S2S coexisting connections](/documentation/articles/expressroute-howto-coexist-resource-manager/) for information about coexisting connections.

### Deployment models and methods

It's important to know that Azure currently works with two deployment models: Resource Manager and classic. Before you begin your configuration, make sure that you understand the deployment models and tools. You'll need to know which model that you want to work in. Not all networking features are supported yet for both models. For information about the deployment models, see [Understanding Resource Manager deployment and classic deployment](/documentation/articles/resource-manager-deployment-model/).
 

We update this table as new articles and additional tools become available for this configuration. When an article is available, we link directly to it from this table.

|**Deployment Model/Method**| **Azure Portal Preview** | **Classic Management Portal** | **PowerShell**|
|---|---|---|---|
| **Resource Manager**      |[Article](/documentation/articles/vpn-gateway-howto-multi-site-to-site-resource-manager-portal/)| Not Supported | Supported|
| **Classic** | Not Supported | Not Supported | [Article](/documentation/articles/vpn-gateway-multi-site/) | 
 


## <a name="before"></a>Before you begin

Verify the following items:

- You are not creating an ExpressRoute/S2S coexisting connection.
- You have a virtual network that was created using the Resource Manager deployment model with an existing connection.
- The virtual network gateway for your VNet is RouteBased. If you have a PolicyBased VPN gateway, you must delete the virtual network gateway and create a new VPN gateway as RoutBased.
- None of the address ranges overlap for any of the VNets that this VNet is connecting to.
- You have compatible VPN device and someone who is able to configure it. See [About VPN Devices](/documentation/articles/vpn-gateway-about-vpn-devices/). If you aren't familiar with configuring your VPN device, or are unfamiliar with the IP address ranges located in your on-premises network configuration, you need to coordinate with someone who can provide those details for you.
- You have an externally facing public IP address for your VPN device. This IP address cannot be located behind a NAT.


## <a name="part1"></a>Part 1 - Configure a connection

1. From a browser, navigate to the [Azure portal Preview](http://portal.azure.cn) and, if necessary, sign in with your Azure account.
2. Click **All resources** and locate your **virtual network gateway** from the list of resources and click it.
3. On the **Virtual network gateway** blade, click **Connections**.

	![Connections blade](./media/vpn-gateway-howto-multi-site-to-site-resource-manager-portal/connectionsblade.png "Connections blade")<br>

4. On the **Connections** blade, click **+Add**.

	![Add connection button](./media/vpn-gateway-howto-multi-site-to-site-resource-manager-portal/addbutton.png "Add connection button")<br>

5. On the **Add connection** blade, fill out the following fields:
	- **Name:** The name you want to give to the site you are creating the connection to.
	- **Connection type:** Select **Site-to-site (IPsec)**.

	![Add connection blade](./media/vpn-gateway-howto-multi-site-to-site-resource-manager-portal/addconnectionblade.png "Add connection blade")<br>

## <a name="part2"></a>Part 2 - Add a local network gateway

1. Click **Local network gateway** ***Choose a local network gateway***. This will open the **Choose local network gateway** blade.

	![Choose local network gateway](./media/vpn-gateway-howto-multi-site-to-site-resource-manager-portal/chooselng.png "Choose local network gateway")<br>
2. Click **Create new** to open the **Create local network gateway** blade.

	![Create local network gateway blade](./media/vpn-gateway-howto-multi-site-to-site-resource-manager-portal/createlngblade.png "Create local network gateway")<br>

3. On the **Create local network gateway** blade, fill out the following fields:
	- **Name:** The name you want to give to the local network gateway resource.
	- **IP address:** The public IP address of the VPN device on the site that you want to connect to.
	- **Address space:** The address space that you want to be routed to the new local network site.
4. Click **OK** on the **Create local network gateway** blade to save the changes.

## <a name="part3"></a>Part 3 - Add the shared key and create the connection

1. On the **Add connection** blade, add the shared key that you want to use to create your connection. You can either get the shared key from your VPN device, or make one up here and then configure your VPN device to use the same shared key. The important thing is that the keys are exactly the same.

	![Shared key](./media/vpn-gateway-howto-multi-site-to-site-resource-manager-portal/sharedkey.png "Shared key")<br>
2. At the bottom of the blade, click **OK** to create the connection.

## <a name="part4"></a>Part 4 - Verify the VPN connection

You can verify your VPN connection either in the portal, or by using PowerShell.

### To verify your connection by using PowerShell

You can verify that your connection succeeded by using the `Get-AzureRmVirtualNetworkGatewayConnection` cmdlet, with or without `-Debug`. 

1. Use the following cmdlet example, configuring the values to match your own. If prompted, select 'A' in order to run 'All'. In the example, `-Name` refers to the name of the connection that you created and want to test.

		Get-AzureRmVirtualNetworkGatewayConnection -Name MyGWConnection -ResourceGroupName MyRG

2. After the cmdlet has finished, view the values. In the example below, the connection status shows as 'Connected' and you can see ingress and egress bytes.

		Body:
		{
		  "name": "MyGWConnection",
		  "id":
		"/subscriptions/086cfaa0-0d1d-4b1c-94544-f8e3da2a0c7789/resourceGroups/MyRG/providers/Microsoft.Network/connections/MyGWConnection",
		  "properties": {
		    "provisioningState": "Succeeded",
		    "resourceGuid": "1c484f82-23ec-47e2-8cd8-231107450446b",
		    "virtualNetworkGateway1": {
		      "id":
		"/subscriptions/086cfaa0-0d1d-4b1c-94544-f8e3da2a0c7789/resourceGroups/MyRG/providers/Microsoft.Network/virtualNetworkGa
		teways/vnetgw1"
		    },
		    "localNetworkGateway2": {
		      "id":
		"/subscriptions/086cfaa0-0d1d-4b1c-94544-f8e3da2a0c7789/resourceGroups/MyRG/providers/Microsoft.Network/localNetworkGate
		ways/LocalSite"
		    },
		    "connectionType": "IPsec",
		    "routingWeight": 10,
		    "sharedKey": "abc123",
		    "connectionStatus": "Connected",
		    "ingressBytesTransferred": 33509044,
		    "egressBytesTransferred": 4142431
		  }

### To verify your connection by using the Azure Portal Preview

In the Azure Portal Preview, you can view the connection status by navigating to the connection. There are multiple ways to do this. The following steps show one way to navigate to your connection and verify.

1. In the [Azure Portal Preview](http://portal.azure.cn), click **All resources** and navigate to your virtual network gateway.
2. On the blade for your virtual network gateway, click **Connections**. You can see the status of each connection.
3. Click the name of the connection that you want to verify to open **Essentials**. In Essentials, you can view more information about your connection. The **Status** is 'Succeeded' and 'Connected' when you have made a successful connection.

	![Verify connection](../../includes/media/vpn-gateway-verify-connection-rm-include/connectionsucceeded.png)



## Next steps

- Once your connection is complete, you can add virtual machines to your virtual networks. See the virtual machines [learning path](https://azure.microsoft.com/documentation/learning-paths/virtual-machines) for more information.
