<properties
	pageTitle="Create a virtual machine running Windows in Azure"
	description="Create a Windows virtual machine in the Azure portal."
	services="virtual-machines"
	documentationCenter=""
	authors="KBDAzure"
	manager="timlt"
	editor=""
	tags="azure-service-management"/>

<tags
	ms.service="virtual-machines"
	ms.date="08/11/2015"
	wacn.date=""/>

# Create a virtual machine running Windows in the Azure portal

> [AZURE.SELECTOR]
- [Azure portal](/documentation/articles/virtual-machines-windows-tutorial-classic-portal)
- [PowerShell: Resource Manager deployment](/documentation/articles/virtual-machines-deploy-rmtemplates-powershell)
- [PowerShell: Classic deployment](/documentation/articles/virtual-machines-ps-create-preconfigure-windows-vms)


This tutorial shows you how easy it is to create an Azure virtual machine (VM) in the Azure portal. We'll use a Windows Server image as an example, but that's just one of the many images Azure offers. Note that your image choices depend on your subscription. For example, desktop images may be available to MSDN subscribers.

You can also create VMs using [your own images](/documentation/articles/virtual-machines-create-upload-vhd-windows-server). To learn about this and other methods, see [Different ways to create a Windows virtual machine](/documentation/articles/virtual-machines-windows-choices-create-vm).


## <a id="createvirtualmachine"> </a>How to create the virtual machine

This section shows you how to use the **From Gallery** option in the Azure portal to create the virtual machine. This option provides more configuration choices than the **Quick Create** option. For example, if you want to join a virtual machine to a virtual network, you'll need to use the **From Gallery** option.

> [AZURE.NOTE] You can also try the richer, customizable [Azure Preview portal](https://manage.windowsazure.cn) to create a virtual machine, automate the deployment of multi-VM application templates, use enhanced VM monitoring and diagnostics features, and more. The available VM configuration options in the two portals overlap substantially but aren't identical.  

[AZURE.INCLUDE [virtual-machines-create-WindowsVM](../includes/virtual-machines-create-windowsvm.md)]

## Next steps

- Log on to the virtual machine. For instructions, see [How to log on to a virtual machine running Windows Server](/documentation/articles/virtual-machines-log-on-windows-server).

- Attach a disk to store data. You can attach both empty disks and disks that contain data. For instructions, see the [Attach a data disk tutorial](/documentation/articles/storage-windows-attach-disk).

## Additional resources

To learn more about what you can configure for a virtual machine and when you can do it, see [About Azure VM configuration settings](http://msdn.microsoft.com/zh-cn/library/azure/dn763935.aspx).
