<!-- rename to virtual-machines-windows-creation-choices -->

<properties
	pageTitle="Different ways to create a Windows VM | Azure"
	description="Lists the different ways to create a Windows virtual machine with Resource Manager."
	services="virtual-machines"
	documentationCenter=""
	authors="cynthn"
	manager="timlt"
	editor=""
	tags="azure-resource-manager"/>

<tags
	ms.service="virtual-machines"
	ms.date="10/22/2015"
	wacn.date=""/>

# Different ways to create a Windows virtual machine with Resource Manager

Azure offers different ways to create a virtual machine because virtual machines are suited for different users and purposes. This means that you need to make some choices about the virtual machine and how to create it. This article gives you a summary of these choices and links to instructions.

> [AZURE.NOTE] Azure has two different deployment models for creating and working with resources:  [Resource Manager and classic](/documentation/articles/resource-manager-deployment-model/).  This article covers using the Resource Manager deployment model, which Azure recommends for most new deployments instead of the classic deployment model.

Azure Resource Manager templates were recently introduced as a way to create and manage a virtual machine and its different resources as one logical deployment unit. Instructions for this approach are included below, where available. To learn more about Azure Resource Manager and how to manage resources as one unit, see the [Overview][].

## Tool choices

### GUI: Azure portal

The graphical user interface of the Azure classic portal is an easy way to try out a virtual machine, especially if you're just starting out with Azure. Use the Azure portal to create the virtual machine:

[Create a virtual machine running Windows][]

### Command shell: Azure CLI or Azure PowerShell

If you prefer working in a command shell, choose between the Azure command-line interface (CLI) for Mac and Linux users, or Azure PowerShell, which has cmdlets for Azure and a custom console.

For Azure CLI, see:

- [Equivalent Resource Manager and Service Management commands for virtual machine operations with the Azure CLI for Mac, Linux, and Windows][]
- [Deploy and manage virtual machines using Azure Resource Manager templates and the Azure CLI][].

For Azure PowerShell, see:

- [Create a Windows VM with Resource Manager and PowerShell][]
- [Create and preconfigure a Windows virtual machine with Resource Manager and Azure PowerShell][]
- [Deploy and manage virtual machines using Azure Resource Manager templates and PowerShell][]
- [Create a Windows virtual machine with a Resource Manager template and PowerShell][]

### Development environment: Visual Studio

[Deploy Azure resources using the Compute, Network, and Storage .NET libraries][]

## Operating system and image choices

Choose an image based on the operating system you want to run. Azure and its partners offer many images, some of which include applications and tools. Or, use one of your own images. Find the platform image that you need for your application by using the information in: [Navigate and select Azure virtual machine images with Windows PowerShell and the Azure CLI][].

<!-- LINKS -->
[overview]: /documentation/articles/resource-group-overview/

[Create a virtual machine running Windows]: /documentation/articles/virtual-machines-windows-classic-tutorial/

[Equivalent Resource Manager and Service Management commands for virtual machine operations with the Azure CLI for Mac, Linux, and Windows]: /documentation/articles/virtual-machines-windows-cli-manage/
[Deploy and manage virtual machines using Azure Resource Manager templates and the Azure CLI]: /documentation/articles/virtual-machines-deploy-rmtemplates-azure-cli/
[Create and preconfigure a Windows virtual machine with Resource Manager and Azure PowerShell]: /documentation/articles/virtual-machines-ps-create-preconfigure-windows-resource-manager-vms/
[Deploy and manage virtual machines using Azure Resource Manager templates and PowerShell]: /documentation/articles/virtual-machines-deploy-rmtemplates-powershell/
[Create a Windows VM with Resource Manager and PowerShell]: /documentation/articles/virtual-machines-create-windows-powershell-resource-manager/
[Create a Windows virtual machine with a Resource Manager template and PowerShell]: /documentation/articles/virtual-machines-create-windows-powershell-resource-manager-template/


[Navigate and select Azure virtual machine images with Windows PowerShell and the Azure CLI]: /documentation/articles/virtual-machines-linux-cli-ps-findimage/
[Deploy Azure resources using the Compute, Network, and Storage .NET libraries]: /documentation/articles/virtual-machines-arm-deployment/

[Sign in to the virtual machine]: /documentation/articles/virtual-machines-windows-classic-connect-logon/

[Base configuration test environment]: /documentation/articles/virtual-machines-windows-classic-test-config-env/

[Azure hybrid cloud test environments]: /documentation/articles/none/
