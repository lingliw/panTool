<!-- need to be verified -->

<properties
    pageTitle="Capture a VM image from generalized Azure VM | Azure"
    description="Learn how to capture a VM image from a generalized Azure VM created in the Resource Manager deployment model"
    services="virtual-machines-windows"
    documentationcenter=""
    author="cynthn"
    manager="timlt"
    editor=""
    tags="azure-resource-manager" />
<tags
    ms.assetid="afdae4a1-6dfb-47b4-902a-f327f9bfe5b4"
    ms.service="virtual-machines-windows"
    ms.workload="infrastructure-services"
    ms.tgt_pltfrm="vm-windows"
    ms.devlang="na"
    ms.topic="article"
    ms.date="10/20/2016"
    wacn.date=""
    ms.author="cynthn" />

# How to capture a VM image from a generalized Azure VM
This article shows you how to use Azure PowerShell to create an image of a generalized Azure VM. You can then use the image to create another VM. The image includes the OS disk and the data disks that are attached to the virtual machine. The image doesn't include the virtual network resources, so you need to set up those resources when you create the new VM. 

## Prerequisites
* You need to have already [generalized the VM](/documentation/articles/virtual-machines-windows-generalize-vhd/). Generalizing a VM removes all your personal account information, among other things, and prepares the machine to be used as an image.
* You need to have Azure PowerShell version 1.0.x or newer installed. If you haven't already installed PowerShell, read [How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure/) for installation steps.

## Log in to Azure PowerShell
1. Open Azure PowerShell and sign in to your Azure account.

        Login-AzureRmAccount -EnvironmentName AzureChinaCloud

A pop-up window opens for you to enter your Azure account credentials.
2. Get the subscription IDs for your available subscriptions.

        Get-AzureRmSubscription

3. Set the correct subscription using the subscription ID.

        Select-AzureRmSubscription -SubscriptionId "<subscriptionID>"

## Deallocate the VM and set the state to generalized
1. Deallocate the VM resources.

        Stop-AzureRmVM -ResourceGroupName <resourceGroup> -Name <vmName>

The *Status* for the VM in the Azure portal preview changes from **Stopped** to **Stopped (deallocated)**.
2. Set the status of the virtual machine to **Generalized**. 

        Set-AzureRmVm -ResourceGroupName <resourceGroup> -Name <vmName> -Generalized

3. Check the status of the VM. The **OSState/generalized** section for the VM should have the **DisplayStatus** set to **VM generalized**.  

        $vm = Get-AzureRmVM -ResourceGroupName <resourceGroup> -Name <vmName> -Status
        $vm.Statuses

## <a name="capture-the-vm"></a> Create the image
1. Copy the virtual machine image to the destination storage container using this command. The image is created in the same storage account as the original virtual machine. The `-Path` parameter saves a copy of the JSON template locally. The `-DestinationContainerName` parameter is the name of the container that you want to hold your images. If the container doesn't exist, it is created for you.

        Save-AzureRmVMImage -ResourceGroupName <resourceGroupName> -Name <vmName> `
            -DestinationContainerName <destinationContainerName> -VHDNamePrefix <templateNamePrefix> `
            -Path <C:\local\Filepath\Filename.json>

You can get the URL of your image from the JSON file template. Go to the **resources** > **storageProfile** > **osDisk** > **image** > **uri** section for the complete path of your image. The URL of the image looks like: `https://<storageAccountName>.blob.core.chinacloudapi.cn/system/Microsoft.Compute/Images/<imagesContainer>/<templatePrefix-osDisk>.xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.vhd`.
   
    You can also verify the URI in the portal. The image is copied to a container named **system** in your storage account. 

## Next steps
* Now you can [create a VM from the image](/documentation/articles/virtual-machines-windows-create-vm-generalized/).

