<properties
	pageTitle="Manage Hadoop clusters in HDInsight with .NET SDK | Azure"
	description="Learn how to perform administrative tasks for the Hadoop clusters in HDInsight using HDInsight .NET SDK."
	services="hdinsight"
	editor="cgronlun"
	manager="paulettm"
	tags="azure-portal"
	authors="mumian"
	documentationCenter=""/>

<tags
	ms.service="hdinsight"
	ms.date="05/02/2016"
	wacn.date=""/>

# Manage Hadoop clusters in HDInsight by using .NET SDK

> [AZURE.SELECTOR]
- [Portal (Windows cluster)](/documentation/articles/hdinsight-administer-use-management-portal-v1)
- [Azure CLI](/documentation/articles/hdinsight-administer-use-command-line)
- [Azure PowerShell](/documentation/articles/hdinsight-administer-use-powershell)
- [.NET SDK](/documentation/articles/hdinsight-administer-use-dotnet-sdk)


Learn how to manage HDInsight clusters using [HDInsight.NET SDK](https://msdn.microsoft.com/zh-cn/library/mt271028.aspx).


**Prerequisites**

Before you begin this article, you must have the following:

- **An Azure subscription**. See [Get Azure trial](/pricing/1rmb-trial/).


##Connect to Azure HDInsight

You will need the following Nuget package:

	Install-Package Microsoft.WindowsAzure.Management.HDInsight

The following code sample shows you how to connect to Azure before you can administer HDInsight clusters under your Azure subscription.

	using System;
	using Microsoft.WindowsAzure.Management.HDInsight;
	using System.Security.Cryptography.X509Certificates;

	namespace HDInsightManagement
	{
		class Program
		{
			private static IHDInsightClient _hdinsightClient;
			private static String SubscriptionId = "<Your Azure Subscription ID>";
			private static Uri baseUri = new Uri("https://management.core.chinacloudapi.cn");
			private static X509Certificate2 cert = new X509Certificate2("c:/path/to/cert.cer");

			static void Main(string[] args)
			{
				_hdinsightClient = HDInsightClient.Connect(new HDInsightCertificateCredential(new Guid(SubscriptionId), cert, baseUri));

				// insert code here

				System.Console.WriteLine("Press ENTER to continue");
				System.Console.ReadLine();
			}
		}
	}

To use this piece of code, you need to create your certificate file and upload it to Azure. See [Upload an Azure Management API Management Certificate](/documentation/articles/azure-api-management-certs) for more details.

##Create clusters

See [Create Linux-based clusters in HDInsight using the .NET SDK](/documentation/articles/hdinsight-hadoop-create-linux-clusters-dotnet-sdk)

##List clusters

The following code snippet lists clusters and some properties:

    var results = _hdinsightClient.ListClusters();
    foreach (var name in results) {
        Console.WriteLine("Cluster Name: " + name.Name);
        Console.WriteLine("\t Cluster type: " + name.ClusterType);
        Console.WriteLine("\t Cluster location: " + name.Location);
        Console.WriteLine("\t Cluster version: " + name.Version);
    }

##Delete clusters

Use the following code snippet to delete a cluster synchronously or asynchronously: 

    _hdinsightClient.DeleteCluster("<Cluster Name>");
    _hdinsightClient.DeleteClusterAsync("<Cluster Name>");

##Grant/revoke access

HDInsight clusters have the following HTTP web services (all of these services have RESTful endpoints):

- ODBC
- JDBC
- Oozie
- Templeton


By default, these services are granted for access. You can revoke/grant the access. To revoke:

	var cluster = _hdinsightClient.GetCluster("<Cluster Name>");
    _hdinsightClient.DisableHttp(cluster.Name, cluster.Location);

To grant:

	_hdinsightClient.EnableHttp(cluster.Name, cluster.Location, "admin","<password>");

>[AZURE.NOTE] By granting/revoking the access, you will reset the cluster user name and password.

This can also be done via the Portal. See [Administer HDInsight by using the Azure Portal][hdinsight-admin-portal].

##Update HTTP user credentials

It is the same procedure as [Grant/revoke HTTP access](#grant/revoke-access).If the cluster has been granted the HTTP access, you must first revoke it.  And then grant the access with new HTTP user credentials.


##Find the default storage account

The following code snippet demonstrates how to get the default storage account name and the default storage account key for a cluster.

	var cluster = _hdinsightClient.GetCluster("<Cluster Name>");
	var storageKey = cluster.DefaultStorageAccount.Key;


##Submit jobs

**To submit Hive jobs** 

See [Run Hive queries using .NET SDK](/documentation/articles/hdinsight-hadoop-use-hive-dotnet-sdk).

**To submit Pig jobs**

See [Run Pig jobs using .NET SDK](/documentation/articles/hdinsight-hadoop-use-pig-dotnet-sdk-v1).

**To submit Sqoop jobs**

See [Use Sqoop with HDInsight](/documentation/articles/hdinsight-hadoop-use-sqoop-dotnet-sdk).

**To submit Oozie jobs**

See [Use Oozie with Hadoop to define and run a workflow in HDInsight](/documentation/articles/hdinsight-use-oozie).

##Upload data to Azure Blob storage
See [Upload data to HDInsight][hdinsight-upload-data].


## See Also
* [HDInsight .NET SDK reference documentation](https://msdn.microsoft.com/zh-cn/library/mt271028.aspx)
* [Administer HDInsight by using the Azure Portal][hdinsight-admin-portal]
* [Administer HDInsight using a command-line interface][hdinsight-admin-cli]
* [Create HDInsight clusters][hdinsight-provision]
* [Upload data to HDInsight][hdinsight-upload-data]
* [Get started with Azure HDInsight][hdinsight-get-started]


[azure-purchase-options]: /pricing/overview/
[azure-member-offers]: /pricing/member-offers/
[azure-trial]: /pricing/1rmb-trial/

[hdinsight-get-started]: /documentation/articles/hdinsight-hadoop-tutorial-get-started-windows-v1
[hdinsight-provision]: /documentation/articles/hdinsight-provision-clusters-v1
[hdinsight-provision-custom-options]: /documentation/articles/hdinsight-provision-clusters-v1#configuration
[hdinsight-submit-jobs]: /documentation/articles/hdinsight-submit-hadoop-jobs-programmatically

[hdinsight-admin-cli]: /documentation/articles/hdinsight-administer-use-command-line
[hdinsight-admin-portal]: /documentation/articles/hdinsight-administer-use-portal-linux
[hdinsight-storage]: /documentation/articles/hdinsight-hadoop-use-blob-storage
[hdinsight-use-hive]: /documentation/articles/hdinsight-use-hive
[hdinsight-use-mapreduce]: /documentation/articles/hdinsight-use-mapreduce
[hdinsight-upload-data]: /documentation/articles/hdinsight-upload-data
[hdinsight-flight]: /documentation/articles/hdinsight-analyze-flight-delay-data


