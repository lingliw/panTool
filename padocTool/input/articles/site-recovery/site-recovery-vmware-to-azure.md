<properties
	pageTitle="Set up protection between on-premises VMware virtual machines or physical servers and Azure"
	description="Describes up Azure Site Recovery to coordinate the replication, failover and recovery of on-premises VMware virtual machines or Windows/Linux physical servers to Azure." 
	services="site-recovery"
	documentationCenter=""
	authors="rayne-wiselman"
	manager="jwhit"
	editor=""/>

<tags
	ms.service="site-recovery"
	ms.date="08/04/2015"
	wacn.date="05/15/2015"/>


# Set up protection between on-premises VMware virtual machines or physical servers and Azure

This article describes how to deploy Site Recovery to:

- **Protect VMware virtual machines**—Coordinate replication, failover, and recovery of on-premises VMware virtual machines to Azure
- **Protect physical servers**—Coordinate replication, failover, and recovery of on-premises physical Windows and Linux servers to Azure using the Azure Site Recovery service.

The article includes an overview, deployment prerequisites, and set up instructions. At the end of the article your VMware virtual machines or physical servers will be replicating to Azure.
If you run into problems, post your questions on the [Azure Recovery Services Forum](https://social.msdn.microsoft.com/forums/zh-cn/home?forum=hypervrecovmgr).


## What is Azure Site Recovery?

The Azure Site Recovery contributes to your business continuity and disaster recovery (BCDR) strategy by orchestrating replication, failover and recovery of virtual machines and physical servers. Machines can be replicated to Azure, or to a secondary on-premises data center. Read more about [Azure Site Recovery](/documentation/articles/site-recovery-overview).

## How does it protect on-premises resources?

Site Recovery helps protect your on-premises resources by orchestrating, simplifying replication, failover and failback in a number of [deployment scenarios](/documentation/articles/site-recovery-overview). If you want to protect your on-premises VMware virtual machines or Windows or Linux physical servers here's how Site Recovery can help:

- Allows VMware users to replicate virtual machines to Azure.
- Allows the replication of physical on-premises servers to Azure.
- Provides a single location to setup and manage replication, failover, and recovery.
- Provides easy failover from your on-premises infrastructure to Azure, and failback (restore) from Azure to on-premises.
- Implements recovery plans for easy failover of workloads that are tiered over multiple machines.
- Provides multi VM consistency so that virtual machines and physical servers running specific workloads can be recovered together to a consistent data point.
- Supports data replication over the Internet, over a site-to-site VPN connection, or over Azure ExpressRoute.
- Provides automated discovery of VMware virtual machines.


## What do I need?

This diagram shows the deployment components.

![New vault](./media/site-recovery-vmware-to-azure/ASRVMWare_Arch.png)

Here's what you'll need:

**Component** | **Deployment** | **Details**
--- | --- | ---
**Configuration server** | <p>Deploy as a Azure standard A3 virtual machine in the same subscription as Site Recovery.</p> <p>You set up in the Site Recovery portal</p> | This server coordinates communication between protected machines, the process server, and master target servers in Azure. It sets up replication and coordinates recovery in Azure when failover occurs.
**Master target server** | <p>Deploy as Azure virtual machine — Either a Windows server based on a Windows Server 2012 R2 gallery image (to protect Windows machines) or as a Linux server based on a OpenLogic CentOS 6.6 gallery image (to protect Linux machines).</p> <p>Three sizing options are available – Standard A4, Standard D14 and Standard DS4.<p><p>The server is connected to the same Azure network as the configuration server.</p><p>You set up in the Site Recovery portal</p> | <p>It receives and retains replicated data from your protected machines using attached VHDs created on blob storage in your Azure storage account.</p> <p>Select Standard DS4 specifically for configuring protection for workloads requiring consistent high performance and low latency using Premium Storage Account.</p>
**Process server** | <p>Deploy as an on-premises virtual or physical server running Windows Server 2012 R2</p> <p>We recommend it's placed on the same network and LAN segment as the machines that you want to protect, but it can run on a different network as long as protected machines have L3 network visibility to it.<p>You set it up and register it to the configuration server in the Site Recovery portal.</p> | <p>Protected machines send replication data to the on-premises process server. It has a disk-based cache to cache replication data that it receives. It performs a number of actions on that data.</p><p>It optimizes data by caching, compressing, and encrypting it before sending it on to the master target server.</p><p>It handles push installation of the Mobility Service.</p><p>It performs automatic discovery of VMware virtual machines.</p>
**On-premises machines** | On-premises virtual  machines running on a VMware hypervisor, or physical servers running Windows or Linux. | You set up replication settings that apply to virtual machines and servers. You can fail over an individual machine or more commonly, as part of a recovery plan containing multiple virtual machines that fail over together.
**Mobility service** | <p>Installs on each virtual machine or physical server you want to protect</p><p>Can be installed manually or pushed and installed automatically by the process server when protection is enabled for the server. | The Mobility service send data to the Process Server as part of initial replication (resync.) Once the server reaches a protected state(after resync is completed) the Mobility service performs an in-memory capture of writes to disk and sends it to the Process Server. Application consistency for Windows servers is achieved using the VSS framework.
**Azure Site Recovery vault** | Set up after you've subscribed to the Site Recovery service. | You register servers in a Site Recovery vault. The vault coordinates and orchestrates data replication, failover, and recovery between your on-premises site and Azure.
**Replication mechanism** | <p>**Over the Internet**—Communicates and replicates data from protected on-premises servers and Azure using a secure SSL/TLS communication channel over a public internet connection. This is the default option.</p><p>**VPN/ExpressRoute**—Communicates and replicates data between on-premises servers and Azure over a VPN connection. You'll need to set up a site-to-site VPN or an [ExpressRoute](../expressroute-introduction.md) connection between the on-premises site and your Azure network.</p><p>You'll select how you want to replicate during Site Recovery deployment. You can't change the mechanism after it's configured without impacting protection on already protected servers.| <p>Neither option requires you to open any inbound network ports on protected machines. All network communication is initiated from the on-premises site.</p> 

You can learn more about Site Recovery components, Providers and agents in [Site Recovery Components](site-recovery-components.md).

## Capacity planning

Main areas for considerations are:

- **Source environment**—The VMware infrastructure, source machine settings and requirements.
- **Component servers**—The process server, configuration server, and master target server 

### Considerations for the source environment

- **Maximum disk size**—The current maximum size of the disk that can be attached to a virtual machine is 1 TB. Thus the maximum size of a source disk that can be replicated is also limited to 1 TB.
- **Maximum size per source**—The maximum size of a single source machine is 31 TB (with 31 disks) and with a D14 instance provisioned for the master target server. 
- **Number of sources per master target server**—Multiple source machines can be protected with a single master target server. However, a single source machine can’t be protected across multiple master target servers, because as disks replicate, a VHD that mirrors the size of the disk is created on Azure blob storage and attached as a data disk to the master target server.  
- **Maximum daily change rate per source**—There are three factors that need to be considered when considering the recommended change rate per source. For the target based considerations two IOPS are required on the target disk for each operation on the source. This is because a read of old data and a write of the new data will happen on the target disk. 
	- **Daily change rate supported by the process server**—A source machine can't span multiple process servers. A single process server can support up to 1 TB of daily change rate. Hence 1 TB is the maximum daily data change rate supported for a source machine. 
	- **Maximum throughput supported by the target disk**—Maximum churn per source disk can't be more than 144 GB/day (with 8K write size). See the table in the master target section for the throughput and IOPs of the target for various write sizes. This number must be divided by two because each source IOP generates 2 IOPS on the target disk. Refer [Scalability and Performance Targets when using Premium Storage](../storage/storage-scalability-targets.md#scalability-targets-for-premium-storage-accounts) while configuring target for Premium Storage account.
	- **Maximum throughput supported by the storage account**—A source can't span multiple storage accounts. Given that a storage account takes a maximum of 20,000 requests per second and that each source IOP generates 2 IOPS at the master target server, we recommend you keep the number of IOPS across the source to 10,000. Refer [Scalability and Performance Targets when using Premium Storage](../storage/storage-scalability-targets.md#scalability-targets-for-premium-storage-accounts) while configuring source for Premium Storage account.

### Considerations for component servers

Table 1 summarizes the virtual machine sizes for the configuration and master target servers.

**Component** | **Deployed Azure instances** | **Cores** | **Memory** | **Max disks** | **Disk size**
--- | --- | --- | --- | --- | ---
Configuration server | Standard A3 | 4 | 7 GB | 8 | 1023 GB
Master target server | Standard A4 | 8 | 14 GB | 16 | 1023 GB
 | Standard D14 | 16 | 112 GB | 32 | 1023 GB
 | Standard DS4 | 8 | 28 GB | 16 | 1023 GB

**Table 1**

#### Process server considerations

Generally process server sizing depends on the daily change rate across all protected workloads. Primary considerations include:

-	You need sufficient compute to perform tasks such as inline compression and encryption.
-	Process server uses disk based cache. Make sure the recommended cache space and disk throughput is available to facilitate the data changes stored in the event of network bottleneck or outage. 
-	Ensure sufficient bandwidth  so that the process server can upload the data to the master target server to provide continuous data protection. 

Table 2 provides a summary of the process server guidelines.

**Data change rate** | **CPU** | **Memory** | **Cache disk size**| **Cache disk throughput** | **Bandwidth ingress/egress**
--- | --- | --- | --- | --- | ---
< 300 GB | 4 vCPUs (2 sockets * 2 cores @ 2.5GHz) | 4 GB | 600 GB | 7 to 10 MB per second | 30 Mbps/21 Mbps
300 to 600 GB | 8 vCPUs (2 sockets * 4 cores @ 2.5GHz) | 6 GB | 600 GB | 11 to 15 MB per second | 60 Mbps/42 Mbps
600 GB to 1 TB | 12 vCPUs (2 sockets * 6 cores @ 2.5GHz) | 8 GB | 600 GB | 16 to 20 MB per second | 100 Mbps/70 Mbps
> 1 TB | Deploy another process server | | | | 

**Table 2**

Where: 

- Ingress is download bandwidth (intranet between the source and process server).
- Egress is upload bandwidth (internet between the process server and master target server). Egress numbers presume average 30% process server compression.
- For cache disk a separate OS disk of minimum 128 GB is recommended for all process servers.
- For cache disk throughput the following storage was used for benchmarking: 8 SAS drives of 10 K RPM with RAID 10 configuration.

#### Configuration server considerations

Each configuration server can support up to 100 source machines with 3-4 volumes. If these numbers are exceeded we recommend you deploy another configuration server. See Table 1 for the default virtual machine properties of the configuration server. 

#### Master target server and storage account considerations

The storage for each master target server is comprised of an OS disk, a retention volume, and data disks. The retention drive maintains the journal of disk changes for the duration of the retention window defined in the Site Recovery portal.  Refer to Table 1 for the virtual machine properties of the master target server. Table 3 shows how the disks of A4 are used.

**Instance** | **OS disk** | **Retention** | **Data disks**
--- | --- | --- | ---
 | | **Retention** | **Data disks**
Standard A4 | 1 disk (1 * 1023 GB) | 1 disk ( 1 * 1023 GB) | 15 disks (15 * 1023 GB)
Standard D14 |  1 disk (1 * 1023 GB) | 1 disk ( 1 * 1023 GB) | 31 disks (15 * 1023 GB)
Standard DS4 |  1 disk (1 * 1023 GB) | 1 disk ( 1 * 1023 GB) | 15 disks (15 * 1023 GB)

**Table 3**

Capacity planning for the master target server depends on:

- Azure storage performance and limitations
	- The maximum number of highly utilized disks for a Standard Tier VM, is about 40 (20,000/500 IOPS per disk) in a single storage account. Refer [Scalability Targets for Standard Storage Accounts](../storage/storage-scalability-targets.md#scalability-targets-for-standard-storage-accounts) for more information. Similarly refer [Scalability Targets for Premium Storage Accounts](../storage/storage-scalability-targets.md#scalability-targets-for-premium-storage-accounts) for more information about Premium Storage account.
-	Daily change rate 
-	Retention volume storage.

Note that:

- One source can't span multiple storage accounts. This applies to the data disk that go to the storage accounts selected when you configure protection. The OS and the retention disks usually go to the automatically deployed storage account.
- The retention storage volume required depends on the daily change rate and the number of retention days. The retention storage required per master target server = total churn from source per day * number of retention days. 
- Each master target server has only one retention volume. The retention volume is shared across the disks attached to the master target server. For example:
	- If there's a source machine with 5 disks and each disk generates 120 IOPS (8K size) on the source, this translates to 240 IOPS per disk (2 operations on the target disk per source IO). 240 IOPS is within the Azure per disk IOPS limit of 500.
	- On the retention volume, this becomes 120 * 5 = 600 IOPS and this can become a bottle neck. In this scenario, a good strategy would be to add more disks to the retention volume and span it across, as a RAID stripe configuration. This will improve performance because the IOPS are distributed across multiple drives. The number of drives to be added to the retention volume will be as follows:
		- Total IOPS from source environment / 500
		- Total churn per day from source environment (uncompressed) / 287 GB. 287 GB is the maximum throughput supported by a target disk per day. This metric will vary based on the write size with a factor of 8K, because in this case 8K is thee assumed write size. For example, if the write size is 4K then throughput will be 287/2. And if the write size is 16K then throughput will be 287*2.
- The number of storage accounts required = total source IOPs/10000.


## Before you start

**Component** | **Requirements** | **Details**
--- | --- | --- 
**Azure account** | You'll need a [Microsoft Azure](http://azure.microsoft.com/) account. You can start with a [free trial](pricing/free-trial/).
**Azure storage** | <p>You'll need an Azure storage account to store replicated data</p><p>Either the account should be a [Standard Geo-redundant Storage Account](../storage/storage-redundancy.md#geo-redundant-storage) or [Premium Storage Account](../storage/storage-premium-storage-preview-portal.md).</p><p>It must in the same region as the Azure Site Recovery service, and be associated with the same subscription.</p><p>To learn more read [Introduction to Microsoft Azure Storage](../storage/storage-introduction.md)</p>
**Azure virtual network** | You'll need an Azure virtual network on which the configuration server and master target server will be deployed. It should be in the same subscription and region as the Azure Site Recovery vault. If you wish to replicate data over an ExpressRoute or VPN connection the Azure virtual network must be connected to your on-premises network over an ExpressRoute connection or a Site-to-Site VPN.
**Azure resources** | Make sure you have enough Azure resources to deploy all components. Read more in [Azure Subscription Limits](../azure-subscription-service-limits.md).
**Azure virtual machines** | <p>Virtual machines you want to protect should conform with [Azure prerequisites](site-recovery-best-practices.md).</p><p>**Disk count**—A maximum of 31 disks can be supported on a single protected server</p><p>**Disk sizes**—Individual disk capacity shouldn't be more than 1023 GB</p><p>**Clustering**—Clustered servers aren't supported</p><p>**Boot**—Unified Extensible Firmware Interface(UEFI)/Extensible Firmware Interface(EFI) boot isn't supported</p><p>**Volumes**—Bitlocker encrypted volumes aren't supported</p><p> **Server names**—Names should contain between 1 and 63 characters (letters, numbers and hyphens). The name must start with a letter or number and end with a letter or number. After a machine is protected you can modify the Azure name.</p>
**Configuration server** | <p>Standard A3 virtual machine based on an Azure Site Recovery Windows Server 2012 R2 gallery image will be created in your subscription for the configuration server. It's created as the first instance in a new cloud service. If you select Public Internet as the connectivity type for the Configuration Server the cloud service will be created with a reserved public IP address.</p><p>The installation path should be in English characters only.</p>
**Master target server** | <p>Azure virtual machine, standard A4, D14 or DS4.</p><p>The installation path  should be in English characters only. For example the path should be **/usr/local/ASR** for a master target server running Linux.</p></p>
**Process server** | <p>You can deploy the process server on physical or virtual machine running Windows Server 2012 R2 with the latest updates. Install on C:/.</p><p>We recommend you place the server on the same network and subnet as the machines you want to protect.</p><p>Install VMware vSphere CLI 5.5.0 on the process server. The VMware vSphere CLI component is required on the process server in order to discover virtual machines managed by a vCenter server or virtual machines running on an ESXi host.</p><p>The installation path should be in English characters only.</p>
**VMware** | <p>A VMware vCenter server managing your VMware vSphere hypervisors. It should be running vCenter version 5.1 or 5.5 with the latest updates.</p><p>One or more vSphere hypervisors containing VMware virtual machines you want to protect. The hypervisor should be running ESX/ESXi version 5.1 or 5.5 with the latest updates.</p><p>VMware virtual machines should have VMware tools installed and running.</p>
**Windows machines** | <p>Protected physical servers or VMware virtual machines running Windows have a number of requirements.</p><p>A supported 64-bit operating system: **Windows Server 2012 R2**, **Windows Server 2012**, or **Windows Server 2008 R2 with at least SP1**.</p><p>The host name, mount points, device names, Windows system path (eg: C:\Windows) should be in English only.</p><p>The operating system should be installed on C:\ drive.</p><p>Only basic disks are supported. Dynamic disks aren't supported.</p><p><Firewall rules on protected machines should allow them to reach the configuration and master target servers in Azure.p><p>You'll need to provide an administrator account (must be a local administrator on the Windows machine) to push install the Mobility Service on Windows servers. If the provided account is a non-domain account you'll need to disable Remote User Access control on the local machine. To do this add the LocalAccountTokenFilterPolicy DWORD registry entry with a value of 1 under HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System. To add the registry entry from a CLI open cmd or powershell and enter **`REG ADD HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1`**. [Learn more](https://msdn.microsoft.com/library/aa826699.aspx) about access control.</p><p>After failover, if you want connect to Windows virtual machines in Azure with Remote Desktop make sure that Remote Desktop is enabled for the on-premises machine. If you're not connecting over VPN, firewall rules should allow Remote Desktop connections over the internet.</p>
**Linux machines** | <p> A supported 64 bit operating system: **Centos 6.4, 6.5, 6.6**; **Oracle Enterprise Linux 6.4, 6.5 running either the Red Hat compatible kernel or Unbreakable Enterprise Kernel Release 3 (UEK3)**, **SUSE Linux Enterprise Server 11 SP3**.</p><p>Firewall rules on protected machines should allow them to reach the configuration and master target servers in Azure.</p><p>/etc/hosts files on protected machines should  contain entries that map the local host name to IP addresses associated with all NICs </p><p>If you want to connect to an Azure virtual machine running Linux after failover using a Secure Shell client (ssh), ensure that the Secure Shell service on the protected machine is set to start automatically on system boot, and that firewall rules allow an ssh connection to it.</p><p>The host name, mount points, device names, and Linux system paths and file names (eg /etc/; /usr) should be in English only.</p><p>Protection can be enabled for on-premises machines with the following storage:-<br>File system: EXT3, ETX4, ReiserFS, XFS<br>Multipath software-Device Mapper (multipath)<br>Volume manager: LVM2<br>Physical servers with HP CCISS controller storage are not supported.</p>
**Third-party** | Some deployment components in this scenario depend on third-party software to function properly. For a complete list see [Third-party software notices and information](#third-party)

## Deployment

The graphic summarizes the deployment steps.

![Deployment steps](./media/site-recovery-vmware-to-azure/VMWare2AzureSteps.png)

## Network connectivity Type

You have two options to configure network connectivity between your on-premises site and the Azure virtual network on which your Infrastructure components (Configuration Server, Master target Servers) are deployed. You'll need to decide which network connectivity option to use before you can deploy your Configuration Server. This is a deployment time choice, and cannot be changed later.

**Public Internet :** Communication and replication of data between the on-premises servers (Process Server, Protected Servers) and the Azure Infrastructure component servers (Configuration Server, Master Target Server) happens over a secure SSL/TLS connection from on-premises to the Public endpoints on the Configuration Server and the Master Target server. (The only exception is the connection between the Process Server and the Master Target server on TCP port 9080 which is un-encrypted. Only control information related to the replication protocol related used to setup the replication is exchanged on this connection.)

![Deployment diagram internet](./media/site-recovery-vmware-to-azure/ASRVmware_deploymentInternet.png)

**VPN :** Communication and replication of data between the on-premises servers (Process Server, Protected Servers) and the Azure Infrastructure component servers (Configuration Server, Master Target Server) happens over a VPN connection between your on-premises network and the Azure virtual network on which the Configuration server and Master Target servers are deployed. Ensure that your on-premises network is connected to the Azure virtual network by an ExpressRoute connection or a site-to-site VPN connection.

![Deployment diagram VPN](./media/site-recovery-vmware-to-azure/ASRVmware_deploymentVPN.png)


## Step 1: Create a vault

1. Sign in to the [Management Portal](https://portal.azure.com).


2. Expand **Data Services** > **Recovery Services** and click **Site Recovery Vault**.


3. Click **Create New** > **Quick Create**.

4. In **Name**, enter a friendly name to identify the vault.

5. In **Region**, select the geographic region for the vault. To check supported regions see Geographic Availability in [Azure Site Recovery Pricing Details](/home/features/site-recovery/#price)

6. Click **Create vault**.

	![New vault](./media/site-recovery-vmware-to-azure/ASRVMWare_CreateVault.png)

Check the status bar to confirm that the vault was successfully created. The vault will be listed as **Active** on the main **Recovery Services** page.

## Step 2: Deploy a configuration server

### Configure server settings

1. In the **Recovery Services** page, click the vault to open the Quick Start page. Quick Start can also be opened at any time using the icon.

	![Quick Start Icon](./media/site-recovery-vmware-to-azure/ASRVMWare_QuickStartIcon.png)

2. In the dropdown list, select **Between an on-premises site with VMware/physical servers and Azure**.
3. In **Prepare Target(Azure) Resources** click **Deploy Configuration Server**.

	![Deploy configuration server](./media/site-recovery-vmware-to-azure/ASRVMWare_DeployCS2.png)

4. In **New Configuration Server Details** specify:

	- A name for the configuration server and credentials to connect to it.
	- In the network connectivity type drop down select Public Internet or VPN.
	[AZURE.NOTE] This setting is a deployment time choice you make and cannot be changed later.  
	- Select the Azure network on which the server should be located. If you specified VPN as the network connectivity type ensure that this Azure vnet is connected to your on-premises site over an ExpressRoute connection or a site-to-site VPN.
	- Specify the internal IP address and subnet to assign to the server. Note that the first four IP addresses in any subnet are reserved for internal Azure usage. Use any other available IP address.
	
	![Deploy configuration server](./media/site-recovery-vmware-to-azure/ASRVMware_CSDetails2.png)

5. When you click **OK** a standard A3 virtual machine based on an Azure Site Recovery Windows Server 2012 R2 gallery image will be created in your subscription for the configuration server. It's created as the first instance in a new cloud service. If you specified the network connectivity type to be Public Internet the cloud service is created with a reserved public IP address. You can monitor progress in the **Jobs** tab.

	![Monitor progress](./media/site-recovery-vmware-to-azure/ASRVMWare_MonitorConfigServer.png)

6.  **This step is applicable only if your connectivity type is Public Internet.** After the configuration server is deployed note the public IP address assigned to it on the **Virtual Machines** page in the Azure portal. Then on the **Endpoints** tab note the public HTTPS port mapped to private port 443. You'll need this information later when you register the master target and process servers with the configuration server. The configuration server is deployed with these endpoints:

	- HTTPS: Public port is used to coordinate communication between component servers and Azure over the internet. Private port 443 is used to coordinate communication between component servers and Azure over VPN.
	- Custom: Public port is used for failback tool communication over the inter
	- net. Private port 9443 is used for failback tool communication over VPN.
	- PowerShell: Private port 5986
	- Remote desktop: Private port 3389
	
	![VM endpoints](./media/site-recovery-vmware-to-azure/ASRVMWare_VMEndpoints.png)

    >[AZURE.WARNING] Don't delete or change the public or private port number of any of the endpoints created during configuration server deployment.

The configuration server is deployed in an automatically created Azure cloud service with a reserved IP address. The reserved address is needed to ensure that the Configuration Server cloud service IP address remains the same across reboots of the virtual machines (including the configuration server) on the cloud service. The reserved public IP address will need to be manually unreserved when the configuration server is decommissioned or it'll remain reserved. There's a default limit of 20 reserved public IP addresses per subscription. [Find out more](../virtual-network/virtual-networks-reserved-private-ip.md) about reserved IP addresses. 

### Register the configuration server in the vault

1. In the **Quick Start** page click **Prepare Target Resources** > **Download a registration key**. The key file is generated automatically. It's valid for 5 days after it's generated. Copy it to the configuration server.
2. In **Virtual Machines** select the configuration server from the virtual machines list. Open the **Dashboard** tab and click **Connect**. **Open** the downloaded RDP file to log onto the configuration server using Remote Desktop. If your Configuration server is deployed on a VPN network, use the internal IP address (this is the IP address you specified when you deployed the configuration server and can also be seen on the virtual machines dashboard page for the configuration server virtual machine) of the configuration server to Remote desktop to it from your on-premises network. The Azure Site Recovery Configuration Server Setup Wizard runs automatically when you log on for the first time.

	![Registration](./media/site-recovery-vmware-to-azure/ASRVMWare_RegistrationSplashscreen.png)

3. In **Third-Party Software Installation** click **I Accept** to download and install MySQL.

	![MySQL install](./media/site-recovery-vmware-to-azure/ASRVMWare_RegistrationMySQLEULA.png)

4. In **MySQL Server Details** create credentials to log onto the MySQL server instance.

	![MySQL credentials](./media/site-recovery-vmware-to-azure/ASRVMWare_RegistrationMySQLPWD.png)

5. In **Internet Settings** specify how the configuration server will connect to the internet. Note that:

	- If you want to use a custom proxy you should set it up before you install the Provider.
	- When you click **Next** a test will run to check the proxy connection.
	- If you do use a custom proxy, or your default proxy requires authentication you'll need to enter the proxy details, including the address, port, and credentials.
	- The following URLs should be accessible via the proxy:
		- *.hypervrecoverymanager.windowsazure.cn
		- *.accesscontrol.chinacloudapi.cn
		- *.backup.windowsazure.cn
		- *.blob.core.chinacloudapi.cn
		- *.store.core.chinacloudapi.cn
	- If you have IP address-based firewall rules ensure that the rules are set to allow communication from the configuration server to the IP addresses described in [Azure Datacenter IP Ranges](https://msdn.microsoft.com/en-us/library/azure/dn175718.aspx) and HTTPS (443) protocol. You would have to white-list IP ranges of the Azure region that you plan to use, and that of West US.

	![Registration](./media/site-recovery-vmware-to-azure/ASRVMWareRegister1.png)

3. Follow the wizard instructions. You'll need to download and install MySQL Server and specify credentials for it. On the **Azure Site Recovery Registration** page browse to the key file you copied to the server.

	![Registration key](./media/site-recovery-vmware-to-azure/ASRVMWareRegister2.png)

4. After registration finishes a passphrase is generated. Copy it to a secure location. You'll need it to authenticate and register the process and master target servers with the configuration server. It's also used to ensure channel integrity in configuration server communications. You can regenerate the passphrase but then you'll need to reregister the master target and process servers using the new passphrase.

	![Passphrase](./media/site-recovery-vmware-to-azure/ASRVMWareRegister2.png)

After registration the configuration server will be listed on the **Configuration Servers** page in the vault. To route configuration server internet communication via a proxy server, run C:\Program Files\Microsoft Azure Site Recovery Provider\DRConfigurator.exe and specify the  proxy server to use. You'll need to re-register to Azure Site Recovery using the registration key you downloaded and copied to the configuration server.  

## Step 4: Set up a VPN connection

You can connect to the configuration server over the internet or using a VPN or ExpressRoute connection. An internet connection uses the endpoints of the virtual machine in conjunction with the public virtual IP address of the server. VPN uses the internal IP address of the server together with the endpoint private ports.

You can configure a VPN connection to the server as follows:

1. If you don't have a site-to-site or Azure ExpressRoute connection set up you can learn more here:

	- [Configure a site-to-site connection to an Azure virtual machine](https://msdn.microsoft.com/zh-CN/library/azure/dn133795.aspx)
	- [Configure ExpressRoute](https://msdn.microsoft.com/zh-CN/library/azure/dn606306.aspx)

2. In the vault click **Servers** > **Configuration Servers** > configuration server > **Configure**.
3. In **Connectivity Settings** set **Connectivity Type** to **VPN**. Note that if you have VPN set up and no internet access from the on-premises site make sure you select the VPN option. If you don't the process server won't be able to send replication data to the master target server on its public endpoints.

	![Enable VPN](./media/site-recovery-vmware-to-azure/ASRVMWare_EnableVPN.png)

## Step 5: Deploy the master target server

1. In **Prepare Target(Azure) Resources**, click **Deploy master target server**.
2. Specify the master target server details and credentials. The server will be deployed in the same Azure network as the configuration server you register it to. When you click to complete an Azure virtual machine will be created with a Windows or Linux gallery image.

	![Target server settings](./media/site-recovery-vmware-to-azure/ASRVMWare_TSDetails.png)

    **Note:** The first four IP addresses in any subnet are reserved for internal Azure usage. Specify any other available IP address.

3. A Windows master target server virtual machine is created with these endpoints:

	- Custom: Public port is used by the process server to send replication data over the internet. Private port 9443 is used by the process server to send replication data to the master target server over VPN.
	- Custom1: Public port is used by the process server to send control meta-data over the internet. Private port 9080 is used by process server to send control meta-data to the master target server over VPN.
	- PowerShell: Private port 5986
	- Remote desktop: Private port 3389

    **Note:** Don't delete or change the public or private port number of any of the endpoints created during the master target server deployment.

4. A Linux master target server virtual machine is created with these endpoints:

	- Custom: Public port is used by the process server to send replication data over the internet. Private port 9443 is used by the process server to send replication data to the master target server over VPN.
	- Custom1: Public port is used by the process server to send control meta-data over the internet. Private port 9080 is used by the process server to send control data to the master target server over VPN
	- SSH: Private port 22

    **Note:** Don't delete or change the public or private port number of any of the endpoints created during the master target server deployment.

5. In **Virtual Machines** wait for the virtual machine to start.

	- If you've configured the server with Windows note down the remote desktop details.
	- If you configured with Linux and you're connecting over VPN note the internal IP address of the virtual machine. If you're connecting over the internet note the public IP address.

6.  Log onto the server to complete installation and register it with the configuration server. If you're running Windows:

	1. Initiate a remote desktop connection to the virtual machine. The first time you log on a script will run in a PowerShell window. Don't close it. When it finishes the Host Agent Config tool opens automatically to register the server.
	2. In **Host Agent Config** specify the internal IP address of the configuration server and port 443. You can use the internal address and private port 443 even if you're not connecting over VPN mode because the virtual machine is attached to the same Azure network as the configuration server. Leave **Use HTTPS** enabled. Enter the passphrase for the configuration server that you noted earlier. Click **OK** to register server. Note that you can ignore the NAT options on the page. They're not used.

	![Windows master target server](./media/site-recovery-vmware-to-azure/ASRVMWare_TSRegister.png)

6. If you're running Linux:
	1. Copy the [server installer tar file](http://go.microsoft.com/fwlink/?LinkID=529757&clcid=0x409) to the virtual machine using an sftp client.Alternatively you can log on and use wget to download the the file from the link in the Quick Start page.
	2. Log onto the server using a Secure Shell client. Note that if you're connected to the Azure network over VPN use the internal IP address. Otherwise use the external IP address and the SSH public endpoint.
	3. Extract the files from the gzipped installer by running: **tar –xvzf Microsoft-ASR_UA_8.2.0.0_RHEL6-64***.”

		![Linux master target server](./media/site-recovery-vmware-to-azure/ASRVMWare_TSLinuxTar.png)

	4. Make sure you're in the directory to which you extracted the contents of the tar file and run the command “**sudo ./install.sh**”. Select option **2. Master Target**. Leave the other options with the default settings.

		![Register target server](./media/site-recovery-vmware-to-azure/ASRVMWare_TSLinux.png)

	5. After the installation finishes the command line **Host Config Interface** appears. Don't resize the window.
	6. Use the arrow keys to select **Global** and press Enter.
	7. In **Enter the IP address** enter  the internal address of the configuration server and port 22.
	8.  Specify the passphrase of the configuration server that you noted down earlier, and press enter. Select **Quit** to finish installation. Note that if you're using PuTTY client to ssh into the virtual machne you can use Shift+Insert to paste.
	9.  Use the right arrow key to quit and press Enter.

		![Master target server settings](./media/site-recovery-vmware-to-azure/ASRVMWare_TSLinux2.png)

7. Wait for a few minutes (5-10) and on the **Servers** > **Configuration Servers** page check that the master target server is listed as registered on the **Server Details** tab. If you're running Linux and  it didn't register run the host config tool again from /usr/local/ASR/Vx/bin/hostconfigcli. You'll need to set access permissions by running chmod as super user.

	![Verify target server](./media/site-recovery-vmware-to-azure/ASRVMWare_TSList.png)

## Step 6: Deploy on-premises process server

1. Click Quick Start > **Install Process Server on-premises** > **Download and install the process server**.

	![Install process server](./media/site-recovery-vmware-to-azure/ASRVMWare_PSDeploy.png)

2. Copy the downloaded zip file to the server on which you're going to install the process server. The zip file contains two installation files:

	- Microsoft-ASR_CX_TP_8.2.0.0_Windows*
	- Microsoft-ASR_CX_8.2.0.0_Windows*

3. Unzip the archive and copy the installation files to a location on the server.
4. Run the **Microsoft-ASR_CX_TP_8.2.0.0_Windows*** installation file and follow the instructions. This installs third-party components needed for the deployment.
5. Then run **Microsoft-ASR_CX_8.2.0.0_Windows***.
6. On the **Server Mode** page select **Process Server**.
7.	In **Configuration Server Details** if you're connecting over VPN specify the internal IP address of the configuration server and 443 for the port. Otherwise specify the public virtual IP address and mapped public HTTP endpoint.
8.	Clear **Verify Mobility service software signature** if you want to disable verification when you use automatic push to install the service. Signature verification needs internet connectivity from the process server.
9.	Type in the passphrase of the configuration server.

	![Register configuration server](./media/site-recovery-vmware-to-azure/ASRVMWare_CSRegister.png)

8. Finish installing the server. Remember that you'll need to install VMware vSphere CLI 5.1 on the server to be able to discover vCenter Servers. If you install VMware vSphere CLI 5.1 after the process server installation is complete, remember to reboot the process server.

	![Register process server](./media/site-recovery-vmware-to-azure/ASRVMWare_PSRegister2.png)

Validate that the process server registered successfully in the vault > **Configuration Server** > **Server Details**.

![Validate process server](./media/site-recovery-vmware-to-azure/ASRVMWare_ProcessServerRegister.png)

Note that if you didn't disable signature verification for the Mobility service when you registered the process server you can do it later as follows:

1. Log onto the process server as an administrator and open the file C:\pushinstallsvc\pushinstaller.conf for editing. Under the section **[PushInstaller.transport]** add this line: **SignatureVerificationChecks=”0”**. Save and close the file.
2. Restart the InMage PushInstall service.


## Step 7: Install latest updates

Before proceeding, ensure that you have the latest updates installed. Remember to install the updates in the following order:
1. Log onto the configuration server using the **Virtual Machines** page in Azure and download the latest update from: [http://go.microsoft.com/fwlink/?LinkID=533809](http://go.microsoft.com/fwlink/?LinkID=533809). Follow the installer instructions to install the update
2. On the server that you installed the process server, download the latest update from [http://go.microsoft.com/fwlink/?LinkID=533810](http://go.microsoft.com/fwlink/?LinkID=533810) and install it using the installer instructions
3.	On the server that you have installed the master target server(s), install the latest update
	1. For Windows master target server(s), log onto the Windows master target server(s) using the **Virtual Machines** page in Azure and download the latest update from [http://go.microsoft.com/fwlink/?LinkID=533811](http://go.microsoft.com/fwlink/?LinkID=533811). Follow the installer instructions to install the update
	2. For Linux master target server(s), copy the installer tar file that is available at [http://go.microsoft.com/fwlink/?LinkID=533812](http://go.microsoft.com/fwlink/?LinkID=533812) using a sftp client. Alternatively you can log onto the Linux master target server(s) using the **Virtual Machines** page in Azure use wget to download the file. Extract the files from the gzipped installer and run the command “sudo ./install.sh” to install the update


## Step 8: Add vCenter servers

1. On the **Servers** > **Configuration Servers** tab select the configuration server and click to add a vCenter server.

	![Select vCenter server](./media/site-recovery-vmware-to-azure/ASRVMWare_AddVCenter.png)

2. Specify details for the vCenter server and select the process server that will be used to discover it.  The process server must be on the same network as the vCenter server and should have VMware vSphere CLI 5.1 installed.
3. After discovery completes the vCenter server will be listed under the configuration server details.

	![vCenter server settings](./media/site-recovery-vmware-to-azure/ASRVMWare_AddVCenter2.png)


## Step 9: Create a protection group

1. Open **Protected Items** > **Protection Group** and click to add a protection group.

	![Create protection group](./media/site-recovery-vmware-to-azure/ASRVMWare_CreatePG1.png)

2. On the **Specify Protection Group Settings** page specify a name for the group and select the configuration server on which you want to create the group.

	![Protection group settings](./media/site-recovery-vmware-to-azure/ASRVMWare_CreatePG2.png)

3. On the **Specify Replication Settings** page configure the replication settings that will be used for all the machines in the group.

	![Protection group replication](./media/site-recovery-vmware-to-azure/ASRVMWare_CreatePG3.png)

4. Settings:
	- **Multi VM consistency**: If you turn this on it creates shared application-consistent recovery points across the machines in the protection group. This setting is most relevant when all of the machines in the protection group are running the same workload. All machines will be recovered to the same data point. Only available for Windows servers.
	- **RPO threshold**: Alerts will be generated when the continuous data protection replication RPO exceeds the configured RPO threshold value.
	- **Recovery point retention**: Specifies the retention window. Protected machines can be recovered to any point within this window.
	- **Application-consistent snapshot frequency**: Specifies how frequently recovery points containing application-consistent snapshots will be created.

You can monitor the protection group as they're created on the **Protected Items** page.

## Step 10: Push the Mobility service

When you add machines to a protection group the  Mobility service is automatically pushed and installed on each machine by the process server. If you want use this automatic push mechanism for protected machines running Windows you'll need to do the following on each machine:

1. Configure the Windows firewall to allow **File and Printer Sharing** and **Windows Management Instrumentation**. For machines that belong to a domain you can configure the firewall policy with a GPO.
2. The account used to perform the push installation must be in the Administrators group on the machine you want to protect. Note that these credentials are only use for the push installation. They're not stored anywhere by the Mobility service and are discarded after the server is protected. You'll provide these credentials when you add a machine to a protection group.

	![Mobility credentials](./media/site-recovery-vmware-to-azure/ASRVMWare_PushCredentials.png)

3. If the admin account isn't a domain account you'll need to disable Remote User Access control on the local machine. To do this in HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System create the entry LocalAccountTokenFilterPolicy if it doesn't exist and assign it a DWORD value of 1

If you want to protect machines running Linux you'll need to do the following:

1. Make sure the account is a root user on the source Linux server
1. Install the latest openssh, openssh-server,  openssl packages on the machine you want to protect.
1. Enable ssh port 22.
2. Enable Sftp subsystem and password authentication in the sshd config file:
	1. Log in under the root user account.
	2. In the file /etc/ssh/sshd_config file the line that begins with “PasswordAuthentication”. Uncomment the line and change the value from “no” to “yes”.

		![Linux mobility](./media/site-recovery-vmware-to-azure/ASRVMWare_LinuxPushMobility1.png)

	4. Find the line that begins with “Subsystem” and uncomment the line.

		![Linux push mobility](./media/site-recovery-vmware-to-azure/ASRVMWare_LinuxPushMobility1.png)

## Step 11: Add machines to a protection group

1. Open **Protected Items** > **Protection Group** > **Machines** tab and add virtual or physical machines managed by a discovered vCenter server. We recommend that protection groups should mirror your workloads so that you add machines running a specific application to the same group.

	![Add machines](./media/site-recovery-vmware-to-azure/ASRVMWare_PushCredentials.png)

2. In the  **Select Virtual Machine** page of **Add Virtual Machine** select a V-Center server and then select machines from it.

	![Add V-Center server](./media/site-recovery-vmware-to-azure/ASRVMWare_SelectVMs.png)

    If you had a protection group already created and added a vCenter Server after that, it takes fifteen minutes for the Azure Site Recovery portal to refresh and for virtual machines to get listed in the Add machines to a protection group dialog. If you would like to proceed immediately with adding machines to protection group, please highlight the configuration server (don’t click it) and hit the Refresh button in the bottom action pane.

3. When you add machines to a protection group, the Mobility service is automatically installed from the on-premises process server. For the automatic push mechanism to work make sure you've set up your protected machines as described in the previous step.
4. In **Select Virtual Machines** select the vCenter server that management the machines you want to protect and then select the virtual machines.

4. Select the servers and storage to use for replication.

	![vCenter server](./media/site-recovery-vmware-to-azure/ASRVMWare_MachinesResources.png)

5. Provide the user credentials for the source server. This is required to automatically install the Mobility service on the source machines. For Windows server the account should have administrator privileges on the source server. For Linux the  account must be root.

	![Linux credentials](./media/site-recovery-vmware-to-azure/ASRVMWare_VMMobilityInstall.png)

6. Click the check mark to finish adding machines to the protection group and to start initial replication for each machine. You can monitor status on the **Jobs** page.

	![Add V-Center server](./media/site-recovery-vmware-to-azure/ASRVMWare_PGJobs.png)

7. In addition click **Protected Items** > <protection group> > **Virtual Machines** to monitor protection status. After initial replication completes and the machines are synchronizing data they will show **Protected** status.

	![Virtual machine jobs](./media/site-recovery-vmware-to-azure/ASRVMWare_PGJobs.png)

## Step 12: Set protected machine properties

1. After a machines has a **Protected** status you can configure its failover properties. In the protection group details select the machine and open the **Configure** tab.
2. You can modify the name that will be given to the machine in Azure after failover and the Azure size. You can also select the Azure network to which the machine will be connected after failover. Note that:

	- The name of the Azure machine must comply with the Azure requirements described in the Prerequisites.
	- By default replicated virtual machines in Azure aren't connected to an Azure network. If you want replicated virtual machines to communicate make sure to set the same Azure network for them.

	![Set virtual machine properties](./media/site-recovery-vmware-to-azure/ASRVMWare_VMProperties.png)

## Step 13: Run a failover

1. On the **Recovery Plans** page and add a recovery plan. Specify details for the plan and select **Azure** as the target.

	![Configure recovery plan](./media/site-recovery-vmware-to-azure/ASRVMWare_RP1.png)

2. In **Select Virtual Machine** select a protection group and then select machines in the group to add to the recovery plan.

	![Add virtual machines](./media/site-recovery-vmware-to-azure/ASRVMWare_RP2.png)

3. If required you can customize the plan to create groups and sequence the order in which machines in the recovery plan are failed over. You can also add prompts for manual actions and scripts. The scripts when recovering to Azure can be added by using [Azure Automation Runbooks](/documentation/articles/site-recovery-runbook-automation).

	![Customize recovery plan](./media/site-recovery-vmware-to-azure/ASRVMWare_RP2.png)

5. In the **Recovery Plans** page select the plan and click **Test Failover**.
6. In **Confirm Failover** verify the failover direction (To Azure) and select the recovery point to fail over to.
7. Wait for the failover job to complete and then verify that the failover worked as expected and that the replicated virtual machines start successfully in Azure.

## THIRD-PARTY SOFTWARE NOTICES AND INFORMATION

Do Not Translate or Localize

The software and firmware running in the Microsoft product or service is based on or incorporates material from the projects listed below (collectively, “Third Party Code”).  Microsoft is the not original author of the Third Party Code.  The original copyright notice and license, under which Microsoft received such Third Party Code, are set forth below.

The information in Section A is regarding Third Party Code components from the projects listed below. Such licenses and information are provided for informational purposes only.  This Third Party Code is being relicensed to you by Microsoft under Microsoft's software licensing terms for the Microsoft product or service.  

The information in Section B is regarding Third Party Code components that are being made available to you by Microsoft under the original licensing terms.

The complete file may be found on the [Microsoft Download Center](http://go.microsoft.com/fwlink/?LinkId=530254). Microsoft reserves all rights not expressly granted herein, whether by implication, estoppel or otherwise.
