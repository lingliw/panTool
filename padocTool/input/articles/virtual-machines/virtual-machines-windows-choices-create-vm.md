<properties
	pageTitle="Different ways to create a Windows virtual machine"
	description="Lists the different ways to create a Windows virtual machine and gives links to instructions."
	services="virtual-machines"
	documentationCenter=""
	authors="cynthn"
	manager="timlt"
	editor=""
	tags="azure-resource-manager,azure-service-management"/>

<tags
	ms.service="virtual-machines"
	ms.date="09/15/2015"
	wacn.date=""/>

# Different ways to create a Windows virtual machine

Azure offers different ways to create a virtual machine because virtual machines are suited for different users and purposes. This means that you need to make some choices about the virtual machine and how to create it. This article gives you a summary of these choices and links to instructions.

Azure Resource Manager templates were recently introduced as a way to create and manage a virtual machine and its different resources as one logical deployment unit. Instructions for this approach are included below, where available. To learn more about Azure Resource Manager and how to manage resources as one unit, see the [Overview][].

## Tool choices

### GUI: The Azure portal

The graphical user interface of the Azure portal is an easy way to try out a virtual machine, especially if you're just starting out with Azure. Use either the Azure portal or the Azure preview portal to create the VM:

[Create a virtual machine running Windows][]

### Command shell: Azure CLI or Azure PowerShell

If you prefer working in a command shell, choose between the Azure command-line interface (CLI) for Mac and Linux users, or Azure PowerShell, which has Windows PowerShell cmdlets for Azure and a custom console.

For Azure CLI, see [Equivalent Resource Manager and Service Management commands for virtual machine operations with the Azure CLI for Mac, Linux, and Windows][]. To use a template, see [Deploy and manage virtual machines using Azure Resource Manager templates and the Azure CLI][].

For Azure PowerShell, see [Use Azure PowerShell to create and preconfigure Windows virtual machines][] To use a template, see [Deploy and manage virtual machines using Azure Resource Manager templates and PowerShell][]. To create virtual machines in the Service Management stack, see [Use Azure PowerShell to create and preconfigure Windows virtual machines][].

### Development environment: Visual Studio

[Create a virtual machine for a website with Visual Studio][]

[Deploy Azure resources using the Compute, Network, and Storage .NET libraries][]

## Operating system and image choices

Choose an image based on the operating system you want to run. Azure and its partners offer many images, some of which include applications and tools. Or, use one of your own images.

### Azure images

These instructions show you how to use an Azure image to create a virtual machine that's customized with options for networking, load balancing, and more. See [How to create a custom virtual machine running Windows][].

### Use your own image

Use an image based on an existing Azure virtual machine by *capturing* that virtual machine, or upload an image of your own, stored in a virtual hard disk (VHD):

- [How to capture a Windows virtual machine to use as an image][]
- [Create and upload a Windows Server VHD to Azure][]

## Next steps

[Sign in to the virtual machine][]

[Attach a data disk][]

## Additional resources
[Base configuration test environment][]

[Azure hybrid cloud test environments][]

<!-- LINKS -->
[overview]: /documentation/articles/resource-group-overview

[Create a virtual machine running Windows]: /documentation/articles/virtual-machines-windows-tutorial

[Equivalent Resource Manager and Service Management commands for virtual machine operations with the Azure CLI for Mac, Linux, and Windows]:/documentation/articles/xplat-cli-azure-manage-vm-asm-arm
[Deploy and manage virtual machines using Azure Resource Manager templates and the Azure CLI]: /documentation/articles/virtual-machines-deploy-rmtemplates-azure-cli
[Create and preconfigure a Windows virtual machine with Resource Manager and Azure PowerShell]:  /documentation/articles/virtual-machines-ps-create-preconfigure-windows-resource-manager-vms
[Deploy and manage virtual machines using Azure Resource Manager templates and PowerShell]: /documentation/articles/virtual-machines-deploy-rmtemplates-powershell
[Use Azure PowerShell to create and preconfigure Windows virtual machines]: /documentation/articles/virtual-machines-ps-create-preconfigure-windows-vms
[How to create a custom virtual machine running Windows]: /documentation/articles/virtual-machines-windows-create-custom

[How to capture a Windows virtual machine to use as an image]:/documentation/articles/virtual-machines-capture-image-windows-server

[Create and upload a Windows Server VHD to Azure]: /documentation/articles/virtual-machines-create-upload-vhd-windows-server


[Create a virtual machine for a website with Visual Studio]: /documentation/articles/virtual-machines-dotnet-create-visual-studio-powershell
[Deploy Azure resources using the Compute, Network, and Storage .NET libraries]: /documentation/articles/virtual-machines-arm-deployment

[Sign in to the virtual machine]: /documentation/articles/virtual-machines-log-on-windows-server

[Attach a data disk]: /documentation/articles/storage-windows-attach-disk

[Base configuration test environment]: /documentation/articles/virtual-machines-base-configuration-test-environment

[Azure hybrid cloud test environments]: /documentation/articles/virtual-machines-hybrid-cloud-test-environments
