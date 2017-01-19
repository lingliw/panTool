<properties
    pageTitle="Attach a data disk to a Windows VM | Azure"
    description="How to attach new or existing data disk to a Windows VM in the Azure portal preview using the Resource Manager deployment model."
    services="virtual-machines-windows"
    documentationcenter=""
    author="cynthn"
    manager="timlt"
    editor=""
    tags="azure-resource-manager" />
<tags
    ms.assetid="3790fc59-7264-41df-b7a3-8d1226799885"
    ms.service="virtual-machines-windows"
    ms.workload="infrastructure-services"
    ms.tgt_pltfrm="vm-windows"
    ms.devlang="na"
    ms.topic="article"
    ms.date="11/02/2016"
    wacn.date=""
    ms.author="cynthn" />

# How to attach a data disk to a Windows VM in the Azure portal preview
This article shows you how to attach both new and existing disks to a Windows virtual machine through the Azure portal preview. You can also [attach a data disk to a Linux VM in the Azure portal preview](/documentation/articles/virtual-machines-linux-attach-disk-portal/). Before you do this, review these tips:

* The size of the virtual machine controls how many data disks you can attach. For details, see [Sizes for virtual machines](/documentation/articles/virtual-machines-windows-sizes/).
* For a new disk, you don't need to create it first because Azure creates it when you attach it.
* For an existing disk, the .vhd file must be available in an Azure storage account. You can use a .vhd that's already there, if it's not attached to another virtual machine, or upload your own .vhd file to the storage account.

You can also [attach a data disk using Powershell](/documentation/articles/virtual-machines-windows-ps-manage/#add-a-data-disk-to-a-virtual-machine).

[AZURE.INCLUDE [virtual-machines-common-attach-disk-portal](../../includes/virtual-machines-common-attach-disk-portal.md)]

## <a id="initializeinWS"></a>How to: initialize a new data disk in Windows Server
1. Connect to the virtual machine. For instructions, see [How to connect and log on to an Azure virtual machine running Windows](/documentation/articles/virtual-machines-windows-connect-logon/).
2. After you log on to the virtual machine, open **Server Manager**. In the left pane, select **File and Storage Services**.
   
    ![Open Server Manager](./media/virtual-machines-windows-classic-attach-disk/fileandstorageservices.png)
3. Expand the menu and select **Disks**.
4. The **Disks** section lists the disks. In most cases, it will have disk 0, disk 1, and disk 2. Disk 0 is the operating system disk, disk 1 is the temporary disk, and disk 2 is the data disk you just attached to the VM. The new data disk will list the Partition as **Unknown**. Right-click the disk and select **Initialize**.
5. You're notified that all data will be erased when the disk is initialized. Click **Yes** to acknowledge the warning and initialize the disk. Once complete, the partition will be listed as **GPT**. Right-click the disk again and select **New Volume**.
6. Complete the wizard using the default values. When the wizard is done, the **Volumes** section lists the new volume. The disk is now online and ready to store data.

    ![Volume successfully initialized](./media/virtual-machines-windows-classic-attach-disk/newvolumecreated.png)

> [AZURE.NOTE]
> The size of the VM determines how many disks you can attach to it. For details, see [Sizes for virtual machines](/documentation/articles/virtual-machines-linux-sizes/).
> 
> 

## Next steps
If you application needs to use the D: drive to store data, you can [change the drive letter of the Windows temporary disk](/documentation/articles/virtual-machines-windows-classic-change-drive-letter/).

