<!-- not suitable for mooncake-->

<properties
   	pageTitle="Create Hadoop, HBase, or Storm clusters on Linux in HDInsight using the Azure CLI | Windows Azure"
   	description="Learn how to create Hadoop, HBase, or Storm clusters on Linux for HDInsight using the Azure CLI."
   	services="hdinsight"
   	documentationCenter=""
   	authors="nitinme"
   	manager="paulettm"
   	editor="cgronlun"
	tags="azure-portal"/>

<tags
	ms.service="hdinsight"
	ms.date="10/14/2015"
	wacn.date=""/>

#Create Linux-based clusters in HDInsight using Azure PowerShell

[AZURE.INCLUDE [selector](../includes/hdinsight-create-linux-cluster-selector.md)]

Azure PowerShell is a powerful scripting environment that you can use to control and automate the deployment and management of your workloads in Azure. This document provides information on how to provision a Linux-based HDInsight cluster by using Azure PowerShell, as well as an example script.

> [AZURE.NOTE] Azure PowerShell is only available on Windows clients. If you are using a Linux, Unix, or Mac OS X client, see [Create a Linux-based HDInsight cluster using Azure CLI](/documentation/articles/hdinsight-hadoop-create-linux-cluster-azure-cli) for information on using the Azure CLI to create a cluster.

##Prerequisites

- **An Azure subscription**. See [Get Azure trial](/pricing/1rmb-trial/).

- __Azure PowerSHell__. For information on configuring a workstation to run HDInsight Windows PowerShell cmdlets, see [Install and configure Azure PowerShell](/documentation/articles/install-configure-powershell). For more information on using Azure PowerShell with HDInsight, see [Administer HDInsight using PowerShell](/documentation/articles/hdinsight-administer-use-powershell). For the list of the HDInsight Windows PowerShell cmdlets, see [HDInsight cmdlet reference](http://msdn.microsoft.com/zh-cn/library/azure/dn858087.aspx).

##Create the cluster

The following procedures are needed to provision an HDInsight cluster by using Azure PowerShell:

- Create an Azure resource group
- Create an Azure Storage account
- Create an Azure Blob container
- Create an HDInsight cluster

The two most important parameters that you must set to provision Linux clusters are the ones where you specify the OS type and the SSH user details:

- Make sure you specify the **-OSType** parameter as **Linux**.
- To use SSH for remote sessions on the clusters, you can specify either SSH user password or the SSH public key. If you specify both the SSH user password and the SSH public key, the key will be ignored. If you want to use the SSH key for remote sessions, you must specify a blank SSH password when prompted for one. For more information on using SSH with HDInsight, see one of the following articles:
    
    * [Use SSH with Linux-based Hadoop on HDInsight from Linux, Unix, or OS X](/documentation/articles/hdinsight-hadoop-linux-use-ssh-unix)
    * [Use SSH with Linux-based Hadoop on HDInsight from Windows](/documentation/articles/hdinsight-hadoop-linux-use-ssh-windows)

The following script demonstrates how to create a new cluster:

    # Use the new Azure Resource Manager mode
    Switch-AzureMode AzureResourceManager

    ###########################################
    # Create required items, if none exist
    ###########################################

    # Sign in
    Add-AzureAccount

    # Select the subscription to use
    $subscriptionName = "<SubscriptionName>"        # Provide your Subscription Name
    Select-AzureSubscription -SubscriptionName $subscriptionName

    # Register your subscription to use HDInsight
    Register-AzureProvider -ProviderNamespace "Microsoft.HDInsight" -Force

    # Create an Azure Resource Group
    $resourceGroupName = "<ResourceGroupName>"      # Provide a Resource Group name
    $location = "<Location>"                        # For example, "China North"
    New-AzureResourceGroup -Name $resourceGroupName -Location $location

    # Create an Azure Storage account
    $storageAccountName = "<StorageAcccountName>"   # Provide a Storage account name
    New-AzureStorageAccount -ResourceGroupName $resourceGroupName -StorageAccountName $storageAccountName -Location $location -Type Standard_GRS

    # Create an Azure Blob Storage container
    $containerName = "<ContainerName>"              # Provide a container name
    $storageAccountKey = Get-AzureStorageAccountKey -Name $storageAccountName -ResourceGroupName $resourceGroupName | %{ $_.Key1 }
    $destContext = New-AzureStorageContext -StorageAccountName $storageAccountName -StorageAccountKey $storageAccountKey
    New-AzureStorageContainer -Name $containerName -Context $destContext

    ###########################################
    # Create an HDInsight Cluster
    ###########################################

    # Skip these variables if you just created them
    $resourceGroupName = "<ResourceGroupName>"      # Provide the Resource Group name
    $storageAccountName = "<StorageAcccountName>"   # Provide the Storage account name
    $containerName = "<ContainerName>"              # Provide the container name
    $storageAccountKey = Get-AzureStorageAccountKey -Name $storageAccountName -ResourceGroupName $resourceGroupName | %{ $_.Key1 }

    # Set these variables
    $clusterName = $containerName           		# As a best practice, have the same name for the cluster and container
    $clusterNodes = <ClusterSizeInNodes>    		# The number of nodes in the HDInsight cluster
    $credentials = Get-Credential
    $sshCredentials = Get-Credential

    # The location of the HDInsight cluster. It must be in the same data center as the Storage account.
    $location = Get-AzureStorageAccount -ResourceGroupName $resourceGroupName -StorageAccountName $storageAccountName | %{$_.Location}

    # Create a new HDInsight cluster
    New-AzureHDInsightCluster -ClusterName $clusterName -ResourceGroupName $resourceGroupName -HttpCredential $credentials -Location $location -DefaultStorageAccountName "$storageAccountName.blob.core.chinacloudapi.cn" -DefaultStorageAccountKey $storageAccountKey -DefaultStorageContainer $containerName  -ClusterSizeInNodes $clusterNodes -ClusterType Hadoop -OSType Linux -Version "3.2" -SshCredential $sshCredentials

> [AZURE.NOTE] The values you specify for **$clusterCredentials** are used to create the Hadoop user account for the cluster. You will use this account to connect to the cluster. The values you specify for the **$sshCredentials** are used to create the SSH user for the cluster. You use this account to start a remote SSH session on the cluster and run jobs. If you use the Quick Create option from the Azure Management Portal to provision a cluster, the default Hadoop user name is "admin" and default SSH user name is "hdiuser".

It can take up to 15 minutes for the provisioning to complete.

##Next steps

Now that you have successfully created an HDInsight cluster, use the following to learn how to work with your cluster:

###Hadoop clusters

* [Use Hive with HDInsight](/documentation/articles/hdinsight-use-hive)
* [Use Pig with HDInsight](/documentation/articles/hdinsight-use-pig)
* [Use MapReduce with HDInsight](/documentation/articles/hdinsight-use-mapreduce)

###HBase clusters

* [Get started with HBase on HDInsight](/documentation/articles/hdinsight-hbase-tutorial-get-stared-linux)
* [Develop Java applications for HBase on HDInsight](/documentation/articles/hdinsight-hbase-build-java-maven-linux)

###Storm clusters

* [Develop Java topologies for Storm on HDInsight](/documentation/articles/hdinsight-storm-develop-java-topology)
* [Use Python components in Storm on HDInsight](/documentation/articles/hdinsight-storm-develop-python)
* [Deploy and monitor topologies with Storm on HDInsight](/documentation/articles/hdinsight-storm-deploy-monitor-topology-linux)