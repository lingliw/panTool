<properties 
   pageTitle="Control routing and use virtual appliances using PowerShell in the classic deployment model | Windows Azure"
   description="Learn how to control routing in VNets using PowerShell in the classic deployment model"
   services="virtual-network"
   documentationCenter="na"
   authors="telmosampaio"
   manager="carolz"
   editor=""
   tags="azure-service-management"
/>
<tags
	ms.service="virtual-network"
	ms.date="10/06/2015"
	wacn.date=""/>

#Control routing and use virtual appliances (classic) using PowerShell



 This article covers the classic deployment model. You can also [ENTER ACTION FOR ARM HERE](/documentation/articles/armToken).

The sample Azure CLI commands below expect a simple environment already created based on the scenario above. If you want to run the commands as they are displayed in this document, create the environment shown in [create a VNet (classic) using PowerShell](/documentation/articles/virtual-networks-create-vnet-classic-ps).

## Create the UDR for the front end subnet
To create the route table and route needed for the front end subnet based on the scenario above, follow the steps below.

3. Run the **`New-AzureRouteTable`** cmdlet to create a route table for the front end subnet.

		```powershell
		New-AzureRouteTable -Name UDR-FrontEnd `
			-Location uswest `
			-Label "Route table for front end subnet"
		```

	Output:

		Name         Location   Label                          
		----         --------   -----                          
		UDR-FrontEnd China North    Route table for front end subnet

4. Run the **`Set-AzureRoute`** cmdlet to create a route in the route table created above to send all traffic destined to the back end subnet (192.168.2.0/24) to the **FW1** VM (192.168.0.4).
	
		```powershell
		Get-AzureRouteTable UDR-FrontEnd `
			|Set-AzureRoute -RouteName RouteToBackEnd -AddressPrefix 192.168.2.0/24 `
			-NextHopType VirtualAppliance `
			-NextHopIpAddress 192.168.0.4
		```

	Output:

		Name     : UDR-FrontEnd
		Location : China North
		Label    : Route table for frontend subnet
		Routes   : 
		           Name                 Address Prefix    Next hop type        Next hop IP address
		           ----                 --------------    -------------        -------------------
		           RouteToBackEnd       192.168.2.0/24    VirtualAppliance     192.168.0.4  

5. Run the **`Set-AzureSubnetRouteTable`** cmdlet to associate the route table created above with the **FrontEnd** subnet.

		```powershell
		Set-AzureSubnetRouteTable -VirtualNetworkName TestVNet `
			-SubnetName FrontEnd `
			-RouteTableName UDR-FrontEnd
		```
 
## Create the UDR for the back end subnet
To create the route table and route needed for the back end subnet based on the scenario above, follow the steps below.

3. Run the **`New-AzureRouteTable`** cmdlet to create a route table for the back end subnet.

		```powershell
		New-AzureRouteTable -Name UDR-BackEnd `
			-Location uswest `
			-Label "Route table for back end subnet"
		```

4. Run the **`Set-AzureRoute`** cmdlet to create a route in the route table created above to send all traffic destined to the front end subnet (192.168.1.0/24) to the **FW1** VM (192.168.0.4).

		```powershell
		Get-AzureRouteTable UDR-BackEnd `
			|Set-AzureRoute -RouteName RouteToFrontEnd -AddressPrefix 192.168.1.0/24 `
			-NextHopType VirtualAppliance `
			-NextHopIpAddress 192.168.0.4
		```

5. Run the **`Set-AzureSubnetRouteTable`** cmdlet to associate the route table created above with the **BackEnd** subnet.

		```powershell
		Set-AzureSubnetRouteTable -VirtualNetworkName TestVNet `
			-SubnetName FrontEnd `
			-RouteTableName UDR-FrontEnd
		```
## Enable IP forwrding on the FW1 VM
To enable IP forwarding in the FW1 VM, follow the steps below.

1. Run the **`Get-AzureIPForwarding`** cmdlet to chec the status of IP forwarding

		Get-AzureVM -Name FW1 -ServiceName TestRGFW `
			| Get-AzureIPForwarding

	Output:

		Disabled

2. Run the **`Set-AzureIPForwarding`** command to enable IP forwarding for the *FW1* VM.

		Get-AzureVM -Name FW1 -ServiceName TestRGFW `
			| Set-AzureIPForwarding -Enable