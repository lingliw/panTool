<properties
   pageTitle="Hadoop tutorial: Get started with Hadoop on Windows | Windows Azure"
   description="Get started with Hadoop in HDInsight. Learn how to create Hadoop clusters on Windows, run a Hive query on data, and analyze output in Excel."
   keywords="hadoop tutorial,hadoop on windows,hadoop cluster,learn hadoop, hive query"
   services="hdinsight"
   documentationCenter=""
   authors="nitinme"
   manager="paulettm"
   editor="cgronlun"
   tags="azure-portal"/>

<tags
	ms.service="hdinsight"
	ms.date="11/13/2015"
	wacn.date=""/>


# Hadoop tutorial: Get started using Hadoop in HDInsight on Windows

To help you learn Hadoop on Windows and start using HDInsight, this tutorial shows you 
how to run a Hive query on unstructured data in a Hadoop cluster and then analyze the 
results in Microsoft Excel.

Assume you have a large unstructured data set and you want to run a Hive query on it 
to extract some meaningful information. That's exactly what you are going to do in this 
tutorial. Here's how you achieve this:

   !["Hadoop tutorial: Create an account; create a Hadoop cluster; submit a Hive query; analyze data in Excel.][image-hdi-getstarted-flow]

In conjunction with the general availability of Azure HDInsight, Microsoft also provides 
HDInsight Emulator for Azure, formerly known as *Microsoft HDInsight Developer Preview*. 
The Emulator targets developer scenarios and only supports single-node deployments. For 
information about using HDInsight Emulator, see [Get Started with the HDInsight Emulator][hdinsight-emulator].

### Prerequisites

Before you begin this tutorial for Hadoop on Windows, you must have the following:

- **An Azure subscription**. See [Get Azure trial](/pricing/1rmb-trial/).
- **A workstation computer** with Office 2013 Professional Plus, Office 365 Pro Plus, Excel 2013 Standalone, or Office 2010 Professional Plus.

##Create Hadoop clusters

When you create a cluster, you create Azure compute resources that contain Hadoop 
and related applications. In this section, you create an HDInsight version 3.2 cluster. 
You can also create Hadoop clusters for other versions. For instructions, see 
[Create HDInsight clusters using custom options][hdinsight-provision]. For information 
about HDInsight versions and their SLAs, see 
[HDInsight component versioning](/documentation/articles/hdinsight-component-versioning).


**To create a Hadoop cluster**

1. Sign in to the [Azure Management Portal][azure-management-portal].

2. Click **HDInsight** in the left pane to list the status of the clusters in your account. In the following screenshot, there are no existing HDInsight clusters.

	![Status of HDInsight clusters in the Azure Management Portal.][image-hdi-clusterstatus]

3. Click **NEW** in the lower-left corner, click **Data Services**, click **HDInsight**, and then click **Hadoop**.

	![Creation of a Hadoop cluster in HDInsight.][image-hdi-quickcreatecluster]

4. Enter or select the following values:

	<table border="1">
	<tr><th>Name</th><th>Value</th></tr>
	<tr><td>Cluster Name</td><td>Name of the cluster.</td></tr>
	<tr><td>Cluster Size</td><td>Number of data nodes you want to deploy. The default value is 4. But the option to use 1 or 2 data nodes is also available from the drop-down list. Any number of cluster nodes can be specified by using the <strong>Custom Create</strong> option. Pricing details about the billing rates for various cluster sizes are available. Click the <strong>?</strong> symbol above the drop-down list and follow the link that appears.</td></tr>
	<tr><td>Password</td><td>The password for the <i>admin</i> account. The cluster user name "admin" is specified when you are not using the <strong>Custom Create</strong> option. Note that this is NOT the Windows Administrator account for the VMs on which the clusters are provisioned. The account name can be changed by using the <strong>Custom Create</strong> wizard.</td></tr>
	<tr><td>Storage Account</td><td>Click the drop-down list, and select the storage account that you created. <br/>

	When a storage account is chosen, it cannot be changed. If the storage account is removed, the cluster will no longer be available for use.

	The HDInsight cluster is located in the same datacenter as the storage account.
	</td></tr>
	</table>

	Keep a copy of the cluster name. You will need it later in the tutorial.


5. Click **Create HDInsight Cluster**. When the provisioning completes, the  status column shows **Running**.

	>[AZURE.NOTE] The previous procedure creates a Hadoop cluster by using HDInsight version 3.1. To create cluster with other versions, use the **Custom Create** method from the portal or use Azure PowerShell. For information about what's different between each version, see [What's new in the cluster versions provided by HDInsight?][hdinsight-versions]. For information about using the **CUSTOM CREATE** option, see [Provision HDInsight clusters using custom options][hdinsight-provision].

## Run a Hive query from the portal
Now that you have created an HDInsight cluster, the next step is to run a Hive job to query a sample Hive table. We will use *hivesampletable*, which comes with HDInsight clusters. The table contains data about mobile device manufacturers, platforms, and models. A Hive query on this table retrieves data for mobile devices by a specific manufacturer.

> [AZURE.NOTE] HDInsight Tools for Visual Studio comes with the Azure SDK for .NET version 2.5 or later. By using the tools in Visual Studio, you can connect to HDInsight cluster, create Hive tables, and run Hive queries. For more information, see [Get started using HDInsight Hadoop Tools for Visual Studio][1].

**To run a Hive job from the cluster dashboard**

1. Sign in to the [Azure Management Portal](https://manage.windowsazure.cn/).
2. Click **BROWSE ALL** and then click **HDInsight Clusters** to see a list of clusters, including the cluster you just created in the previous section.
3. Click the name of the cluster that you want to use to run the Hive job, and then click **Dashboard** at the top of the blade.
4. A webpage opens in a different browser tab. Enter the Hadoop user account and password. The default user name is **admin**; the password is what you entered while creating the cluster.
5. From the dashboard, click the **Hive Editor** tab. The following web page opens.

	![Hive Editor tab in the HDInsight cluster dashboard.][img-hdi-dashboard]

	There are several tabs at the top of the page. The default tab is **Hive Editor**, and the other tabs are **Job History** and **File Browser**. By using the dashboard, you can submit Hive queries, check Hadoop job logs, and browse files in storage.

	> [AZURE.NOTE] Note that the URL of the webpage is *&lt;ClusterName&gt;.azurehdinsight.cn*. So instead of opening the dashboard from the portal, you can open the dashboard from a web browser by using the URL.

6. On the **Hive Editor** tab, for **Query Name**, enter **HTC20**.  The query name is the job title. In the query pane, enter the Hive query as shown in the image:

	![Hive query entered in the query pane of the Hive Editor.][img-hdi-dashboard-query-select]

4. Click **Submit**. It takes a few moments to get the results back. The screen refreshes every 30 seconds. You can also click **Refresh** to refresh the screen.

    ![Results from a Hive query in listed at the bottom of the cluster dashboard.][img-hdi-dashboard-query-select-result]

5. After the status shows that the job is completed, click the query name on the screen to see the output. Make a note of **Job Start Time (UTC)**. You will need it later.

    ![Job Start Time listed in the Job History tab of the HDInsight cluster dashboard.][img-hdi-dashboard-query-select-result-output]

    The page also shows the **Job Output** and the **Job Log**. You also have the option to download the output file (\_stdout) and the log file \(_stderr).


**To browse to the output file**

1. On the cluster dashboard, click **File Browser**.
2. Click your storage account name, click your container name (which is the same as your cluster name), and then click **user**.
3. Click **admin** and then click the GUID that has the last modified time (a little after the job start time you noted earlier). Copy this GUID. You will need it in the next section.


   	![The Hive query output file GUID listed in the File Browser tab.][img-hdi-dashboard-query-browse-output]


##Connect to Microsoft business intelligence tools for Excel

You can use the Power Query add-in for Microsoft Excel to import the job output from HDInsight into Excel, where Microsoft business intelligence tools can be used to further analyze the results.

You must have Excel 2013 or 2010 installed to complete this part of the tutorial.

**To download Microsoft Power Query for Excel**

- Download Microsoft Power Query for Microsoft Excel from the [Microsoft Download Center](http://www.microsoft.com/download/details.aspx?id=39379) and install it.

**To import HDInsight data**

1. Open Excel, and create a new workbook.
3. Click the **Power Query** menu, click **From Other Sources**, and then click **From Azure HDInsight**.

	![Excel PowerQuery Import menu open for Azure HDInsight.][image-hdi-gettingstarted-powerquery-importdata]

3. Enter the **Account Name** of the Azure Blob Storage account that is associated with your cluster, and then click **OK**. (This is the storage account you created earlier in the tutorial.)
4. Enter the **Account Key** for the Azure Blob Storage account, and then click **Save**.
5. In the right pane, double-click the blob name. By default the blob name is the same as the cluster name.

6. Locate **stdout** in the **Name** column. Verify that the GUID in the corresponding **Folder Path** column matches the GUID you copied earlier. A match suggests that the output data corresponds to the job you submitted. Click **Binary** in the column left of **stdout**.

	![Finding the data output by GUID in the list of content.][image-hdi-gettingstarted-powerquery-importdata2]

9. Click **Close & Load** in the upper-left corner to import the Hive job output into Excel.

##Run samples

HDInsight cluster provides a query console that includes a Getting Started gallery to run samples directly from the portal. You can use the samples to learn how to work with HDInsight by walking through some basic scenarios. These samples come with all the required components, such as the data to analyze and the queries to run on the data. To learn more about the samples in the Getting Started gallery, see [Learn Hadoop in HDInsight using the HDInsight Getting Started Gallery](/documentation/articles/hdinsight-learn-hadoop-use-sample-gallery).

**To run the sample**

1. From the Azure Management Portal startboard, click the tile for the cluster you just created.
 
2. On the new cluster blade, click **Dashboard**. When prompted, enter the admin username and password for the cluster.

	![Launch cluster dashboard](./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.Cluster.Dashboard.png "Launch cluster dashboard")
 
3. From the webpage that opens, click the **Getting Started Gallery** tab, and then under the **Solutions with Sample Data** category, click the sample that you want to run. Follow the instructions on the Web page to finish the sample. The following table lists a couple of samples and provides more information about what each sample does.

Sample | What does it do?
------ | ---------------
[Sensor data analysis][hdinsight-sensor-data-sample] | Learn how to use HDInsight to process historical data that is produced by heating, ventilation, and air conditioning (HVAC) systems to identify systems that are not able to reliably maintain a set temperature.
[Website log analysis][hdinsight-weblogs-sample] | Learn how to use HDInsight to analyze website log files to get insight into the frequency of visits to the website in a day from external websites, and a summary of website errors that the users experience.



##Next steps
In this Hadoop tutorial, you learned how to create a Hadoop cluster on Windows in HDInsight, run a Hive query on data, and import the results into Excel, where they can be further processed and graphically displayed with business intelligence tools. To learn more, see the following tutorials:

- [Get started using HDInsight Hadoop Tools for Visual Studio][1]
- [Get started with the HDInsight Emulator][hdinsight-emulator]
- [Use Azure Blob storage with HDInsight][hdinsight-storage]
- [Administer HDInsight using PowerShell][hdinsight-admin-powershell]
- [Upload data to HDInsight][hdinsight-upload-data]
- [Use MapReduce with HDInsight][hdinsight-use-mapreduce]
- [Use Hive with HDInsight][hdinsight-use-hive]
- [Use Pig with HDInsight][hdinsight-use-pig]
- [Use Oozie with HDInsight][hdinsight-use-oozie]
- [Develop C# Hadoop streaming programs for HDInsight][hdinsight-develop-streaming]
- [Develop Java MapReduce programs for HDInsight][hdinsight-develop-mapreduce]


[1]: /documentation/articles/hdinsight-hadoop-visual-studio-tools-get-started

[hdinsight-versions]: /documentation/articles/hdinsight-component-versioning


[hdinsight-provision]: /documentation/articles/hdinsight-provision-clusters
[hdinsight-admin-powershell]: /documentation/articles/hdinsight-administer-use-powershell
[hdinsight-upload-data]: /documentation/articles/hdinsight-upload-data
[hdinsight-use-mapreduce]: /documentation/articles/hdinsight-use-mapreduce
[hdinsight-use-hive]: /documentation/articles/hdinsight-use-hive
[hdinsight-use-pig]: /documentation/articles/hdinsight-use-pig
[hdinsight-use-oozie]: /documentation/articles/hdinsight-use-oozie
[hdinsight-storage]: /documentation/articles/hdinsight-hadoop-use-blob-storage
[hdinsight-emulator]: /documentation/articles/hdinsight-hadoop-emulator-get-started
[hdinsight-develop-streaming]: /documentation/articles/hdinsight-hadoop-develop-deploy-streaming-jobs
[hdinsight-develop-mapreduce]: /documentation/articles/hdinsight-develop-deploy-java-mapreduce
[hadoop-hdinsight-intro]: /documentation/articles/hdinsight-hadoop-introduction
[hdinsight-weblogs-sample]: /documentation/articles/hdinsight-hive-analyze-website-log
[hdinsight-sensor-data-sample]: /documentation/articles/hdinsight-hive-analyze-sensor-data

[azure-purchase-options]: /pricing/overview/
[azure-member-offers]: /pricing/member-offers/
[azure-trial]: /pricing/1rmb-trial/
[azure-management-portal]: https://manage.windowsazure.cn/
[azure-create-storageaccount]: /documentation/articles/storage-create-storage-account

[apache-hadoop]: http://hadoop.apache.org/
[apache-hive]: https://cwiki.apache.org/confluence/display/Hive/Home%3bjsessionid=AF5B37E667D7DBA633313BB2280C9072
[apache-mapreduce]: http://wiki.apache.org/hadoop/MapReduce
[apache-hdfs]: http://hadoop.apache.org/docs/r1.0.4/hdfs_design.html
[hdinsight-hbase-custom-provision]: /documentation/articles/hdinsight-hbase-tutorial-get-started


[powershell-download]: http://go.microsoft.com/fwlink/p/?linkid=320376&clcid=0x409
[powershell-install-configure]: /documentation/articles/powershell-install-configure
[powershell-open]: /documentation/articles/powershell-install-configure#Install


[img-hdi-dashboard]: ./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.dashboard.png
[img-hdi-dashboard-query-select]: ./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.dashboard.query.select.png
[img-hdi-dashboard-query-select-result]: ./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.dashboard.query.select.result.png
[img-hdi-dashboard-query-select-result-output]: ./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.dashboard.query.select.result.output.png
[img-hdi-dashboard-query-browse-output]: ./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.dashboard.query.browse.output.png

[img-hdi-getstarted-video]: ./media/hdinsight-hadoop-tutorial-get-started-windows/hdi-get-started-video.png


[image-hdi-storageaccount-quickcreate]: ./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.StorageAccount.QuickCreate.png
[image-hdi-clusterstatus]: ./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.ClusterStatus.png
[image-hdi-quickcreatecluster]: ./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.QuickCreateCluster.png
[image-hdi-getstarted-flow]: ./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.GetStartedFlow.png

[image-hdi-gettingstarted-powerquery-importdata]: ./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.GettingStarted.PowerQuery.ImportData.png
[image-hdi-gettingstarted-powerquery-importdata2]: ./media/hdinsight-hadoop-tutorial-get-started-windows/HDI.GettingStarted.PowerQuery.ImportData2.png
 