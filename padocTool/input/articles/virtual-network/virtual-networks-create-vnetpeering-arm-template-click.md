<!-- not suitable for Mooncake -->

<properties
   pageTitle="Create VNet Peering using Resource Manager templates | Azure"
   description="Learn how to create a virtual network peering using the templates in Resource Manager."
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

# Create VNet Peering using Resource Manager templates

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

To create a VNet peering by using Resource Manager templates, please follow the steps below:

1. If you have never used Azure PowerShell, see [How to Install and Configure Azure PowerShell](/documentation/articles/powershell-install-configure/) and follow the instructions all the way to the end to sign into Azure and select your subscription.

    Note: The PowerShell cmdlet for managing VNet peering is shipped with [Azure PowerShell 1.6.](http://www.powershellgallery.com/packages/Azure/1.6.0)

2. The text below shows the definition of a VNet peering link for VNet1 to VNet2, based on the scenario above. Copy the content below and save it to a file named VNetPeeringVNet1.json.

        {
        "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
        "contentVersion": "1.0.0.0",
        "parameters": {
        },
        "variables": {
        },
        "resources": [
            {
            "apiVersion": "2016-06-01",
            "type": "Microsoft.Network/virtualNetworks/virtualNetworkPeerings",
            "name": "VNet1/LinkToVNet2",
            "location": "[resourceGroup().location]",
            "properties": {
            "allowVirtualNetworkAccess": true,
            "allowForwardedTraffic": false,
            "allowGatewayTransit": false,
            "useRemoteGateways": false,
                "remoteVirtualNetwork": {
                "id": "[resourceId('Microsoft.Network/virtualNetworks', 'vnet2')]"       
        }
            }
            }
        ]
        }
    
3. The section below shows the definition of a VNet peering link for VNet2 to VNet1, based on the scenario above.  Copy the content below and save it to a file named VNetPeeringVNet2.json.

        {
        "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
        "contentVersion": "1.0.0.0",
        "parameters": {
        },
        "variables": {
        },
        "resources": [
            {
            "apiVersion": "2016-06-01",
            "type": "Microsoft.Network/virtualNetworks/virtualNetworkPeerings",
            "name": "VNet2/LinkToVNet1",
            "location": "[resourceGroup().location]",
            "properties": {
            "allowVirtualNetworkAccess": true,
            "allowForwardedTraffic": false,
            "allowGatewayTransit": false,
            "useRemoteGateways": false,
                "remoteVirtualNetwork": {
                "id": "[resourceId('Microsoft.Network/virtualNetworks', 'vnet1')]"       
                }
            }
            }
        ]
        }

    As seen in the template above, there are a few configurable properties for VNet peering:

    |Option|Description|Default|
    |:-----|:----------|:------|
    |AllowVirtualNetworkAccess|Whether or not the address space of a peer VNet is included as part of the virtual_network tag.|Yes|
    |AllowForwardedTraffic|Whether traffic not originating from a peered VNet is accepted or dropped.|No|
    |AllowGatewayTransit|Allows the peer VNet to use your VNet gateway.|No|
    |UseRemoteGateways|Use your peer's VNet gateway. The peer VNet must have a gateway configured and AllowGatewayTransit selected. You cannot use this option if you have a gateway configured.|No|

    Each link in VNet peering has the set of properties above. For example, you can set AllowVirtualNetworkAccess to True for VNet peering link VNet1 to VNet2 and set it to False for the VNet peering link in the other direction. 


4. To deploy the template file, you can run the New-AzureRmResourceGroupDeployment cmdlet to create or update the deployment. For more information about using Resource Manager templates, please refer to this [article](/documentation/articles/resource-group-template-deploy/).

        New-AzureRmResourceGroupDeployment -ResourceGroupName <resource group name> -TemplateFile <template file path> -DeploymentDebugLogLevel all

    > [AZURE.NOTE] Please replace the resource group name and template file as appropriate. 

    Below is an example based the scenario above:

        New-AzureRmResourceGroupDeployment -ResourceGroupName VNet101 -TemplateFile .\VNetPeeringVNet1.json -DeploymentDebugLogLevel all

    Output shows:

        DeploymentName		: VNetPeeringVNet1
        ResourceGroupName	: VNet101
        ProvisioningState		: Succeeded
        Timestamp			: 7/26/2016 9:05:03 AM
        Mode			: Incremental
        TemplateLink		:
        Parameters			:
        Outputs			:
        DeploymentDebugLogLevel : RequestContent, ResponseContent

        New-AzureRmResourceGroupDeployment -ResourceGroupName VNet101 -TemplateFile .\VNetPeeringVNet2.json -DeploymentDebugLogLevel all

    Output shows:

        DeploymentName		: VNetPeeringVNet2
        ResourceGroupName	: VNet101
        ProvisioningState		: Succeeded
        Timestamp			: 7/26/2016 9:07:22 AM
        Mode			: Incremental
        TemplateLink		:
        Parameters			:
        Outputs			:
        DeploymentDebugLogLevel : RequestContent, ResponseContent

5. After the deployment is finished, you can run the cmdlet below to view the peering state:

        Get-AzureRmVirtualNetworkPeering -VirtualNetworkName VNet1 -ResourceGroupName VNet101 -Name linktoVNet2

    Output shows:

        Name			: LinkToVNet2
        Id				: /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/VNet101/providers/Microsoft.Network/virtualNetworks/VNet1/virtualNetworkPeerings/LinkToVNet2
        Etag			: W/"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        ResourceGroupName	: VNet101
        VirtualNetworkName	: VNet1
        ProvisioningState		: Succeeded
        RemoteVirtualNetwork	: {
                                            "Id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/VNet101/providers/Microsoft.Network/virtualNetworks/VNet2"
                                        }
        AllowVirtualNetworkAccess	: True
        AllowForwardedTraffic            : False
        AllowGatewayTransit              : False
        UseRemoteGateways                : False
        RemoteGateways                   : null
        RemoteVirtualNetworkAddressSpace : null

	After peering is established in this scenario, you should be able to initiate the connections from any virtual machine to any virtual machine in both VNets. By default, AllowVirtualNetworkAccess is True and VNet peering will provision the proper ACLs to allow the communication between VNets. You can still apply network security group (NSG) rules to block connectivity between specific subnets or virtual machines to gain fine-grain control of access between two virtual networks.  For more information of creating NSG rules, please refer to this [article](/documentation/articles/virtual-networks-create-nsg-arm-ps/).

<!-- not suitable for Mooncake -->

## Peering across subscriptions

In this scenario you will create a peering between two VNets belonging to different subscriptions.

![cross sub scenario](../../includes/media/virtual-networks-create-vnetpeering-scenario-crosssub-include/figure01.PNG)

VNet peering relies on Role based access control (RBAC) for authorization. For cross-subscriptions scenario, you first need to grant sufficient permission to users who will create the peering link:
NOTE: if the same user has the privilege over both subscriptions, then you can skip step1-4 below.

To create a VNet peering across subscriptions, please follow the steps below:

1. Sign in to Azure with privileged User-A's account in Subscription-A and run the following cmdlet:

        New-AzureRmRoleAssignment -SignInName <UserB ID> -RoleDefinitionName "Network Contributor" -Scope /subscriptions/<Subscription-A-ID>/resourceGroups/<ResourceGroupName>/providers/Microsoft.Network/VirtualNetwork/VNet5

	This is not a requirement, peering can be established even if users individually raise peering requests for their respective Vnets as long as the requests match. Adding a privileged user of the other VNet as users in the local VNet makes it easier to do the setup. 

2. Sign in to Azure with privileged User-B's account for Subscription-B and run the following cmdlet:

        New-AzureRmRoleAssignment -SignInName <UserA ID> -RoleDefinitionName "Network Contributor" -Scope /subscriptions/<Subscription-B-ID>/resourceGroups/<ResourceGroupName>/providers/Microsoft.Network/VirtualNetwork/VNet3

3. In User-A's login session, run this cmdlet:

        New-AzureRmResourceGroupDeployment -ResourceGroupName VNet101 -TemplateFile .\VNetPeeringVNet3.json -DeploymentDebugLogLevel all

    Here is how the JSON file is defined.  
    
        {
        "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
        "contentVersion": "1.0.0.0",
        "parameters": {
        },
        "variables": {
        },
        "resources": [
            {
            "apiVersion": "2016-06-01",
            "type": "Microsoft.Network/virtualNetworks/virtualNetworkPeerings",
            "name": "VNet3/LinkToVNet5",
            "location": "[resourceGroup().location]",
            "properties": {
            "allowVirtualNetworkAccess": true,
            "allowForwardedTraffic": false,
            "allowGatewayTransit": false,
            "useRemoteGateways": false,
                "remoteVirtualNetwork": {
                "id": "/subscriptions/<Subscription-B-ID>/resourceGroups/<resource group name>/providers/Microsoft.Network/virtualNetworks/VNet5"
                }
            }
            }
        ]
        }
   
4. In User-B's login session, run the following cmdlet:

        New-AzureRmResourceGroupDeployment -ResourceGroupName VNet101 -TemplateFile .\VNetPeeringVNet5.json -DeploymentDebugLogLevel all
   
	Here is how the JSON file is defined:

        {
        "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
        "contentVersion": "1.0.0.0",
        "parameters": {
        },
        "variables": {
        },
        "resources": [
            {
            "apiVersion": "2016-06-01",
            "type": "Microsoft.Network/virtualNetworks/virtualNetworkPeerings",
            "name": "VNet5/LinkToVNet3",
            "location": "[resourceGroup().location]",
            "properties": {
            "allowVirtualNetworkAccess": true,
            "allowForwardedTraffic": false,
            "allowGatewayTransit": false,
            "useRemoteGateways": false,
                "remoteVirtualNetwork": {
                "id": "/subscriptions/Subscription-A-ID /resourceGroups/<resource group name>/providers/Microsoft.Network/virtualNetworks/VNet3"
                }
            }
            }
        ]
        }
 
 	After peering is established in this scenario, you should be able to initiate the connections from any virtual machine to any virtual machine of both VNets across different subscriptions. 

<!-- not suitable for Mooncake -->

## Service Chaining - Transit through peered VNet

Although the use of system routes facilitates traffic automatically for your deployment, there are cases in which you want to control the routing of packets through a virtual appliance.
In this scenario, there are two VNets in a subscription, HubVNet and VNet1 as described in below diagram. You deploy Network Virtual Appliance(NVA) in VNet HubVNet. After establishing VNet peering between HubVNet and VNet1, you can set up User Defined Routes and specify the next hop to NVA in the HubVNet.

![NVA Transit](../../includes/media/virtual-networks-create-vnetpeering-scenario-transit-include/figure01.PNG)

NOTE: For the simplicity, assume all VNets here are in the same subscription. But it also works for cross-subscription scenario. 

The key property to enable Transit routing is the "Allow Forwarded Traffic" parameter. This allows accepting and sending trafic from/to the NVA in the peered VNet.

1. In this scenario, you can deploy the sample template below to establish the VNet peering.  You'll need to set the AllowForwardedTraffic property to True, which allows the network virtual appliance in the peered VNet to send and receive traffic.

	Here is the template for creating a VNet peering from HubVNet to VNet1. Please note AllowForwardedTraffic is set to false.

        {
        "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
        "contentVersion": "1.0.0.0",
        "parameters": {
        },
        "variables": {
        },
        "resources": [
            {
            "apiVersion": "2016-06-01",
            "type": "Microsoft.Network/virtualNetworks/virtualNetworkPeerings",
            "name": "HubVNet/LinkToVNet1",
            "location": "[resourceGroup().location]",
            "properties": {
            "allowVirtualNetworkAccess": true,
            "allowForwardedTraffic": false,
            "allowGatewayTransit": false,
            "useRemoteGateways": false,
                "remoteVirtualNetwork": {
                "id": "[resourceId('Microsoft.Network/virtualNetworks', 'vnet1')]"       
                }
            }
            }
            }
        ]
        }

2. Here is the template for creating a VNet peering from VNet1 to HubVnet. Please note AllowForwardedTraffic is set to true. 

        {
        "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
        "contentVersion": "1.0.0.0",
        "parameters": {
        },
        "variables": {
        },
        "resources": [
            {
            "apiVersion": "2016-06-01",
            "type": "Microsoft.Network/virtualNetworks/virtualNetworkPeerings",
            "name": "VNet1/LinkToHubVNet",
            "location": "[resourceGroup().location]",
            "properties": {
            "allowVirtualNetworkAccess": true,
            "allowForwardedTraffic": true,
            "allowGatewayTransit": false,
            "useRemoteGateways": false,
                "remoteVirtualNetwork": {
                "id": "[resourceId('Microsoft.Network/virtualNetworks', 'HubVnet')]"       
                }
            }
            }
        ]
        }


3. After peering is established, you can refer to this [article](/documentation/articles/virtual-network-create-udr-arm-ps/) to define user-defined routes(UDR) to redirect VNet1 traffic through a virtual appliance to use its capabilities. When you specify the next hop address in route, you can set it to the IP address of the virtual appliance in the peer VNet HubVNet.