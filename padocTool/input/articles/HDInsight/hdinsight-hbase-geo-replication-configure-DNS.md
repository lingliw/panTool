<properties 
   pageTitle="Configure DNS between two Azure virtual networks | Windows Azure" 
   description="Learn how to configure VPN connections and domain name resolution between two virtual networks, and how to configure HBase geo-replication." 
   services="hdinsight,virtual-network" 
   documentationCenter="" 
   authors="mumian" 
   manager="paulettm" 
   editor="cgronlun"/>

<tags
	ms.service="hdinsight"
	ms.date="07/28/2015"
	wacn.date=""/>

# Configure DNS between two Azure virtual networks

> [AZURE.SELECTOR]
- [Configure VPN connectivity](/documentation/articles/hdinsight-hbase-geo-replication-configure-VNETs)
- [Configure DNS](/documentation/articles/hdinsight-hbase-geo-replication-configure-DNS)
- [Configure HBase replication](/documentation/articles/hdinsight-hbase-geo-replication) 


Learn how to add and configure DNS servers to Azure virtual networks to handle name resolution within and across the virtual networks.

This tutorial is the second part of the [series][hdinsight-hbase-geo-replication] on creating HBase geo-replication:

- [Configure a VPN connectivity between two virtual networks][hdinsight-hbase-geo-replication-vnet]
- Configure DNS for the virtual networks (this tutorial)
- [Configure HBase geo replication][hdinsight-hbase-geo-replication]


The following diagram illustrates the two virtual networks you created in [Configure a VPN connectivity between two virtual networks][hdinsight-hbase-geo-replication-vnet]:

![HDInsight HBase replication virtual network diagram][img-vnet-diagram]

##Prerequisites
Before you begin this tutorial, you must have the following:

- **An Azure subscription**. See [Get Azure trial](/pricing/1rmb-trial/).

- **A workstation with Azure PowerShell**. See [Install and use Azure PowerShell](/documentation/articles/install-configure-powershell).

	Before running PowerShell scripts, make sure you are connected to your Azure subscription using the following cmdlet:

		Add-AzureAccount

	If you have multiple Azure subscriptions, use the following cmdlet to set the current subscription:

		Select-AzureSubscription <AzureSubscriptionName>

- **Two Azure virtual network with VPN connectivity**.  For instructions, see [Configure a VPN connection between two Azure virtual networks][hdinsight-hbase-geo-replication-vnet].

>[AZURE.NOTE] Azure service names and virtual machine names must be unique. The name used in this tutorial is Contoso-[Azure Service/VM name]-[CN/CE]. For example, Contoso-VNet-CN is the Azure virtual network in the China North data center; Contoso-DNS-CE is the DNS server VM in the China East data center. You must come up with your own names.
 
 
##Create Azure virtual machines to be used as DNS servers

**To create a virtual machine within Contoso-VNet-CN, called Contoso-DNS-CN**

1.	Click **NEW**, **COMPUTE**, **VIRTUAL MACHINE**, **FROM GALLERY**.
2.	Choose **Windows Server 2012 R2 Datacenter**.
3.	Enter:
	- **VIRTUAL MACHINE NAME**: Contoso-DNS-CN
	- **NEW USER NAME**: 
	- **NEW PASSWORD**: 
4.	Enter:
	- **CLOUD SERVICE**: Create a new cloud service
	- **REGION/AFFINITY GROUP/VIRTUAL NETWORK**: (Select Contoso-VNet-CN)
	- **VIRTUAL NETWORK SUBNETS**: Subnet-1
	- **STORAGE ACCOUNT**: Use an automatically generated storage account
	
		The cloud service name will be the same as the virtual machine name. In this case, that is Contoso-DNS-CN. For subsequent virtual machines, I can choose to use the same cloud service.  All the virtual machines under the same cloud service share the same virtual network and domain suffix.

		The storage account is used to store the virtual machine image file. 
	- **ENDPOINTS**: (scroll down and select **DNS**) 

After the virtual machine is created, find out the internal IP and external IP.

1.	Click the virtual machine name, **Contoso-DNS-CN**.
2.	Click **DashBoard**.
3.	Write down:
	- PUBLIC VIRTUAL IP ADDRESS
	- INTERNAL IP ADDRESS


**To create a virtual machine within Contoso-VNet-CE, called Contoso-DNS-CE** 

- Repeat the same procedure to create a virtual machine with the following values:
	- VIRTUAL MACHINE NAME: Contoso-DNS-CE
	- REGION/AFFINITY GROUP/VIRTUAL NETWORK: Select Contoso-VNET-US
	- VIRTUAL NETWORK SUBNETS: Subnet-1
	- STORAGE ACCOUNT: Use an automatically generated storage account
	- ENDPOINTS: (select DNS)

##Set static IP addresses for the two virtual machines

DNS servers requires static IP addresses.  This step can't be done from the Azure Management Portal. You will use Azure PowerShell.

**To configure static IP address for the two virtual machines**

1. Open Windows PowerShell ISE.
2. Run the following cmdlets.  

		Add-AzureAccount
		Select-AzureSubscription [YourAzureSubscriptionName]
		
		Get-AzureVM -ServiceName Contoso-DNS-CN -Name Contoso-DNS-CN | Set-AzureStaticVNetIP -IPAddress 10.1.0.4 | Update-AzureVM
		Get-AzureVM -ServiceName Contoso-DNS-CE -Name Contoso-DNS-CE | Set-AzureStaticVNetIP -IPAddress 10.2.0.4 | Update-AzureVM 

	ServiceName is the cloud service name. Because the DNS server is the first virtual machine of the cloud service, the cloud service name is the same as the virtual machine name.

	You might need to update ServiceName and Name to match the names that you have.


##Add the DNS Server role the two virtual machines

**To add the DNS Server role for Contoso-DNS-CN**

1.	From the Azure Management Portal, click **Virtual Machines** on the left. 
2.	Click **Contoso-DNS-CN**.
3.	Click **DASHBOARD** from the top.
4.	Click **CONNECT** from the bottom and follow the instructions to connect to the virtual machine via RDP.
2.	Within the RDP session, click the Windows button on the bottom left corner to open the Start screen.
3.	Click the **Server Manager** tile.
4.	Click **Add Roles and Features**.
5.	Click **Next**
6.	Select **Role-based or feature-based installation**, and then click **Next**.
7.	Select your DNS virtual machine (it shall be highlighted already), and then click **Next**.
8.	Check **DNS Server**.
9.	Click **Add Features**, and then click **Continue**.
10.	Click **Next** three times, and then click **Install**. 

**To add the DNS Server role for Contoso-DNS-CE**

- Repeat the steps to add DNS role to **Contoso-DNS-CE**.

##Assign DNS servers to the virtual networks

**To register the two DNS servers**

1.	From the Azure Management Portal, click **NEW**, **NETWORK SERVICES**, **VIRTUAL NETWORK**, **REGISTER DNS SERVER**.
2.	Enter:
	- **NAME**: Contoso-DNS-CN
	- **DNS SERVER IP ADDRESS**: 10.1.0.4 – the IP address must matching the DNS server virtual machine IP address.
	 
3.	Repeat the process to register Contoso-DNS-CE with the following settings:
	- **NAME**: Contoso-DNS-CE
	- **DNS SERVER IP ADDRESS**: 10.2.0.4

**To assign the two DNS servers to the two virtual networks**

1.	Click **Networks** from the left pane in the Management portal.
2.	Click **Contoso-VNet-CN**.
3.	Click **CONFIGURE**.
4.	Select **Contoso-DNS-CN** in the **dns servers** section.
5.	Click **SAVE** on the bottom of the page, and click **Yes** to confirm.
6.	Repeat the process to assign the **Contoso-DNS-CE** DNS server to the **Contoso-VNet-CE** virtual network.

All the virtual machines that have been deployed to the virtual networks must be rebooted to update the DNS server configuration.

**To reboot the virtual machines**

1. From the Azure Management Portal, click **Virtual Machines** on the left.
2. Click **Contoso-DNS-CN**.
3. Click **Dashboard** from the top.
4. Click **RESTART** on the bottom.
5. Repeat the same steps to reboot **Contoso-DNS-CE**.


##Configure DNS conditional forwarders

The DNS server on each virtual network can only resolve DNS names within that virtual network. You need to configure a conditional forwarder to point to the peer DNS server for name resolutions in the peer virtual network.

To configure conditional forwarder, you need to know the domain suffixes of the two DNS servers. The DNS suffixes can be different depending on the Cloud Services configuration you used when you created the virtual machines. For each DNS suffix used in the virtual network, you must add a conditional forwarder. 

**To find the domain suffixes of the two DNS servers**

1. RDP into **Contoso-DNS-CN**.
2. Open Windows PowerShell console, or command prompt.
3. Run **ipconfig**, and write down **Connection-specific DNS suffix**.
4. Do not close the RDP session, you will still need it. 
5. Repeat the same steps to find out the **Connection-specific DNS suffix** of **Contoso-DNS-CE**.


**To configure DNS forwarders**
 
1.	From the RDP session to **Contoso-DNS-CN**, click the Windows key on the lower left.
2.	Click **Administrative Tools**.
3.	Click **DNS**.
4.	In the left pane, expand **DSN**, **Contoso-DNS-CN**.
5.	Enter the following information:
	- **DNS Domain**: enter the DNS suffix of the Contoso-DNS-CE. For example: Contoso-DNS-CE.b5.internal.chinacloudapp.cn.
	- **IP addresses of the master servers**: enter 10.2.0.4, which is the Contoso-DNS-CE’s IP address.
6.	Press **ENTER**, and then click **OK**.  Now you will be able to resolve the Contoso-DNS-CE’s IP address from Contoso-DNS-CN.
7.	Repeat the steps to add a DNS forwarder to the DNS service on the Contoso-DNS-CE virtual machine with the following values:
	- **DNS Domain**: enter the DNS suffix of the Contoso-DNS-CN. 
	- **IP addresses of the master servers**: enter 10.2.0.4, which is the Contoso-DNS-CN’s IP address.

##Test the name resolution across the virtual networks

Now you can test host name resolution across the virtual networks. Ping is blocked by firewall by default.  You can use nslookup to resolve the DNS server virtual machines (you must use FQDN) in the peer networks.  


##Next Steps

In this tutorial, you have learned how to configure name resolution across virtual networks with VPN connections. The other two articles in the series cover:

- [Configure a VPN connection between two Azure virtual networks][hdinsight-hbase-geo-replication-vnet]
- [Configure HBase geo replication][hdinsight-hbase-geo-replication]



[hdinsight-hbase-geo-replication]: /documentation/articles/hdinsight-hbase-geo-replication
[hdinsight-hbase-geo-replication-vnet]: /documentation/articles/hdinsight-hbase-geo-replication-configure-VNets
[powershell-install]: /documentation/articles/install-configure-powershell
[img-vnet-diagram]: ./media/hdinsight-hbase-geo-replication-configure-DNS/HDInsight.HBase.VPN.diagram.png 