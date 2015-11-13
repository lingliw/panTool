<properties 
	pageTitle="Use Script Action to install Solr on Hadoop cluster | Windows Azure" 
	description="Learn how to customize HDInsight cluster with Solr. You'll use a Script Action configuration option to use a script to install Solr." 
	services="hdinsight" 
	documentationCenter="" 
	authors="nitinme" 
	manager="paulettm" 
	editor="cgronlun"/>

<tags
	ms.service="hdinsight"
	ms.date="10/02/2015"
	wacn.date=""/>

# Install and use Solr on HDInsight Hadoop clusters


Learn how to customize Windows based HDInsight cluster with Solr using Script Action, and how to use Solr to search data.<!-- deleted by customization For information on using Solr with a Linux-based cluster, see [Install and use Solr on HDinsight Hadoop clusters (Linux)](/documentation/articles/hdinsight-hadoop-solr-install-linux).-->
 
You can install Solr on any type of cluster (Hadoop, Storm, HBase<!-- deleted by customization , Spark -->) on Azure HDInsight by using *Script Action*. A sample script to install Solr on an HDInsight cluster is available from a read-only Azure storage blob at [https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1](https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1). 

The sample script works only with HDInsight cluster version 3.1. For more information on HDInsight cluster versions, see [HDInsight cluster versions](/documentation/articles/hdinsight-component-versioning).

The sample script used in this topic creates a Windows-based Solr cluster with a specific configuration. If you want to configure the Solr cluster with different collections, shards, schemas, replicas, etc., you must modify the script and Solr binaries accordingly.

**Related articles**
<!-- deleted by customization 

- [Install Solr on HDInsight clusters](/documentation/articles/hdinsight-hadoop-solr-install): install Solr on HDInsight cluster using the Azure Preview Portal
- [Install and use Solr on HDinsight Hadoop clusters (Linux)](/documentation/articles/hdinsight-hadoop-solr-install-linux)
-->
- [Create Hadoop clusters in HDInsight](/documentation/articles/hdinsight-provision-clusters): general information on creating HDInsight clusters
- [Customize HDInsight cluster using Script Action][hdinsight-cluster-customize]: general information on customizing HDInsight clusters using Script Action
- [Develop Script Action scripts for HDInsight](/documentation/articles/hdinsight-hadoop-script-actions)

<!-- keep by customization: begin -->
<a name="whatis"></a>
<!-- keep by customization: end -->
## What is Solr?

<a href="http://lucene.apache.org/solr/features.html" target="_blank">Apache Solr</a> is an enterprise search platform that enables powerful full-text search on data. While Hadoop enables storing and managing vast amounts of data, Apache Solr provides the search capabilities to quickly retrieve the data.    
<!-- deleted by customization 

## Install Solr using portal

[AZURE.INCLUDE [hdinsight-azure-portal](../includes/hdinsight-azure-portal.md)]

-->
<!-- keep by customization: begin -->
<a name="install"></a>
## How do I install Solr?

A sample script to install Solr on an HDInsight cluster is available from a read-only Azure storage blob at [https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1](https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1). This section provides instructions on how to use the sample script while provisioning the cluster by using the Azure Management Portal. 
<!-- keep by customization: end -->
* [Install Solr on HDInsight clusters](/documentation/articles/hdinsight-hadoop-solr-install)

1. Start creating a cluster by using the **CUSTOM CREATE** option, as described at [Create Hadoop clusters in HDInsight](/documentation/articles/hdinsight-provision-clusters#portal). 
2. On the **Script Actions** page of the wizard, click **add script action** to provide details about the script action, as shown below:

	![Use Script Action to customize a cluster](./media/hdinsight-hadoop-solr-install-v1/hdi-script-action-solr.png "Use Script Action to customize a cluster")
	
	<table border='1'>
		<tr><th>Property</th><th>Value</th></tr>
		<tr><td>Name</td>
			<td>Specify a name for the script action. For example, <b>Install Solr</b>.</td></tr>
		<tr><td>Script URI</td>
			<td>Specify the Uniform Resource Identifier (URI) to the script that is invoked to customize the cluster. For example, <i>https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1</i></td></tr>
		<tr><td>Node Type</td>
			<td>Specify the nodes on which the customization script is run. You can choose <b>All nodes</b>, <b>Head nodes only</b>, or <b>Worker nodes only</b>.
		<tr><td>Parameters</td>
			<td>Specify the parameters, if required by the script. The script to install Solr does not require any parameters, so you can leave this blank.</td></tr>
	</table>	

	You can add more than one script action to install multiple components on the cluster. After you have added the scripts, click the checkmark to start creating the cluster.

You can also use the script to install Solr on HDInsight by using Azure PowerShell or the HDInsight .NET SDK. Instructions for these procedures are provided later in this topic.

<!-- keep by customization: begin -->
<a name="usesolr"></a>
<!-- keep by customization: end -->
## Use Solr

You must start with indexing Solr with some data files. You can then use Solr to run search queries on the indexed data. Perform the following steps to use Solr in an HDInsight cluster:

1. **Use Remote Desktop Protocol (RDP) to remote into the HDInsight cluster with Solr installed**. From the Azure Management Portal, enable Remote Desktop for the cluster you created with Solr installed, and then remote into the cluster. For instructions, see <a href="/documentation/articles/hdinsight-administer-use-management-portal-v1/#rdp" target="_blank">Connect to HDInsight clusters using RDP</a>.

2. **Index Solr by uploading data files**. When you index Solr, you put documents in it that you may need to search on. To index Solr, use RDP to remote into the cluster, navigate to the desktop, open the Hadoop command line, and navigate to **C:\apps\dist\solr-4.7.2\example\exampledocs**. Run the following command: 
	
		java -jar post.jar solr.xml monitor.xml

	You'll see the following output on the console:

		POSTing file solr.xml
		POSTing file monitor.xml
		2 files indexed.
		COMMITting Solr index changes to http://localhost:8983/solr/update..
		Time spent: 0:00:01.624

	The post.jar utility indexes Solr with two sample documents, **solr.xml** and **monitor.xml**. The post.jar utility and the sample documents are available with Solr installation.

3. **Use the Solr dashboard to search within the indexed documents**. In the RDP session to the HDInsight cluster, open Internet Explorer, and launch the Solr dashboard at **http://headnodehost:8983/solr/#/**. From the left pane, from the **Core Selector** drop-down, select **collection1**, and within that, click **Query**. As an example, to select and return all the docs in Solr, provide the following values:
	1. In the **q** text box, enter **\*:**\*. This will return all the documents that are indexed in Solr. If you want to search for a specific string within the documents, you can enter that string here.
	2. In the **wt** text box, select the output format. Default is **json**. Click **Execute Query**.

		![Use Script Action to customize a cluster](./media/hdinsight-hadoop-solr-install-v1/hdi-solr-dashboard-query.png "Run a query on Solr dashboard")
	
	The output returns the two docs that we used for indexing Solr. The output resembles the following:

			"response": {
			    "numFound": 2,
			    "start": 0,
			    "maxScore": 1,
			    "docs": [
			      {
			        "id": "SOLR1000",
			        "name": "Solr, the Enterprise Search Server",
			        "manu": "Apache Software Foundation",
			        "cat": [
			          "software",
			          "search"
			        ],
			        "features": [
			          "Advanced Full-Text Search Capabilities using Lucene",
			          "Optimized for High Volume Web Traffic",
			          "Standards Based Open Interfaces - XML and HTTP",
			          "Comprehensive HTML Administration Interfaces",
			          "Scalability - Efficient Replication to other Solr Search Servers",
			          "Flexible and Adaptable with XML configuration and Schema",
			          "Good unicode support: héllo (hello with an accent over the e)"
			        ],
			        "price": 0,
			        "price_c": "0,USD",
			        "popularity": 10,
			        "inStock": true,
			        "incubationdate_dt": "2006-01-17T00:00:00Z",
			        "_version_": 1486960636996878300
			      },
			      {
			        "id": "3007WFP",
			        "name": "Dell Widescreen UltraSharp 3007WFP",
			        "manu": "Dell, Inc.",
			        "manu_id_s": "dell",
			        "cat": [
			          "electronics and computer1"
			        ],
			        "features": [
			          "30\" TFT active matrix LCD, 2560 x 1600, .25mm dot pitch, 700:1 contrast"
			        ],
			        "includes": "USB cable",
			        "weight": 401.6,
			        "price": 2199,
			        "price_c": "2199,USD",
			        "popularity": 6,
			        "inStock": true,
			        "store": "43.17614,-90.57341",
			        "_version_": 1486960637584081000
			      }
			    ]
			  }
   

4. **Recommended: Back up the indexed data from Solr to Azure Blob storage associated with the HDInsight cluster**. As a good practice, you should back up the indexed data from the Solr cluster nodes onto Azure Blob storage. Perform the following steps to do so:

	1. From the RDP session, open Internet Explorer, and point to the following URL:

			http://localhost:8983/solr/replication?command=backup

		You should see a response like this:

			<?xml version="1.0" encoding="UTF-8"?>
			<response>
			  <lst name="responseHeader">
			    <int name="status">0</int>
			    <int name="QTime">9</int>
			  </lst>
			  <str name="status">OK</str>
			</response>

	2. In the remote session, navigate to {SOLR_HOME}\{Collection}\data. For the cluster created via the sample script, this should be **C:\apps\dist\solr-4.7.2\example\solr\collection1\data**. At this location, you should see a snapshot folder created with a name similar to **snapshot.*timestamp***.
	
	3. Zip the snapshot folder and upload it to Azure Blob storage. From the Hadoop command line, navigate to the location of the snapshot folder by using the following command:

			  hadoop fs -CopyFromLocal snapshot._timestamp_.zip /example/data

		This command copies the snapshot to /example/data/ under the container within the default Storage account associated with the cluster.

<!-- keep by customization: begin -->
<a name="usingPS"></a>
<!-- keep by customization: end -->
## Install Solr using Aure PowerShell
<!-- deleted by customization

See [Customize HDInsight clusters using Script Action](/documentation/articles/hdinsight-hadoop-customize-cluster#call_scripts_using_powershell).  The sample demonstrates how to install Spark using Azure PowerShell. You need to customize the script to use [https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1](https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1).

-->
<!-- keep by customization: begin -->
In this section we use the **<a href = "http://msdn.microsoft.com/zh-cn/library/dn858088.aspx" target="_blank">Add-AzureHDInsightScriptAction</a>** cmdlet to invoke scripts by using Script Action to customize a cluster. Before proceeding, make sure you have installed and configured Azure PowerShell. For information on configuring a workstation to run HDInsight Windows PowerShell cmdlets, see [Install and configure Azure PowerShell][powershell-install-configure].

Perform the following steps:

1. Open an Azure PowerShell window and declare the following variables:

		# PROVIDE VALUES FOR THESE VARIABLES
		$subscriptionName = "<SubscriptionName>"		# Name of the Azure subscription
		$clusterName = "<HDInsightClusterName>"			# HDInsight cluster name
		$storageAccountName = "<StorageAccountName>"	# Azure Storage account that hosts the default container
		$storageAccountKey = "<StorageAccountKey>"      # Key for the Storage account
		$containerName = $clusterName
		$location = "<MicrosoftDataCenter>"				# Location of the HDInsight cluster. It must be in the same data center as the Storage account.
		$clusterNodes = <ClusterSizeInNumbers>			# Number of nodes in the HDInsight cluster
		$version = "<HDInsightClusterVersion>"          # For example, "3.1"
	
2. Specify the configuration values such as nodes in the cluster and the default storage to be used.

		# Specify the configuration options
		Select-AzureSubscription $subscriptionName
		$config = New-AzureHDInsightClusterConfig -ClusterSizeInNodes $clusterNodes
		$config.DefaultStorageAccount.StorageAccountName="$storageAccountName.blob.core.chinacloudapi.cn"
		$config.DefaultStorageAccount.StorageAccountKey=$storageAccountKey
		$config.DefaultStorageAccount.StorageContainerName=$containerName
	
3. Use the **Add-AzureHDInsightScriptAction** cmdlet to add a script action to the cluster configuration. Later, when the cluster is being created, the script action gets executed. 

		# Add the script action to the cluster configuration
		$config = Add-AzureHDInsightScriptAction -Config $config -Name "Install Solr" -ClusterRoleCollection HeadNode,DataNode -Uri https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1

	The **Add-AzureHDInsightScriptAction** cmdlet takes the following parameters:

	<table style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse;">
	<tr>
	<th style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; width:90px; padding-left:5px; padding-right:5px;">Parameter</th>
	<th style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; width:550px; padding-left:5px; padding-right:5px;">Definition</th></tr>
	<tr>
	<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Config</td>
	<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px; padding-right:5px;">Configuration object to which script action information is added.</td></tr>
	<tr>
	<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Name</td>
	<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Name of the script action.</td></tr>
	<tr>
	<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">ClusterRoleCollection</td>
	<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Nodes on which the customization script is run. The valid values are HeadNode (to install on the head node) or DataNode (to install on all the data nodes). You can use either or both values.</td></tr>
	<tr>
	<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Uri</td>
	<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">URI to the script that is executed.</td></tr>
	<tr>
	<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Parameters</td>
	<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Parameters required by the script. The sample script used in this topic does not require any parameters, and hence you do not see this parameter in the snippet above.
	</td></tr>
	</table>
	
4. Finally, start provisioning a customized cluster with Solr installed.  
	
		# Start provisioning a cluster with Solr installed
		New-AzureHDInsightCluster -Config $config -Name $clusterName -Location $location -Version $version 

When prompted, enter the credentials for the cluster. It can take several minutes before the cluster is created.

<a name="usingSDK"></a>
<!-- keep by customization: end -->
## Install Sole using .NET SDK
<!-- deleted by customization

See [Customize HDInsight clusters using Script Action](/documentation/articles/hdinsight-hadoop-customize-cluster#call_scripts_using_azure_powershell). The sample demonstrates how to install Spark using the .NET SDK. You need to customize the script to use [https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1](https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1).
-->
<!-- keep by customization: begin -->
The HDInsight .NET SDK provides .NET client libraries that make it easier to work with HDInsight from a .NET Framework application. This section provides instructions on how to use Script Action from the SDK to provision a cluster that has Solr installed. The following procedures must be performed:

- Install the HDInsight .NET SDK
- Create a self-signed certificate
- Create a console application
- Run the application


**To install the HDInsight .NET SDK**

You can install the latest published build of the SDK from [NuGet](http://nuget.codeplex.com/wikipage?title=Getting%20Started). The instructions will be shown in the next procedure.

**To create a self-signed certificate**

Create a self-signed certificate, install it on your workstation, and upload it to your Azure subscription. For instructions, see [Create a self-signed certificate](/documentation/articles/hdinsight-administer-use-management-portal-v1). 


**To create a Visual Studio application**

1. Open Visual Studio 2013.

2. From the **File** menu, click **New**, and then click **Project**.

3. From **New Project**, type or select the following values:
	
	<table style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse;">
	<tr>
	<th style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; width:90px; padding-left:5px; padding-right:5px;">Property</th>
	<th style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; width:90px; padding-left:5px; padding-right:5px;">Value</th></tr>
	<tr>
	<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Category</td>
	<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px; padding-right:5px;">Templates/Visual C#/Windows</td></tr>
	<tr>
	<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Template</td>
	<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Console Application</td></tr>
	<tr>
	<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">Name</td>
	<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">CreateSolrCluster</td></tr>
	</table>

4. Click **OK** to create the project.

5. From the **Tools** menu, click **Nuget Package Manager**, and then click **Package Manager Console**.

6. Run the following command in the console to install the package:

		Install-Package Microsoft.WindowsAzure.Management.HDInsight

	This command adds the .NET libraries and references to them from the current Visual Studio project.

	
7. From Solution Explorer, double-click **Program.cs** to open it.

8. Add the following using statements to the top of the file:

		using System.Security.Cryptography.X509Certificates;
		using Microsoft.WindowsAzure.Management.HDInsight;
		using Microsoft.WindowsAzure.Management.HDInsight.ClusterProvisioning;
		using Microsoft.WindowsAzure.Management.HDInsight.Framework.Logging;
	
9. In the Main() function, copy and paste the following code, and provide values for the variables:
		
        var clusterName = args[0];

        // Provide values for the variables
        string thumbprint = "<CertificateThumbprint>";  
        string subscriptionId = "<AzureSubscriptionID>";
        string location = "<MicrosoftDataCenterLocation>";
        string storageaccountname = "<AzureStorageAccountName>.blob.core.chinacloudapi.cn";
        string storageaccountkey = "<AzureStorageAccountKey>";
        string username = "<HDInsightUsername>";
        string password = "<HDInsightUserPassword>";
        int clustersize = <NumberOfNodesInTheCluster>;

        // Provide the certificate thumbprint to retrieve the certificate from the certificate store 
        X509Store store = new X509Store();
        store.Open(OpenFlags.ReadOnly);
        X509Certificate2 cert = store.Certificates.Cast<X509Certificate2>().First(item => item.Thumbprint == thumbprint);

        // Create an HDInsight client object
        HDInsightCertificateCredential creds = new HDInsightCertificateCredential(new Guid(subscriptionId), cert);
        var client = HDInsightClient.Connect(creds);
		client.IgnoreSslErrors = true;
        
        // Provide the cluster information
		var clusterInfo = new ClusterCreateParameters()
        {
            Name = clusterName,
            Location = location,
            DefaultStorageAccountName = storageaccountname,
            DefaultStorageAccountKey = storageaccountkey,
            DefaultStorageContainer = clusterName,
            UserName = username,
            Password = password,
            ClusterSizeInNodes = clustersize,
            Version = "3.1"
        };        

10. Append the following code to the Main() function to use the [ScriptAction](http://msdn.microsoft.com/zh-cn/library/microsoft.windowsazure.management.hdinsight.clusterprovisioning.data.scriptaction.aspx) class to invoke a custom script to install Solr.

		// Add the script action to install Solr
        clusterInfo.ConfigActions.Add(new ScriptAction(
          "Install Solr", // Name of the config action
          new ClusterNodeType[] { ClusterNodeType.HeadNode, ClusterNodeType.DataNode }, // List of nodes to install Solr on
          new Uri("https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1"), // Location of the script to install Solr
		  null //Because the script used does not require any parameters
        ));

11. Finally, create the cluster.

		client.CreateCluster(clusterInfo);

11. Save changes to the application and build the solution. 

**To run the application**

Open a Windows PowerShell or Azure PowerShell console, navigate to the location where you saved the Visual Studio project, navigate to the \bin\debug directory within the project, and then run the following command:

	.\CreateSolrCluster <cluster-name>

Provide a cluster name and press ENTER to provision a cluster with Solr installed.
<!-- keep by customization: end -->

## See also
<!-- deleted by customization

- [Install Solr on HDInsight clusters](/documentation/articles/hdinsight-hadoop-solr-install): install Solr on HDInsight cluster using the Azure Preview Portal
- [Install and use Solr on HDinsight Hadoop clusters (Linux)](/documentation/articles/hdinsight-hadoop-solr-install-linux)
-->
- [Create Hadoop clusters in HDInsight](/documentation/articles/hdinsight-provision-clusters): general information on creating HDInsight clusters
- [Customize HDInsight cluster using Script Action][hdinsight-cluster-customize]: general information on customizing HDInsight clusters using Script Action
- [Develop Script Action scripts for HDInsight](/documentation/articles/hdinsight-hadoop-script-actions)
<!-- deleted by customization
- [Install and use Spark on HDInsight clusters][hdinsight-install-spark]: Script Action sample about installing Spark
-->
- [Install R on HDInsight clusters][hdinsight-install-r]: Script Action sample about installing R
- [Install Giraph on HDInsight clusters](/documentation/articles/hdinsight-hadoop-giraph-install): Script Action sample about installing Giraph

[powershell-install-configure]: /documentation/articles/install-configure-powershell
[hdinsight-provision]: /documentation/articles/hdinsight-provision-clusters
[hdinsight-install-r]: /documentation/articles/hdinsight-hadoop-r-scripts
<!-- deleted by customization
[hdinsight-install-spark]: /documentation/articles/hdinsight-hadoop-spark-install
-->
[hdinsight-cluster-customize]: /documentation/articles/hdinsight-hadoop-customize-cluster