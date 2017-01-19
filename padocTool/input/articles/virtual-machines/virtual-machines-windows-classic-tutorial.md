<properties
    pageTitle="Create a VM in the Classic Management Portal | Azure"
    description="Create a Windows virtual machine in the Azure Classic Management Portal."
    services="virtual-machines-windows"
    documentationcenter=""
    author="cynthn"
    manager="timlt"
    editor=""
    tags="azure-service-management" />
<tags
    ms.assetid="1871f823-ebd7-4eff-9a22-8e2411555595"
    ms.service="virtual-machines-windows"
    ms.workload="infrastructure-services"
    ms.tgt_pltfrm="vm-windows"
    ms.devlang="na"
    ms.topic="article"
    ms.date="10/18/2016"
    wacn.date=""
    ms.author="cynthn" />

# Create a virtual machine running Windows in the Azure Classic Management Portal
> [AZURE.SELECTOR]
- [Azure Classic Management Portal](/documentation/articles/virtual-machines-windows-classic-tutorial/)
- [PowerShell: Classic deployment](/documentation/articles/virtual-machines-windows-classic-create-powershell/)

<br>

[AZURE.INCLUDE [learn-about-deployment-models](../../includes/learn-about-deployment-models-classic-include.md)]

Learn how to [perform these steps using the Resource Manager deployment model](/documentation/articles/virtual-machines-windows-hero-tutorial/) using the **new Azure portal preview**. 

This tutorial shows you how to create an Azure virtual machine (VM) running Windows in the Azure Classic Management Portal. We'll use a Windows Server image as an example, but that's just one of the many images Azure offers. Note that your image choices depend on your subscription. For example, Windows desktop images may be available to MSDN subscribers.

This section shows you how to use the **From Gallery** option in the Azure Classic Management Portal to create the virtual machine. This option provides more configuration choices than the **Quick Create** option. For example, if you want to join a virtual machine to a virtual network, you'll need to use the **From Gallery** option.

You can also create VMs using [your own images](/documentation/articles/virtual-machines-windows-classic-createupload-vhd/). To learn about this and other methods, see [Different ways to create a Windows virtual machine](/documentation/articles/virtual-machines-windows-creation-choices/).
## <a id="createvirtualmachine"> </a>Create the virtual machine
[AZURE.INCLUDE [virtual-machines-create-WindowsVM](../../includes/virtual-machines-create-windowsvm.md)]

## Next steps
* Learn how to [create a VM using the Resource Manager deployment model](/documentation/articles/virtual-machines-windows-hero-tutorial/) in the new Azure portal preview. 
* Log on to the virtual machine. For instructions, see [Log on to a virtual machine running Windows Server](/documentation/articles/virtual-machines-windows-classic-connect-logon/).
* Attach a disk to store data. You can attach both empty disks and disks that contain data. For instructions, see the [Attach a data disk to a Windows virtual machine created with the classic deployment model](/documentation/articles/virtual-machines-windows-classic-attach-disk/).

