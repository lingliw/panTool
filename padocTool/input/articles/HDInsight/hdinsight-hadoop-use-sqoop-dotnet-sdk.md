<properties
	pageTitle="Use Hadoop Sqoop in HDInsight | Azure"
	description="Learn how to use HDInsight .NET SDK to run Sqoop import and export between an Hadoop cluster and an Azure SQL database."
	editor="cgronlun"
	manager="paulettm"
	services="hdinsight"
	documentationCenter=""
	tags="azure-portal"
	authors="mumian"/>

<tags
	ms.service="hdinsight"
	ms.date="04/06/2016"
	wacn.date=""/>

#Run Sqoop jobs using .NET SDK for Hadoop in HDInsight

> [AZURE.SELECTOR]
- [Overview](/documentation/articles/hdinsight-use-sqoop)
- [PowerShell](/documentation/articles/hdinsight-hadoop-use-sqoop-powershell)
- [.NET](/documentation/articles/hdinsight-hadoop-use-sqoop-dotnet-sdk)


Learn how to use HDInsight .NET SDK to run Sqoop jobs in HDInsight to import and export between HDInsight cluster and Azure SQL database or SQL Server database.

###Prerequisites

Before you begin this tutorial, you must have the following:

- **A Hadoop cluster in HDInsight**. See [Create cluster and SQL database](/documentation/articles/hdinsight-use-sqoop#create-cluster-and-sql-database).

## Run Sqoop using .NET SDK

The HDInsight .NET SDK provides .NET client libraries, which makes it easier to work with HDInsight clusters from .NET. In this section, you will create a C# console application to export the hivesampletable to the SQL Database table you created earlier in this tutorials.

**To submit a Sqoop job**

1. Create a C# console application in Visual Studio.
2. From the Visual Studio Package Manager Console, run the following Nuget command to import the package.

        Install-Package Microsoft.Azure.Management.HDInsight.Job
        
3. Use the following code in the Program.cs file:

        using System.Collections.Generic;
        using Microsoft.Azure.Management.HDInsight.Job;
        using Microsoft.Azure.Management.HDInsight.Job.Models;
        using Hyak.Common;
        
        namespace SubmitHDInsightJobDotNet
        {
            class Program
            {
                private static HDInsightJobManagementClient _hdiJobManagementClient;
        
                private const string ExistingClusterName = "<Your HDInsight Cluster Name>";
                private const string ExistingClusterUri = ExistingClusterName + ".azurehdinsight.cn";
                private const string ExistingClusterUsername = "<Cluster Username>";
                private const string ExistingClusterPassword = "<Cluster User Password>";
        
                static void Main(string[] args)
                {
                    System.Console.WriteLine("The application is running ...");
        
                    var clusterCredentials = new BasicAuthenticationCloudCredentials { Username = ExistingClusterUsername, Password = ExistingClusterPassword };
                    _hdiJobManagementClient = new HDInsightJobManagementClient(ExistingClusterUri, clusterCredentials);
        
                    SubmitSqoopJob();
        
                    System.Console.WriteLine("Press ENTER to continue ...");
                    System.Console.ReadLine();
                }
        
                private static void SubmitSqoopJob()
                {
                    var sqlDatabaseServerName = "<SQLDatabaseServerName>";
                    var sqlDatabaseLogin = "<SQLDatabaseLogin>";
                    var sqlDatabaseLoginPassword = "<SQLDatabaseLoginPassword>";
                    var sqlDatabaseDatabaseName = "<DatabaseName>";
        
                    var tableName = "<TableName>";
                    var exportDir = "/tutorials/usesqoop/data";
        
                    // Connection string for using Azure SQL Database.
                    // Comment if using SQL Server
                    var connectionString = "jdbc:sqlserver://" + sqlDatabaseServerName + ".database.chinacloudapi.cn;user=" + sqlDatabaseLogin + "@" + sqlDatabaseServerName + ";password=" + sqlDatabaseLoginPassword + ";database=" + sqlDatabaseDatabaseName;
                    // Connection string for using SQL Server.
                    // Uncomment if using SQL Server
                    //var connectionString = "jdbc:sqlserver://" + sqlDatabaseServerName + ";user=" + sqlDatabaseLogin + ";password=" + sqlDatabaseLoginPassword + ";database=" + sqlDatabaseDatabaseName;
        
                    var parameters = new SqoopJobSubmissionParameters
                    {
                        Command = "export --connect " + connectionString + " --table " + tableName + "_mobile --export-dir " + exportDir + "_mobile --fields-terminated-by \\t -m 1"
                    };
        
                    System.Console.WriteLine("Submitting the Sqoop job to the cluster...");
                    var response = _hdiJobManagementClient.JobManagement.SubmitSqoopJob(parameters);
                    System.Console.WriteLine("Validating that the response is as expected...");
                    System.Console.WriteLine("Response status code is " + response.StatusCode);
                    System.Console.WriteLine("Validating the response object...");
                    System.Console.WriteLine("JobId is " + response.JobSubmissionJsonResponse.Id);
                }
            }
        }
        
4. Press **F5** to run the program. 

##Next steps

Now you have learned how to use Sqoop. To learn more, see:

- [Use Oozie with HDInsight](/documentation/articles/hdinsight-use-oozie): Use Sqoop action in an Oozie workflow.
- [Analyze flight delay data using HDInsight](/documentation/articles/hdinsight-analyze-flight-delay-data): Use Hive to analyze flight delay data, and then use Sqoop to export data to an Azure SQL database.
- [Upload data to HDInsight](/documentation/articles/hdinsight-upload-data): Find other methods for uploading data to HDInsight/Azure Blob storage.


