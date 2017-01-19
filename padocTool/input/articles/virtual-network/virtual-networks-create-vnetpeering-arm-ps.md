<!-- not suitable for Mooncake -->

<properties
   pageTitle="Create VNet Peering using Powershell cmdlets | Azure"
   description="Learn how to create a virtual network using the Azure portal in Resource Manager."
   services="virtual-network"
   documentationCenter=""
   authors="narayanannamalai"
   manager="jefco"
   editor=""
   tags="azure-resource-manager"/>

<tags
	ms.service="virtual-network"
	ms.date="08/02/2016"
	wacn.date=""/>

# Create VNet Peering using Powershell cmdlets

<!-- not suitable for Mooncake -->

> [AZURE.SELECTOR]
- [Azure Portal](/documentation/articles/virtual-networks-create-vnetpeering-arm-portal/)
- [PowerShell](/documentation/articles/virtual-networks-create-vnetpeering-arm-ps/)
- [ARM template](/documentation/articles/virtual-networks-create-vnetpeering-arm-template-click/)

<!-- not suitable for Mooncake -->

VNet Peering is a mechanism to connect two Virtual Networks in the same region through the Azure backbone network. Once peered, the two Virtual Networks will appear like a single Virtual Network for all connectivity purposes. Read the [VNet Peering overview](/documentation/articles/virtual-network-peering-overview/) if you are not familiar with VNet Peering.

VNet Peering is in public preview, to be able to use it you must register using the below commands:

    Register-AzureRmProviderFeature -FeatureName AllowVnetPeering -ProviderNamespace Microsoft.Network

    Register-AzureRmResourceProvider -ProviderNamespace Microsoft.Network


<!-- not suitable for Mooncake -->

## Peering VNets in the same subscription

In this scenario you will create a peering between two VNets named **VNet1** and **VNet2** belonging to the same subscription. 

![Basic scenario](../../includes/media/virtual-networks-create-vnetpeering-scenario-basic-include/figure01.PNG)

VNet peering will allow full connectivity between the entire address space of peered virtual networks.

To create a VNet peering by using PowerShell, please follow the steps below:

1. If you have never used Azure PowerShell, see [How to Install and Configure Azure PowerShell](/documentation/articles/powershell-install-configure/) and follow the instructions all the way to the end to sign into Azure and select your subscription.

        Note: PowerShell cmdlet for managing VNet peering is shipped with [Azure PowerShell 1.6.](http://www.powershellgallery.com/packages/Azure/1.6.0)

2. Read virtual network objects:

        $vnet1 = Get-AzureRmVirtualNetwork -ResourceGroupName vnet101 -Name vnet1
        $vnet2 = Get-AzureRmVirtualNetwork -ResourceGroupName vnet101 -Name vnet2
	
3. To establish VNet peering, you need to create two links,  one for each direction. The following step will create a VNet peering link for VNet1 to VNet2 first:

        Add-AzureRmVirtualNetworkPeering -name LinkToVNet2 -VirtualNetwork $vnet1 -RemoteVirtualNetworkId $vnet2.id 

        Output shows:

        Name			: LinkToVNet2
        Id: /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/vnet101/providers/Microsoft.Network/virtualNetworks/vnet1/virtualNetworkPeerings/LinkToVNet2
        Etag			: W/"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        ResourceGroupName	: vnet101
        VirtualNetworkName	: vnet1
        ProvisioningState		: Succeeded
        RemoteVirtualNetwork	: {
                                            "Id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/vnet101/providers/Microsoft.Network/virtualNetworks/vnet2"
                                        }
        AllowVirtualNetworkAccess	: True
        AllowForwardedTraffic	: False
        AllowGatewayTransit	: False
        UseRemoteGateways	: False
        RemoteGateways		: null
        RemoteVirtualNetworkAddressSpace : null

4. This step will create a VNet peering link for VNet2 to VNet1:

        Add-AzureRmVirtualNetworkPeering -name LinkToVNet1 -VirtualNetwork $vnet2 -RemoteVirtualNetworkId $vnet1.id 

        Output shows:

        Name			: LinkToVNet1
        Id				: /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/vnet101/providers/Microsoft.Network/virtualNetworks/vnet2/virtualNetworkPeerings/LinkToVNet1
        Etag			: W/"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        ResourceGroupName	: vnet101
        VirtualNetworkName	: vnet2
        ProvisioningState		: Succeeded
        RemoteVirtualNetwork	: {
                                            "Id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/vnet101/providers/Microsoft.Network/virtualNetworks/vnet1"
                                        }
        AllowVirtualNetworkAccess	: True
        AllowForwardedTraffic	: False
        AllowGatewayTransit	: False
        UseRemoteGateways	: False
        RemoteGateways		: null
        RemoteVirtualNetworkAddressSpace : null

5. Once the VNet peering link is created, you can see the link state below:

        Get-AzureRmVirtualNetworkPeering -VirtualNetworkName vnet1 -ResourceGroupName vnet101 -Name linktovnet2

        Output shows:

		Name			: LinkToVNet2
		Id				: /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/vnet101/providers/Microsoft.Network/virtualNetworks/vnet1/virtualNetworkPeerings/LinkToVNet2
		Etag			: W/"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
		ResourceGroupName	: vnet101
		VirtualNetworkName	: vnet1
		ProvisioningState		: Succeeded
		RemoteVirtualNetwork	: {
		                                     "Id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/vnet101/providers/Microsoft.Network/virtualNetworks/vnet2"
		                                }
		AllowVirtualNetworkAccess	: True
		AllowForwardedTraffic            : False
		AllowGatewayTransit              : False
		UseRemoteGateways                : False
		RemoteGateways                   : null
		RemoteVirtualNetworkAddressSpace : null

	There are a few configurable properties for VNet peering:

	|Option|Description|Default|
	|:-----|:----------|:------|
	|AllowVirtualNetworkAccess|Whether address space of Peer VNet to be included as part of the Virtual_network Tag|Yes|
	|AllowForwardedTraffic|Allows traffic not originated from peered VNet is accepted or dropped|No|
	|AllowGatewayTransit|Allows the peer VNet to use your VNet gateway|No|
	|UseRemoteGateways|Use your peer's VNet gateway. The peer VNet must have a gateway configured and AllowGatewayTransit is selected. You cannot use this option if you have a gateway configured|No|

	Each link in VNet peering has the set of properties above. For example, you can set AllowVirtualNetworkAccess to True for VNet peering link VNet1 to VNet2 and set it to False for the VNet peering link in the other direction.

        $LinktoVNet2 = Get-AzureRmVirtualNetworkPeering -VirtualNetworkName vnet1 -ResourceGroupName vnet101 -Name LinkToVNet2
        $LinktoVNet2.AllowForwardedTraffic = $true
        Set-AzureRmVirtualNetworkPeering -VirtualNetworkPeering $LinktoVNet2

        You can run Get-AzureRmVirtualNetworkPeering to double check the property value after the change.  From the output, you can see AllowForwardedTraffic changes set to True after running the above cmdlets. 

        Name			: LinkToVNet2
        Id			: /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/vnet101/providers/Microsoft.Network/virtualNetworks/vnet1/virtualNetworkPeerings/LinkToVNet2
        Etag			: W/"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        ResourceGroupName	: vnet101
        VirtualNetworkName	: vnet1
        ProvisioningState	: Succeeded
        RemoteVirtualNetwork	: {
                                            "Id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/vnet101/providers/Microsoft.Network/virtualNetworks/vnet2"
                                        }
        AllowVirtualNetworkAccess	: True
        AllowForwardedTraffic		: True
        AllowGatewayTransit		: False
        UseRemoteGateways		: False
        RemoteGateways		: null
        RemoteVirtualNetworkAddressSpace : null

	After peering is established in this scenario, you should be able to initiate the connections from any virtual machine to any virtual machine of both VNets. By default, AllowVirtualNetworkAccess is True and VNet peering will provision the proper ACLs to allow the communication between VNets. You can still apply network security group (NSG) rules to block connectivity between specific subnets or virtual machines to gain fine grain control of access between two virtual networks.  For more information about creating NSG rules, please refer to this [article](/documentation/articles/virtual-networks-create-nsg-arm-ps/).

<!-- not suitable for Mooncake -->

## Peering across subscriptions

In this scenario you will create a peering between two VNets belonging to different subscriptions.

![cross sub scenario](../../includes/media/virtual-networks-create-vnetpeering-scenario-crosssub-include/figure01.PNG)

VNet peering relies on Role based access control (RBAC) for authorization. For cross-subscriptions scenario, you first need to grant sufficient permission to users who will create the peering link:
NOTE: if the same user has the privilege over both subscriptions, then you can skip step1-4 below.

To create VNet peering across subscriptions using PowerShell, please follow the steps below:

1. Sign in to Azure with privileged User-A's account for Subscription-A and run the following cmdlet:

        New-AzureRmRoleAssignment -SignInName <UserB ID> -RoleDefinitionName "Network Contributor" -Scope /subscriptions/<Subscription-A-ID>/resourceGroups/<ResourceGroupName>/providers/Microsoft.Network/VirtualNetwork/VNet5

        This is not a requirement, peering can be established even if users individually raise peering requests for thier respective Vnets as long as the requests match. Adding a privileged user of the other VNet as a user in the local VNet makes it easier to do the setup. 

2. Sign in to Azure with privileged User-B's account for Subscription-B and run the following cmdlet:

        New-AzureRmRoleAssignment -SignInName <UserA ID> -RoleDefinitionName "Network Contributor" -Scope /subscriptions/<Subscription-B-ID>/resourceGroups/<ResourceGroupName>/providers/Microsoft.Network/VirtualNetwork/VNet3

3. In User-A's login session, run the cmdlet below:

        $vnet3 = Get-AzureRmVirtualNetwork -ResourceGroupName hr-vnets -Name vnet3

        Add-AzureRmVirtualNetworkPeering -name LinkToVNet5 -VirtualNetwork $vnet3 -RemoteVirtualNetworkId "/subscriptions/<Subscriptoin-B-Id>/resourceGroups/<ResourceGroupName>/providers/Microsoft.Network/virtualNetworks/VNet5" -BlockVirtualNetworkAccess

4. In User-B's login session, run the cmdlet below:

        $vnet5 = Get-AzureRmVirtualNetwork -ResourceGroupName vendor-vnets -Name vnet5

        Add-AzureRmVirtualNetworkPeering -name LinkToVNet3 -VirtualNetwork $vnet5 -RemoteVirtualNetworkId "/subscriptions/<Subscriptoin-A-Id>/resourceGroups/<ResourceGroupName>/providers/Microsoft.Network/virtualNetworks/VNet3" -BlockVirtualNetworkAccess

5. After peering is established, any virtual machine in VNet3 should be able to communicate with any virtual machine in VNet5.

<!-- not suitable for Mooncake -->

## Service Chaining - Transit through peered VNet

Although the use of system routes facilitates traffic automatically for your deployment, there are cases in which you want to control the routing of packets through a virtual appliance.
In this scenario, there are two VNets in a subscription, HubVNet and VNet1 as described in below diagram. You deploy Network Virtual Appliance(NVA) in VNet HubVNet. After establishing VNet peering between HubVNet and VNet1, you can set up User Defined Routes and specify the next hop to NVA in the HubVNet.

![NVA Transit](../../includes/media/virtual-networks-create-vnetpeering-scenario-transit-include/figure01.PNG)

NOTE: For the simplicity, assume all VNets here are in the same subscription. But it also works for cross-subscription scenario. 

The key property to enable Transit routing is the "Allow Forwarded Traffic" parameter. This allows accepting and sending trafic from/to the NVA in the peered VNet.

1. In this scenario, you can run the PowerShell cmdlets below to establish the VNet peering.  You need to set the AllowForwardedTraffic property to True and link VNET1 to HubVnet, which allows the inbound traffic from outside of the peering VNet address space. 

        $hubVNet = Get-AzureRmVirtualNetwork -ResourceGroupName vnet101 -Name HubVNet
        $vnet1 = Get-AzureRmVirtualNetwork -ResourceGroupName vnet101 -Name vnet1

        Add-AzureRmVirtualNetworkPeering -name LinkToHub -VirtualNetwork $vnet1 -RemoteVirtualNetworkId $HubVNet.id -AllowForwardedTraffic

        Add-AzureRmVirtualNetworkPeering -name LinkToVNet1 -VirtualNetwork $HubVNet -RemoteVirtualNetworkId $vnet1.id

2. After peering is established, you can refer to this [article](/documentation/articles/virtual-network-create-udr-arm-ps/) and define a user-defined route (UDR) to redirect VNet1 traffic through a virtual appliance to use its capabilities. When you specify the next hop address in the route, you can set it to the IP address of the virtual appliance in the peer VNet HubVNet. Below is a sample:

        $route = New-AzureRmRouteConfig -Name TestNVA -AddressPrefix 10.3.0.0/16 -NextHopType VirtualAppliance -NextHopIpAddress 192.0.1.5

        $routeTable = New-AzureRmRouteTable -ResourceGroupName VNet101 -Location brazilsouth -Name TestRT -Route $route

        $vnet1 = Get-AzureRmVirtualNetwork -ResourceGroupName VNet101 -Name VNet1

        Set-AzureRmVirtualNetworkSubnetConfig -VirtualNetwork $vnet1 -Name subnet-1 -AddressPrefix 10.1.1.0/24 -RouteTable $routeTable

        Set-AzureRmVirtualNetwork -VirtualNetwork $vnet1

## Remove VNet Peering

1.	In order to remove the VNet peering, you need run the following cmdlet: 

        Remove-AzureRmVirtualNetworkPeering  
    
        remove both links, as shown below:

        Remove-AzureRmVirtualNetworkPeering -ResourceGroupName vnet101 -VirtualNetworkName vnet1 -Name linktovnet2 
        Remove-AzureRmVirtualNetworkPeering -ResourceGroupName vnet101 -VirtualNetworkName vnet1 -Name linktovnet2 

2. Once you remove one link in a VNET peering, the  peer link state will go to disconnected. In this state, you cannot re-create the link until the peer link state changes to Initiated. We recommend you remove both links before you re-create the VNet peering. 
