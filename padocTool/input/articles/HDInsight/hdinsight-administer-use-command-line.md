<properties
	pageTitle="Manage Hadoop clusters using Azure CLI | Windows Azure"
	description="How to use the Azure CLI to manage Hadoop clusters in HDIsight"
	services="hdinsight"
	editor="cgronlun"
	manager="paulettm"
	authors="mumian"
	tags="azure-portal"
	documentationCenter=""/>

<tags
	ms.service="hdinsight"
	ms.date="09/17/2015"
	wacn.date=""/>

# Manage Hadoop clusters in HDInsight by using the Azure Command-line Interface (Azure CLI)

[AZURE.INCLUDE [selector](../includes/hdinsight-portal-management-selector.md)]

Learn how to use the Azure CLI to manage Hadoop clusters in Azure HDInsight. The Azure CLI is implemented in Node.js. It can be used on any platform that supports Node.js<!-- deleted by customization , including Windows, Mac, and Linux -->.

The Azure CLI is open source. The source code is managed in GitHub at <a href= "https://github.com/azure/azure-xplat-cli">https://github.com/azure/azure-xplat-cli</a>.

This article covers only using the Azure CLI with HDInsight. For a general guide on how to use Azure CLI, see [How to use the Azure CLI] [azure-command-line-tools].


##Prerequisites

Before you begin this article, you must have the following:

- **An Azure subscription**. See [Get Azure trial](/pricing/1rmb-trial/).

- **Azure CLI** - See [Install and configure the Azure CLI](/documentation/articles/xplat-cli-install) for installation and configuration information.

##Installation

If you have not already done so, use the [Install and configure the Azure CLI](/documentation/articles/xplat-cli-install) document to install and configure the Azure CLI.

##Provision an HDInsight cluster

[AZURE.INCLUDE [provisioningnote](../includes/hdinsight-provisioning.md)]


HDInsight uses an Azure Blob storage container as the default file system. An Azure Storage account is required before you can create an HDInsight cluster.

After you have imported the publishsettings file, you can use the following command to create a Storage account:

	azure account storage create [options] <StorageAccountName>


> [AZURE.NOTE] The Storage account must be collocated with HDInsight in the data center.


For information on creating an Azure Storage account by using the Azure <!-- deleted by customization preview portal --><!-- keep by customization: begin -->Management Portal<!-- keep by customization: end -->, see [Create, manage, or delete a Storage account][azure-create-storageaccount].

If you already have a Storage account but do not know the account name and account key, you can use the following commands to retrieve the information:

	-- Lists Storage accounts
	azure account storage list
	-- Shows a Storage account
	azure account storage show <StorageAccountName>
	-- Lists the keys for a Storage account
	azure account storage keys list <StorageAccountName>

For details on getting the information by using the Azure <!-- deleted by customization preview portal --><!-- keep by customization: begin -->Management Portal<!-- keep by customization: end -->, see the "View, copy, and regenerate storage access keys" section of [Create, manage, or delete a Storage account][azure-create-storageaccount].


The **azure hdinsight cluster create** command creates the container if it doesn't exist. If you choose to create the container beforehand, you can use the following command:

	azure storage container create --account-name <StorageAccountName> --account-key <StorageAccountKey> [ContainerName]

Once you have the Storage account and the Blob container prepared, you are ready to create a cluster:

	azure hdinsight cluster create --clusterName <ClusterName> --storageAccountName <StorageAccountName> --storageAccountKey <storageAccountKey> --storageContainer <StorageContainer> --nodes <NumberOfNodes> --location <DataCenterLocation> --username <HDInsightClusterUsername> --clusterPassword <HDInsightClusterPassword>

![HDI.CLIClusterCreation][image-cli-clustercreation]

















##Provision an HDInsight cluster by using a configuration file
Typically, you provision an HDInsight cluster, run jobs on it, and then delete the cluster to cut down the cost. The command-line interface gives you the option to save the configurations into a file, so that you can reuse it every time you provision a cluster.  

	azure hdinsight cluster config create <file>

	azure hdinsight cluster config set <file> --clusterName <ClusterName> --nodes <NumberOfNodes> --location "<DataCenterLocation>" --storageAccountName "<StorageAccountName>.blob.core.chinacloudapi.cn" --storageAccountKey "<StorageAccountKey>" --storageContainer "<BlobContainerName>" --username "<Username>" --clusterPassword "<UserPassword>"

	azure hdinsight cluster config storage add <file> --storageAccountName "<StorageAccountName>.blob.core.chinacloudapi.cn"
	       --storageAccountKey "<StorageAccountKey>"

	azure hdinsight cluster config metastore set <file> --type "hive" --server "<SQLDatabaseName>.database.chinacloudapi.cn"
	       --database "<HiveDatabaseName>" --user "<Username>" --metastorePassword "<UserPassword>"

	azure hdinsight cluster config metastore set <file> --type "oozie" --server "<SQLDatabaseName>.database.chinacloudapi.cn"
	       --database "<OozieDatabaseName>" --user "<SQLUsername>" --metastorePassword "<SQLPassword>"

	azure hdinsight cluster create --config <file>



![HDI.CLIClusterCreationConfig][image-cli-clustercreation-config]


##List and show cluster details
Use the following commands to list and show cluster details:

	azure hdinsight cluster list
	azure hdinsight cluster show <ClusterName>

![HDI.CLIListCluster][image-cli-clusterlisting]


##Delete a cluster
Use the following command to delete a cluster:

	azure hdinsight cluster delete <ClusterName>

##<a name="scaling"></a>Scale a cluster

To change the Hadoop cluster size by using Azure PowerShell, run the following command from a client machine:

	Set-AzureHDInsightClusterSize -ClusterSizeInNodes <NewSize> -name <clustername>

##Next steps
In this article, you have learned how to perform different HDInsight cluster administrative tasks. To learn more, see the following articles:

* [Administer HDInsight by using the Azure <!-- deleted by customization preview portal --><!-- keep by customization: begin -->Management Portal<!-- keep by customization: end -->] [hdinsight-admin-portal]
* [Administer HDInsight by using Azure PowerShell] [hdinsight-admin-powershell]
* [Get started with Azure HDInsight] [hdinsight-get-started]
* [How to use the Azure CLI] [azure-command-line-tools]


[azure-command-line-tools]: /documentation/articles/xplat-cli-install
[azure-create-storageaccount]: /documentation/articles/storage-create-storage-account
[azure-purchase-options]: /pricing/overview/
[azure-member-offers]: http://azure.microsoft.com/pricing/member-offers/
[azure-trial]: /pricing/1rmb-trial/


[hdinsight-admin-portal]: /documentation/articles/hdinsight-administer-use-management-portal-v1
[hdinsight-admin-powershell]: /documentation/articles/hdinsight-administer-use-powershell
[hdinsight-get-started]: /documentation/articles/hdinsight-get-started
[image-cli-account-download-import]: ./media/hdinsight-administer-use-command-line/HDI.CLIAccountDownloadImport.png
[image-cli-clustercreation]: ./media/hdinsight-administer-use-command-line/HDI.CLIClusterCreation.png
[image-cli-clustercreation-config]: ./media/hdinsight-administer-use-command-line/HDI.CLIClusterCreationConfig.png
[image-cli-clusterlisting]: ./media/hdinsight-administer-use-command-line/HDI.CLIListClusters.png "List and show clusters"
