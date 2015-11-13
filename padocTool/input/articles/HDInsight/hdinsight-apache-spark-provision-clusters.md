<!-- not suitable for mooncake-->

<properties 
   pageTitle="Provision Apache Spark clusters in HDInsight | Azure" 
   description="Learn how to provision Spark clusters for Azure HDInsight by using the Azure Management Portal, Azure PowerShell, a command line, or the HDInsight .NET SDK" 
   services="hdinsight" 
   documentationCenter="" 
   authors="nitinme" 
   manager="paulettm" 
   editor="cgronlun"/>

<tags
   ms.service="hdinsight"
    ms.date="08/17/2015"
   wacn.date=""/>

# Provision Apache Spark clusters in HDInsight using custom options

For most scenarios, you can provision a Spark cluster using the quick create method as described in [Get Started with Apache Spark on HDInsight](/documentation/articles/hdinsight-apache-spark-zeppelin-notebook-jupyter-spark-sql). In certain scenarios, you might want to provision a customized cluster. For example, you might want to attach an external metadata store to keep your Hive metadata persistent beyond the lifetime of a cluster, or you might want to use additional storage with the cluster. 

For such and other scenarios, this article provides instructions on how to use the Azure Management Portal, Azure PowerShell, or the HDInsight .NET SDK to provision a customized Spark cluster on HDInsight.  


**Prerequisites:**

Before you begin the instructions in this article, you must have an Azure subscription. See [Get Azure trial][azure-trial].

##<a id="configuration"></a>What are the different configuration options?

###Additional storage

During configuration, you must specify an Azure Blob storage account and a default container. This is used as the default storage location by the cluster. Optionally, you can specify an additional Azure Storage account that will also be associated with the cluster.   

>[AZURE.NOTE] Don't share one Blob storage container for multiple clusters. This is not supported. 

For more information on using secondary Blob stores, see [Using Azure Blob Storage with HDInsight](/documentation/articles/hdinsight-use-blob-storage).

###Metastore

Spark enables you to define schema and Hive tables over raw data. You can save these schemas and table metadata to external metastores. Using the metastore helps you to retain your Hive metadata, so that you don't need to re-create Hive tables when you provision a new cluster. By default, Hive uses an embedded database to store this information. The embedded database can't preserve the metadata when the cluster is deleted.

### Cluster customization

You can install additional components or customize cluster configuration by using scripts during provisioning. Such scripts are invoked via **Script Action**, which is a configuration option that can be used from the Azure Management Portal, HDInsight Windows PowerShell cmdlets, or the HDInsight .NET SDK. For more information, see [Customize HDInsight cluster using Script Action][hdinsight-customize-cluster].


###Virtual networking

[Azure Virtual Network](http://www.windowsazure.cn/home/features/networking/) allows you to create a secure, persistent network containing the resources you need for your solution. A virtual network allows you to:

* Connect cloud resources together in a private network (cloud-only).

	![diagram of cloud-only configuration](./media/hdinsight-apache-spark-provision-clusters/hdinsight-vnet-cloud-only.png)

* Connect your cloud resources to your local data-center network (site-to-site or point-to-site) by using a virtual private network (VPN).

	Site-to-site configuration allows you to connect multiple resources from your data center to the Azure virtual network by using a hardware VPN or the Routing and Remote Access Service.

	![diagram of site-to-site configuration](./media/hdinsight-apache-spark-provision-clusters/hdinsight-vnet-site-to-site.png)

	Point-to-site configuration allows you to connect a specific resource to the Azure virtual network by using a software VPN.

	![diagram of point-to-site configuration](./media/hdinsight-apache-spark-provision-clusters/hdinsight-vnet-point-to-site.png)

For more information on Virtual Network features, benefits, and capabilities, see the [Azure Virtual Network overview](http://msdn.microsoft.com/zh-cn/library/azure/jj156007.aspx).

> [AZURE.NOTE] You must create the Azure virtual network before provisioning a cluster. For more information, see [How to create a Virtual Network](http://msdn.microsoft.com/zh-cn/library/azure/jj156206.aspx).
>
> Azure HDInsight supports only location-based virtual networks and does not currently work with affinity group-based virtual networks.
>
> It is highly recommended to designate a single subnet for one cluster.

##<a id="portal"></a> Using the Azure Management Portal

Spark clusters on HDInsight use an Azure Blob storage container as the default file system. An Azure Storage account located on the same data center is required before you can create an HDInsight cluster. For more information, see [Use Azure Blob Storage with HDInsight](/documentation/articles/hdinsight-hadoop-use-blob-storage). For details on creating an Azure Storage account, see [How to Create a Storage Account][azure-create-storageaccount].

**To create an HDInsight cluster by using the Custom Create option**

1. Sign in to the [Azure Management Portal][azure-management-portal].
2. Click **+ NEW** on the bottom of the page, click **DATA SERVICES**, click **HDINSIGHT**, and then click **CUSTOM CREATE**.
3. On the **Cluster Details** page, type or choose the following values:

	![Provide Spark on HDInsight cluster details](./media/hdinsight-apache-spark-provision-clusters/HDI.CustomProvision.Page1.png "Provide Spark on HDInsight cluster details")

    <table border='1'>
		<tr><th>Property</th><th>Value</th></tr>
		<tr><td>Cluster Name</td>
			<td><p>Name the cluster. </p>
				<ul>
				<li>The Domain Name System (DNS) name must start and end with an alphanumeric character and may contain dashes.</li>
				<li>The field must be a string from 3 to 63 characters.</li>
				</ul></td></tr>
		<tr><td>Cluster Type</td>
			<td>For cluster type, select <strong>Spark</strong>.</td></tr>
		<tr><td>Operating System</td>
			<td>Select <b>Windows Server 2012 R2 Data Center</b> to provision a Spark cluster running on Windows. </td></tr>
		<tr><td>HDInsight Version</td>
			<td>Choose the version. For Spark, the only available version option is <b>HDInsight 3.2</b>, which uses Spark 1.3.1.</td></tr>
		</table>

	Enter or select the values as shown in the table and then click the right arrow.

4. On the **Configure Cluster** page, enter or select the following values:

	![Provide number of nodes and types of nodes for the cluster](./media/hdinsight-apache-spark-provision-clusters/HDI.CustomProvision.Page2.png "Provide number of nodes and types of nodes for the cluster")

	<table border="1">
	<tr><th>Name</th><th>Value</th></tr>
	<tr><td>Data Nodes</td><td>Number of data nodes you want to deploy. For testing purposes, create a single-node cluster. <br />The cluster size limit varies for Azure subscriptions. Contact Azure billing support to increase the limit.</td></tr>
	<tr><td>Region/Virtual Network</td><td><p>Choose the same region as the Storage account you created in the last procedure. HDInsight requires the Storage account to be located in the same region. Later in the configuration, you can choose only a Storage account that is in the same region that you specified here.</p>.<br/>If you have created an Azure virtual network, you can select the network that the HDInsight cluster will be configured to use.</p><p>For more information on creating an Azure virtual network.</p></td></tr>
	<tr><td>Head Node Size</td><td><p>Select a virtual machine (VM) size for the head node.</p></td></tr>
	<tr><td>Data Node Size</td><td><p>Select a VM size for the data nodes.</p></td></tr>
	</table>

	>[AZURE.NOTE] Based on the choice of VMs, your cost might vary. HDInsight uses all standard-tier VMs for cluster nodes. For information on how VM sizes affect your prices, see <a href="/home/features/hdinsight/#price" target="_blank">HDInsight Pricing</a>.	


5. On the **Configure Cluster User** page, provide the following values:

    ![Provide admin user and RDP user details](./media/hdinsight-apache-spark-provision-clusters/HDI.CustomProvision.Page3.png "Provide admin user and RDP user details")

    <table border='1'>
		<tr><th>Property</th><th>Value</th></tr>
		<tr><td>HTTP User Name</td>
			<td>Specify the HDInsight cluster user name.</td></tr>
		<tr><td>HTTP Password/Confirm Password</td>
			<td>Specify the HDInsight cluster user password.</td></tr>
		<tr><td>Enable remote desktop for cluster</td>
			<td>Select this check box to specify a username, password, and expiry date for a remote desktop user that can remote into the cluster nodes, once it is provisioned. You can also enable remote desktop later, after the cluster is provisioned. For instructions, see <a href="hdinsight-administer-use-management-portal-v1/#rdp" target="_blank">Connect to HDInsight clusters using RDP</a>.</td></tr>
		<tr><td>Enter the Hive/Oozie Metastore</td>
			<td>Select this check box to specify a SQL database on the same data center as the cluster, to be used as the Hive/Oozie metastore. If you select this checkbox, you must spcecify details about the Azure SQL database in the subsequent pages of the wizard. This is useful if you want to retain the metadata about Hive/Oozie jobs even after a cluster has been deleted. For instructions on how to create a metastore, see <a href="http://www.windowsazure.cn/documentation/articles/sql-database-get-started/" target="_blank">Create your first Azure SQL Database</a>.</td></tr>
		</td></tr>
	</table>

	>[AZURE.NOTE] The Azure SQL database used for the metastore must allow connectivity to other Azure services, including Azure HDInsight. On the Azure SQL database dashboard, on the right side, click the server name. This is the server on which the SQL database instance is running. Once you are on the server view, click **Configure**, and then for **Windows** **Azure Services**, click **Yes**, and then click **Save**.

    Click the right arrow.

6. On the **Configure Hive/Oozie Metastore** page, provide the following values:

    ![Provide Hive/Oozie metastore database details](./media/hdinsight-apache-spark-provision-clusters/HDI.CustomProvision.Page4.png "Provide Hive/Oozie metastore database details")

	Specify an Azure SQL database that will be used as the Hive/Oozie metastore. You can specify the same database for both Hive and Oozie metastores. This SQL database must be in the same data center as the HDInsight cluster. The list box lists only the SQL databases in the same data center that you specified on the <strong>Cluster Details</strong> page. Also specify the username and password to connect to the Azure SQL database you selected.

    >[AZURE.NOTE] The Azure SQL database used for the metastore must allow connectivity to other Azure services, including Azure HDInsight. On the Azure SQL database dashboard, on the right side, click the server name. This is the server on which the SQL database instance is running. Once you are on the server view, click **Configure**, and then for **Azure Services**, click **Yes**, and then click **Save**.

    Click the right arrow.

7. On the **Storage Account** page, provide the following values:

    ![Provide storage account details](./media/hdinsight-apache-spark-provision-clusters/HDI.CustomProvision.Page5.png "Provide storage account details")

	<table border='1'>
		<tr><th>Property</th><th>Value</th></tr>
		<tr><td>Storage Account</td>
			<td>Specify the Azure Storage account that will be used as the default file system for the HDInsight cluster. You can choose one of the three options:
			<ul>
				<li><strong>Use Existing Storage</strong></li>
				<li><strong>Create New Storage</strong></li>
				<li><strong>Use Storage from Another Subscription</strong></li>
			</ul>
			</td></tr>
		<tr><td>Account Name</td>
			<td><ul>
				<li>If you chose to use existing storage, for <strong>Account Name</strong>, select an existing Storage account. The drop-down lists only the Storage accounts located in the same data center where you chose to provision the cluster.</li>
				<li>If you chose the <strong>Create New Storage</strong> or <strong>Use Storage from Another Subscription</strong> option, you must provide the Storage account name.</li>
			</ul></td></tr>
		<tr><td>Account Key</td>
			<td>If you chose the <strong>Use Storage from Another Subscription</strong> option, specify the account key for that Storage account.</td></tr>
		<tr><td>Default Container</td>
			<td><p>Specify the default container on the Storage account that is used as the default file system for the HDInsight cluster. If you chose <strong>Use Existing Storage</strong> for the <strong>Storage Account</strong> field, and there are no existing containers in that account, the container is created by default with the same name as the cluster name. If a container with the name of the cluster already exists, a sequence number will be appended to the container name. For example, mycontainer1, mycontainer2, and so on. However, if the existing Storage account has a container with a name different from the cluster name you specified, you can use that container as well.</p>
            <p>If you chose to create new storage or use storage from another Azure subscription, you must specify the default container name.</p>
        </td></tr>
		<tr><td>Additional Storage Accounts</td>
			<td>HDInsight supports multiple Storage accounts. There is no limit on the additional Storage accounts that can be used by a cluster. However, if you create a cluster by using the Azure Management Portal, you have a limit of seven due to the UI constraints. Each additional Storage account you specify adds an extra **Storage Account** page to the wizard where you can specify the account information. For example, in the screenshot above, one additional Storage account is selected, and hence page 5 is added to the dialog.</td></tr>
	</table>

	Click the right arrow.

8. If you chose to configure additional storage for the cluster, on the **Storage Account** page, enter the account information for the additional Storage account:

	![Provide additional storage account details](./media/hdinsight-apache-spark-provision-clusters/HDI.CustomProvision.Page6.png "Provide additional storage account details")

    Here again, you have the option to choose from existing storage, create new storage, or use storage from another Azure subscription. The procedure to provide the values is similar to the previous step.

    > [AZURE.NOTE] Once an Azure Storage account is chosen for your HDInsight cluster, you can neither delete the account nor change the account to a different account.

8. On the **Script Actions** page, click **add script action** and provide details about the custom script that you want to run to customize a cluster, as the cluster is being created. For more information, see [Customize HDInsight clusters using Script Action][hdinsight-customize-cluster].

	If you need to use a script action, you must provide the following inputs. 
	
	<table border='1'>
		<tr><th>Property</th><th>Value</th></tr>
		<tr><td>Name</td>
			<td>Specify a name for the script action.</td></tr>
		<tr><td>Script URI</td>
			<td>Specify the Uniform Resource Identifier (URI) to the script that is invoked to customize the cluster.</td></tr>
		<tr><td>Node Type</td>
			<td>Specify the nodes on which the customization script is run. You can choose <b>All Nodes</b>, <b>Head nodes only</b>, or <b>Worker nodes only</b>.
		<tr><td>Parameters</td>
			<td>Specify the parameters, if required by the script.</td></tr>
	</table>

	You can add more than one script action to install multiple components on the cluster. After you have added the scripts, click the check mark to start provisioning the cluster. 



##<a id="powershell"></a> Using Azure PowerShell

Azure PowerShell is a powerful scripting environment that you can use to control and automate the deployment and management of your workloads in Azure. This section provides instructions on how to provision an HDInsight cluster by using Azure PowerShell. For information on configuring a workstation to run HDInsight Windows PowerShell cmdlets, see [Install and configure Azure PowerShell](/documentation/articles/install-configure-powershell). For more information on using Azure PowerShell with HDInsight, see [Administer HDInsight using PowerShell](/documentation/articles/hdinsight-administer-use-powershell). For the list of the HDInsight Windows PowerShell cmdlets, see [HDInsight cmdlet reference](https://msdn.microsoft.com/zh-cn/library/azure/dn858087.aspx).


The following procedures are needed to provision an HDInsight cluster by using Azure PowerShell:

- Create an Azure resource group
- Create an Azure Storage account
- Create an Azure Blob container
- Create an HDInsight cluster


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

		# The location of the HDInsight cluster. It must be in the same data center as the Storage account.
		$location = Get-AzureStorageAccount -ResourceGroupName $resourceGroupName -StorageAccountName $storageAccountName | %{$_.Location}

		# Create a new HDInsight cluster
		New-AzureHDInsightCluster -ClusterName $clusterName -ResourceGroupName $resourceGroupName -HttpCredential $credentials -Location $location -DefaultStorageAccountName "$storageAccountName.blob.core.chinacloudapi.cn" -DefaultStorageAccountKey $storageAccountKey -DefaultStorageContainer $containerName  -ClusterSizeInNodes $clusterNodes -ClusterType Spark


	![HDI.CLI.Provision](./media/hdinsight-apache-spark-provision-clusters/HDI.ps.provision.png)


##<a id="sdk"></a> Using the ARM-based HDInsight .NET SDK
The HDInsight .NET SDK provides .NET client libraries that make it easier to work with HDInsight from a .NET Framework application. Follow the instructions below to create a Visual Studio console application and paste the code for creating a cluster.

**To create a Visual Studio console application**

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
	<td style="border-color: #c6c6c6; border-width: 2px; border-style: solid; border-collapse: collapse; padding-left:5px;">CreateHDICluster</td></tr>
	</table>

4. Click **OK** to create the project.

5. From the **Tools** menu, click **Nuget Package Manager**, and then click **Manage Nuget Packages for Solutions**. In the Search text box within the dialog box, search for **HDInsight**. From the results that show up, install the following:

	 * Microsoft.Azure.Management.HDInsight
	 * Microsoft.Azure.Management.HDInsight.Job

	Search for Azure Authentication and from the results that show up, install **Microsoft.Azure.Common.Authentication**.

6. From Solution Explorer, double-click **Program.cs** to open it, paste the following code, and provide values for the variables:


        using System;
		using System.Collections.Generic;
		using System.Diagnostics;
		using System.Linq;
		using System.Security;
		using System.Text;
		using System.Threading.Tasks;
		using Hyak.Common;
		using Microsoft.Azure;
		using Microsoft.Azure.Common.Authentication;
		using Microsoft.Azure.Common.Authentication.Models;
		using Microsoft.Azure.Management.HDInsight;
		using Microsoft.Azure.Management.HDInsight.Job;
		using Microsoft.Azure.Management.HDInsight.Job.Models;
		using Microsoft.Azure.Management.HDInsight.Models;
		using Newtonsoft.Json;


		namespace CreateHDICluster
		{
		    internal class Program
		    {
		        private static ProfileClient _profileClient;
		        private static SubscriptionCloudCredentials _cloudCredentials;
		        private static HDInsightManagementClient _hdiManagementClient;

		        private static Guid SubscriptionId = new Guid("<SubscriptionID>");
		        private const string ResourceGroupName = "<ResourceGroupName>";
		        private const string ExistingStorageName = "<storageaccountname>.blob.core.chinacloudapi.cn";
		        private const string ExistingStorageKey = "<account key>";
		        private const string ExistingContainer = "<container name>";
		        private const string NewClusterName = "<cluster name>";
		        private const int NewClusterNumNodes = <number of nodes>;
		        private const string NewClusterLocation = "<location>";		//should be same as the storage account
		        private const OSType NewClusterOsType = OSType.Windows;
		        private const HDInsightClusterType NewClusterType = HDInsightClusterType.Spark;
		        private const string NewClusterVersion = "3.2";
		        private const string NewClusterUsername = "admin";
		        private const string NewClusterPassword = "<password>";

		        private static void Main(string[] args)
		        {
		            System.Console.WriteLine("Start cluster provisioning");

		            _profileClient = GetProfile();
		            _cloudCredentials = GetCloudCredentials();
		            _hdiManagementClient = new HDInsightManagementClient(_cloudCredentials);

		            System.Console.WriteLine(String.Format("Creating the cluster {0}...", NewClusterName));
		            CreateCluster();
		            System.Console.WriteLine("Done. Press any key to continue.");
		            System.Console.ReadKey(true);
		        }

		        private static void CreateCluster()
		        {
		            var parameters = new ClusterCreateParameters
		            {
		                ClusterSizeInNodes = NewClusterNumNodes,
		                UserName = NewClusterUsername,
		                Password = NewClusterPassword,
		                Location = NewClusterLocation,
		                DefaultStorageAccountName = ExistingStorageName,
		                DefaultStorageAccountKey = ExistingStorageKey,
		                DefaultStorageContainer = ExistingContainer,
		                ClusterType = NewClusterType,
		                OSType = NewClusterOsType
		            };

		            _hdiManagementClient.Clusters.Create(ResourceGroupName, NewClusterName, parameters);
		        }

		        private static ProfileClient GetProfile(string username = null, SecureString password = null)
		        {
		            var profileClient = new ProfileClient(new AzureProfile());
		            var env = profileClient.GetEnvironmentOrDefault(EnvironmentName.AzureCloud);
		            var acct = new AzureAccount { Type = AzureAccount.AccountType.User };

		            if (username != null && password != null)
		                acct.Id = username;

		            profileClient.AddAccountAndLoadSubscriptions(acct, env, password);

		            return profileClient;
		        }

		        private static SubscriptionCloudCredentials GetCloudCredentials()
		        {
		            var sub = _profileClient.Profile.Subscriptions.Values.FirstOrDefault(s => s.Id.Equals(SubscriptionId));

		            Debug.Assert(sub != null, "subscription != null");
		            _profileClient.SetSubscriptionAsDefault(sub.Id, sub.Account);

		            return AzureSession.AuthenticationFactory.GetSubscriptionCloudCredentials(_profileClient.Profile.Context);
		        }

		    }
		}

7. Press **F5** to run the application. A console window should open and display the status of the application. You will also be prompted to enter your Azure account credentials. It can take several minutes to create an HDInsight cluster.


##<a id="nextsteps"></a> Next steps

* See [Perform interactive data analysis using Spark in HDInsight with BI tools](/documentation/articles/hdinsight-apache-spark-use-bi-tools) to learn how to use Apache Spark in HDInsight with BI tools like Power BI and Tableau. 
* See [Use Spark in HDInsight for building machine learning applications](/documentation/articles/hdinsight-apache-spark-ipython-notebook-machine-learning) to learn how to build machine learning applications using Apache Spark on HDInsight.
* See [Use Spark in HDInsight for building real-time streaming applications](/documentation/articles/hdinsight-apache-spark-csharp-apache-zeppelin-eventhub-streaming) to learn how to build streaming applications using Apache Spark on HDInsight.
* See [Manage resources for the Apache Spark cluster in Azure HDInsight](/documentation/articles/hdinsight-apache-spark-resource-manager) to learn how to use the Resource Manager to manage resources allocated to the Spark cluster.


[hdinsight-sdk-documentation]: http://msdn.microsoft.com/zh-cn/library/dn479185.aspx
[hdinsight-hbase-custom-provision]: http://www.windowsazure.cn/documentation/articles/hdinsight-hbase-get-started

[hdinsight-customize-cluster]: /documentation/articles/hdinsight-hadoop-customize-cluster
[hdinsight-get-started]: /documentation/articles/hdinsight-get-started
[hdinsight-admin-powershell]: /documentation/articles/hdinsight-administer-use-powershell
[hdinsight-admin-portal]: /documentation/articles/hdinsight-administer-use-management-portal-v1
[hadoop-hdinsight-intro]: /documentation/articles/hdinsight-hadoop-introduction
[hdinsight-submit-jobs]: /documentation/articles/hdinsight-submit-hadoop-jobs-programmatically
[hdinsight-powershell-reference]: https://msdn.microsoft.com/zh-cn/library/dn858087.aspx
[hdinsight-storm-get-started]: /documentation/articles/hdinsight-storm-getting-started
[azure-management-portal]: https://manage.windowsazure.cn/

[azure-command-line-tools]: /documentation/articles/xplat-cli
[azure-create-storageaccount]: /documentation/articles/storage-create-storage-account
[apache-hadoop]: http://go.microsoft.com/fwlink/?LinkId=510084
[azure-purchase-options]: http://www.windowsazure.cn/pricing/overview/
[azure-trial]: http://www.windowsazure.cn/pricing/1rmb-trial/
[hdi-remote]: http://www.windowsazure.cn/documentation/articles/hdinsight-administer-use-management-portal-v1/#rdp


[powershell-install-configure]: /documentation/articles/install-configure-powershell
[89e2276a]: /documentation/articles/hdinsight-use-sqoop/ "Use Sqoop with HDInsight"
