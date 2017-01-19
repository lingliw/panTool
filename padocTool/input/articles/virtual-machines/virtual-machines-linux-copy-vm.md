<properties
    pageTitle="Create a copy of your Azure Linux VM | Azure"
    description="Learn how to create a copy of your Azure Linux virtual machine in the Resource Manager deployment model"
    services="virtual-machines-linux"
    documentationcenter=""
    author="cynthn"
    manager="timlt"
    tags="azure-resource-manager" />
<tags
    ms.assetid="770569d2-23c1-4a5b-801e-cddcd1375164"
    ms.service="virtual-machines-linux"
    ms.workload="infrastructure-services"
    ms.tgt_pltfrm="vm-linux"
    ms.devlang="na"
    ms.topic="article"
    ms.date="07/28/2016"
    wacn.date=""
    ms.author="cynthn" />

# Create a copy of a Linux virtual machine running on Azure
This article shows you how to create a copy of your Azure virtual machine (VM) running Linux using the Resource Manager deployment model. First you copy over the operating system and data disks to a new container, then set up the network resources and create the new virtual machine.

You can also [upload and create a VM from custom disk image](/documentation/articles/virtual-machines-linux-upload-vhd/).

## Before you begin
Ensure that you meet the following prerequisites before you start the steps:

* You have the [Azure CLI](/documentation/articles/xplat-cli-install/) downloaded and installed on your machine. 
* You also need some information about your existing Azure Linux VM:

| Source VM information | Where to get it |
| --- | --- |
| VM name |`azure vm list` |
| Resource Group name |`azure vm list` |
| Location |`azure vm list` |
| Storage Account name |`azure storage account list -g <resourceGroup>` |
| Container name |`azure storage container list -a <sourcestorageaccountname>` |
| Source VM VHD file name |`azure storage blob list --container <containerName>` |

* You will need to make some choices about your new VM: 
     <br> -Container name
     <br> -VM name 
     <br> -VM size 
     <br> -vNet name 
     <br> -SubNet name 
     <br> -IP Name 
     <br> -NIC name

## Login and set your subscription
1. Login to the CLI.

        azure login -e AzureChinaCloud

2. Make sure you are in Resource Manager mode.

        azure config mode arm

3. Set the correct subscription. You can use 'azure account list' to see all of your subscriptions.

        azure account set mySubscriptionID

## Stop the VM
Stop and deallocate the source VM. You can use 'azure vm list' to get a list of all of the VMs in your subscription and their resource group names.

    azure vm stop myResourceGroup myVM
    azure vm deallocate myResourceGroup MyVM

## Copy the VHD
You can copy the VHD from the source storage to the destination using the `azure storage blob copy start`. In this example, we are going to copy the VHD to the same storage account, but a different container.

To copy the VHD to another container in the same storage account, type:

    azure storage blob copy start \
            https://mystorageaccountname.blob.core.chinacloudapi.cn:8080/mycontainername/myVHD.vhd \
            myNewContainerName

## Set up the virtual network for your new VM
Set up a virtual network and NIC for your new VM. 

    azure network vnet create myResourceGroup myVnet -l myLocation

    azure network vnet subnet create -a <address.prefix.in.CIDR/format> myResourceGroup myVnet mySubnet

    azure network public-ip create myResourceGroup myPublicIP -l myLocation

    azure network nic create myResourceGroup myNic -k mySubnet -m myVnet -p myPublicIP -l myLocation

## Create the new VM
You can now create a VM from your uploaded virtual disk [using a resource manager template](https://github.com/Azure/azure-quickstart-templates/tree/master/201-vm-from-specialized-vhd) or through the CLI by specifying the URI to your copied disk by typing:

    azure vm create -n myVM -l myLocation -g myResourceGroup -f myNic \
            -z Standard_DS1_v2 -y Linux \
            https://mystorageaccountname.blob.core.chinacloudapi.cn:8080/mycontainername/myVHD.vhd 

## Next steps
To learn how to use Azure CLI to manage your new virtual machine, see [Azure CLI commands for the Azure Resource Manager](/documentation/articles/azure-cli-arm-commands/).

