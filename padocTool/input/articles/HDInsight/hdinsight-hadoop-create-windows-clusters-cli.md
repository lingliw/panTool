<properties
   pageTitle="Create Windows-based Hadoop clusters in HDInsight using Azure CLI"
   	description="Learn how to create clusters for Azure HDInsight by using Azure CLI."
   services="hdinsight"
   documentationCenter=""
   tags="azure-portal"
   authors="mumian"
   manager="paulettm"
   editor="cgronlun"/>

<tags
	ms.service="hdinsight"
	ms.date="01/04/2016"
	wacn.date=""/>

# Create Windows-based Hadoop clusters in HDInsight using Azure CLI

> [AZURE.SELECTOR]
- [Overview](/documentation/articles/hdinsight-provision-clusters-v1)
- [Azure Management Portal](/documentation/articles/hdinsight-hadoop-create-windows-clusters-portal)
- [Azure CLI](/documentation/articles/hdinsight-hadoop-create-windows-clusters-cli)
- [Azure PowerShell](/documentation/articles/hdinsight-hadoop-create-windows-clusters-powershell)
- [.NET SDK](/documentation/articles/hdinsight-hadoop-create-windows-clusters-dotnet-sdk)


Learn how to create HDInsight clusters using Azure CLI. For other cluster creation tools and features click the tab select on the top of this page or see [Cluster creation methods](/documentation/articles/hdinsight-provision-clusters-v1#cluster-creation-methods).

###Prerequisites:

Before you begin the instructions in this article, you must have the following:

- **Azure subscription**. See [Get Azure trial](/pricing/1rmb-trial/).
- **Azure CLI** - See [Install and configure the Azure CLI](/documentation/articles/xplat-cli-install) for installation and configuration information.

##Connect to Azure

Use the following command to connect to Azure:

	azure login -e AzureChinaCloud -u <your account>

For more information on authenticating using a work or school account, see [Connect to an Azure subscription from the Azure CLI](/documentation/articles/xplat-cli-connect).

To get help, use the **-h** switch.  For example:

	azure hdinsight cluster create -h
	
##Create clusters

You must have a Azure Blob storage account before you can create an HDInsight cluster. To create an HDInsight cluster, you must specify the following:

- **HDInsight cluster name**

- **Location**: One of the Azure data centers that supports HDInsight clusters. For a list of supported locations, see [HDInsight pricing](/home/features/hdinsight/#price).

- **Default storage account**: HDInsight uses an Azure Blob storage container as the default file system. An Azure Storage account is required before you can create an HDInsight cluster.

	To create a new Azure storage account:
	
		azure storage account create "<Azure Storage Account Name>" -l "<Azure Location>" --type LRS

	> [AZURE.NOTE] The Storage account must be collocated with HDInsight in the data center.
	> The storage account type can't be ZRS, because ZRS doesn't support table.

	For information on creating an Azure Storage account by using the Azure Management Portal, see [Create, manage, or delete a Storage account][azure-create-storageaccount].
	
	If you already have a Storage account but do not know the account name and account key, you can use the following commands to retrieve the information:
	
		-- Lists Storage accounts
		azure storage account list
		-- Shows a Storage account
		azure storage account show "<Storage Account Name>"
		-- Lists the keys for a Storage account
		azure storage account keys list "<Storage Account Name>"

	For details on getting the information by using the Azure Management Portal, see the "View, copy, and regenerate storage access keys" section of [Create, manage, or delete a Storage account][azure-create-storageaccount].

- **(Optional) Default Blob container**: The **azure hdinsight cluster create** command creates the container if it doesn't exist. If you choose to create the container beforehand, you can use the following command:

	azure storage container create --account-name "<Storage Account Name>" --account-key <Storage Account Key> [ContainerName]

Once you have the Storage account prepared, you are ready to create a cluster:

    
    azure hdinsight cluster create -c <HDInsight Cluster Name> -l <Location> --osType Windows --version <Cluster Version> --clusterType <Hadoop | HBase | Spark | Storm> --workerNodeCount 2 --headNodeSize Large --workerNodeSize Large --defaultStorageAccountName <Azure Storage Account Name>.blob.core.chinacloudapi.cn --defaultStorageAccountKey "<Default Storage Account Key>" --defaultStorageContainer <Default Blob Storage Container> --userName admin --password "<HTTP User Password>" --rdpUserName <RDP Username> --rdpPassword "<RDP User Password" --rdpAccessExpiry "03/01/2016"

## See also

- [Get started with Azure HDInsight](/documentation/articles/hdinsight-hadoop-tutorial-get-started-windows-v1) - Learn how to start working with your HDInsight cluster
- [Submit Hadoop jobs programmatically](/documentation/articles/hdinsight-submit-hadoop-jobs-programmatically) - Learn how to programmatically submit jobs to HDInsight
- [Manage Hadoop clusters in HDInsight using the Azure CLI](/documentation/articles/hdinsight-administer-use-command-line)
- [Using the Azure CLI for Mac, Linux, and Windows with Azure Service Management](/documentation/articles/virtual-machines-command-line-tools)