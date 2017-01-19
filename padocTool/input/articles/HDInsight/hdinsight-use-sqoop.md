<!-- need to be customized -->

<properties
	pageTitle="Use Hadoop Sqoop in HDInsight | Azure"
	description="Learn how to use Azure PowerShell from a workstation to run Sqoop import and export between an Hadoop cluster and an Azure SQL database."
	editor="cgronlun"
	manager="paulettm"
	services="hdinsight"
	documentationCenter=""
	tags="azure-portal"
	authors="mumian"/>

<tags
	ms.service="hdinsight"
	ms.date="03/03/2016"
	wacn.date=""/>

#Use Sqoop with Hadoop in HDInsight (Windows)

> [AZURE.SELECTOR]
- [PowerShell](/documentation/articles/hdinsight-use-sqoop)


Learn how to use Sqoop in HDInsight to import and export between HDInsight cluster and Azure SQL database or SQL Server database.

Although Hadoop is a natural choice for processing unstructured and semistructured data, 
such as logs and files, there may also be a need to process structured data that is 
stored in relational databases.

[Sqoop][sqoop-user-guide-1.4.4] is a tool designed to transfer data between Hadoop 
clusters and relational databases. You can use it to import data from a relational 
database management system (RDBMS) such as SQL Server, MySQL, or Oracle into the Hadoop 
distributed file system (HDFS), transform the data in Hadoop with MapReduce or Hive, and 
then export the data back into an RDBMS. In this tutorial, you are using a SQL Server 
database for your relational database.

For Sqoop versions that are supported on HDInsight clusters, 
see [What's new in the cluster versions provided by HDInsight?][hdinsight-versions].

###<a name="prerequisites"></a> Prerequisites

Before you begin this tutorial, you must have the following:

- **A workstation with Azure PowerShell**. See [Install Azure PowerShell 1.0 and greater](/documentation/articles/hdinsight-administer-use-powershell#install-azure-powershell-10-and-greater).

##Understand the scenario

HDInsight cluster comes with some sample data. You will use the following two samples:

- A log4j log file, which is located at */example/data/sample.log*. The following logs are extracted from the file:

		2012-02-03 18:35:34 SampleClass6 [INFO] everything normal for id 577725851
		2012-02-03 18:35:34 SampleClass4 [FATAL] system problem at id 1991281254
		2012-02-03 18:35:34 SampleClass3 [DEBUG] detail for id 1304807656
		...

- A Hive table named *hivesampletable*, which references the data file located at */hive/warehouse/hivesampletable*. The table contains some mobile device data. 

You will first export *sample.log* and *hivesampletable* to the Azure 
SQL database or to SQL Server, and then import the table that contains the 
mobile device data back to HDInsight by using the following path:

	/tutorials/usesqoop/importeddata

## Create cluster and SQL database

Create a SQL database on [Azure Management Portal](https://manage.windowsazure.cn).

1. log into [Azure Management Portal](https://manage.windowsazure.cn).
2. Click **New** > **Data Services** > **Sql Database** > **Custom Create**.
3. Enter the name for your database, select **Service Tiers**, **Performance Level**, **Collation**, and **Server** for you database.
4. If you Choose to create a new SQL database server for you database, click next. If you Choose an existing Service, make sure it satisfy the [below conditions](#sql_server_condition), and click complete.
5. Enter the login username and password, and select the region for your sql server if you choose to create a new server.

> [AZURE.NOTE] The Resource Group Name of a SQl Server is "Default-Sql-chinaeast" or "Default-Sql-chinanorth" depending on the region of the SQL Server.

Create a cluster on [Azure Management Portal](https://manage.windowsazure.cn).

1. log into [Azure Management Portal](https://manage.windowsazure.cn).
2. Click **New** > **Data Services** > **HDInsight** > **Hadoop**.
3. Enter the name, HTTP password for your cluster, and select the **Cluster Size**, and **Storage Account**.
4. Click **Create HDInsight Cluster**.

If you choose to use existing Azure SQL database or Microsoft SQL Server

- **Azure SQL database**: You must configure a firewall rule for the Azure SQL database server to allow access from your workstation. For instructions about creating an Azure SQL database and configuring the firewall, see [Get started using Azure SQL database][sqldatabase-get-started]. 

    > [AZURE.NOTE] By default an Azure SQL database allows connections from Azure services, such as Azure HDInsight. If this firewall setting is disabled, you must enabled it from the Azure Management Portal. For instruction about creating an Azure SQL database and configuring firewall rules, see [Create and Configure SQL Database][sqldatabase-create-configue].

<a name="sql_server_condition"></a>
- **SQL Server**: If your HDInsight cluster is on the same virtual network in Azure as SQL Server, you can use the steps in this article to import and export data to a SQL Server database.

    > [AZURE.NOTE] HDInsight supports only location-based virtual networks, and it does not currently work with affinity group-based virtual networks.

    * To create and configure a virtual network, see [Virtual Network Configuration Tasks](/home/features/virtual-machines/).

        * When you are using SQL Server in your datacenter, you must configure the virtual network as *site-to-site* or *point-to-site*.

            > [AZURE.NOTE] For **point-to-site** virtual networks, SQL Server must be running the VPN client configuration application, which is available from the **Dashboard** of your Azure virtual network configuration.

        * When you are using SQL Server on an Azure virtual machine, any virtual network configuration can be used if the virtual machine hosting SQL Server is a member of the same virtual network as HDInsight.

    * To create an HDInsight cluster on a virtual network, see [Create Hadoop clusters in HDInsight using custom options](/documentation/articles/hdinsight-provision-clusters-v1)

    > [AZURE.NOTE] SQL Server must also allow authentication. You must use a SQL Server login to complete the steps in this article.
	

## Run Sqoop using PowerShell

The following PowerShell script pre-processes the source file, and exports it to an Azure SQL database:

    $hdinsightClusterName = "<HDInsightClusterName>"

    $httpUserName = "admin"
    $httpPassword = "<Password>"

    $defaultStorageAccountName = $hdinsightClusterName + "store"
    $defaultBlobContainerName = $hdinsightClusterName


    $sqlDatabaseServerName = $hdinsightClusterName + "dbserver"
    $sqlDatabaseName = $hdinsightClusterName + "db"
    $sqlDatabaseLogin = "sqluser"
    $sqlDatabasePassword = "<Password>"

    #region - Connect to Azure subscription
    Write-Host "`nConnecting to your Azure subscription ..." -ForegroundColor Green
    try{Get-AzureSubscription}
    catch{Add-AzureAccount -Environment AzureChinaCloud}
    #endregion
        
    #region - pre-process the source file
        
    Write-Host "`nPreprocessing the source file ..." -ForegroundColor Green
        
    # This procedure creates a new file with $destBlobName
    $sourceBlobName = "example/data/sample.log"
    $destBlobName = "tutorials/usesqoop/data/sample.log"
        
    # Define the connection string
    $defaultStorageAccountKey = Get-AzureStorageKey `
                                    -StorageAccountName $defaultStorageAccountName |  %{ $_.primary }
    $storageConnectionString = "DefaultEndpointsProtocol=https;AccountName=$defaultStorageAccountName;AccountKey=$defaultStorageAccountKey"
        
    # Create block blob objects referencing the source and destination blob.
    $storageAccount = [Microsoft.WindowsAzure.Storage.CloudStorageAccount]::Parse($storageConnectionString)
    $storageClient = $storageAccount.CreateCloudBlobClient();
    $storageContainer = $storageClient.GetContainerReference($defaultBlobContainerName)
    $sourceBlob = $storageContainer.GetBlockBlobReference($sourceBlobName)
    $destBlob = $storageContainer.GetBlockBlobReference($destBlobName)
        
    # Define a MemoryStream and a StreamReader for reading from the source file
    $stream = New-Object System.IO.MemoryStream
    $stream = $sourceBlob.OpenRead()
    $sReader = New-Object System.IO.StreamReader($stream)
        
    # Define a MemoryStream and a StreamWriter for writing into the destination file
    $memStream = New-Object System.IO.MemoryStream
    $writeStream = New-Object System.IO.StreamWriter $memStream
        
    # Pre-process the source blob
    $exString = "java.lang.Exception:"
    while(-Not $sReader.EndOfStream){
        $line = $sReader.ReadLine()
        $split = $line.Split(" ")
        
        # remove the "java.lang.Exception" from the first element of the array
        # for example: java.lang.Exception: 2012-02-03 19:11:02 SampleClass8 [WARN] problem finding id 153454612
        if ($split[0] -eq $exString){
            #create a new ArrayList to remove $split[0]
            $newArray = [System.Collections.ArrayList] $split
            $newArray.Remove($exString)
        
            # update $split and $line
            $split = $newArray
            $line = $newArray -join(" ")
        }
        
        # remove the lines that has less than 7 elements
        if ($split.count -ge 7){
            write-host $line
            $writeStream.WriteLine($line)
        }
    }
        
    # Write to the destination blob
    $writeStream.Flush()
    $memStream.Seek(0, "Begin")
    $destBlob.UploadFromStream($memStream)
        
    #endregion
        
    #region - export the log file from the cluster to the SQL database
        
    Write-Host "Exporting the log file ..." -ForegroundColor Green

    $pw = ConvertTo-SecureString -String $httpPassword -AsPlainText -Force
    $httpCredential = New-Object System.Management.Automation.PSCredential($httpUserName,$pw)
        
    # Connection string for Azure SQL Database.
    # Comment if using SQL Server
    $connectionString = "jdbc:sqlserver://$sqlDatabaseServerName.database.chinacloudapi.cn;user=$sqlDatabaseLogin@$sqlDatabaseServerName;password=$sqlDatabasePassword;database=$sqlDatabaseName"
    # Connection string for SQL Server.
    # Uncomment if using SQL Server.
    #$connectionString = "jdbc:sqlserver://$sqlDatabaseServerName;user=$sqlDatabaseLogin;password=$sqlDatabasePassword;database=$sqlDatabaseName"
        
    $tableName_log4j = "log4jlogs"
    $exportDir_log4j = "/tutorials/usesqoop/data"
        
    # Submit a Sqoop job
    $sqoopDef = New-AzureHDInsightSqoopJobDefinition `
        -Command "export --connect $connectionString --table $tableName_log4j --export-dir $exportDir_log4j --input-fields-terminated-by ' ' -m 1"

    $sqoopJob = Start-AzureHDInsightJob `
                    -Cluster $hdinsightClusterName `
                    -Credential $httpCredential `
                    -JobDefinition $sqoopDef #-Debug -Verbose

    Wait-AzureHDInsightJob `
        -Cluster $hdinsightClusterName `
        -Credential $httpCredential `
        -JobId $sqoopJob.JobId
        
    Write-Host "Standard Error" -BackgroundColor Green
    Get-AzureHDInsightJobOutput -Cluster $hdinsightClusterName -JobId $sqoopJob.JobId -StandardError
    Write-Host "Standard Output" -BackgroundColor Green
    Get-AzureHDInsightJobOutput -Cluster $hdinsightClusterName -JobId $sqoopJob.JobId -StandardOutput
    #endregion

## Run Sqoop using .NET SDK

In this section, you will create a C# console application to export the hivesampletable to the SQL Database table you created earlier in this tutorials.

**To submit a Sqoop job**

1. From the Visual Studio Package Manager Console, run the following Nuget command to import the package.

		Install-Package Microsoft.Azure.Management.HDInsight.Job -Pre
2. Use the following using statements in the Program.cs file:

		using System;
		using Microsoft.Azure.Management.HDInsight.Job;
		using Microsoft.Azure.Management.HDInsight.Job.Models;
		using Hyak.Common;
3. Add the following code into the Main() function. For the general information about using the HDInsight .NET SDK, see [Submit Hadoop jobs programmatically][hdinsight-submit-jobs].

		var ExistingClusterName = "<HDInsightClusterName>";
		var ExistingClusterUri = ExistingClusterName + ".azurehdinsight.cn";
		var ExistingClusterUsername = "<HDInsightClusterHttpUsername>";
		var ExistingClusterPassword = "<HDInsightClusterHttpUserPassword>";
		
		var sqlDatabaseServerName = "<AzureSQLDatabaseServerName>";
		var sqlDatabaseLogin = "<AzureSQLDatabaseLogin>";
		var sqlDatabaseLoginPassword = "<AzureSQLDatabaseLoginPassword>";
		var sqlDatabaseDatabaseName = "<AzureSQLDatabaseDatabaseName>";
		
		var sqlDatabaseTableName = "log4jlogs";
		var exportDir = "/hive/warehouse/hivesampletable";

		var cmdExport = @"export";
		// Connection string for using Azure SQL Database.
		// Comment if using SQL Server
		cmdExport = cmdExport + @" --connect 'jdbc:sqlserver://" + sqlDatabaseServerName + ".database.chinacloudapi.cn;user=" + sqlDatabaseLogin + "@" + sqlDatabaseServerName + ";password=" + sqlDatabaseLoginPassword + ";database=" + sqlDatabaseDatabaseName +"'"; 
		// Connection string for using SQL Server.
		// Uncomment if using SQL Server
		//cmdExport = cmdExport + @" --connect jdbc:sqlserver://" + sqlDatabaseServerName + ";user=" + sqlDatabaseLogin + ";password=" + sqlDatabaseLoginPassword + ";database=" + sqlDatabaseDatabaseName;
		cmdExport = cmdExport + @" --table " + sqlDatabaseTableName;
		cmdExport = cmdExport + @" --export-dir " + exportDir;
		cmdExport = cmdExport + @" --input-fields-terminated-by \0x20 -m 1";
		
		HDInsightJobManagementClient _hdiJobManagementClient;
		var clusterCredentials = new BasicAuthenticationCloudCredentials { Username = ExistingClusterUsername, Password = ExistingClusterPassword };
		_hdiJobManagementClient = new HDInsightJobManagementClient(ExistingClusterUri, clusterCredentials);

		var parameters = new SqoopJobSubmissionParameters
		{
		    Command = cmdExport
		};
		
		System.Console.WriteLine("Submitting the Sqoop job to the cluster...");
		var response = _hdiJobManagementClient.JobManagement.SubmitSqoopJob(parameters);
		System.Console.WriteLine("Validating that the response is as expected...");
		System.Console.WriteLine("Response status code is " + response.StatusCode);
		System.Console.WriteLine("Validating the response object...");
		System.Console.WriteLine("JobId is " + response.JobSubmissionJsonResponse.Id);
		Console.WriteLine("Press ENTER to continue ...");
		Console.ReadLine();
4. Press **F5** to run the program. 

##Next steps

Now you have learned how to use Sqoop. To learn more, see:

- [Use Oozie with HDInsight][hdinsight-use-oozie]: Use Sqoop action in an Oozie workflow.
- [Analyze flight delay data using HDInsight][hdinsight-analyze-flight-data]: Use Hive to analyze flight delay data, and then use Sqoop to export data to an Azure SQL database.
- [Upload data to HDInsight][hdinsight-upload-data]: Find other methods for uploading data to HDInsight/Azure Blob storage.


## Appendix A - a PowerShell sample

The PowerShell sample performs the following steps:

1. Connect to Azure.
2. Create an Azure resource group. For more information, see [Using Azure PowerShell with Azure Resource Manager](/documentation/articles/powershell-azure-resource-manager)
3. Create an Azure SQL Database server, an Azure SQL database, and two tables. 

	If you use SQL Server instead, use the following statements to create the tables:
	
		CREATE TABLE [dbo].[log4jlogs](
		 [t1] [nvarchar](50),
		 [t2] [nvarchar](50),
		 [t3] [nvarchar](50),
		 [t4] [nvarchar](50),
		 [t5] [nvarchar](50),
		 [t6] [nvarchar](50),
		 [t7] [nvarchar](50))

		CREATE TABLE [dbo].[mobiledata](
		 [clientid] [nvarchar](50),
		 [querytime] [nvarchar](50),
		 [market] [nvarchar](50),
		 [deviceplatform] [nvarchar](50),
		 [devicemake] [nvarchar](50),
		 [devicemodel] [nvarchar](50),
		 [state] [nvarchar](50),
		 [country] [nvarchar](50),
		 [querydwelltime] [float],
		 [sessionid] [bigint],
		 [sessionpagevieworder][bigint])

	The easiest way to examine the database and tables is to use Visual Studio. The database server and the database can be examined using the Azure Management Portal.

4. Create an HDInsight cluster.

	To examine the cluster, you can use the Azure Management Portal or Azure PowerShell.

5. Pre-process the source data file.

	In this tutorial, you will export a log4j log file (a delimited file) and a Hive table to an Azure SQL database. The delimited file is called */example/data/sample.log*. Earlier in the tutorial, you saw a few samples of log4j logs. In the log file, there are some empty lines and some lines similar to these:
	
		java.lang.Exception: 2012-02-03 20:11:35 SampleClass2 [FATAL] unrecoverable system problem at id 609774657
			at com.osa.mocklogger.MockLogger$2.run(MockLogger.java:83)
	
	This is fine for other examples that use this data, but we must remove these exceptions before we can import into the Azure SQL database or SQL Server. Sqoop export will fail if there is an empty string or a line with a fewer number of elements than the number of fields defined in the Azure SQL database table. The log4jlogs table has 7 string-type fields.

	This procedure creates a new file on the cluster: tutorials/usesqoop/data/sample.log. To examine the modified data file, you can use the Azure Management Portal, an Azure Storage explorer tool, or Azure PowerShell. [Get started with HDInsight][hdinsight-get-started] has a code sample for using Azure PowerShell to download a file and display the file content.

6. Export a data file to the Azure SQL database.

	The source file is tutorials/usesqoop/data/sample.log. The table where the data is exported to is called log4jlogs.
	
	> [AZURE.NOTE] Other than connection string information, the steps in this section should work for an Azure SQL database or for SQL Server. These steps were tested by using the following configuration:
	>
	> * **Azure virtual network point-to-site configuration**: A virtual network connected the HDInsight cluster to a SQL Server in a private datacenter. See [Configure a Point-to-Site VPN in the Management Portal](/documentation/articles/vpn-gateway-point-to-site-create) for more information.
	> * **Azure HDInsight 3.1**: See [Create Hadoop clusters in HDInsight using custom options](/documentation/articles/hdinsight-provision-clusters-v1) for information about creating a cluster on a virtual network.
	> * **SQL Server 2014**: Configured to allow authentication and running the VPN client configuration package to connect securely to the virtual network.

7. Export a Hive table to the Azure SQL database.

8. Import the mobiledata table to the HDInsight cluster.

	To examine the modified data file, you can use the Azure Management Portal, an Azure Storage explorer tool, or Azure PowerShell.  [Get started with HDInsight][hdinsight-get-started] has a code sample about using Azure PowerShell to download a file and display the file content.


### The PowerShell sample

	# Prepare an Azure SQL database to be used by the Sqoop tutorial
	
	#region - provide the following values
	
	$subscriptionID = "<Enter your Azure Subscription ID>"
	
	$sqlDatabaseLogin = "<Enter a SQL Database Login name>" #SQL Database server login
	$sqlDatabasePassword = "<Enter a Password>"
	
	$httpUserName = "admin"  #HDInsight cluster username
	$httpPassword = "<Enter a Password>"
	
	# used for creating Azure service names
	$nameToken = "<Enter an alias>" 
	$namePrefix = $nameToken.ToLower() + (Get-Date -Format "MMdd")
	#endregion
	
	#region - variables
	
	# Resource group variables
	$resourceGroupName = $namePrefix + "rg"
	$location = "China East 2" # used by all Azure services defined in this tutorial
	
	# SQL database varialbes
	$sqlDatabaseServerName = $namePrefix + "sqldbserver"
	$sqlDatabaseName = $namePrefix + "sqldb"
	$sqlDatabaseConnectionString = "Data Source=$sqlDatabaseServerName.database.chinacloudapi.cn;Initial Catalog=$sqlDatabaseName;User ID=$sqlDatabaseLogin;Password=$sqlDatabasePassword;Encrypt=true;Trusted_Connection=false;"
	$sqlDatabaseMaxSizeGB = 10
	
	# Used for retrieving external IP address and creating firewall rules
	$ipAddressRestService = "http://bot.whatismyipaddress.com"
	$fireWallRuleName = "UseSqoop"
	
	# Used for creating tables and clustered indexes
	$cmdCreateLog4jTable = "CREATE TABLE [dbo].[log4jlogs](
		[t1] [nvarchar](50),
		[t2] [nvarchar](50),
		[t3] [nvarchar](50),
		[t4] [nvarchar](50),
		[t5] [nvarchar](50),
		[t6] [nvarchar](50),
		[t7] [nvarchar](50))"
	
	$cmdCreateLog4jClusteredIndex = "CREATE CLUSTERED INDEX log4jlogs_clustered_index on log4jlogs(t1)"
	
	$cmdCreateMobileTable = " CREATE TABLE [dbo].[mobiledata](
	[clientid] [nvarchar](50),
	[querytime] [nvarchar](50),
	[market] [nvarchar](50),
	[deviceplatform] [nvarchar](50),
	[devicemake] [nvarchar](50),
	[devicemodel] [nvarchar](50),
	[state] [nvarchar](50),
	[country] [nvarchar](50),
	[querydwelltime] [float],
	[sessionid] [bigint],
	[sessionpagevieworder][bigint])"
	
	$cmdCreateMobileDataClusteredIndex = "CREATE CLUSTERED INDEX mobiledata_clustered_index on mobiledata(clientid)"
	
	# HDInsight variables
	$hdinsightClusterName = $namePrefix + "hdi"
	$defaultStorageAccountName = $namePrefix + "store"
	$defaultBlobContainerName = $hdinsightClusterName
	#endregion
	
	# Treat all errors as terminating
	$ErrorActionPreference = "Stop"
	
	#region - Connect to Azure subscription
	Write-Host "`nConnecting to your Azure subscription ..." -ForegroundColor Green
	try{Get-AzureRmContext}
	catch{Login-AzureRmAccount -EnvironmentName AzureChinaCloud}

    try{Get-AzureSubscription}
	catch{Add-AzureAccount -Environment AzureChinaCloud}
	#endregion
	
	#region - Create Azure resouce group
	Write-Host "`nCreating an Azure resource group ..." -ForegroundColor Green
	try{
		Get-AzureRmResourceGroup -Name $resourceGroupName
	}
	catch{
		New-AzureRmResourceGroup -Name $resourceGroupName -Location $location
	}
	#endregion
	
	#region - Create Azure SQL database server
	Write-Host "`nCreating an Azure SQL Database server ..." -ForegroundColor Green
	try{
		Get-AzureRmSqlServer -ServerName $sqlDatabaseServerName -ResourceGroupName $resourceGroupName}
	catch{
		Write-Host "`nCreating SQL Database server ..."  -ForegroundColor Green
	
		$sqlDatabasePW = ConvertTo-SecureString -String $sqlDatabasePassword -AsPlainText -Force
		$credential = New-Object System.Management.Automation.PSCredential($sqlDatabaseLogin,$sqlDatabasePW)
	
		$sqlDatabaseServerName = (New-AzureRmSqlServer `
									-ResourceGroupName $resourceGroupName `
									-ServerName $sqlDatabaseServerName `
									-SqlAdministratorCredentials $credential `
									-Location $location).ServerName
		Write-Host "`tThe new SQL database server name is $sqlDatabaseServerName." -ForegroundColor Cyan
	
		Write-Host "`nCreating firewall rule, $fireWallRuleName ..." -ForegroundColor Green
		$workstationIPAddress = Invoke-RestMethod $ipAddressRestService
		New-AzureRmSqlServerFirewallRule `
			-ResourceGroupName $resourceGroupName `
			-ServerName $sqlDatabaseServerName `
			-FirewallRuleName "$fireWallRuleName-workstation" `
			-StartIpAddress $workstationIPAddress `
			-EndIpAddress $workstationIPAddress
	
		#To allow other Azure services to access the server add a firewall rule and set both the StartIpAddress and EndIpAddress to 0.0.0.0. 
		#Note that this allows Azure traffic from any Azure subscription to access the server.
		New-AzureRmSqlServerFirewallRule `
			-ResourceGroupName $resourceGroupName `
			-ServerName $sqlDatabaseServerName `
			-FirewallRuleName "$fireWallRuleName-Azureservices" `
			-StartIpAddress "0.0.0.0" `
			-EndIpAddress "0.0.0.0"
	}
	
	#endregion
	
	#region - Create and validate Azure SQL database
	Write-Host "`nCreating an Azure SQL database ..." -ForegroundColor Green
	
	try {
		Get-AzureRmSqlDatabase `
			-ResourceGroupName $resourceGroupName `
			-ServerName $sqlDatabaseServerName `
			-DatabaseName $sqlDatabaseName
	}
	catch {
		Write-Host "`nCreating SQL Database, $sqlDatabaseName ..."  -ForegroundColor Green
		New-AzureRMSqlDatabase `
			-ResourceGroupName $resourceGroupName `
			-ServerName $sqlDatabaseServerName `
			-DatabaseName $sqlDatabaseName `
			-Edition "Standard" `
			-RequestedServiceObjectiveName "S1"
	}
	
	#endregion
	
	#region - Create tables
	Write-Host "Creating the log4jlogs table and the mobiledata table ..." -ForegroundColor Green
	
	$conn = New-Object System.Data.SqlClient.SqlConnection
	$conn.ConnectionString = $sqlDatabaseConnectionString
	$conn.Open()
	
	# Create the log4jlogs table and index
	$cmd = New-Object System.Data.SqlClient.SqlCommand
	$cmd.Connection = $conn
	$cmd.CommandText = $cmdCreateLog4jTable
	$ret = $cmd.ExecuteNonQuery()
	$cmd.CommandText = $cmdCreateLog4jClusteredIndex
	$cmd.ExecuteNonQuery()
	
	# Create the mobiledata table and index
	$cmd.CommandText = $cmdCreateMobileTable
	$cmd.ExecuteNonQuery()
	$cmd.CommandText = $cmdCreateMobileDataClusteredIndex
	$cmd.ExecuteNonQuery()
	
	$conn.close()
	
	#endregion
	
	
	#region - Create HDInsight cluster
	
	Write-Host "Creating the HDInsight cluster and the dependent services ..." -ForegroundColor Green
	
	# Create the default storage account
	New-AzureStorageAccount `
		-StorageAccountName $defaultStorageAccountName `
		-Location $location `
		-Type Standard_LRS
	
	# Create the default Blob container
	$defaultStorageAccountKey = Get-AzureStorageAccountKey `
									-StorageAccountName $defaultStorageAccountName |  %{ $_.primary }
	$defaultStorageAccountContext = New-AzureStorageContext `
										-StorageAccountName $defaultStorageAccountName `
										-StorageAccountKey $defaultStorageAccountKey 
	New-AzureStorageContainer `
		-Name $defaultBlobContainerName `
		-Context $defaultStorageAccountContext 
	
	# Create the HDInsight cluster
	$pw = ConvertTo-SecureString -String $httpPassword -AsPlainText -Force
	$httpCredential = New-Object System.Management.Automation.PSCredential($httpUserName,$pw)
	
	New-AzureHDInsightCluster `
		-Name $HDInsightClusterName `
		-Location $location `
		-ClusterType Hadoop `
		-OSType Windows `
		-ClusterSizeInNodes 2 `
		-Credential $httpCredential `
		-DefaultStorageAccountName "$defaultStorageAccountName.blob.core.chinacloudapi.cn" `
		-DefaultStorageAccountKey $defaultStorageAccountKey `
		-DefaultStorageContainerName $defaultBlobContainerName 
	
	# Validate the cluster
	Get-AzureHDInsightCluster -Name $hdinsightClusterName
	#endregion
	
	#region - pre-process the source file
	
	Write-Host "Preprocessing the source file ..." -ForegroundColor Green
	
	# This procedure creates a new file with $destBlobName
	$sourceBlobName = "example/data/sample.log"
	$destBlobName = "tutorials/usesqoop/data/sample.log"
	
	# Define the connection string
	$storageConnectionString = "DefaultEndpointsProtocol=https;AccountName=$defaultStorageAccountName;AccountKey=$defaultStorageAccountKey"
	
	# Create block blob objects referencing the source and destination blob.
	$storageAccount = [Microsoft.WindowsAzure.Storage.CloudStorageAccount]::Parse($storageConnectionString)
	$storageClient = $storageAccount.CreateCloudBlobClient();
	$storageContainer = $storageClient.GetContainerReference($defaultBlobContainerName)
	$sourceBlob = $storageContainer.GetBlockBlobReference($sourceBlobName)
	$destBlob = $storageContainer.GetBlockBlobReference($destBlobName)
	
	# Define a MemoryStream and a StreamReader for reading from the source file
	$stream = New-Object System.IO.MemoryStream
	$stream = $sourceBlob.OpenRead()
	$sReader = New-Object System.IO.StreamReader($stream)
	
	# Define a MemoryStream and a StreamWriter for writing into the destination file
	$memStream = New-Object System.IO.MemoryStream
	$writeStream = New-Object System.IO.StreamWriter $memStream
	
	# Pre-process the source blob
	$exString = "java.lang.Exception:"
	while(-Not $sReader.EndOfStream){
		$line = $sReader.ReadLine()
		$split = $line.Split(" ")
	
		# remove the "java.lang.Exception" from the first element of the array
		# for example: java.lang.Exception: 2012-02-03 19:11:02 SampleClass8 [WARN] problem finding id 153454612
		if ($split[0] -eq $exString){
			#create a new ArrayList to remove $split[0]
			$newArray = [System.Collections.ArrayList] $split
			$newArray.Remove($exString)
	
			# update $split and $line
			$split = $newArray
			$line = $newArray -join(" ")
		}
	
		# remove the lines that has less than 7 elements
		if ($split.count -ge 7){
			write-host $line
			$writeStream.WriteLine($line)
		}
	}
	
	# Write to the destination blob
	$writeStream.Flush()
	$memStream.Seek(0, "Begin")
	$destBlob.UploadFromStream($memStream)
	
	#endregion
	
	#region - export a log file from the cluster to the SQL database
	
	Write-Host "Preprocessing the source file ..." -ForegroundColor Green
	
	$tableName_log4j = "log4jlogs"
	
	# Connection string for Azure SQL Database.
	# Comment if using SQL Server
	$connectionString = "jdbc:sqlserver://$sqlDatabaseServerName.database.chinacloudapi.cn;user=$sqlDatabaseLogin@$sqlDatabaseServerName;password=$sqlDatabasePassword;database=$sqlDatabaseName"
	# Connection string for SQL Server.
	# Uncomment if using SQL Server.
	#$connectionString = "jdbc:sqlserver://$sqlDatabaseServerName;user=$sqlDatabaseLogin;password=$sqlDatabasePassword;database=$sqlDatabaseName"
	
	$exportDir_log4j = "/tutorials/usesqoop/data"
	
	# Submit a Sqoop job
	$sqoopDef = New-AzureHDInsightSqoopJobDefinition `
		-Command "export --connect $connectionString --table $tableName_log4j --export-dir $exportDir_log4j --input-fields-terminated-by \0x20 -m 1"
	$sqoopJob = Start-AzureHDInsightJob `
					-Cluster $hdinsightClusterName `
					-Credential $httpCredential `
					-JobDefinition $sqoopDef #-Debug -Verbose
	Wait-AzureHDInsightJob `
		-Cluster $hdinsightClusterName `
		-Credential $httpCredential `
		-JobId $sqoopJob.JobId
	
	Write-Host "Standard Error" -BackgroundColor Green
	Get-AzureHDInsightJobOutput -Cluster $hdinsightClusterName -JobId $sqoopJob.JobId -StandardError
	Write-Host "Standard Output" -BackgroundColor Green
	Get-AzureHDInsightJobOutput -Cluster $hdinsightClusterName -JobId $sqoopJob.JobId -StandardOutput
	
	#endregion
	
	#region - export a Hive table
	
	$tableName_mobile = "mobiledata"
	$exportDir_mobile = "/hive/warehouse/hivesampletable"
	
	$sqoopDef = New-AzureHDInsightSqoopJobDefinition `
		-Command "export --connect $connectionString --table $tableName_mobile --export-dir $exportDir_mobile --fields-terminated-by \t -m 1"
	$sqoopJob = Start-AzureHDInsightJob `
					-Cluster $hdinsightClusterName `
					-Credential $httpCredential `
					-JobDefinition $sqoopDef #-Debug -Verbose
	
	Wait-AzureHDInsightJob `
		-Cluster $hdinsightClusterName `
		-Credential $httpCredential `
		-JobId $sqoopJob.JobId
	
	Write-Host "Standard Error" -BackgroundColor Green
	Get-AzureHDInsightJobOutput `
		-Cluster $hdinsightClusterName `
		-JobId $sqoopJob.JobId `
		-StandardError
	
	Write-Host "Standard Output" -BackgroundColor Green
	Get-AzureHDInsightJobOutput `
		-Cluster $hdinsightClusterName `
		-JobId $sqoopJob.JobId `
		-StandardOutput
	
	#endregion
	
	#region - import a database
	
	$targetDir_mobile = "/tutorials/usesqoop/importeddata/"
	
	$sqoopDef = New-AzureHDInsightSqoopJobDefinition `
		-Command "import --connect $connectionString --table $tableName_mobile --target-dir $targetDir_mobile --fields-terminated-by \t --lines-terminated-by \n -m 1"
	
	$sqoopJob = Start-AzureHDInsightJob `
					-Cluster $hdinsightClusterName `
					-Credential $httpCredential `
					-JobDefinition $sqoopDef #-Debug -Verbose
	
	Wait-AzureHDInsightJob `
		-Cluster $hdinsightClusterName `
		-Credential $httpCredential `
		-JobId $sqoopJob.JobId
	
	Write-Host "Standard Error" -BackgroundColor Green
	Get-AzureHDInsightJobOutput `
		-Cluster $hdinsightClusterName `
		-JobId $sqoopJob.JobId `
		-StandardError
	
	Write-Host "Standard Output" -BackgroundColor Green
	Get-AzureHDInsightJobOutput `
		-Cluster $hdinsightClusterName `
		-JobId $sqoopJob.JobId `
		-StandardOutput
	
	#endregion



[azure-management-portal]: https://manage.windowsazure.cn/

[hdinsight-versions]: /documentation/articles/hdinsight-component-versioning-v1
[hdinsight-provision]: /documentation/articles/hdinsight-provision-clusters-v1
[hdinsight-get-started]: /documentation/articles/hdinsight-hadoop-linux-tutorial-get-started
[hdinsight-storage]: /documentation/articles/hdinsight-hadoop-use-blob-storage
[hdinsight-analyze-flight-data]: /documentation/articles/hdinsight-analyze-flight-delay-data
[hdinsight-use-oozie]: /documentation/articles/hdinsight-use-oozie
[hdinsight-upload-data]: /documentation/articles/hdinsight-upload-data
[hdinsight-submit-jobs]: /documentation/articles/hdinsight-submit-hadoop-jobs-programmatically

[sqldatabase-get-started]: /documentation/articles/sql-database-get-started
[sqldatabase-create-configue]: /documentation/articles/sql-database-get-started

[powershell-start]: http://technet.microsoft.com/zh-cn/library/hh847889.aspx
[powershell-install]: /documentation/articles/powershell-install-configure
[powershell-script]: https://technet.microsoft.com/zh-cn/library/dn425048.aspx

[sqoop-user-guide-1.4.4]: https://sqoop.apache.org/docs/1.4.4/SqoopUserGuide.html
