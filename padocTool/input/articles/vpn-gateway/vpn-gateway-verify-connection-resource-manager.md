<properties
   pageTitle="Verify a gateway connection | Azure"
   description="This article shows you how to verify a gateway connection in the Resource Manager deployment model"
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
   ms.date="10/14/2016"
   wacn.date=""
   ms.author="cherylmc"/>

# Verify a gateway connection

You can verify your gateway connection in a few different ways. This article will show you how to verify the status of a Resource Manager gateway connection by using the Azure Portal Preview and by using PowerShell.


## Verify using PowerShell

You'll need to install the latest version of the Azure Resource Manager PowerShell cmdlets. For information on installing PowerShell cmdlets, see [How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure/). For more information about using Resource Manager cmdlets, see [Using Windows PowerShell with Resource Manager](/documentation/articles/powershell-azure-resource-manager/).

### Step 1: Log in to your Azure account

1. Open your PowerShell console with elevated privileges and connect to your account.

		Login-AzureRmAccount -EnvironmentName AzureChinaCloud

2. Check the subscriptions for the account.

		Get-AzureRmSubscription 

3. Specify the subscription that you want to use.

		Select-AzureRmSubscription -SubscriptionName "Replace_with_your_subscription_name"

### Step 2: Verify your connection


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


## Verify using the Azure portal Preview

In the Azure portal Preview, you can view the connection status by navigating to the connection. There are multiple ways to do this. The following steps show one way to navigate to your connection and verify.

1. In the [Azure portal Preview](http://portal.azure.cn), click **All resources** and navigate to your virtual network gateway.
2. On the blade for your virtual network gateway, click **Connections**. You can see the status of each connection.
3. Click the name of the connection that you want to verify to open **Essentials**. In Essentials, you can view more information about your connection. The **Status** is 'Succeeded' and 'Connected' when you have made a successful connection.

	![Verify connection](../../includes/media/vpn-gateway-verify-connection-portal-rm-include/connectionsucceeded.png) 


## Next steps

- You can add virtual machines to your virtual networks. See [Create a Virtual Machine](/documentation/articles/virtual-machines-windows-hero-tutorial/) for steps.

