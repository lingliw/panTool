<!-- need to be verified -->

<properties
    pageTitle="Use a Linux troubleshooting VM with the CLI | Azure"
    description="Learn how to troubleshoot Linux VM issues by connecting the OS disk to a recovery VM using the Azure CLI"
    services="virtual-machines-linux"
    documentationCenter=""
    authors="iainfoulds"
    manager="timlt"
    editor="" />
<tags
    ms.service="virtual-machines-linux"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="vm-linux"
    ms.workload="infrastructure"
    ms.date="11/14/2016"
    wacn.date=""
    ms.author="iainfou" />

# Troubleshoot a Linux VM by attaching the OS disk to a recovery VM using the Azure CLI
If your Linux virtual machine (VM) encounters a boot or disk error, you may need to perform troubleshooting steps on the virtual hard disk itself. A common example would be an invalid entry in `/etc/fstab` that prevents the VM from being able to boot successfully. This article details how to use the Azure CLI to connect your virtual hard disk to another Linux VM to fix any errors, then re-create your original VM.


## Recovery process overview
The troubleshooting process is as follows:

1. Delete the VM encountering issues, keeping the virtual hard disks.
2. Attach and mount the virtual hard disk to another Linux VM for troubleshooting purposes.
3. Connect to the troubleshooting VM. Edit files or run any tools to fix issues on the original virtual hard disk.
4. Unmount and detach the virtual hard disk from the troubleshooting VM.
5. Create a VM using the original virtual hard disk.

Make sure that you have [the Azure CLI](/documentation/articles/xplat-cli-install/) logged in and using Resource Manager mode:

    azure config mode arm

In the following examples, replace parameter names with your own values. Example parameter names include `myResourceGroup`, `mystorageaccount`, and `myVM`.


## Determine boot issues
Examine the serial output to determine why your VM is not able to boot correctly. A common example is an invalid entry in `/etc/fstab`, or the underlying virtual hard disk being deleted or moved.

The following example gets the serial output from the VM named `myVM` in the resource group named `myResourceGroup`:

    azure vm get-serial-output --resource-group myResourceGroup --name myVM

Review the serial output to determine why the VM is failing to boot. If the serial output isn't providing any indication, you may need to review log files in `/var/log` once you have the virtual hard disk connected to a troubleshooting VM.


## View existing virtual hard disk details
Before you can attach your virtual hard disk to another VM, you need to identify the name of the virtual hard disk (VHD). 

The following example gets information for the VM named `myVM` in the resource group named `myResourceGroup`:

    azure vm show --resource-group myResourceGroup --name myVM

Look for `Vhd URI` in the output from the preceding command. The following truncated example output shows the `Vhd URI` on the last line:

    info:    Executing command vm show
    + Looking up the VM "myVM"
    + Looking up the NIC "myNic"
    + Looking up the public ip "myPublicIP"
    ...
    data:
    data:      OS Disk:
    data:        OSType                      :Linux
    data:        Name                        :myVM
    data:        Caching                     :ReadWrite
    data:        CreateOption                :FromImage
    data:        Vhd:
    data:          Uri                       :https://mystorageaccount.blob.core.chinacloudapi.cn/vhds/myVM201610292712.vhd

## Delete existing VM
Virtual hard disks and VMs are two distinct resources in Azure. A virtual hard disk is where the operating system itself, applications, and configurations are stored. The VM itself is just metadata that defines the size or location, and references resources such as a virtual hard disk or virtual network interface card (NIC). Each virtual hard disk has a lease assigned when attached to a VM. Although data disks can be attached and detached even while the VM is running, the OS disk cannot be detached unless the VM resource is deleted. The lease continues to associate the OS disk with a VM even when that VM is in a stopped and deallocated state.

The first step to recover your VM is to delete the VM resource itself. Deleting the VM leaves the virtual hard disks in your storage account. After the VM is deleted, you attach the virtual hard disk to another VM to troubleshoot and resolve the errors.

The following example deletes the VM named `myVM` from the resource group named `myResourceGroup`:

    azure vm delete --resource-group myResourceGroup --name myVM 

Wait until the VM has finished deleting before you attach the virtual hard disk to another VM. The lease on the virtual hard disk that associates it with the VM needs to be released before you can attach the virtual hard disk to another VM.


## Attach existing virtual hard disk to another VM
For the next few steps, you use another VM for troubleshooting purposes. You attach the existing virtual hard disk to this troubleshooting VM to browse and edit the disk's content. This process allows you to correct any configuration errors or review additional application or system log files, for example. Choose or create another VM to use for troubleshooting purposes.

When you attach the existing virtual hard disk, specify the URL to the disk obtained in the preceding `azure vm show` command. The following example attaches an existing virtual hard disk to the troubleshooting VM named `myVMRecovery` in the resource group named `myResourceGroup`:

    azure vm disk attach --resource-group myResourceGroup --name myVMRecovery \
        --vhd-url https://mystorageaccount.blob.core.chinacloudapi.cn/vhds/myVM.vhd

## Mount the attached data disk

1. SSH to your troubleshooting VM using the appropriate credentials. If this disk is the first data disk attached to your troubleshooting VM, the disk is likely connected to `/dev/sdc`. Use `dmseg` to view attached disks:

        dmesg | grep SCSI

    The output is similar to the following example:

        [    0.294784] SCSI subsystem initialized
        [    0.573458] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 252)
        [    7.110271] sd 2:0:0:0: [sda] Attached SCSI disk
        [    8.079653] sd 3:0:1:0: [sdb] Attached SCSI disk
        [ 1828.162306] sd 5:0:0:0: [sdc] Attached SCSI disk

    In the preceding example, the OS disk is at `/dev/sda` and the temporary disk provided for each VM is at `/dev/sdb`. If you had multiple data disks, they should be at `/dev/sdd`, `/dev/sde`, and so on.

2. Create a directory to mount your existing virtual hard disk. The following example creates a directory named `troubleshootingdisk`:

        sudo mkdir /mnt/troubleshootingdisk

3. If you have multiple partitions on your existing virtual hard disk, mount the required partition. The following example mounts the first primary partition at `/dev/sdc1`:

        sudo mount /dev/sdc1 /mnt/troubleshootingdisk

> [AZURE.NOTE]
    > Best practice is to mount data disks on VMs in Azure using the universally unique identifier (UUID) of the virtual hard disk. For this short troubleshooting scenario, mounting the virtual hard disk using the UUID is not necessary. However, under normal use, editing `/etc/fstab` to mount virtual hard disks using device name rather than UUID may cause the VM to fail to boot.


## Fix issues on original virtual hard disk
With the existing virtual hard disk mounted, you can now perform any maintenance and troubleshooting steps as needed. Once you have addressed the issues, continue with the following steps.


## Unmount and detach original virtual hard disk
Once your errors are resolved, you unmount and detach the existing virtual hard disk from your troubleshooting VM. You cannot use your virtual hard disk with any other VM until the lease attaching the virtual hard disk to the troubleshooting VM is released.

1. From the SSH session to your troubleshooting VM, unmount the existing virtual hard disk. Change out of the parent directory for your mount point first:

        cd /

    Now unmount the existing virtual hard disk. The following example unmounts the device at `/dev/sdc1`:

        sudo umount /dev/sdc1

2. Now detach the virtual hard disk from the VM. Exit the SSH session to your troubleshooting VM. In the Azure CLI, first list the attached data disks to your troubleshooting VM. The following example lists the data disks attached to the VM named `myVMRecovery` in the resource group named `myResourceGroup`:

        azure vm disk list --resource-group myResourceGroup --vm-name myVMRecovery

    Note the `Lun` value for your existing virtual hard disk. The following example command output shows the existing virtual disk attached at LUN 0:

        info:    Executing command vm disk list
        + Looking up the VM "myVMRecovery"
        data:    Name              Lun  DiskSizeGB  Caching  URI
        data:    ------            ---  ----------  -------  ------------------------------------------------------------------------
        data:    myVM              0                None     https://mystorageaccount.blob.core.chinacloudapi.cn/vhds/myVM.vhd
        info:    vm disk list command OK

    Detach the data disk from your VM using the applicable `Lun` value:

        azure vm disk detach --resource-group myResourceGroup --vm-name myVMRecovery \
            --lun 0

## Create VM from original hard disk
To create a VM from your original virtual hard disk, use [this Azure Resource Manager template](https://github.com/Azure/azure-quickstart-templates/tree/master/201-vm-specialized-vhd-existing-vnet). The actual JSON template is at the following link:

- https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/201-vm-specialized-vhd-existing-vnet/azuredeploy.json

The template deploys a VM into an existing virtual network, using the VHD URL from the earlier command. The following example deploys the template to the resource group named `myResourceGroup`:

    azure group deployment create --resource-group myResourceGroup --name myDeployment \
        --template-uri https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/201-vm-specialized-vhd-existing-vnet/azuredeploy.json

Answer the prompts for the template such as VM name (`myDeployedVM` the following example), OS type (`Linux`), and VM size (`Standard_DS1_v2`). The `osDiskVhdUri` is the same as previously used when attaching the existing virtual hard disk to the troubleshooting VM. An example of the command output and prompts is as follows:

    info:    Executing command group deployment create
    info:    Supply values for the following parameters
    vmName:  myDeployedVM
    osType:  Linux
    osDiskVhdUri:  https://mystorageaccount.blob.core.chinacloudapi.cn/vhds/myVM201610292712.vhd
    vmSize:  Standard_DS1_v2
    existingVirtualNetworkName:  myVnet
    existingVirtualNetworkResourceGroup:  myResourceGroup
    subnetName:  mySubnet
    dnsNameForPublicIP:  mypublicipdeployed
    + Initializing template configurations and parameters
    + Creating a deployment
    info:    Created template deployment "mydeployment"
    + Waiting for deployment to complete
    +

## Re-enable boot diagnostics

When you create your VM from the existing virtual hard disk, boot diagnostics may not automatically be enabled. The following example enables the diagnostic extension on the VM named `myDeployedVM` in the resource group named `myResourceGroup`:

    azure vm enable-diag --resource-group myResourceGroup --name myDeployedVM

## Next steps
If you are having issues connecting to your VM, see [Troubleshoot SSH connections to an Azure VM](/documentation/articles/virtual-machines-linux-troubleshoot-ssh-connection/). For issues with accessing applications running on your VM, see [Troubleshoot application connectivity issues on a Linux VM](/documentation/articles/virtual-machines-linux-troubleshoot-app-connection/).