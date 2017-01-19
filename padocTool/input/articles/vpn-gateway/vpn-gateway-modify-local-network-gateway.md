<properties
   pageTitle="Modify local network gateway IP address prefixes and gateway IP | Azure"
   description="This article walks you through changing IP address prefixes for your local network gateway"
   services="vpn-gateway"
   documentationCenter="na"
   authors="cherylmc"
   manager="carmonm"
   editor=""
   tags="azure-resource-manager"/>

<tags
	ms.service="vpn-gateway"
	ms.date="08/08/2016"
	wacn.date=""/>

# Modify local network gateway settings using PowerShell

Sometimes the settings for your local network gateway AddressPrefix or GatewayIPAddress change. The instructions below will help you modify your local network gateway settings. You can also modify these settings in the Azure portal.

## Before you begin
	
You'll need to install the latest version of the Azure Resource Manager PowerShell cmdlets. See [How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure/) for more information about installing the PowerShell cmdlets.

## To modify IP address prefixes

### <a name="noconnection"></a>How to add or remove prefixes - no gateway connection

- **To add** additional address prefixes to a local network gateway that you created, but that doesn't yet have a gateway connection, use the example below. Be sure to change the values to your own.

		$local = Get-AzureRmLocalNetworkGateway -Name MyLocalNetworkGWName -ResourceGroupName MyRGName `
		Set-AzureRmLocalNetworkGateway -LocalNetworkGateway $local `
		-AddressPrefix @('10.0.0.0/24','20.0.0.0/24','30.0.0.0/24')

- **To remove** an address prefix from a local network gateway that doesn't have a VPN connection, use the example below. Leave out the prefixes that you no longer need. In this example, we no longer need prefix 20.0.0.0/24 (from the previous example), so we will update the local network gateway and exclude that prefix.

		$local = Get-AzureRmLocalNetworkGateway -Name MyLocalNetworkGWName -ResourceGroupName MyRGName `
		Set-AzureRmLocalNetworkGateway -LocalNetworkGateway $local `
		-AddressPrefix @('10.0.0.0/24','30.0.0.0/24')

### <a name="withconnection"></a>How to add or remove prefixes - existing gateway connection

If you have created your gateway connection and want to add or remove the IP address prefixes contained in your local network gateway, you'll need to do the following steps in order. This will result in some downtime for your VPN connection. When updating your prefixes, you'll first remove the connection, modify the prefixes, and then create a new connection. In the examples below, be sure to change the values to your own.

>[AZURE.IMPORTANT] Don't delete the VPN gateway. If you do so, you'll have to go back through the steps to recreate it, as well as reconfigure your on-premises router with the new settings.
 
1. Remove the connection.

		Remove-AzureRmVirtualNetworkGatewayConnection -Name MyGWConnectionName -ResourceGroupName MyRGName

2. Modify the address prefixes for your local network gateway.

	Set the variable for the LocalNetworkGateway.

		$local = Get-AzureRmLocalNetworkGateway -Name MyLocalNetworkGWName -ResourceGroupName MyRGName

	Modify the prefixes.

		Set-AzureRmLocalNetworkGateway -LocalNetworkGateway $local `
		-AddressPrefix @('10.0.0.0/24','20.0.0.0/24','30.0.0.0/24')

4. Create the connection. In this example, we are configuring an IPsec connection type. When you recreate your connection, use the connection type that is specified for your configuration. For additional connection types, see the [PowerShell cmdlet](https://msdn.microsoft.com/zh-cn/library/mt603611.aspx) page.

 	Set the variable for the VirtualNetworkGateway.

		$gateway1 = Get-AzureRmVirtualNetworkGateway -Name RMGateway  -ResourceGroupName MyRGName

	Create the connection. Note that this sample uses the variable $local that you set in the preceding step.


		New-AzureRmVirtualNetworkGatewayConnection -Name MyGWConnectionName `
		-ResourceGroupName MyRGName -Location 'China North' `
		-VirtualNetworkGateway1 $gateway1 -LocalNetworkGateway2 $local `
		-ConnectionType IPsec `
		-RoutingWeight 10 -SharedKey 'abc123'


## To modify the gateway IP address

To modify the gateway IP address, use the `New-AzureRmVirtualNetworkGatewayConnection` cmdlet. As long as you keep the name of the local network gateway exactly the same as the existing name, the settings will overwrite. At this time, the "Set" cmdlet does not support modifying the gateway IP address.

### <a name="gwipnoconnection"></a>How to modify the gateway IP address - no gateway connection

To update the gateway IP address for your local network gateway that doesn't yet have a connection, use the example below. You can also update the address prefixes at the same time. The settings you specify will overwrite the existing settings. Be sure to use the existing name of your local network gateway. If you don't, you'll be creating a new local network gateway, not overwriting the existing one.

Use the following example, replacing the values for your own.

	New-AzureRmLocalNetworkGateway -Name MyLocalNetworkGWName `
	-Location "China North" -AddressPrefix @('10.0.0.0/24','20.0.0.0/24','30.0.0.0/24') `
	-GatewayIpAddress "5.4.3.2" -ResourceGroupName MyRGName


### <a name="gwipwithconnection"></a>How to modify the gateway IP address - existing gateway connection

If a gateway connection already exists, you'll first need to remove the connection. Then, you can modify the gateway IP address and recreate a new connection. This will result in some downtime for your VPN connection.


>[AZURE.IMPORTANT] Don't delete the VPN gateway. If you do so, you'll have to go back through the steps to recreate it, as well as reconfigure your on-premises router with the IP address that will be assigned to the newly created gateway.
 

1. Remove the connection. You can find the name of your connection by using the `Get-AzureRmVirtualNetworkGatewayConnection` cmdlet.

		Remove-AzureRmVirtualNetworkGatewayConnection -Name MyGWConnectionName `
		-ResourceGroupName MyRGName

2. Modify the GatewayIpAddress value. You can also modify your address prefixes at this time, if necessary. Note that this will overwrite the existing local network gateway settings. Use the existing name of your local network gateway when modifying so that the settings will overwrite. If you don't, you'll be creating a new local network gateway, not modifying the existing one.

		New-AzureRmLocalNetworkGateway -Name MyLocalNetworkGWName `
		-Location "China North" -AddressPrefix @('10.0.0.0/24','20.0.0.0/24','30.0.0.0/24') `
		-GatewayIpAddress "104.40.81.124" -ResourceGroupName MyRGName

3. Create the connection. In this example, we are configuring an IPsec connection type. When you recreate your connection, use the connection type that is specified for your configuration. For additional connection types, see the [PowerShell cmdlet](https://msdn.microsoft.com/zh-cn/library/mt603611.aspx) page.  To obtain the VirtualNetworkGateway name, you can run the `Get-AzureRmVirtualNetworkGateway` cmdlet.

	Set the variables:

		$local = Get-AzureRMLocalNetworkGateway -Name MyLocalNetworkGWName -ResourceGroupName MyRGName `
		$vnetgw = Get-AzureRmVirtualNetworkGateway -Name RMGateway -ResourceGroupName MyRGName

	Create the connection:
	
		New-AzureRmVirtualNetworkGatewayConnection -Name MyGWConnectionName -ResourceGroupName MyRGName `
		-Location "China North" `
		-VirtualNetworkGateway1 $vnetgw `
		-LocalNetworkGateway2 $local `
		-ConnectionType IPsec -RoutingWeight 10 -SharedKey 'abc123'



## Next steps

You can verify your gateway connection. See [Verify a gateway connection](/documentation/articles/vpn-gateway-verify-connection-resource-manager/).

