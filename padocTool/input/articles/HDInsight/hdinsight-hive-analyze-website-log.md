<properties 
	pageTitle="Use Hive with Hadoop for website log analysis| Windows Azure" 
	description="Learn how to use Hive with HDInsight to analyze website logs. You'll use a log file as input into an HDInsight table, and use HiveQL to query the data." 
	services="hdinsight" 
	documentationCenter="" 
	authors="nitinme" 
	manager="paulettm" 
	editor="cgronlun"
	tags="azure-portal"/>

<tags
	ms.service="hdinsight"
	ms.date="08/07/2015"
	wacn.date=""/>

# Use Hive with HDInsight to analyze logs from websites

Learn how to use HiveQL with HDInsight to analyze logs from a website. Website log analysis can be used to segment your audience based on similar activities, categorize site visitors by demographics, and to find out the content they view, the websites they come from, and so on.

In this sample, you will use an HDInsight cluster to analyze website log files to get insight into the frequency of visits to the website from external websites in a day. You'll also generate a summary of website errors that the users experience. You will learn how to:

- Connect to a Azure Blob storage, which contains website log files.
- Create HIVE tables to query those logs.
- Create HIVE queries to analyze the data.
- Use Microsoft Excel to connect to HDInsight (by using open database connectivity (ODBC) to retrieve the analyzed data.

![HDI.Samples.Website.Log.Analysis][img-hdi-weblogs-sample]

##Prerequisites

- You must have provisioned a Hadoop cluster on Azure HDInsight. For instructions, see [Provision HDInsight Clusters][hdinsight-provision]. 
- You must have Microsoft Excel 2013 or Excel 2010 installed.
- You must have [Microsoft Hive ODBC Driver](http://www.microsoft.com/download/details.aspx?id=40886) to import data from Hive into Excel.


##To run the sample
<!-- deleted by customization

1. From the [Azure Preview Portal](https://ms.portal.azure.com/), from the Startboard (if you pinned the cluster there), click the cluster tile on which you want to run the sample.

2. From the cluster blade, under **Quick Links**, click **Cluster Dashboard**, and then from the **Cluster Dashboard** blade, click **HDInsight Cluster Dashboard**. Alternatively, you can directly open the dashboard by using the following URL:

-->
<!-- keep by customization: begin -->
1. From the Azure Management Portal, click the cluster on which you want to run the sample, and then click **Query Console** at the bottom. Alternatively, you can directly open the Query Console by using the following URL:
<!-- keep by customization: end -->
	 	https://<clustername>.azurehdinsight.cn
	
	When prompted, authenticate by using the administrator user name and password you used when provisioning the cluster.
  
2. From the web page that opens, click the **Getting Started Gallery** tab, and then under the **Samples** category, click the **Website Log Analysis** sample.

3. Follow the instructions provided on the web page to finish the sample.

##Next steps
Try the following sample: [Analyzing sensor data using Hive with HDInsight](/documentation/articles/hdinsight-hive-analyze-sensor-data).


[hdinsight-provision]: /documentation/articles/hdinsight-provision-clusters
[hdinsight-sensor-data-sample]: /documentation/articles/hdinsight-use-hive-sensor-data-analysis
[img-hdi-weblogs-sample]: ./media/hdinsight-hive-analyze-website-log/hdinsight-weblogs-sample.png
 