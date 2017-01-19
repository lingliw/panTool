<properties
    pageTitle="Create and upload a Linux VHD | Azure"
    description="Create and upload an Azure virtual hard disk (VHD) with the classic deployment model that contains the Linux operating system."
    services="virtual-machines-linux"
    documentationcenter=""
    author="iainfoulds"
    manager="timlt"
    editor="tysonn"
    tags="azure-service-management" />
<tags
    ms.assetid="8058ff98-db03-4309-9bf4-69842bd64dd4"
    ms.service="virtual-machines-linux"
    ms.workload="infrastructure-services"
    ms.tgt_pltfrm="vm-linux"
    ms.devlang="na"
    ms.topic="article"
    ms.date="09/01/2016"
    wacn.date=""
    ms.author="iainfou" />

# Creating and Uploading a Virtual Hard Disk that Contains the Linux Operating System
[AZURE.INCLUDE [learn-about-deployment-models](../../includes/learn-about-deployment-models-classic-include.md)]

You can also [upload a custom disk image using Azure Resource Manager](/documentation/articles/virtual-machines-linux-upload-vhd/).

This article shows you how to create and upload a virtual hard disk (VHD) so you can use it as your own image to create virtual machines in Azure. Learn how to prepare the operating system so you can use it to create multiple virtual machines based on that image. 

> [AZURE.NOTE]
> If you have a few moments, please help us to improve the Azure Linux VM documentation by taking this [quick survey](https://aka.ms/linuxdocsurvey) of your experiences. Every answer helps us help you get your work done.
> 
> 

## Prerequisites
This article assumes that you have the following items:

* **Linux operating system installed in a .vhd file** - You have installed an [Azure-endorsed Linux distribution](/documentation/articles/virtual-machines-linux-endorsed-distros/) (or see [information for non-endorsed distributions](/documentation/articles/virtual-machines-linux-create-upload-generic/)) to a virtual disk in the VHD format. Multiple tools exist to create a VM and VHD:
  * Install and configure [QEMU](https://en.wikibooks.org/wiki/QEMU/Installing_QEMU) or [KVM](http://www.linux-kvm.org/page/RunningKVM), taking care to use VHD as your image format. If needed, you can [convert an image](https://en.wikibooks.org/wiki/QEMU/Images#Converting_image_formats) using `qemu-img convert`.
  * You can also use Hyper-V [on Windows 10](https://msdn.microsoft.com/virtualization/hyperv_on_windows/quick_start/walkthrough_install) or [on Windows Server 2012/2012 R2](https://technet.microsoft.com/zh-cn/library/hh846766.aspx).

> [AZURE.NOTE]
> The newer VHDX format is not supported in Azure. When you create a VM, specify VHD as the format. If needed, you can convert VHDX disks to VHD using [`qemu-img convert`](https://en.wikibooks.org/wiki/QEMU/Images#Converting_image_formats) or the [`Convert-VHD`](https://technet.microsoft.com/zh-cn/library/hh848454.aspx) PowerShell cmdlet. Further, Azure does not support uploading dynamic VHDs, so you need to convert such disks to static VHDs before uploading. You can use tools such as [Azure VHD Utilities for GO](https://github.com/Microsoft/azure-vhd-utils-for-go) to convert dynamic disks during the process of uploading to Azure.
> 
> 

* **Azure Command-line Interface** - Install the latest [Azure Command-Line Interface](/documentation/articles/virtual-machines-command-line-tools/) to upload the VHD.

## <a id="prepimage"></a> Step 1: Prepare the image to be uploaded
Azure supports various Linux distributions (see [Endorsed Distributions](/documentation/articles/virtual-machines-linux-endorsed-distros/)). The following articles guide you through how to prepare the various Linux distributions that are supported on Azure. After you complete the steps in the following guides, come back here once you have a VHD file that is ready to upload to Azure:

* **[CentOS-based Distributions](/documentation/articles/virtual-machines-linux-create-upload-centos/)**
* **[Debian Linux](/documentation/articles/virtual-machines-linux-debian-create-upload-vhd/)**
* **[Oracle Linux](/documentation/articles/virtual-machines-linux-oracle-create-upload-vhd/)**
* **[Red Hat Enterprise Linux](/documentation/articles/virtual-machines-linux-redhat-create-upload-vhd/)**
* **[SLES & openSUSE](/documentation/articles/virtual-machines-linux-suse-create-upload-vhd/)**
* **[Ubuntu](/documentation/articles/virtual-machines-linux-create-upload-ubuntu/)**
* **[Other - Non-Endorsed Distributions](/documentation/articles/virtual-machines-linux-create-upload-generic/)**

> [AZURE.NOTE]
> The Azure platform SLA applies to virtual machines running the Linux OS only when one of the endorsed distributions is used with the configuration details as specified under 'Supported Versions' in [Linux on Azure-Endorsed Distributions](/documentation/articles/virtual-machines-linux-endorsed-distros/). All Linux distributions in the Azure image gallery are endorsed distributions with the required configuration.
> 
> 

Also see the **[Linux Installation Notes](/documentation/articles/virtual-machines-linux-create-upload-generic/#general-linux-installation-notes)** for more general tips on preparing Linux images for Azure.

## <a id="connect"></a> Step 2: Prepare the connection to Azure
Make sure you are using the Azure CLI in the classic deployment model (`azure config mode asm`), then log in to your account:

    azure login -e AzureChinaCloud

## <a id="upload"></a> Step 3: Upload the image to Azure
You need a storage account to upload your VHD file to. You can either pick an existing storage account or [create a new one](/documentation/articles/storage-create-storage-account/).

Use the Azure CLI to upload the image by using the following command:

    azure vm image create <ImageName> `
        --blob-url <BlobStorageURL>/<YourImagesFolder>/<VHDName> `
        --os Linux <PathToVHDFile>

In the previous example:

* **BlobStorageURL** is the URL for the storage account you plan to use
* **YourImagesFolder** is the container within blob storage where you want to store your images
* **VHDName** is the label that appears in portal to identify the virtual hard disk.
* **PathToVHDFile** is the full path and name of the .vhd file on your machine.

The following shows a complete example:

    azure vm image create UbuntuLTS `
        --blob-url https://teststorage.blob.core.chinacloudapi.cn/vhds/UbuntuLTS.vhd `
        --os Linux /home/ahmet/UbuntuLTS.vhd

## Step 4: Create a VM from the image
You create a VM using `azure vm create` in the same way as a regular VM. Specify the name you gave your image in the previous step. In the following example, we use the **UbuntuLTS** image name given in the previous step:

    azure vm create --userName ops --password P@ssw0rd! --vm-size Small --ssh `
        --location "China North" "DeployedUbuntu" UbuntuLTS

To create your own VMs, provide your own username + password, location, DNS name, and image name.

## Next steps
For more information, see [Azure CLI reference for the Azure classic deployment model](/documentation/articles/virtual-machines-command-line-tools/).

[Step 1: Prepare the image to be uploaded]: #prepimage
[Step 2: Prepare the connection to Azure]: #connect
[Step 3: Upload the image to Azure]: #upload
