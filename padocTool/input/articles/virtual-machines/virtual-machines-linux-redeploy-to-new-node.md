<properties
    pageTitle="Redeploy Linux Virtual Machines | Azure"
    description="Describes how to redeploy Linux virtual machines to mitigate SSH connection issues."
    services="virtual-machines-linux"
    documentationcenter="virtual-machines"
    author="iainfoulds"
    manager="timlt"
    tags="azure-resource-manager,top-support-issue" />
<tags
    ms.assetid="e9530dd6-f5b0-4160-b36b-d75151d99eb7"
    ms.service="virtual-machines-linux"
    ms.devlang="na"
    ms.topic="support-article"
    ms.tgt_pltfrm="vm-linux"
    ms.workload="infrastructure"
    ms.date="09/19/2016"
    wacn.date=""
    ms.author="iainfou" />

# Redeploy virtual machine to new Azure node
If you have been facing difficulties troubleshooting SSH or application access to an Azure virtual machine (VM), redeploying the VM may help. When you redeploy a VM, it moves the VM to a new node within the Azure infrastructure and then powers it back on, retaining all your configuration options and associated resources. This article shows you how to redeploy a VM using Azure CLI or the Azure portal preview.

> [AZURE.NOTE]
> After you redeploy a VM, the temporary disk is lost and dynamic IP addresses associated with virtual network interface are updated. 
> 
> 

## Using Azure CLI
Make sure you have the [latest Azure CLI installed](/documentation/articles/xplat-cli-install/) on your machine and you are in Resource Manager mode (`azure config mode arm`).

Use the following Azure CLI command to redeploy your virtual machine:

    azure vm redeploy --resourcegroup <resourcegroup> --vm-name <vmname> 

You can see the status of the VM change as it goes through the redeploy process. The `PowerState` of the VM goes from 'Running' to 'Updating', then 'Starting', and finally 'Running' as it goes through the process of redeploying to a new host. Check the status of the VMs within a resource group with:

    azure vm list -g <resourcegroup>

[AZURE.INCLUDE [virtual-machines-common-redeploy-to-new-node](../../includes/virtual-machines-common-redeploy-to-new-node.md)]

## Next steps
If you are having issues connecting to your VM, you can find specific help on [troubleshooting SSH connections](/documentation/articles/virtual-machines-linux-troubleshoot-ssh-connection/) or [detailed SSH troubleshooting steps](/documentation/articles/virtual-machines-linux-detailed-troubleshoot-ssh-connection/). If you cannot access an application running on your VM, you can also read [application troubleshooting issues](/documentation/articles/virtual-machines-linux-troubleshoot-app-connection/).

