<!-- not suitable for Mooncake -->

<properties
    pageTitle="Migrate to Resource Manager with PowerShell | Azure"
    description="This article walks through the platform-supported migration of IaaS resources from classic to Azure Resource Manager by using Azure PowerShell commands"
    services="virtual-machines-windows"
    documentationcenter=""
    author="cynthn"
    manager="timlt"
    editor=""
    tags="azure-resource-manager" />
<tags
    ms.assetid="2b3dff9b-2e99-4556-acc5-d75ef234af9c"
    ms.service="virtual-machines-windows"
    ms.workload="infrastructure-services"
    ms.tgt_pltfrm="vm-windows"
    ms.devlang="na"
    ms.topic="article"
    ms.date="10/19/2016"
    wacn.date=""
    ms.author="cynthn" />

# Migrate IaaS resources from classic to Azure Resource Manager by using Azure PowerShell
These steps show you how to use Azure PowerShell commands to migrate infrastructure as a service (IaaS) resources from the classic deployment model to the Azure Resource Manager deployment model. 

If you want, you can also migrate resources by using the [Azure Command Line Interface (Azure CLI)](/documentation/articles/virtual-machines-linux-cli-migration-classic-resource-manager/).

* For background on supported migration scenarios, see [Platform-supported migration of IaaS resources from classic to Azure Resource Manager](/documentation/articles/virtual-machines-windows-migration-classic-resource-manager/). 
* For detailed guidance and a migration walkthrough, see [Technical deep dive on platform-supported migration from classic to Azure Resource Manager](/documentation/articles/virtual-machines-windows-migration-classic-resource-manager-deep-dive/).
* [Review most common migration errors](/documentation/articles/virtual-machines-migration-errors/)

## Step 1: Plan for migration
Here are a few best practices that we recommend as you evaluate migrating IaaS resources from classic to Resource Manager:

* Read through the [supported and unsupported features and configurations](/documentation/articles/virtual-machines-windows-migration-classic-resource-manager/). If you have virtual machines that use unsupported configurations or features, we recommend that you wait for the configuration/feature support to be announced. Alternatively, if it suits your needs, remove that feature or move out of that configuration to enable migration.
* If you have automated scripts that deploy your infrastructure and applications today, try to create a similar test setup by using those scripts for migration. Alternatively, you can set up sample environments by using the Azure portal preview.

> [AZURE.IMPORTANT]
> ExpressRoute gateways and Application Gateways are not currently supported for migration from classic to Resource Manager. To migrate a classic virtual network with a ExpressRoute or Application gateway, remove the gateway before running a Commit operation to move the network (you can run the Prepare step without deleting the ExpressRoute or Application gateway). After you complete the migration, reconnect the gateway in Azure Resource Manager.
> 
> 

## Step 2: Install the latest version of Azure PowerShell
There are two main options to install Azure PowerShell: [PowerShell Gallery](https://www.powershellgallery.com/profiles/azure-sdk/) or [Web Platform Installer (WebPI)](http://aka.ms/webpi-azps). WebPI receives monthly updates. PowerShell Gallery receives updates on a continuous basis. This article is based on Azure PowerShell version 2.1.0.

For installation instructions, see [How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure/).

<br>

## Step 3: Set your subscription and sign up for migration
First, start a PowerShell prompt. For migration, you need to set up your environment for both classic and Resource Manager.

Sign in to your account for the Resource Manager model.

        Login-AzureRmAccount -EnvironmentName AzureChinaCloud

Get the available subscriptions by using the following command:

        Get-AzureRMSubscription | Sort SubscriptionName | Select SubscriptionName

Set your Azure subscription for the current session. This example sets the default subscription name to **My Azure Subscription**. Replace the example subscription name with your own. 

        Select-AzureRmSubscription -SubscriptionName "My Azure Subscription"

> [AZURE.NOTE]
> Registration is a one-time step, but you must do it once before attempting migration. Without registering, you see the following error message: 
> 
> *BadRequest : Subscription is not registered for migration.* 
> 
> 

Register with the migration resource provider by using the following command:

        Register-AzureRmResourceProvider -ProviderNamespace Microsoft.ClassicInfrastructureMigrate

Please wait five minutes for the registration to finish. You can check the status of the approval by using the following command:

        Get-AzureRmResourceProvider -ProviderNamespace Microsoft.ClassicInfrastructureMigrate

Make sure that RegistrationState is `Registered` before you proceed. 

Now sign in to your account for the classic model.

        Add-AzureAccount -Environment AzureChinaCloud

Get the available subscriptions by using the following command:

        Get-AzureSubscription | Sort SubscriptionName | Select SubscriptionName

Set your Azure subscription for the current session. This example sets the default subscription to **My Azure Subscription**. Replace the example subscription name with your own. 

        Select-AzureSubscription -SubscriptionName "My Azure Subscription"

<br>

## Step 4: Make sure you have enough Azure Resource Manager Virtual Machine cores in the Azure region of your current deployment or VNET
You can use the following PowerShell command to check the current number of cores you have in Azure Resource Manager. To learn more about core quotas, see [Limits and the Azure Resource Manager](/documentation/articles/azure-subscription-service-limits/#limits-and-the-azure-resource-manager). 

This example checks the availability in the **China North** region. Replace the example region name with your own. 

    Get-AzureRmVMUsage -Location "China North"

## Step 5: Run commands to migrate your IaaS resources
> [AZURE.NOTE]
> All the operations described here are idempotent. If you have a problem other than an unsupported feature or a configuration error, we recommend that you retry the prepare, abort, or commit operation. The platform then tries the action again.
> 
> 

### Migrate virtual machines in a cloud service (not in a virtual network)
Get the list of cloud services by using the following command, and then pick the cloud service that you want to migrate. If the VMs in the cloud service are in a virtual network or if they have web or worker roles, the command returns an error message.

        Get-AzureService | ft Servicename

Get the deployment name for the cloud service. In this example, the service name is **My Service**. Replace the example service name with your own service name. 

        $serviceName = "My Service"
        $deployment = Get-AzureDeployment -ServiceName $serviceName
        $deploymentName = $deployment.DeploymentName

Prepare the virtual machines in the cloud service for migration. You have two options to choose from.

* **Option 1. Migrate the VMs to a platform-created virtual network**
  
    First, validate if you can migrate the cloud service using the following commands:

        $validate = Move-AzureService -Validate -ServiceName $serviceName `
            -DeploymentName $deploymentName -CreateNewVirtualNetwork
        $validate.ValidationMessages

The preceding command displays any warnings and errors that block migration. If validation is successful, then you can move on to the **Prepare** step:

        Move-AzureService -Prepare -ServiceName $serviceName `
            -DeploymentName $deploymentName -CreateNewVirtualNetwork

* **Option 2. Migrate to an existing virtual network in the Resource Manager deployment model**
  
    This example sets the resource group name to **myResourceGroup**, the virtual network name to **myVirtualNetwork** and the subnet name to **mySubNet**. Replace the names in the example with the names of your own resources.

        $existingVnetRGName = "myResourceGroup"
        $vnetName = "myVirtualNetwork"
        $subnetName = "mySubNet"

First, validate if you can migrate the cloud service using the following command:

        $validate = Move-AzureService -Validate -ServiceName $serviceName `
            -DeploymentName $deploymentName -UseExistingVirtualNetwork -VirtualNetworkResourceGroupName $existingVnetRGName -VirtualNetworkName $vnetName -SubnetName $subnetName
        $validate.ValidationMessages

The preceding command displays any warnings and errors that block migration. If validation is successful, then you can proceed with the following Prepare step:

        Move-AzureService -Prepare -ServiceName $serviceName -DeploymentName $deploymentName `
            -UseExistingVirtualNetwork -VirtualNetworkResourceGroupName $existingVnetRGName `
            -VirtualNetworkName $vnetName -SubnetName $subnetName

After the Prepare operation succeeds with either of the preceding options, query the migration state of the VMs. Ensure that they are in the `Prepared` state.

This example sets the VM name to **myVM**. Replace the example name with your own VM name.

        $vmName = "myVM"
        $vm = Get-AzureVM -ServiceName $serviceName -Name $vmName
        $vm.VM.MigrationState

Check the configuration for the prepared resources by using either PowerShell or the Azure portal preview. If you are not ready for migration and you want to go back to the old state, use the following command:

        Move-AzureService -Abort -ServiceName $serviceName -DeploymentName $deploymentName

If the prepared configuration looks good, you can move forward and commit the resources by using the following command:

        Move-AzureService -Commit -ServiceName $serviceName -DeploymentName $deploymentName

### Migrate virtual machines in a virtual network
To migrate virtual machines in a virtual network, you migrate the network. The virtual machines automatically migrate with the network. Pick the virtual network that you want to migrate. 

This example sets the virtual network name to **myVnet**. Replace the example virtual network name with your own. 

        $vnetName = "myVnet"

> [AZURE.NOTE]
> If the virtual network contains web or worker roles, or VMs with unsupported configurations, you get a validation error message.
> 
> 

First, validate if you can migrate the virtual network by using the following command:

        Move-AzureVirtualNetwork -Validate -VirtualNetworkName $vnetName

The preceding command displays any warnings and errors that block migration. If validation is successful, then you can proceed with the following Prepare step:

        Move-AzureVirtualNetwork -Prepare -VirtualNetworkName $vnetName

Check the configuration for the prepared virtual machines by using either Azure PowerShell or the Azure portal preview. If you are not ready for migration and you want to go back to the old state, use the following command:

        Move-AzureVirtualNetwork -Abort -VirtualNetworkName $vnetName

If the prepared configuration looks good, you can move forward and commit the resources by using the following command:

        Move-AzureVirtualNetwork -Commit -VirtualNetworkName $vnetName

### Migrate a storage account
Once you're done migrating the virtual machines, we recommend you migrate the storage accounts.

Prepare each storage account for migration by using the following command. In this example, the storage account name is **myStorageAccount**. Replace the example name with the name of your own storage account. 

        $storageAccountName = "myStorageAccount"
        Move-AzureStorageAccount -Prepare -StorageAccountName $storageAccountName

Check the configuration for the prepared storage account by using either Azure PowerShell or the Azure portal preview. If you are not ready for migration and you want to go back to the old state, use the following command:

        Move-AzureStorageAccount -Abort -StorageAccountName $storageAccountName

If the prepared configuration looks good, you can move forward and commit the resources by using the following command:

        Move-AzureStorageAccount -Commit -StorageAccountName $storageAccountName

## Next steps
* For more information about migration, see [Platform-supported migration of IaaS resources from classic to Azure Resource Manager](/documentation/articles/virtual-machines-windows-migration-classic-resource-manager/).
* To migrate additional network resources to Resource Manager using Azure PowerShell, use similar steps with [Move-AzureNetworkSecurityGroup](https://msdn.microsoft.com/zh-cn/library/mt786729.aspx), [Move-AzureReservedIP](https://msdn.microsoft.com/zh-cn/library/mt786752.aspx), and [Move-AzureRouteTable](https://msdn.microsoft.com/zh-cn/library/mt786718.aspx).
* For open-source scripts you can use to migrate Azure resources from classic to Resource Manager, see [Community tools for migration to Azure Resource Manager migration](/documentation/articles/virtual-machines-windows-migration-scripts/)

