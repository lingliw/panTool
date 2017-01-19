<properties
    pageTitle="Attach a data disk to a Linux VM | Azure"
    description="How to attach new or existing data disk to a Linux VM in the Azure portal preview using the Resource Manager deployment model."
    services="virtual-machines-linux"
    documentationcenter=""
    author="cynthn"
    manager="timlt"
    editor=""
    tags="azure-resource-manager" />
<tags
    ms.assetid="5e1c6212-976c-4962-a297-177942f90907"
    ms.service="virtual-machines-linux"
    ms.workload="infrastructure-services"
    ms.tgt_pltfrm="vm-linux"
    ms.devlang="na"
    ms.topic="article"
    ms.date="07/06/2016"
    wacn.date=""
    ms.author="cynthn" />

# How to attach a data disk to a Linux VM in the Azure portal preview
This article shows you how to attach both new and existing disks to a Linux virtual machine through the Azure portal preview. You can also [attach a data disk to a Windows VM in the Azure portal preview](/documentation/articles/virtual-machines-windows-attach-disk-portal/). Before you do this, review these tips:

* The size of the virtual machine controls how many data disks you can attach. For details, see [Sizes for virtual machines](/documentation/articles/virtual-machines-linux-sizes/).
* To use Premium storage, you'll need a DS-series or GS-series virtual machine. You can use disks from both Premium and Standard storage accounts with these virtual machines. Premium storage is available in certain regions. For details, see [Premium Storage: High-Performance Storage for Azure Virtual Machine Workloads](/documentation/articles/storage-premium-storage/).
* Disks attached to virtual machines are actually .vhd files in an Azure storage account. For details, see [About disks and VHDs for virtual machines](/documentation/articles/virtual-machines-linux-about-disks-vhds/).
* For a new disk, you don't need to create it first because Azure creates it when you attach it.
* For an existing disk, the .vhd file must be available in an Azure storage account. You can use a .vhd that's already there, if it's not attached to another virtual machine, or upload your own .vhd file to the storage account.

[AZURE.INCLUDE [virtual-machines-common-attach-disk-portal](../../includes/virtual-machines-common-attach-disk-portal.md)]

## Next steps
After the disk is added, you need to prepare it for use. See in the virtual machine's operating system: "How to: Initialize a new data disk in Linux" in this [article](/documentation/articles/virtual-machines-linux-classic-attach-disk/#initialize-a-new-data-disk-in-linux).
