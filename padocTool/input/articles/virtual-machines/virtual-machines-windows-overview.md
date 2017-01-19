<!-- need to be verified -->

<properties
    pageTitle="Windows Virtual Machines Overview | Azure"
    description="Learn about creating and managing Windows virtual machines in Azure."
    services="virtual-machines-windows"
    documentationcenter=""
    author="davidmu1"
    manager="timlt"
    editor="tysonn"
    tags="azure-resource-manager,azure-service-management" />
<tags
    ms.assetid="fbae9c8e-2341-4ed0-bb20-fd4debb2f9ca"
    ms.service="virtual-machines-windows"
    ms.workload="infrastructure-services"
    ms.tgt_pltfrm="vm-windows"
    ms.devlang="na"
    ms.topic="get-started-article"
    ms.date="10/20/2016"
    wacn.date=""
    ms.author="davidmu" />

# Overview of Windows virtual machines in Azure
Azure Virtual Machines (VM) is one of several types of [on-demand, scalable computing resources](/documentation/articles/choose-web-site-cloud-service-vm/) that Azure offers. Typically, you choose a VM when you need more control over the computing environment than the other choices offer. This article gives you information about what you should consider before you create a VM, how you create it, and how you manage it.

An Azure VM gives you the flexibility of virtualization without having to buy and maintain the physical hardware that runs it. However, you still need to maintain the VM by performing tasks, such as configuring, patching, and installing the software that runs on it.

Azure virtual machines can be used in various ways. Some examples are:

* **Development and test** - Azure VMs offer a quick and easy way to create a computer with specific configurations required to code and test an application.
* **Applications in the cloud** - Because demand for your application can fluctuate, it might make economic sense to run it on a VM in Azure. You pay for extra VMs when you need them and shut them down when you don't.
* **Extended datacenter** - Virtual machines in an Azure virtual network can easily be connected to your organization's network.

The number of VMs that your application uses can scale up and out to whatever is required to meet your needs.

## What do I need to think about before creating a VM?
There are always a multitude of [design considerations](/documentation/articles/virtual-machines-windows-infrastructure-virtual-machine-guidelines/) when you build out an application infrastructure in Azure. These aspects of a VM are important to think about before you start:

* The names of your application resources
* The location where the resources are stored
* The size of the VM
* The maximum number of VMs that can be created
* The operating system that the VM runs
* The configuration of the VM after it starts
* The related resources that the VM needs

### Naming
A virtual machine has a [name](/documentation/articles/virtual-machines-windows-infrastructure-naming-guidelines/) assigned to it and it has a computer name configured as part of the operating system. The name of a VM can be up to 15 characters.

If you use Azure to create the operating system disk, the computer name and the virtual machine name are the same. If you [upload and use your own image](/documentation/articles/virtual-machines-windows-upload-image/) that contains a previously configured operating system and use it to create a virtual machine, the names can be different. We recommend that when you upload your own image file, you make the computer name in the operating system and the virtual machine name the same.

### Locations
All resources created in Azure are distributed across multiple [geographical regions](https://azure.microsoft.com/regions/) around the world. Usually, the region is called **location** when you create a VM. For a VM, the location specifies where the virtual hard disks are stored.

This table shows some of the ways you can get a list of available locations.

| Method | Description |
| --- | --- |
| Azure portal preview |Select a location from the list when you create a VM. |
| Azure PowerShell |Use the [Get-AzureRmLocation](https://msdn.microsoft.com/zh-cn/library/mt619449.aspx) command. |
| REST API |Use the [List locations](https://msdn.microsoft.com/zh-cn/library/dn790540.aspx) operation. |

### VM size
The [size](/documentation/articles/virtual-machines-windows-sizes/) of the VM that you use is determined by the workload that you want to run. The size that you choose then determines factors such as processing power, memory, and storage capacity. Azure offers a wide variety of sizes to support many types of uses.

Azure charges an [hourly price](/pricing/details/virtual-machines/windows/) based on the VM's size and operating system. For partial hours, Azure charges only for the minutes used. Storage is priced and charged separately.

### VM Limits
Your subscription has default [quota limits](/documentation/articles/azure-subscription-service-limits/) in place that could impact the deployment of many VMs for your project. The current limit on a per subscription basis is 20 VMs per region. Limits can be raised by filing a support ticket requesting an increase.

### Operating system disks and images
Virtual machines use [virtual hard disks (VHDs)](/documentation/articles/virtual-machines-windows-about-disks-vhds/) to store their operating system (OS) and data. VHDs are also used for the images you can choose from to install an OS. 

Azure provides many [marketplace images](https://azure.microsoft.com/marketplace/virtual-machines/) to use with various versions and types of Windows Server operating systems. Marketplace images are identified by image publisher, offer, sku, and version (typically version is specified as latest). 

This table shows some ways that you can find the information for an image.

| Method | Description |
| --- | --- |
| Azure portal preview |The values are automatically specified for you when you select an image to use. |
| Azure PowerShell |[Get-AzureRMVMImagePublisher](https://msdn.microsoft.com/zh-cn/library/mt603484.aspx) -Location "location"<BR>[Get-AzureRMVMImageOffer](https://msdn.microsoft.com/zh-cn/library/mt603824.aspx) -Location "location" -Publisher "publisherName"<BR>[Get-AzureRMVMImageSku](https://msdn.microsoft.com/zh-cn/library/mt619458.aspx) -Location "location" -Publisher "publisherName" -Offer "offerName" |
| REST APIs |[List image publishers](https://msdn.microsoft.com/zh-cn/library/mt743702.aspx)<BR>[List image offers](https://msdn.microsoft.com/zh-cn/library/mt743700.aspx)<BR>[List image skus](https://msdn.microsoft.com/zh-cn/library/mt743701.aspx) |

You can choose to [upload and use your own image](/documentation/articles/virtual-machines-windows-upload-image/) and when you do, the publisher name, offer, and sku aren't used.

### Extensions
VM [extensions](/documentation/articles/virtual-machines-windows-extensions-features/) give your VM additional capabilities through post deployment configuration and automated tasks.

These common tasks can be accomplished using extensions:

* **Run custom scripts** - The [Custom Script Extension](/documentation/articles/virtual-machines-windows-extensions-customscript/) helps you configure workloads on the VM by running your script when the VM is provisioned.
* **Deploy and manage configurations** - The [PowerShell Desired State Configuration (DSC) Extension](/documentation/articles/virtual-machines-windows-extensions-dsc-overview/) helps you set up DSC on a VM to manage configurations and environments.
* **Collect diagnostics data** - The [Azure Diagnostics Extension](https://azure.microsoft.com/blog/windows-azure-virtual-machine-monitoring-with-wad-extension/) helps you configure the VM to collect diagnostics data that can be used to monitor the health of your application.

### Related resources
The resources in this table are used by the VM and need to exist or be created when the VM is created.

| Resource | Required | Description |
| --- | --- | --- |
| [Resource group](/documentation/articles/resource-group-overview/) |Yes |The VM must be contained in a resource group. |
| [Storage account](/documentation/articles/storage-create-storage-account/) |Yes |The VM needs the storage account to store its virtual hard disks. |
| [Virtual network](/documentation/articles/virtual-networks-overview/) |Yes |The VM must be a member of a virtual network. |
| [Public IP address](/documentation/articles/virtual-network-ip-addresses-overview-arm/) |No |The VM can have a public IP address assigned to it to remotely access it. |
| [Network interface](/documentation/articles/virtual-network-network-interface-overview/) |Yes |The VM needs the network interface to communicate in the network. |
| [Data disks](/documentation/articles/virtual-machines-windows-attach-disk-portal/) |No |The VM can include data disks to expand storage capabilities. |

## How do I create my first VM?
You have several choices for creating your VM. The choice that you make depends on the environment you are in. 

This table provides information to get you started creating your VM.

| Method | Article |
| --- | --- |
| Azure portal preview |[Create a virtual machine running Windows using the portal](/documentation/articles/virtual-machines-windows-hero-tutorial/) |
| Templates |[Create a Windows virtual machine with a Resource Manager template](/documentation/articles/virtual-machines-windows-ps-template/) |
| Azure PowerShell |[Create a Windows VM using PowerShell](/documentation/articles/virtual-machines-windows-ps-create/) |
| Client SDKs |[Deploy Azure Resources using C#](/documentation/articles/virtual-machines-windows-csharp/) |
| REST APIs |[Create or update a VM](https://msdn.microsoft.com/zh-cn/library/mt163591.aspx) |

You hope it never happens, but occasionally something goes wrong. If this situation happens to you, look at the information in [Troubleshoot Resource Manager deployment issues with creating a Windows virtual machine in Azure](/documentation/articles/virtual-machines-windows-troubleshoot-deployment-new-vm/).

## How do I manage the VM that I created?
VMs can be managed using a browser-based portal, command-line tools with support for scripting, or directly through APIs. Some typical management tasks that you might perform are getting information about a VM, logging on to a VM, managing availability, and making backups.

### Get information about a VM
This table shows you some of the ways that you can get information about a VM.

| Method | Description |
| --- | --- |
| Azure portal preview |On the hub menu, click **Virtual Machines** and then select the VM from the list. On the blade for the VM, you have access to overview information, setting values, and monitoring metrics. |
| Azure PowerShell |For information about using PowerShell to manage VMs, see [Manage Azure Virtual Machines using Resource Manager and PowerShell](/documentation/articles/virtual-machines-windows-ps-manage/). |
| REST API |Use the [Get VM information](https://msdn.microsoft.com/zh-cn/library/mt163682.aspx) operation to get information about a VM. |
| Client SDKs |For information about using C# to manage VMs, see [Manage Azure Virtual Machines using Azure Resource Manager and C#](/documentation/articles/virtual-machines-windows-csharp-manage/). |

### Log on to the VM
You use the Connect button in the Azure portal preview to [start a Remote Desktop (RDP) session](/documentation/articles/virtual-machines-windows-connect-logon/). Things can sometimes go wrong when trying to use a remote connection. If this situation happens to you, check out the help information in [Troubleshoot Remote Desktop connections to an Azure virtual machine running Windows](/documentation/articles/virtual-machines-windows-troubleshoot-rdp-connection/).

### Manage availability
It's important for you to understand how to [ensure high availability](/documentation/articles/virtual-machines-windows-manage-availability/) for your application. This configuration involves creating multiple VMs to ensure that at least one is running.

In order for your deployment to qualify for our 99.95 VM Service Level Agreement, you need to deploy two or more VMs running your workload inside an [availability set](/documentation/articles/virtual-machines-windows-infrastructure-availability-sets-guidelines/). This configuration ensures your VMs are distributed across multiple fault domains and are deployed onto hosts with different maintenance windows. The full [Azure SLA](/support/sla/virtual-machines/) explains the guaranteed availability of Azure as a whole.

### Back up the VM
A [Recovery Services vault](/documentation/articles/backup-introduction-to-azure-backup/) is used to protect data and assets in both Azure Backup and Azure Site Recovery services. You can use a Recovery Services vault to [deploy and manage backups for Resource Manager-deployed VMs using PowerShell](/documentation/articles/backup-azure-vms-automation/). 

## Next steps
* If your intent is to work with Linux VMs, look at [Azure and Linux](/documentation/articles/virtual-machines-linux-azure-overview/).
* Learn more about the guidelines around setting up your infrastructure in the [Example Azure infrastructure walkthrough](/documentation/articles/virtual-machines-windows-infrastructure-example/).
* Make sure you follow the [Best Practices for running a Windows VM on Azure](/documentation/articles/virtual-machines-windows-guidance-compute-single-vm/).

