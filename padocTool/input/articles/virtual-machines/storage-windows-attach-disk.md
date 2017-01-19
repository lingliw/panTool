<!-- rename to virtual-machines-windows-classic-attach-disk -->

<properties
	pageTitle="Attach a disk to a VM | Azure"
	description="Attach a data disk to a Windows virtual machine created with the classic deployment model and initialize it."
	services="virtual-machines, storage"
	documentationCenter=""
	authors="cynthn"
	manager="timlt"
	editor="tysonn"
	tags="azure-service-management"/>

<tags
	ms.service="virtual-machines"
	ms.date="02/03/2016"
	wacn.date=""/>

# Attach a data disk to a Windows virtual machine created with the classic deployment model

> [AZURE.IMPORTANT] Azure has two different deployment models for creating and working with resources:  [Resource Manager and classic](/documentation/articles/resource-manager-deployment-model/).  This article covers using the classic deployment model. Azure recommends that most new deployments use the [Resource Manager model](/documentation/articles/virtual-machines-attach-disk-preview/).

If you need an additional data disk, you can attach an empty disk or an existing disk with data to a VM. In both cases, the disks are .vhd files that reside in an Azure storage account. In the case of a new disk, after you attach the disk, you'll also need to initialize it so it's ready for use by a Windows VM.

It's a best practice to use one or more separate disks to store a virtual machine's data. When you create an Azure virtual machine, it has a disk for the operating system mapped to drive C and a temporary disk mapped to drive D. **Do not use the temporary disk to store data**. As the name implies, the temporary disk provides temporary storage only. It offers no redundancy or backup because it doesn't reside in Azure Storage.

[AZURE.INCLUDE [howto-attach-disk-windows-linux](../../includes/howto-attach-disk-windows-linux.md)]

## <a id="initializeinWS"></a>How to: initialize a new data disk in Windows Server

1. Connect to the virtual machine. For instructions, see [How to log on to a virtual machine running Windows Server][logon].

2. After you log on to the virtual machine, open **Server Manager**. In the left pane, select **File and Storage Services**.

	![Open Server Manager](./media/storage-windows-attach-disk/fileandstorageservices.png)

3. Expand the menu and select **Disks**.

4. The **Disks** section lists the disks. In most cases, it will have disk 0, disk 1, and disk 2. Disk 0 is the operating system disk, disk 1 is the temporary disk, and disk 2 is the data disk you just attached to the VM. The new data disk will list the Partition as **Unknown**. Right-click the disk and select **Initialize**.

5.	You're notified that all data will be erased when the disk is initialized. Click **Yes** to acknowledge the warning and initialize the disk. Once complete, the Partion will be listed as **GPT**. Right-click the disk again and select **New Volume**.

6.	Complete the wizard using the default values. When the wizard is done, the **Volumes** section lists the new volume. The disk is now online and ready to store data.

	![Volume successfully initialized](./media/storage-windows-attach-disk/newvolumecreated.png)

> [AZURE.NOTE] The size of the VM determines how many disks you can attach to it. For details, see [Sizes for virtual machines](/documentation/articles/virtual-machines-linux-sizes/).

## Additional resources

[How to detach a disk from a Windows virtual machine](/documentation/articles/virtual-machines-windows-classic-detach-disk/)

[About disks and VHDs for virtual machines](/documentation/articles/virtual-machines-linux-about-disks-vhds/)

[logon]: /documentation/articles/virtual-machines-windows-classic-connect-logon/
