<properties
   pageTitle="Create Windows-based Hadoop clusters in HDInsight using Azure PowerShell| Windows Azure"
   	description="Learn how to create clusters for Azure HDInsight by using Azure PowerShell."
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

# Create Windows-based Hadoop clusters in HDInsight using Azure PowerShell

> [AZURE.SELECTOR]
- [Overview](/documentation/articles/hdinsight-provision-clusters-v1)
- [Azure Management Portal](/documentation/articles/hdinsight-hadoop-create-windows-clusters-portal)
- [Azure CLI](/documentation/articles/hdinsight-hadoop-create-windows-clusters-cli)
- [Azure PowerShell](/documentation/articles/hdinsight-hadoop-create-windows-clusters-powershell)
- [.NET SDK](/documentation/articles/hdinsight-hadoop-create-windows-clusters-dotnet-sdk)


Learn how to create HDInsight clusters using Azure PowerShell. Azure PowerShell is a module that provides cmdlets to manage Azure with Windows PowerShell. For other cluster creation tools and features click the tab select on the top of this page or see [Cluster creation methods](/documentation/articles/hdinsight-provision-clusters-v1#cluster-creation-methods).


###Prerequisites:

Before you begin the instructions in this article, you must have the following:

- Azure subscription. See [Get Azure trial](/pricing/1rmb-trial/).
- Azure PowerShell.  See [Install Azure PowerShell 1.0](/documentation/articles/hdinsight-administer-use-powershell#install-azure-powershell-10-and-greater).



## Create clusters
Azure PowerShell is a powerful scripting environment that you can use to control and automate the deployment and management of your workloads in Azure. This section provides instructions on how to create an HDInsight cluster by using Azure PowerShell. For information on configuring a workstation to run HDInsight Windows PowerShell cmdlets, see [Install and configure Azure PowerShell](/documentation/articles/powershell-install-configure). For more information on using Azure PowerShell with HDInsight, see [Administer HDInsight using PowerShell](/documentation/articles/hdinsight-administer-use-powershell). For the list of the HDInsight Windows PowerShell cmdlets, see [HDInsight cmdlet reference](https://msdn.microsoft.com/zh-cn/library/azure/dn858087.aspx).


The following procedures are needed to create an HDInsight cluster by using Azure PowerShell:

    ####################################
    # Set these variables
    ####################################
    #region - used for creating Azure service names
    $nameToken = "<Enter an Alias>" 
    #endregion

    #region - cluster user accounts
    $httpUserName = "admin"  #HDInsight cluster username
    $httpPassword = "<Enter a Password>"
    #endregion

    ###########################################
    # Service names and varialbes
    ###########################################
    #region - service names
    $namePrefix = $nameToken.ToLower() + (Get-Date -Format "MMdd")

    $hdinsightClusterName = $namePrefix + "hdi"
    $defaultStorageAccountName = $namePrefix + "store"
    $defaultBlobContainerName = $hdinsightClusterName

    $location = "China East 2"
    $clusterSizeInNodes = 1
    #endregion

    # Treat all errors as terminating
    $ErrorActionPreference = "Stop"

    ###########################################
    # Connect to Azure
    ###########################################
    #region - Connect to Azure subscription
    Write-Host "`nConnecting to your Azure subscription ..." -ForegroundColor Green
    try{Get-AzureContext}
    catch{Add-AzureAccount -Environment AzureChinaCloud}
    #endregion

    ###########################################
    # Preapre default storage account and container
    ###########################################
    New-AzureStorageAccount `
        -StorageAccountName $defaultStorageAccountName `
        -Type Standard_GRS `
        -Location $location

    $defaultStorageAccountKey = Get-AzureStorageAccountKey `
                                    -StorageAccountName $defaultStorageAccountName |  %{ $_.Primary }
    $defaultStorageContext = New-AzureStorageContext `
                                    -StorageAccountName $defaultStorageAccountName `
                                    -StorageAccountKey $defaultStorageAccountKey
    New-AzureStorageContainer `
        -Name $hdinsightClusterName ` #use the cluster name as the container name
        -Context $defaultStorageContext 

    ###########################################
    # Create the cluster
    ###########################################

    $httpPW = ConvertTo-SecureString -String $httpPassword -AsPlainText -Force
    $httpCredential = New-Object System.Management.Automation.PSCredential($httpUserName,$httpPW)

    New-AzureHDInsightCluster `
        -Name $hdinsightClusterName `
        -Location $location `
        -ClusterSizeInNodes $clusterSizeInNodes `
        -ClusterType Hadoop `
        -Version "3.2" `
        -Credential $httpCredential `
        -DefaultStorageAccountName "$defaultStorageAccountName.blob.core.chinacloudapi.cn" `
        -DefaultStorageAccountKey $defaultStorageAccountKey `
        -DefaultStorageContainerName $hdinsightClusterName 

    ####################################
    # Verify the cluster
    ####################################
    Get-AzureHDInsightCluster -Name $hdinsightClusterName 

## Create clusters using ARM template

You can use Azure PowerShell to deploy an ARM template which creates an HDInsight cluster.  See [Call templates using Azure PowerShell](/documentation/articles/hdinsight-hadoop-create-windows-clusters-arm-templates#call-templates-using-powershell).

##Customize clusters

- See [Customize HDInsight clusters using Bootstrap](/documentation/articles/hdinsight-hadoop-customize-cluster-v1-bootstrap#use-azure-powershell).
- See [Customize Windows-based HDInsight clusters using Script Action](/documentation/articles/hdinsight-hadoop-customize-cluster-v1#call-scripts-using-azure-powershell).


##Next steps
In this article, you have learned several ways to create an HDInsight cluster. To learn more, see the following articles:

* [Get started with Azure HDInsight](/documentation/articles/hdinsight-hadoop-tutorial-get-started-windows-v1) - Learn how to start working with your HDInsight cluster
* [Submit Hadoop jobs programmatically](/documentation/articles/hdinsight-submit-hadoop-jobs-programmatically) - Learn how to programmatically submit jobs to HDInsight
* [Manage Hadoop clusters in HDInsight using PowerShell](/documentation/articles/hdinsight-administer-use-powershell) - Learn how to work with HDInsight by using Azure PowerShell
* [Azure HDInsight SDK documentation] [hdinsight-sdk-documentation] - Discover the HDInsight SDK




[hdinsight-sdk-documentation]: http://msdn.microsoft.com/zh-cn/library/dn479185.aspx
[azure-preview-portal]: https://manage.windowsazure.cn
[connectionmanager]: http://msdn.microsoft.com/zh-cn/library/mt146773(v=sql.120).aspx
[ssispack]: http://msdn.microsoft.com/zh-cn/library/mt146770(v=sql.120).aspx
[ssisclustercreate]: http://msdn.microsoft.com/zh-cn/library/mt146774(v=sql.120).aspx
[ssisclusterdelete]: http://msdn.microsoft.com/zh-cn/library/mt146778(v=sql.120).aspx
