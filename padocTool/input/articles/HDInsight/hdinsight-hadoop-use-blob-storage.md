<properties
	pageTitle="Query data from HDFS-compatible Blob storage | Windows Azure"
	description="HDInsight uses Azure Blob storage as the big data store for HDFS. Learn how to query data from Blob storage and store results of your analysis."
	keywords="blob storage,hdfs,structured data,unstructured data"
	services="hdinsight,storage"
	documentationCenter=""
	tags="azure-portal"
	authors="mumian"
	manager="paulettm"
	editor="cgronlun"/>

<tags
	ms.service="hdinsight"
	ms.date="10/23/2015"
	wacn.date=""/>


# Use HDFS-compatible Azure Blob storage with Hadoop in HDInsight

Learn how to use low-cost Azure Blob storage with HDInsight, create Azure storage account and Blob storage container, and then address the data inside.

Azure Blob storage is a robust, general-purpose storage solution that integrates seamlessly with HDInsight. Through a Hadoop distributed file system (HDFS) interface, the full set of components in HDInsight can operate directly on structured or unstructured data in Blob storage.

Storing data in Blob storage enables you to safely delete the HDInsight clusters that are used for computation without losing user data.

> [AZURE.NOTE]	The *asv://* syntax is not supported in HDInsight version 3.0 clusters. This means that any jobs submitted to an HDInsight version 3.0 cluster that explicitly use the *asv://* syntax will fail. The *wasb://* syntax should be used instead. Also, jobs submitted to any HDInsight version 3.0 clusters that are created with an existing metastore that contains explicit references to resources that use the asv:// syntax will fail. These metastores need to be re-created using the wasb:// syntax to address resources.

> HDInsight currently only supports block blobs.

> Most HDFS commands (for example, <b>ls</b>, <b>copyFromLocal</b> and <b>mkdir</b>) still work as expected. Only the commands that are specific to the native HDFS implementation (which is referred to as DFS), such as <b>fschk</b> and <b>dfsadmin</b>, will show different behavior in Azure Blob storage.

For information about creating an HDInsight cluster, see [Get Started with HDInsight][hdinsight-get-started] or [Create HDInsight clusters][hdinsight-creation].


## HDInsight storage architecture
The following diagram provides an abstract view of the HDInsight storage architecture:

![Hadoop clusters use the HDFS API to access and store structured and unstructured data in Blob storage.](./media/hdinsight-hadoop-use-blob-storage/HDI.WASB.Arch.png "HDInsight Storage Architecture")

HDInsight provides access to the distributed file system that is locally attached to the compute nodes. This file system can be accessed by using the fully qualified URI, for example:

	hdfs://<namenodehost>/<path>

In addition, HDInsight provides the ability to access data that is stored in Azure Blob storage. The syntax is:

	wasb[s]://<containername>@<accountname>.blob.core.chinacloudapi.cn/<path>


Hadoop supports a notion of the default file system. The default file system implies a default scheme and authority. It can also be used to resolve relative paths. During the HDInsight creation process, an Azure Storage account and a specific Azure Blob storage container from that account is designated as the default file system.

In addition to this storage account, you can add additional storage accounts from the same Azure subscription or different Azure subscriptions during the creation process. For instructions about adding additional storage accounts, see [Create HDInsight clusters][hdinsight-creation].

- **Containers in the storage accounts that are connected to a cluster:** Because the account name and key are associated with the cluster during creation, you have full access to the blobs in those containers.

- **Public containers or public blobs in storage accounts that are NOT connected to a cluster:** You have read-only permission to the blobs in the containers.

	> [AZURE.NOTE]
        > Public containers allow you to get a list of all blobs that are available in that container and get container metadata. Public blobs allow you to access the blobs only if you know the exact URL. For more information, see <a href="/documentation/articles/storage-manage-access-to-resources">Restrict access to containers and blobs</a>.

- **Private containers in storage accounts that are NOT connected to a cluster:** You can't access the blobs in the containers unless you define the storage account when you submit the WebHCat jobs. This is explained later in this article.


The storage accounts that are defined in the creation process and their keys are stored in %HADOOP_HOME%/conf/core-site.xml on the cluster nodes. The default behavior of HDInsight is to use the storage accounts defined in the core-site.xml file. It is not recommended to edit the core-site.xml file because the cluster head node(master) may be reimaged or migrated at any time, and any changes to those files will be lost.

Multiple WebHCat jobs, including Hive, MapReduce, Hadoop streaming, and Pig, can carry a description of storage accounts and metadata with them. (This currently works for Pig with storage accounts, but not for metadata.) In the [Access blobs using Azure PowerShell](#powershell) section of this article, there is a sample of this feature. For more information, see [Using an HDInsight Cluster with Alternate Storage Accounts and Metastores](http://social.technet.microsoft.com/wiki/contents/articles/23256.using-an-hdinsight-cluster-with-alternate-storage-accounts-and-metastores.aspx).

Blob storage can be used for structured and unstructured data. Blob storage containers store data as key/value pairs, and there is no directory hierarchy. However the slash character ( / ) can be used within the key name to make it appear as if a file is stored within a directory structure. For example, a blob's key may be *input/log1.txt*. No actual *input* directory exists, but due to the presence of the slash character in the key name, it has the appearance of a file path.

###<a id="benefits"></a>Benefits of Blob storage
The implied performance cost of not co-locating compute clusters and storage resources is mitigated by the way the compute clusters are created close to the storage account resources inside the Azure datacenter, where the high-speed network makes it very efficient for the compute nodes to access the data inside Azure Blob storage.

There are several benefits associated with storing the data in Azure Blob storage instead of HDFS:

* **Data reuse and sharing:** The data in HDFS is located inside the compute cluster. Only the applications that have access to the compute cluster can use the data by using HDFS APIs. The data in Azure Blob storage can be accessed either through the HDFS APIs or through the [Blob Storage REST APIs][blob-storage-restAPI]. Thus, a larger set of applications (including other HDInsight clusters) and tools can be used to produce and consume the data.
* **Data archiving:** Storing data in Azure Blob storage enables the HDInsight clusters used for computation to be safely deleted without losing user data.
* **Data storage cost:** Storing data in DFS for the long term is more costly than storing the data in Azure Blob storage because the cost of a compute cluster is higher than the cost of an Azure Blob storage container. In addition, because the data does not have to be reloaded for every compute cluster generation, you are also saving data loading costs.
* **Elastic scale-out:** Although HDFS provides you with a scaled-out file system, the scale is determined by the number of nodes that you create for your cluster. Changing the scale can become a more complicated process than relying on the elastic scaling capabilities that you get automatically in Azure  Blob storage.
* **Geo-replication:** Your Azure Blob storage containers can be geo-replicated. Although this gives you geographic recovery and data redundancy, a failover to the geo-replicated location severely impacts your performance, and it may incur additional costs. So our recommendation is to choose the geo-replication wisely and only if the value of the data is worth the additional cost.

Certain MapReduce jobs and packages may create intermediate results that you don't really want to store in Azure Blob storage. In that case, you can elect to store the data in the local HDFS. In fact, HDInsight uses DFS for several of these intermediate results in Hive jobs and other processes.



## Create Blob containers

To use blobs, you first create an [Azure Storage account][azure-storage-create]. As part of this, you specify an Azure datacenter that will store the objects you create using this account. The cluster and the storage account must be hosted in the same datacenter. The Hive metastore SQL Server database and Oozie metastore SQL Server database must also be located in the same datacenter.

Wherever it lives, each blob you create belongs to a container in your Azure Storage account. This container may be an existing blob that was created outside of HDInsight, or it may be a container that is created for an HDInsight cluster.

### Using the Azure Management Portal

When provisioning an HDInsight cluster from the Azure Management Portal, there are two options: **Quick Create** and **Custom Create**. The Quick Create option requires that the Azure Storage account is created beforehand. For instructions, see [How to Create a Storage Account][azure-storage-create].

By using the Quick Create option, you can choose an existing storage account. The provision process creates a new container with the same name as the HDInsight cluster name. If a container with the same name already exists, <clusterName>-<x> will be used. For example, *myHDIcluster-1*. This container is used as the default file system.

![Using Quick Create for a new Hadoop cluster in HDInsight in the Azure Management Portal.][img-hdi-quick-create]

By using Custom Create, you have one of the following options for the default storage account:

- Use existing storage
- Create new storage
- Use storage from another subscription

You also have the option to create your own container or use an existing one.

![Option to use an existing storage account for your HDInsight cluster.][img-hdi-custom-create-storage-account]

To create a container, use the following command:

	azure storage container create <containername> --account-name <storageaccountname> --account-key <storageaccountkey>

### Using Azure PowerShell

If you [installed and configured Azure PowerShell][powershell-install], you can use the following from the Azure PowerShell prompt to create a storage account and container:

	$SubscriptionID = "<Your Azure Subscription ID>"
	$ResourceGroupName = "<New Azure Resource Group Name>"
	$Location = "EAST US 2"
	
	$StorageAccountName = "<New Azure Storage Account Name>"
	$containerName = "<New Azure Blob Container Name>"
	
	Add-AzureRmAccount
	Select-AzureRmSubscription -SubscriptionId $SubscriptionID
	
	# Create resource group
	New-AzureRmResourceGroup -name $ResourceGroupName -Location $Location
	
	# Create default storage account
	New-AzureRmStorageAccount -ResourceGroupName $ResourceGroupName -Name $StorageAccountName -Location $Location -Type Standard_LRS 
	
	# Create default blob containers
	$storageAccountKey = Get-AzureRmStorageAccountKey -ResourceGroupName $resourceGroupName -StorageAccountName $StorageAccountName |  %{ $_.Key1 }
	$destContext = New-AzureStorageContext -StorageAccountName $storageAccountName -StorageAccountKey $storageAccountKey  
	New-AzureStorageContainer -Name $containerName -Context $destContext

## Address files in Blob storage

The URI scheme for accessing files in Blob storage from HDInsight is:

	wasb[s]://<BlobStorageContainerName>@<StorageAccountName>.blob.core.chinacloudapi.cn/<path>


> [AZURE.NOTE] The syntax for addressing the files on the storage emulator (running on HDInsight emulator) is <i>wasb://&lt;ContainerName&gt;@storageemulator</i>.



The URI scheme provides unencrypted access (with the *wasb:* prefix) and SSL encrypted access (with *wasbs*). We recommend using *wasbs* wherever possible, even when accessing data that lives inside the same datacenter in Azure.

The &lt;BlobStorageContainerName&gt; identifies the name of the container in Azure Blob storage.
The &lt;StorageAccountName&gt; identifies the Azure Storage account name. A fully qualified domain name (FQDN) is required.

If neither &lt;BlobStorageContainerName&gt; nor &lt;StorageAccountName&gt; has been specified, the default file system is used. For the files on the default file system, you can use a relative path or an absolute path. For example, the *hadoop-mapreduce-examples.jar* file that comes with HDInsight clusters can be referred to by using one of the following:

	wasb://mycontainer@myaccount.blob.core.chinacloudapi.cn/example/jars/hadoop-mapreduce-examples.jar
	wasb:///example/jars/hadoop-mapreduce-examples.jar
	/example/jars/hadoop-mapreduce-examples.jar

> [AZURE.NOTE] The file name is <i>hadoop-examples.jar</i> in HDInsight versions 2.1 and 1.6 clusters.


The &lt;path&gt; is the file or directory HDFS path name. Because containers in Azure Blob storage are simply key-value stores, there is no true hierarchical file system. A slash character ( / ) inside a blob key is interpreted as a directory separator. For example, the blob name for *hadoop-mapreduce-examples.jar* is:

	example/jars/hadoop-mapreduce-examples.jar

> [AZURE.NOTE] When working with blobs outside of HDInsight, most utilities do not recognize the WASB format and instead expect a basic path format, such as `example/jars/hadoop-mapreduce-examples.jar`.

## Access blobs using Azure CLI

Use the following command to list the blob-related commands:

	azure storage blob

**Example of using Azure CLI to upload a file**

	azure storage blob upload <sourcefilename> <containername> <blobname> --account-name <storageaccountname> --account-key <storageaccountkey>

**Example of using Azure CLI to download a file**

	azure storage blob download <containername> <blobname> <destinationfilename> --account-name <storageaccountname> --account-key <storageaccountkey>

**Example of using Azure CLI to delete a file**

	azure storage blob delete <containername> <blobname> --account-name <storageaccountname> --account-key <storageaccountkey>

**Example of using Azure CLI to list files**

	azure storage blob list <containername> <blobname|prefix> --account-name <storageaccountname> --account-key <storageaccountkey>

## Access blobs using Azure PowerShell

> [AZURE.NOTE] The commands in this section provide a basic example of using PowerShell to access data stored in blobs. For a more full-featured example that is customized for working with HDInsight, see the [HDInsight Tools](https://github.com/Blackmist/hdinsight-tools).

Use the following command to list the blob-related cmdlets:

	Get-Command *blob*

![List of blob-related PowerShell cmdlets.][img-hdi-powershell-blobcommands]

###Upload files

See [Upload data to HDInsight][hdinsight-upload-data].

###Download files

The following scrip downloads a block blob to the current folder. Before running the script, change the directory to a folder where you have write permissions.

	$resourceGroupName = "<AzureResourceGroupName>"
	$storageAccountName = "<AzureStorageAccountName>"   # The storage account used for the default file system specified at creation.
	$containerName = "<BlobStorageContainerName>"  # The default file system container has the same name as the cluster.
	$blob = "example/data/sample.log" # The name of the blob to be downloaded.
	
	# Use Add-AzureAccount if you haven't connected to your Azure subscription
	Login-AzureRmAccount 
	Select-AzureRmSubscription -SubscriptionID "<Your Azure Subscription ID>"
	
	Write-Host "Create a context object ... " -ForegroundColor Green
	$storageAccountKey = Get-AzureRmStorageAccountKey -ResourceGroupName $resourceGroupName -Name $storageAccountName | %{ $_.key1 }
	$storageContext = New-AzureStorageContext -StorageAccountName $storageAccountName -StorageAccountKey $storageAccountKey  
	
	Write-Host "Download the blob ..." -ForegroundColor Green
	Get-AzureStorageBlobContent -Container $ContainerName -Blob $blob -Context $storageContext -Force
	
	Write-Host "List the downloaded file ..." -ForegroundColor Green
	cat "./$blob"

Providing the resource group name and the cluster name, you can use the following code:

	$resourceGroupName = "<AzureResourceGroupName>"
	$clusterName = "<HDInsightClusterName>"
	$blob = "example/data/sample.log" # The name of the blob to be downloaded.
	
	$cluster = Get-AzureRmHDInsightCluster -ResourceGroupName $resourceGroupName -ClusterName $clusterName
	$defaultStorageAccount = $cluster.DefaultStorageAccount -replace '.blob.core.chinacloudapi.cn'
	$defaultStorageAccountKey = Get-AzureRmStorageAccountKey -ResourceGroupName $resourceGroupName -Name $defaultStorageAccount |  %{ $_.Key1 }
	$defaultStorageContainer = $cluster.DefaultStorageContainer
	$storageContext = New-AzureStorageContext -StorageAccountName $defaultStorageAccount -StorageAccountKey $defaultStorageAccountKey 
	
	Write-Host "Download the blob ..." -ForegroundColor Green
	Get-AzureStorageBlobContent -Container $defaultStorageContainer -Blob $blob -Context $storageContext -Force

###Delete files


	Remove-AzureStorageBlob -Container $containerName -Context $storageContext -blob $blob

###List files

	Get-AzureStorageBlob -Container $containerName -Context $storageContext -prefix "example/data/"

###Run Hive queries using an undefined storage account

This example shows how to list a folder from storage account that is not defined during the creating process.
	$clusterName = "<HDInsightClusterName>"

	$undefinedStorageAccount = "<UnboundedStorageAccountUnderTheSameSubscription>"
	$undefinedContainer = "<UnboundedBlobContainerAssociatedWithTheStorageAccount>"

	$undefinedStorageKey = Get-AzureStorageKey $undefinedStorageAccount | %{ $_.Primary }

	Use-AzureRmHDInsightCluster $clusterName

	$defines = @{}
	$defines.Add("fs.azure.account.key.$undefinedStorageAccount.blob.core.chinacloudapi.cn", $undefinedStorageKey)

	Invoke-AzureRmHDInsightHiveJob -Defines $defines -Query "dfs -ls wasb://$undefinedContainer@$undefinedStorageAccount.blob.core.chinacloudapi.cn/;"

## Next steps

In this article, you learned how to use HDFS-compatible Azure Blob storage with HDInsight, and you learned that Azure Blob storage is a fundamental component of HDInsight. This allows you to build scalable, long-term, archiving data acquisition solutions with Azure Blob storage and use HDInsight to unlock the information inside the stored  structured and unstructured data.

For more information, see:

* [Get Started with Azure HDInsight][hdinsight-get-started]
* [Upload data to HDInsight][hdinsight-upload-data]
* [Use Hive with HDInsight][hdinsight-use-hive]
* [Use Pig with HDInsight][hdinsight-use-pig]

[powershell-install]: /documentation/articles/install-configure-powershell
[hdinsight-creation]: /documentation/articles/hdinsight-provision-clusters
[hdinsight-get-started]: /documentation/articles/hdinsight-hadoop-tutorial-get-started-windows
[hdinsight-upload-data]: /documentation/articles/hdinsight-upload-data
[hdinsight-use-hive]: /documentation/articles/hdinsight-use-hive
[hdinsight-use-pig]: /documentation/articles/hdinsight-use-pig

[blob-storage-restAPI]: http://msdn.microsoft.com/zh-cn/library/azure/dd135733.aspx
[azure-storage-create]: /documentation/articles/storage-create-storage-account

[img-hdi-powershell-blobcommands]: ./media/hdinsight-hadoop-use-blob-storage/HDI.PowerShell.BlobCommands.png
[img-hdi-quick-create]: ./media/hdinsight-hadoop-use-blob-storage/HDI.QuickCreateCluster.png
[img-hdi-custom-create-storage-account]: ./media/hdinsight-hadoop-use-blob-storage/HDI.CustomCreateStorageAccount.png  
