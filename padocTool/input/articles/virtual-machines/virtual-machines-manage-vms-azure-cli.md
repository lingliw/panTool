<!-- deleted in Global -->

<properties
   pageTitle="Manage virtual machines with the CLI | Azure"
   description="Automate the management of your Azure Resource Manager VMs by using the Azure Command-Line Interface (CLI)."
   services="virtual-machines"
   documentationCenter=""
   authors="dlepow"
   manager="timlt"
   editor=""
   tags="azure-resource-manager"/>

   <tags
	ms.service="virtual-machines"
	ms.date="10/07/2015"
	wacn.date=""/>

# Manage your Resource Manager virtual machines by using the Azure CLI for Mac, Linux, and Windows


> [AZURE.IMPORTANT] Azure has two different deployment models for creating and working with resources:  [Resource Manager and classic](/documentation/articles/resource-manager-deployment-model/).  This article covers using the classic deployment model. Azure recommends that most new deployments use the [Resource Manager deployment model](/documentation/articles/virtual-machines-how-to-automate-azure-resource-manager/).

Many tasks you do each day to manage your VMs can by automated by using the Azure Command-Line Interface (CLI) for Mac, Linux, and Windows. This article gives you example commands for simpler tasks, and links to articles that show the commands for more complex tasks.

>[AZURE.NOTE] If you haven't installed the Azure CLI yet, you can get instructions [here](/documentation/articles/xplat-cli-install/) and learn how to connect to your subscription [here](/documentation/articles/xplat-cli-connect/). You also need to configure the CLI in Azure Resource Manager (arm) mode.

## How to Use the Example Commands
You'll need to replace some of the text in the commands with text that's appropriate for your environment. The < and > symbols indicate text you need to replace. When you replace the text, remove the symbols but leave the quote marks in place.

> [AZURE.NOTE] If you want to programmatically store and manipulate the output of your console commands, you may want to use a JSON parsing tool such as **[jq](https://github.com/stedolan/jq)**, **[jsawk](https://github.com/micha/jsawk)**, or language libraries good for the task.

## Show information about a VM

This is a basic task you'll use often. Use it to get information about a VM, perform tasks on a VM, or get output to store in a variable.

To get info about the VM, run this command, replacing everything in the quotes, including the < and > characters:

     azure vm show -g <group name> -n <virtual machine name>

To store the output in a $vm variable as a JSON document, run:

    vmInfo=$(azure vm show -g <group name> -n <virtual machine name> --json)

or you can pipe the stdout to a file.

## Log on to a Linux-based virtual machine

Typically Linux machines are connected to through SSH. For more information, see [How to Use SSH with Linux on Azure](/documentation/articles/virtual-machines-linux-ssh-from-linux/).
Azure Resource Manager Overview
## Stop a VM

Run this command:

    azure vm stop <group name> <virtual machine name>

>[AZURE.IMPORTANT] Use this parameter to keep the virtual IP (VIP) of the cloud service in case it's the last VM in that cloud service. <br><br> If you use the StayProvisioned parameter, you'll still be billed for the VM.

## Start a VM

Run this command:
Azure Resource Manager Overview
    azure vm start <group name> <virtual machine name>

## Attach a Data Disk

You'll also need to decide whether to attach a new disk or one that contains data. For a new disk, the command creates the .vhd file and attaches it in the same command.

To attach a new disk, run this command:

     azure vm disk attach-new <resource-group> <vm-name> <size-in-gb>

To attach an existing data disk, run this command:

    azure vm disk attach <resource-group> <vm-name> [vhd-url]

## Create a Linux VM

To create a new Linux-based VM, you're going to need to have several values on hand, including a resource group name, a location, an image name, a vm name, and a storage account to store the backing .vhd image. Once you have the information you want to use, the Azure CLI can create an interactive session to prompt you for those values by typing:

    azure vm create

Of course, if you already have those values you can find the proper switches to pass them directly by typing `azure help vm create`.

## Next steps

* For more examples of Azure CLI usage with the Azure Resource Manager mode, see [Using the Azure CLI for Mac, Linux, and Windows with Azure Resource Management](/documentation/articles/xplat-cli-azure-resource-manager/).

* To learn more about Azure resources and their concepts, see [Azure Resource Manager Overview](/documentation/articles/resource-group-overview/).
