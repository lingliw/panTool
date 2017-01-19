<properties
	pageTitle="Manage Hadoop clusters in HDInsight with PowerShell | Windows Azure"
	description="Learn how to perform administrative tasks for the Hadoop clusters in HDInsight using Azure PowerShell."
	services="hdinsight"
	editor="cgronlun"
	manager="paulettm"
	tags="azure-portal"
	authors="mumian"
	documentationCenter=""/>

<tags
	ms.service="hdinsight"
	ms.date="01/04/2016"
	wacn.date=""/>

# Manage Hadoop clusters in HDInsight by using Azure PowerShell

> [AZURE.SELECTOR]
- [Portal (Windows cluster)](/documentation/articles/hdinsight-administer-use-management-portal-v1)
- [Azure CLI](/documentation/articles/hdinsight-administer-use-command-line)
- [Azure PowerShell](/documentation/articles/hdinsight-administer-use-powershell)


Azure PowerShell is a powerful scripting environment that you can use to control and automate the deployment and management of your workloads in Azure. In this article, you will learn how to manage Hadoop clusters in Azure HDInsight by using a local Azure PowerShell console through the use of Windows PowerShell. For the list of the HDInsight PowerShell cmdlets, see [HDInsight cmdlet reference][hdinsight-powershell-reference].



**Prerequisites**

Before you begin this article, you must have the following:

- **An Azure subscription**. See [Get Azure trial](/pricing/1rmb-trial/).

##Install Azure PowerShell 1.0 and greater

First you must unintall the 0.9x versions.

To check the version of the installed PowerShell:

	Get-Module *azure*
	
To uninstall the older version, run Programs and Features in the control panel. 

There are two main options for installing Azure PowerShell. 

- [PowerShell Gallery](https://www.powershellgallery.com/). Run the following commands from elevated PowerShell ISE or elevated Windows PowerShell console:
		
		# Install the Azure Service Management module from PowerShell Gallery
		Install-Module Azure
		
		# Import Azure Service Management module
		Import-Module Azure

	For more information, see [PowerShell Gallery](https://www.powershellgallery.com/).

- [Microsoft Web Platform Installer (WebPI)](http://aka.ms/webpi-azps). If you have Azure PowerShell 0.9.x installed, you will be prompted to uninstall 0.9.x. If you installed Azure PowerShell modules from PowerShell Gallery, the installer requires the modules be removed prior to installation to ensure a consistent Azure PowerShell Environment. For the instructions, see [Install Azure PowerShell 1.0 via WebPI](https://azure.microsoft.com/blog/azps-1-0/).

WebPI will receive monthly updates. PowerShell Gallery will receive updates on a continuous basis. If you are comfortable with installing from PowerShell Gallery, that will be the first channel for the latest and greatest in Azure PowerShell.

##Create clusters

HDInsight cluster requires a Blob container on an Azure Storage account:

- HDInsight uses a Blob container of an Azure Storage account as the default file system. An Azure Storage account and a storage container are required before you can create an HDInsight cluster. The default storage account and the HDInsight cluster have to be in the same location.


> [AZURE.NOTE] The steps in this article create an HDInsight cluster by using basic configuration settings. For information about other cluster configuration settings (such as using Azure virtual network or a metastore for Hive and Oozie), see [Provision Hadoop clusters in HDInsight](/documentation/articles/hdinsight-provision-clusters).



**To connect to Azure**

> [AZURE.NOTE]
> In order to use the China Cloud Environment, the following Azure PowerShell commands need to add **"-Environment AzureChinaCloud"** parameter.
> 
>	`Add-AzureAccount` <br />
>	`Get-AzurePublishSettingsFile` <br />
>	`Import-AzurePublishSettingsFile` <br />
>	`New-AzureProfile` <br />
>	`New-AzureStorageContext` <br />
>	`Set-AzureSubscription` <br />
>	`Show-AzurePortal` <br />
>	
>For example, `Add-AzureAccount -Credential $Cred -ErrorAction Stop` should become `Add-AzureAccount -Credential $Cred -ErrorAction Stop -Environment AzureChinaCloud`
> 


	Add-AzureAccount -Environment AzureChinaCloud
	Get-AzureSubscription  # list your subscriptions and get your subscription ID
	Select-AzureSubscription -SubscriptionId "<Your Azure Subscription ID>"

**Select-AzureSubscription** is called in case you have multiple Azure subscriptions.

**To create an Azure Storage account**

	New-AzureStorageAccount -StorageAccountName <Azure Storage Account Name> -Location "<Azure Location>" -Type <AccountType> # account type example: Standard_LRS for zero redundancy storage
	
	Don't use **Standard_ZRS** because it deson't support Azure Table.  HDInsight uses Azure Table to logging. For a full list of the storage account types, see [https://msdn.microsoft.com/zh-cn/library/azure/hh264518.aspx](https://msdn.microsoft.com/zh-cn/library/azure/hh264518.aspx).


> [AZURE.IMPORTANT] The storage account must be located in the same datacenter as the HDInsight cluster. For available datacenters, see the **Regions** menu on the [HDInsight Pricing page](/home/features/hdinsight/#price).




If you have already had a Storage account but do not know the account name and account key, you can use the following commands to retrieve the information:

	# List Storage accounts for the current subscription
	Get-AzureStorageAccount
	# List the keys for a Storage account
	Get-AzureStorageKey -StorageAccountName <Azure Storage Account Name>

For details on getting the information by using the Portal, see the "View, copy, and regenerate storage access keys" section of [About Azure storage accounts](/documentation/articles/storage-create-storage-account).

**To create an Azure storage container**

Azure PowerShell cannot create a Blob container during the HDInsight creation process. You can create one by using the following script:

	$storageAccountName = "<Azure Storage Account Name>"
	$storageAccountKey = Get-AzureStorageKey -StorageAccountName $storageAccountName |  %{ $_.Primary }
	$containerName="<AzureBlobContainerName>"

	# Create a storage context object
	$destContext = New-AzureStorageContext -StorageAccountName $storageAccountName -StorageAccountKey $storageAccountKey  

	# Create a Blob storage container
	New-AzureStorageContainer -Name $containerName -Context $destContext

**To create a cluster**

Once you have the Storage account and the Blob container prepared, you are ready to create a cluster.

	$storageAccountName = "<Azure Storage Account Name>"
	$containerName = "<AzureBlobContainerName>"

	$clusterName = "<HDInsightClusterName>"
	$location = "<AzureDataCenter>"
	$clusterNodes = <ClusterSizeInNodes>

	# Get the Storage account key
	$storageAccountKey = Get-AzureStorageKey -StorageAccountName $storageAccountName | %{ $_.Primary }

	# Create a new HDInsight cluster
	New-AzureHDInsightCluster -Name $clusterName `
		-Location $location `
		-DefaultStorageAccountName "$storageAccountName.blob.core.chinacloudapi.cn" `
		-DefaultStorageAccountKey $storageAccountKey `
		-DefaultStorageContainerName $containerName  `
		-ClusterSizeInNodes $clusterNodes

##List clusters
Use the following command to list all clusters in the current subscription:

	Get-AzureHDInsightCluster

##Show cluster

Use the following command to show details of a specific cluster in the current subscription:

	Get-AzureHDInsightCluster -Name <Cluster Name>

##Delete clusters
Use the following command to delete a cluster:

	Remove-AzureHDInsightCluster -Name <Cluster Name>

##Scale clusters
The cluster scaling feature allows you to change the number of worker nodes used by a cluster that is running in Azure HDInsight without having to re-create the cluster.

>[AZURE.NOTE] Only clusters with HDInsight version 3.1.3 or higher are supported. If you are unsure of the version of your cluster, you can check the Properties page.  See [Get familiar with the cluster portal interface](/documentation/articles/hdinsight-administer-use-management-portal-v1#Get-familiar-with-the-cluster-portal-interface).

The impact of changing the number of data nodes for each type of cluster supported by HDInsight:

- Hadoop

	You can seamlessly increase the number of worker nodes in a Hadoop cluster that is running without impacting any pending or running jobs. New jobs can also be submitted while the operation is in progress. Failures in a scaling operation are gracefully handled so that the cluster is always left in a functional state.

	When a Hadoop cluster is scaled down by reducing the number of data nodes, some of the services in the cluster are restarted. This causes all running and pending jobs to fail at the completion of the scaling operation. You can, however, resubmit the jobs once the operation is complete.

- HBase

	You can seamlessly add or remove nodes to your HBase cluster while it is running. Regional Servers are automatically balanced within a few minutes of completing the scaling operation. However, you can also manually balance the regional servers by logging into the headnode of cluster and running the following commands from a command prompt window:

		>pushd %HBASE_HOME%\bin
		>hbase shell
		>balancer

	For more information on using the HBase shell, see []
- Storm

	You can seamlessly add or remove data nodes to your Storm cluster while it is running. But after a successful completion of the scaling operation, you will need to rebalance the topology.

	Rebalancing can be accomplished in two ways:

	* Storm web UI
	* Command-line interface (CLI) tool

	Please refer to the [Apache Storm documentation](http://storm.apache.org/documentation/Understanding-the-parallelism-of-a-Storm-topology.html) for more details.

	The Storm web UI is available on the HDInsight cluster:

	![hdinsight storm scale rebalance](./media/hdinsight-administer-use-management-portal-v1/hdinsight.portal.scale.cluster.storm.rebalance.png)

	Here is an example how to use the CLI command to rebalance the Storm topology:

		## Reconfigure the topology "mytopology" to use 5 worker processes,
		## the spout "blue-spout" to use 3 executors, and
		## the bolt "yellow-bolt" to use 10 executors

		$ storm rebalance mytopology -n 5 -e blue-spout=3 -e yellow-bolt=10

To change the Hadoop cluster size by using Azure PowerShell, run the following command from a client machine:

	Set-AzureHDInsightClusterSize -Name <Cluster Name> -ClusterSizeInNodes <NewSize>
	

##Grant/revoke access

HDInsight clusters have the following HTTP web services (all of these services have RESTful endpoints):

- ODBC
- JDBC
- Oozie
- Templeton


By default, these services are granted for access. You can revoke/grant the access. To revoke:

	Revoke-AzureHDInsightHttpServicesAccess -Name <Cluster Name>

To grant:

	$clusterName = "<HDInsight Cluster Name>"

	# Credential option 1
	$hadoopUserName = "admin"
	$hadoopUserPassword = "<Enter the Password>"
	$hadoopUserPW = ConvertTo-SecureString -String $hadoopUserPassword -AsPlainText -Force
	$credential = New-Object System.Management.Automation.PSCredential($hadoopUserName,$hadoopUserPW)

	# Credential option 2
	#$credential = Get-Credential -Message "Enter the HTTP username and password:" -UserName "admin"
	
	Grant-AzureHDInsightHttpServicesAccess -Name $clusterName -HttpCredential $credential

>[AZURE.NOTE] By granting/revoking the access, you will reset the cluster user name and password.

This can also be done via the Portal. See [Administer HDInsight by using the Azure Management Portal][hdinsight-admin-portal].

##Update HTTP user credentials

It is the same procedure as [Grant/revoke HTTP access](#grant/revoke-access).If the cluster has been granted the HTTP access, you must first revoke it.  And then grant the access with new HTTP user credentials.


##Find the default storage account

The following Powershell script demonstrates how to get the default storage account name and the default storage account key for a cluster.

	$clusterName = "<HDInsight Cluster Name>"
	
	$cluster = Get-AzureHDInsightCluster -Name $clusterName
	$defaultStorageAccountName = ($cluster.DefaultStorageAccount).Replace(".blob.core.chinacloudapi.cn", "")
	$defaultBlobContainerName = $cluster.DefaultStorageContainer
	$defaultStorageAccountKey = Get-AzureStorageKey -StorageAccountName $defaultStorageAccountName |  %{ $_.Primary }
	$defaultStorageAccountContext = New-AzureStorageContext -StorageAccountName $defaultStorageAccountName -StorageAccountKey $defaultStorageAccountKey 

##Submit jobs

**To submit MapReduce jobs**

See [Run Hadoop MapReduce samples in Windows-based HDInsight](/documentation/articles/hdinsight-run-samples).

**To submit Hive jobs** 

See [Run Hive queries using PowerShell](/documentation/articles/hdinsight-hadoop-use-hive-powershell).

**To submit Pig jobs**

See [Run Pig jobs using PowerShell](/documentation/articles/hdinsight-hadoop-use-pig-powershell).

**To submit Sqoop jobs**

See [Use Sqoop with HDInsight](/documentation/articles/hdinsight-use-sqoop).

**To submit Oozie jobs**

See [Use Oozie with Hadoop to define and run a workflow in HDInsight](/documentation/articles/hdinsight-use-oozie).

##Upload data to Azure Blob storage
See [Upload data to HDInsight][hdinsight-upload-data].


## See Also
* [HDInsight cmdlet reference documentation][hdinsight-powershell-reference]
* [Administer HDInsight by using the Azure Management Portal][hdinsight-admin-portal]
* [Administer HDInsight using a command-line interface][hdinsight-admin-cli]
* [Create HDInsight clusters][hdinsight-provision]
* [Upload data to HDInsight][hdinsight-upload-data]
* [Submit Hadoop jobs programmatically][hdinsight-submit-jobs]
* [Get started with Azure HDInsight][hdinsight-get-started]


[hdinsight-hive]: /documentation/articles/hdinsight-use-hive
[azure-purchase-options]: /pricing/overview/
[azure-member-offers]: /pricing/member-offers/
[azure-trial]: /pricing/1rmb-trial/

[hdinsight-get-started]: /documentation/articles/hdinsight-hadoop-tutorial-get-started-windows-v1
[hdinsight-provision]: /documentation/articles/hdinsight-provision-clusters-v1
[hdinsight-provision-custom-options]: /documentation/articles/hdinsight-provision-clusters-v1#configuration
[hdinsight-submit-jobs]: /documentation/articles/hdinsight-submit-hadoop-jobs-programmatically

[hdinsight-admin-cli]: /documentation/articles/hdinsight-administer-use-command-line
[hdinsight-admin-portal]: /documentation/articles/hdinsight-administer-use-management-portal-v1
[hdinsight-storage]: /documentation/articles/hdinsight-hadoop-use-blob-storage
[hdinsight-use-hive]: /documentation/articles/hdinsight-use-hive
[hdinsight-use-mapreduce]: /documentation/articles/hdinsight-use-mapreduce
[hdinsight-upload-data]: /documentation/articles/hdinsight-upload-data
[hdinsight-flight]: /documentation/articles/hdinsight-analyze-flight-delay-data

[hdinsight-powershell-reference]: https://msdn.microsoft.com/zh-cn/library/dn858087.aspx

[powershell-install-configure]: /documentation/articles/powershell-install-configure

[image-hdi-ps-provision]: ./media/hdinsight-administer-use-powershell/HDI.PS.Provision.png
