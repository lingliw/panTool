<properties
   pageTitle="Use Hadoop Hive with PowerShell in HDInsight | Windows Azure"
   description="Use PowerShell to run Hive queries in Hadoop on HDInsight."
   services="hdinsight"
   documentationCenter=""
   authors="Blackmist"
   manager="paulettm"
   editor="cgronlun"
	tags="azure-portal"/>

<tags
	ms.service="hdinsight"
	ms.date="09/03/2015"
	wacn.date=""/>

#Run Hive queries using PowerShell

[AZURE.INCLUDE [hive-selector](../includes/hdinsight-selector-use-hive.md)]

This document provides an example of using Azure PowerShell in the Azure Resource Group mode to run Hive queries in a Hadoop on HDInsight cluster. For using Azure PowerShell in the Azure Service mode, see [Run Hive queries using PowerShell ASM mode](/documentation/articles/hdinsight-hadoop-use-hive-powershell-v1).

> [AZURE.NOTE] This document does not provide a detailed description of what the HiveQL statements that are used in the examples do. For information on the HiveQL that is used in this example, see [Use Hive with Hadoop on HDInsight](/documentation/articles/hdinsight-use-hive).


<!-- keep by customization: begin -->
<a id="prereq"></a>
<!-- keep by customization: end -->
**Prerequisites**

To complete the steps in this article, you will need the following.

- **An Azure HDInsight (Hadoop on HDInsight) cluster (Windows-based<!-- deleted by customization or Linux-based -->)**
- **A workstation with Azure PowerShell**. See [Install and use Azure PowerShell](/documentation/articles/install-configure-powershell).

<!-- keep by customization: begin -->
<a id="powershell"></a>
<!-- keep by customization: end -->
##Run Hive queries using Azure PowerShell

Azure PowerShell provides *cmdlets* that allow you to remotely run Hive queries on HDInsight. Internally, this is accomplished by using REST calls to [WebHCat](https://cwiki.apache.org/confluence/display/Hive/WebHCat) (formerly called Templeton) running on the HDInsight cluster.

The following cmdlets are used when running Hive queries in a remote HDInsight cluster:

* **Add-AzureAccount**: Authenticates Azure PowerShell to your Azure subscription

* **New-AzureHDInsightHiveJobDefinition**: Creates a new *job definition* by using the specified HiveQL statements

* **Start-AzureHDInsightJob**: Sends the job definition to HDInsight, starts the job, and returns a *job* object that can be used to check the status of the job

* **Wait-AzureHDInsightJob**: Uses the job object to check the status of the job. It will wait until the job completes or the wait time is exceeded.

* **Get-AzureHDInsightJobOutput**: Used to retrieve the output of the job

* **Invoke-AzureHDInsightHiveJob**: Used to run HiveQL statements. This will block the query completes, then returns the results

* **Use-AzureHDInsightCluster**: Sets the current cluster to use for the **Invoke-Hive** command

The following steps demonstrate how to use these cmdlets to run a job in your HDInsight cluster:

1. Using an editor, save the following code as **hivejob.ps1**. You must replace **CLUSTERNAME** with the name of your HDInsight cluster.

		#Specify the values
		$clusterName = "CLUSTERNAME"
		$resourceGroupName = "RESOURCEGROUPNAME"
		$httpUsername = "HTTPUSERNAME"
		$httpUserPassword  = "HTTPUSERPASSWORD"

		# Switch to the ARM mode
		Switch-AzureMode -Name AzureResourceManager
		
		# Login to your Azure subscription
		# Is there an active Azure subscription?
		$sub = Get-AzureSubscription -ErrorAction SilentlyContinue
		if(-not($sub))
		{
		    Add-AzureAccount
		}

		#HiveQL
		$queryString = "DROP TABLE log4jLogs;" +
				       "CREATE EXTERNAL TABLE log4jLogs(t1 string, t2 string, t3 string, t4 string, t5 string, t6 string, t7 string) ROW FORMAT DELIMITED FIELDS TERMINATED BY ' ' STORED AS TEXTFILE LOCATION 'wasb:///example/data/';" +
				       "SELECT * FROM log4jLogs WHERE t4 = '[ERROR]';"

		#Create an HDInsight Hive job definition
		$hiveJobDefinition = New-AzureHDInsightHiveJobDefinition -Query $queryString 

		#Submit the job to the cluster
		Write-Host "Start the Hive job..." -ForegroundColor Green

		$passwd = ConvertTo-SecureString $httpUserPassword -AsPlainText -Force
		$creds = New-Object System.Management.Automation.PSCredential ($httpUsername, $passwd)
		$hiveJob = Start-AzureHDInsightJob -ResourceGroupName $resourceGroupName -ClusterName $clusterName -JobDefinition $hiveJobDefinition -ClusterCredential $creds


		#Wait for the Hive job to complete
		Write-Host "Wait for the job to complete..." -ForegroundColor Green
		Wait-AzureHDInsightJob -ResourceGroupName $resourceGroupName -ClusterName $clusterName -JobId $hiveJob.JobId -ClusterCredential $creds

		# Print the output
		Write-Host "Display the standard output..." -ForegroundColor Green
		Get-AzureHDInsightJobOutput -ClusterName $clusterName -JobId $hiveJob.JobId -StandardOutput 

2. Open a new **Azure PowerShell** command prompt. Change directories to the location of the **hivejob.ps1** file, then use the following command to run the script:

		.\hivejob.ps1

7. When the job completes, it should return information similar to the following:

		Display the standard output...
		[ERROR]	3

4. As mentioned earlier, **Invoke-Hive** can be used to run a query and wait for the response. Use the following commands, and replace **CLUSTERNAME** with the name of your cluster:

		Use-AzureHDInsightCluster CLUSTERNAME
		Invoke-Hive -Query @"
		CREATE TABLE IF NOT EXISTS errorLogs (t1 string, t2 string, t3 string, t4 string, t5 string, t6 string, t7 string) STORED AS ORC;
		INSERT OVERWRITE TABLE errorLogs SELECT t1, t2, t3, t4, t5, t6, t7 FROM log4jLogs WHERE t4 = '[ERROR]';
		SELECT * FROM errorLogs;
		"@

	The output will look like the following:

		2012-02-03	18:35:34	SampleClass0	[ERROR]	incorrect	id
		2012-02-03	18:55:54	SampleClass1	[ERROR]	incorrect	id
		2012-02-03	19:25:27	SampleClass4	[ERROR]	incorrect	id

	> [AZURE.NOTE] For longer HiveQL queries, you can use the Azure PowerShell **Here-Strings** cmdlet or HiveQL script files. The following snippet shows how to use the **Invoke-Hive** cmdlet to run a HiveQL script file. The HiveQL script file must be uploaded to wasb://.
	>
	> `Invoke-Hive -File "wasb://<ContainerName>@<StorageAccountName>/<Path>/query.hql"`
	>
	> For more information about **Here-Strings**, see <a href="http://technet.microsoft.com/zh-cn/library/ee692792.aspx" target="_blank">Using Windows PowerShell Here-Strings</a>.

<!-- keep by customization: begin -->
<a id="troubleshooting"></a>
<!-- keep by customization: end -->
##Troubleshooting

If no information is returned when the job completes, an error may have occurred during processing. To view error information for this job, add the following to the end of the **hivejob.ps1** file, save it, and then run it again.

	# Print the output of the Hive job.
	Write-Host "Display the standard output ..." -ForegroundColor Green
	Get-AzureHDInsightJobOutput -Cluster $clusterName -JobId $hiveJob.JobId -StandardError

This returns the information that is written to STDERR on the server when you ran the job, and it may help determine why the job is failing.

<!-- keep by customization: begin -->
<a id="summary"></a>
<!-- keep by customization: end -->
##Summary

As you can see, Azure PowerShell provides an easy way to run Hive queries in an HDInsight cluster, monitor the job status, and retrieve the output.

<!-- keep by customization: begin -->
<a id="nextsteps"></a>
<!-- keep by customization: end -->
##Next steps

For general information about Hive in HDInsight:

* [Use Hive with Hadoop on HDInsight](/documentation/articles/hdinsight-use-hive)

For information about other ways you can work with Hadoop on HDInsight:

* [Use Pig with Hadoop on HDInsight](/documentation/articles/hdinsight-use-pig)

* [Use MapReduce with Hadoop on HDInsight](/documentation/articles/hdinsight-use-mapreduce)
