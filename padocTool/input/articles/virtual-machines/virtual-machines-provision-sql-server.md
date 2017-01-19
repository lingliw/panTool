<!-- deleted in Global -->

<properties
	pageTitle="Provision a SQL Server virtual machine | Azure"
	description="This tutorial teaches you how to create and configure a SQL Server VM on Azure."
	services="virtual-machines"
	documentationCenter=""
	authors="rothja"
	manager="jeffreyg"
	editor="monicar"
	tags="azure-service-management"	/>

<tags
	ms.service="virtual-machines"
	ms.date="12/22/2015"
	wacn.date=""/>

# Provision a SQL Server virtual machine in Azure

> [AZURE.SELECTOR]
- [Classic portal](/documentation/articles/virtual-machines-windows-classic-ps-sql-create/)
- [PowerShell](/documentation/articles/virtual-machines-windows-classic-ps-sql-create/)
- [Azure Resource Manager portal](/documentation/articles/virtual-machines-sql-server-provision-resource-manager/)

## Overview

> [AZURE.IMPORTANT] Azure has two different deployment models for creating and working with resources:  [Resource Manager and classic](/documentation/articles/resource-manager-deployment-model/).  This article covers using the classic deployment model. Azure recommends that most new deployments use the Resource Manager model.

The Azure virtual machine gallery includes several images that contain Microsoft SQL Server. You can select one of the virtual machine images from the gallery and with a few clicks you can provision the virtual machine to your Azure environment.

In this tutorial, you will:

* [Connect to the Azure classic portal and provision a virtual machine from the gallery](#Provision)
* [Open the virtual machine using Remote Desktop and complete setup](#RemoteDesktop)
* [Complete configuration steps to connect to the virtual machine using SQL Server Management Studio on another computer](#SSMS)
* [Next steps](#Optional)

>[AZURE.NOTE] This article describes how to provision a SQL Server VM with the existing portal. However, it is also possible to create and manage SQL Server VMs in the [new portal](https://manage.windowsazure.cn). There are some advantages to the new portal, such as defaulting to the use of Premium Storage, and other options, such as Automated Patching, Automated Backup, and AlwaysOn configurations. Future content will cover step-by-step instructions.

## <a id="Provision"></a>Provision a SQL Server virtual machine from the gallery

1. Log in to the [Azure classic portal](http://manage.windowsazure.cn) using your account. If you do not have an Azure account, visit [Azure trial](/pricing/1rmb-trial/).

2. On the Azure classic portal, at the bottom left of the web page, click **+NEW**, click **COMPUTE**, click **VIRTUAL MACHINE**, and then click **FROM GALLERY**.

3. On the **Choose an Image** page, click **SQL SERVER**. Then select a SQL Server image. Click the next arrow at the bottom right of the page.

	![Choose an Image](./media/virtual-machines-provision-sql-server/choose-sql-vm.png)

For the most up-to-date information on the supported SQL Server images on Azure, see [SQL Server on Azure Virtual Machines Overview](/documentation/articles/virtual-machines-windows-sql-server-iaas-overview/).

>[AZURE.NOTE] If you have a virtual machine created by using the platform image SQL Server Evaluation edition, you cannot upgrade it to a per-minute paid edition image in the gallery. You can choose one of the following two options:
>
> - You can create a new virtual machine by using the per-minute paid SQL Server edition from the gallery and migrate your database files to this new virtual machine by following the steps at [Migrating a Database to SQL Server on an Azure VM](/documentation/articles/virtual-machines-windows-migrate-sql/)
> - Or, you can upgrade an existing instance of SQL Server Evaluation edition to a different edition of SQL Server under the [License Mobility through Software Assurance on Azure](/pricing/license-mobility/) agreement by following the steps at [Upgrade to a Different Edition of SQL Server](https://msdn.microsoft.com/zh-cn/library/cc707783.aspx). For information on how to purchase the licensed copy of SQL Server, see [How to Buy SQL Server](http://www.microsoft.com/sqlserver/get-sql-server/how-to-buy.aspx).

4. On the first **Virtual Machine Configuration** page, provide the following information:
	- A **VERSION RELEASE DATE**. If multiple images are available, select the latest.
	- A unique **VIRTUAL MACHINE NAME**.
	- In the **NEW USER NAME** box, a unique user name for the machine's local administrator account.
	- In the **NEW PASSWORD** box, type a strong password.
	- In the **CONFIRM PASSWORD** box, retype the password.
	- Select the appropriate **SIZE** from the drop down list.

	![VM Configuration](./media/virtual-machines-provision-sql-server/4VM-Config.png)

	>[AZURE.NOTE] The size of the virtual machine is specified during provisioning:
 	>
	> - For production workloads, we recommend using Premium Storage with the following minimum recommended sizes: **DS3** for SQL Server Enterprise edition and **DS2** for SQL Server Standard edition. For more information, see [Performance Best Practices for SQL Server in Azure Virtual Machines](/documentation/articles/virtual-machines-windows-sql-performance/).
	> - The selected size limits the number of data disks you can configure. For most up-to-date information on available virtual machine sizes and the number of data disks that you can attach to a virtual machine, see [Virtual Machine Sizes for Azure](/documentation/articles/virtual-machines-linux-sizes/).

5. After entering your VM configuration details, click the next arrow on the bottom right to continue.

5. On the second **Virtual machine configuration** page, configure resources for networking, storage, and availability:
	- In the **Cloud Service** box, choose **Create a new cloud service**.
	- In the **Cloud Service DNS Name** box, provide the first portion of a DNS name of your choice, so that it completes a name in the format **TESTNAME.chinacloudapp.cn**
	- Select a **SUBSCRIPTION**, if you have multiple subscriptions to choose from. The choice determines which **storage accounts **are available.
	- In the **REGION/AFFINITY GROUP/VIRTUAL NETWORK** box, select a region where this virtual image will be hosted.
	- In the **Storage Account**, automatically generate an account, or select one from the list. Change the **SUBSCRIPTION** to see more accounts.
	- In the **AVAILABILITY SET** box, select **(none)**.
	- Read and accept the legal terms.


6. Click the next arrow to continue.


7. Click the check mark in the bottom right corner to continue.

8. Wait while Azure prepares your virtual machine. Expect the virtual machine status to proceed through:

	- **Starting (Provisioning)**
	- **Stopped**
	- **Starting (Provisioning)**
	- **Running (Provisioning)**
	- **Running**


## <a id="RemoteDesktop"></a>Open the VM using Remote Desktop to complete setup

1. When provisioning completes, click on the name of your virtual machine to go to the DASHBOARD page. At the bottom of the page, click **Connect**.

2. Click the **Open** button.

	![Click the Open button](./media/virtual-machines-provision-sql-server/click-open-to-connect.png)

3. At the **Windows Security** dialog box, click **Use another account**.

	![Click Use another account](./media/virtual-machines-provision-sql-server/credentials.png)

4. Use the name of the machine as the domain name, followed by your administrator name in this format: `machinename\username`. Type your password and connect to the machine.

4. The first time you log on, several processes will complete, including setup of your desktop, Windows updates, and completion of the Windows initial configuration tasks (sysprep). After Windows sysprep completes, SQL Server setup  completes configuration tasks. These tasks make cause a delay of a few minutes while they complete. `SELECT @@SERVERNAME` may not return the correct name until SQL Server setup completes, and SQL Server Management Studio may not be visible on the start page.

Once you are connected to the virtual machine with Windows Remote Desktop, the virtual machine works much like any other computer. Connect to the default instance of SQL Server with SQL Server Management Studio (running on the virtual machine) in the normal way.

## <a id="SSMS"></a>Connect to the SQL Server VM instance from SSMS on another computer

The following steps demonstrate how to connect to the SQL Server instance in over the internet using SQL Server Management Studio (SSMS). However, the same steps apply to making your SQL Server virtual machine accessible for your applications, running both on-premises and in Azure classic deployment model. If your virtual machine is deployed in resource manager model see [Connect to a SQL Server Virtual Machine on Azure (Resource Manager)](/documentation/articles/virtual-machines-windows-classic-sql-connect-resource-manager/)

Before you can connect to the instance of SQL Server from another VM or the internet, you must complete the following tasks as described in the sections that follow:

- [Create a TCP endpoint for the virtual machine](#create-a-tcp-endpoint-for-the-virtual-machine)
- [Open TCP ports in the Windows firewall](#open-tcp-ports-in-the-windows-firewall-for-the-default-instance-of-the-database-engine)
- [Configure SQL Server to listen on the TCP protocol](#configure-sql-server-to-listen-on-the-tcp-protocol)
- [Configure SQL Server for mixed mode authentication](#configure-sql-server-for-mixed-mode-authentication)
- [Create SQL Server authentication logins](#create-sql-server-authentication-logins)
- [Determine the DNS name of the virtual machine](#determine-the-dns-name-of-the-virtual-machine)
- [Connect to the Database Engine from another computer](#connect-to-the-database-engine-from-another-computer)

The connection path is summarized by the following diagram:

![Connecting to a SQL Server virtual machine](./media/virtual-machines-sql-server-connection-steps/SQLServerinVMConnectionMap.png)

[AZURE.INCLUDE [Connect to SQL Server in a VM Classic TCP Endpoint](../../includes/virtual-machines-sql-server-connection-steps-classic-tcp-endpoint.md)]

[AZURE.INCLUDE [Connect to SQL Server in a VM](../../includes/virtual-machines-sql-server-connection-steps.md)]

[AZURE.INCLUDE [Connect to SQL Server in a VM Classic Steps](../../includes/virtual-machines-sql-server-connection-steps-classic.md)]

## <a id="cdea"></a>Connect to the Database Engine from your application

If you can connect to an instance of SQL Server running on an Azure virtual machine by using Management Studio, you should be able to connect by using a connection string similar to the following.

	connectionString = "Server=tutorialtestVM.chinacloudapp.cn,57500;Integrated Security=false;User ID=<login_name>;Password=<your_password>"

For more information, see [How to Troubleshoot Connecting to the SQL Server Database Engine](http://social.technet.microsoft.com/wiki/contents/articles/how-to-troubleshoot-connecting-to-the-sql-server-database-engine.aspx).

## <a id="Optional"></a>Next Steps

You've seen how to create and configure a SQL Server on an Azure virtual machine using the platform image. In many cases, the next step is to migrate your databases to this new SQL Server VM. For database migration guidance, see [Migrating a Database to SQL Server on an Azure VM](/documentation/articles/virtual-machines-windows-migrate-sql/).

The following list provides additional resources for SQL Server in Azure virtual machines.

### Recommended resources for SQL Server on Azure VMs:
- [SQL Server on Azure Virtual Machines Overview](/documentation/articles/virtual-machines-windows-sql-server-iaas-overview/)

- [Connect to a SQL Server Virtual Machine on Azure](/documentation/articles/virtual-machines-windows-classic-sql-connect/)

- [Performance Best Practices for SQL Server in Azure Virtual Machines](/documentation/articles/virtual-machines-windows-sql-performance/)

- [Security Considerations for SQL Server in Azure Virtual Machines](/documentation/articles/virtual-machines-windows-sql-security/)

### High Availability and Disaster Recovery:
- [High Availability and Disaster Recovery for SQL Server in Azure Virtual Machines](/documentation/articles/virtual-machines-windows-sql-high-availability-dr/)

- [Backup and Restore for SQL Server in Azure Virtual Machines](/documentation/articles/virtual-machines-windows-sql-backup-recovery/)

### SQL Server Workloads in Azure:
- [SQL Server Business Intelligence in Azure Virtual Machines](/documentation/articles/virtual-machines-windows-classic-ps-sql-bi/)

### Whitepapers:
- [Understand Azure SQL Database and SQL Server in Azure Virtual Machines](/documentation/articles/data-management-azure-sql-database-and-sql-server-iaas/)

- [Application Patterns and Development Strategies for SQL Server in Azure Virtual Machines](/documentation/articles/virtual-machines-windows-sql-server-app-patterns-dev-strategies/)
