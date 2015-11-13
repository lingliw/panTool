<properties
	pageTitle="Different ways to create a Linux VM | Windows Azure"
	description="Lists the different ways to create a Linux virtual machine on Azure and gives links to further instructions."
	services="virtual-machines"
	documentationCenter=""
	authors="dsk-2015"
	manager="timlt"
	editor=""
	tags="azure-service-management,azure-resource-manager"/>

<tags
	ms.service="virtual-machines"
	ms.date="08/12/2015"
	wacn.date=""/>

# Different Ways to Create a Linux Virtual Machine

Azure offers different ways to create a VM because VMs are suited for different users and purposes. This means you'll need to make some choices about the VM and how you'll create it. This article gives you a summary of these choices and links to instructions.

Azure Resource Manager templates were recently introduced as a way to create and manage a virtual machine and its different resources as one logical deployment unit. Instructions for this approach are included below, where available. To learn more about Azure Resource Manager and how to manage resources as one unit, see the [overview][].

## Tool choices

### GUI: The Azure Portal or Preview Portal

The graphical user interface of the Azure portal is an easy way to try out a virtual machine, especially if you're just starting out with Azure. Use either the [Azure portal](http://manage.windowsazure.com) or the [Azure preview portal](http://portal.azure.com) to create the VM. For general instructions, see [Create a Custom Virtual Machine][] and select any Linux image from the **Gallery**. Note that the [Azure portal](http://manage.windowsazure.com) creates virtual machines using only the classic deployment model.

### Command Shell: Azure CLI or Azure PowerShell

If you prefer working in a command shell, choose between the Azure command-line interface (CLI) for Mac and Linux users, or Azure PowerShell, which has Windows PowerShell cmdlets for Azure and a custom console.

For Azure CLI, see [Create a Virtual Machine Running Linux][]. To use a template, see [Deploy and Manage Virtual Machines using Azure Resource Manager Templates and the Azure CLI][].

For Azure PowerShell, see [Use Azure PowerShell to create and preconfigure Linux-based Virtual Machines][]. To use a template, see [Deploy and Manage Virtual Machines using Azure Resource Manager Templates and PowerShell][].

### Development Environment: Visual Studio

[Creating a virtual machine for a website with Visual Studio][]

[Deploy Azure Resources Using the Compute, Network, and Storage .NET Libraries][]

## Operating System and Image Choices

Choose an image based on the operating system you want to run. Azure and its partners offer many images, some of which include applications and tools. Or, use one of your own images.

### Azure Images

These instructions show you how to use an Azure image to create a virtual machine that's customized with options for networking, load balancing, and more. See [How to Create a Custom Virtual Machine Running Linux in Azure][].

### Use Your Own Image

Use an image based on an existing Azure virtual machine by *capturing* that VM, or upload an image of your own, stored in a virtual hard disk (VHD):

- [How to Capture a Linux Virtual Machine to Use as a Template with the CLI][]
- [Creating and Uploading a Virtual Hard Disk that Contains the Linux Operating System][]

## Next Steps

[Log On to the Virtual Machine][]

[Attach a Data Disk][]

## Additional resources

[Base Configuration Test Environment][]

[Azure hybrid cloud test environments][]

[Equivalent Resource Manager and Service Management Commands for VM Operations with the Azure CLI for Mac, Linux, and Windows][]

<!-- LINKS -->
[overview]: /documentation/articles/resource-group-overview

[Create a Virtual Machine Running Windows]: /documentation/articles/virtual-machines-windows-tutorial
[Create a Virtual Machine Running Linux]: /documentation/articles/virtual-machines-linux-tutorial

[Equivalent Resource Manager and Service Management Commands for VM Operations with the Azure CLI for Mac, Linux, and Windows]:/documentation/articles/xplat-cli-azure-manage-vm-asm-arm 
[Deploy and Manage Virtual Machines using Azure Resource Manager Templates and the Azure CLI]: /documentation/articles/virtual-machines-deploy-rmtemplates-azure-cli
[Deploy and Manage Virtual Machines using Azure Resource Manager Templates and PowerShell]:  /documentation/articles/virtual-machines-deploy-rmtemplates-powershell
[Use Azure PowerShell to create and preconfigure Linux-based Virtual Machines]: /documentation/articles/virtual-machines-ps-create-preconfigure-linux-vms

[How to Create a Custom Virtual Machine Running Linux in Azure]: /documentation/articles/virtual-machines-linux-create-custom
[How to Capture a Linux Virtual Machine to Use as a Template with the CLI]: /documentation/articles/virtual-machines-linux-capture-image

[Creating and Uploading a Virtual Hard Disk that Contains the Linux Operating System]: /documentation/articles/virtual-machines-linux-create-upload-vhd

[Creating a virtual machine for a website with Visual Studio]: /documentation/articles/virtual-machines-dotnet-create-visual-studio-powershell
[Deploy Azure Resources Using the Compute, Network, and Storage .NET Libraries]: /documentation/articles/virtual-machines-arm-deployment

[Log On to the Virtual Machine]: /documentation/articles/virtual-machines-linux-how-to-log-on

[Attach a Data Disk]: /documentation/articles/virtual-machines-linux-how-to-attach-disk

[About Azure VM configuration settings]: https://msdn.microsoft.com/zh-CN/library/azure/dn763935.aspx
[Base Configuration Test Environment]: /documentation/articles/virtual-machines-base-configuration-test-environment
[Azure hybrid cloud test environments]: /documentation/articles/virtual-machines-hybrid-cloud-test-environments  

[Create a Virtual Machine Running Linux]: /documentation/articles/virtual-machines-linux-tutorial
[Create a Custom Virtual Machine]: /documentation/articles/virtual-machines-create-custom
