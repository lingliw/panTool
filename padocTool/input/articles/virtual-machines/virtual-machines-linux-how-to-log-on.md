<!-- rename to virtual-machines-linux-classic-log-on -->

<properties
	pageTitle="Log on to a Linux VM in Azure | Azure"
	description="Learn how to log on to an Azure virtual machine running Linux by using a Secure Shell (SSH) client."
	services="virtual-machines"
	documentationCenter=""
	authors="squillace"
	manager="timlt"
	editor=""
	tags="azure-service-management"/>

<tags
	ms.service="virtual-machines"
	ms.date="12/08/2015"
	wacn.date=""/>


#How to Log on to a Virtual Machine Running Linux #

> [AZURE.IMPORTANT] Azure has two different deployment models for creating and working with resources:  [Resource Manager and classic](/documentation/articles/resource-manager-deployment-model/).  This article covers using the classic deployment model. Azure recommends that most new deployments use the [Resource Manager deployment model](/documentation/articles/virtual-machines-linux-portal-create/).

You'll need to install an SSH client on the computer you want to use to log on to the virtual machine. There are many SSH client programs that you can choose from. The following are possible choices:

- On a computer running a Windows operating system, you might want to use an SSH client such as PuTTY. For more information, see the [PuTTY Download Page](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).
- For a virtual machine running a Linux operating system, you use a Secure Shell (SSH) client to log on; it is hard to think of a distribution that doesn't already have this installed by default. See [How to use SSH](/documentation/articles/virtual-machines-linux-ssh-from-linux/) for a bit more information about Linux.


>[AZURE.NOTE] For more requirements and troubleshooting tips, see [Connect to an Azure virtual machine with RDP or SSH](https://msdn.microsoft.com/zh-cn/library/azure/dn535788.aspx).

This procedure shows you how to use the PuTTY program to access the virtual machine.

1. Find the **Host Name** and **Port information** from the [Management Portal](http://manage.windowsazure.cn). You can find the information that you need from the dashboard of the virtual machine. Click the virtual machine name and look for the **SSH Details** in the **Quick Glance** section of the dashboard.

	![Obtain SSH details](./media/virtual-machines-linux-how-to-log-on/sshdetails.png)

2. Open the PuTTY program.

3. Enter the Host Name and the Port information that you collected from the dashboard, and then click **Open**.

	![Open PuTTY](./media/virtual-machines-linux-how-to-log-on/putty.png)

4. Log on to the virtual machine using the account that you specified when the machine was created. For more details on how to create a virtual machine with user name and password, see [Create a Virtual Machine Running Linux](/documentation/articles/virtual-machines-linux-quick-create-cli/).

	![Log on to the virtual machine](./media/virtual-machines-linux-how-to-log-on/sshlogin.png)

>[AZURE.NOTE] The VMAccess extension can help you reset the SSH key or password if you've forgotten it. If you've forgotten the user name, you can use the extension to create a new one with sudo authority. For instructions, see the [How to Reset a Password or SSH for Linux Virtual Machines].

You can now work with the virtual machine just as you would with any other server.

<!-- LINKS -->
[How to Reset a Password or SSH for Linux Virtual Machines]: /documentation/articles/virtual-machines-linux-classic-reset-access/
