<properties
    pageTitle="How to resize a Linux VM | Azure"
    description="How to scale up or scale down a Linux virtual machine, by changing the VM size."
    services="virtual-machines-linux"
    documentationcenter="na"
    author="mikewasson"
    manager="timlt"
    editor=""
    tags="" />
<tags
    ms.assetid="e163f878-b919-45c5-9f5a-75a64f3b14a0"
    ms.service="virtual-machines-linux"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="na"
    ms.workload="infrastructure-services"
    ms.date="05/16/2016"
    wacn.date=""
    ms.author="mikewasson" />

# How to resize a Linux VM
## Overview
After you provision a virtual machine (VM), you can scale the VM up or down by changing the [VM size][vm-sizes]. In some cases, you must deallocate the VM first. This can happen if the new size is not available on the hardware cluster that is hosting the VM.

This article shows how to resize a Linux VM using the [Azure CLI][azure-cli].

[AZURE.INCLUDE [learn-about-deployment-models](../../includes/learn-about-deployment-models-rm-include.md)]

## Resize a Linux VM
To resize a VM, perform the following steps.

1. Run the following CLI command. This command lists the VM sizes that are available on the hardware cluster where the VM is hosted.

        azure vm sizes -g myResourceGroup --vm-name myVM

2. If the desired size is listed, run the following command to resize the VM.

        azure vm set -g myResourceGroup --vm-size <new-vm-size> -n myVM  \
            --enable-boot-diagnostics
            --boot-diagnostics-storage-uri https://mystorageaccount.blob.core.chinacloudapi.cn/ 

    The VM will restart during this process. After the restart, your existing OS and data disks will be remapped. Anything on the temporary disk will be lost.
   
    Use the `--enable-boot-diagnostics` option enables [boot diagnostics][boot-diagnostics], to log any errors related to startup.
3. Otherwise, if the desired size is not listed, run the following commands to deallocate the VM, resize it, and then restart the VM.

        azure vm deallocate -g myResourceGroup myVM
        azure vm set -g myResourceGroup --vm-size <new-vm-size> -n myVM \
            --enable-boot-diagnostics --boot-diagnostics-storage-uri \
            https://mystorageaccount.blob.core.chinacloudapi.cn/ 
        azure vm start -g myResourceGroup myVM

> [AZURE.WARNING]
   > Deallocating the VM also releases any dynamic IP addresses assigned to the VM. The OS and data disks are not affected.
   > 
   > 

## Next steps
For additional scalability, run multiple VM instances and scale out. For more information, see [Automatically scale Linux machines in a Virtual Machine Scale Set][scale-set]. 

<!-- links -->

[azure-cli]: /documentation/articles/xplat-cli-install/
[boot-diagnostics]: https://azure.microsoft.com/blog/boot-diagnostics-for-virtual-machines-v2/
[scale-set]: /documentation/articles/virtual-machine-scale-sets-linux-autoscale/
[vm-sizes]: /documentation/articles/virtual-machines-linux-sizes/
