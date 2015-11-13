<!-- not suitable for mooncake-->

<properties
   pageTitle="Tips for using Hadoop on Linux-based HDInsight | Azure"
   description="Get implementation tips for using Linux-based HDInsight (Hadoop) clusters on a familiar Linux environment running in the Azure cloud."
   services="hdinsight"
   documentationCenter=""
   authors="Blackmist"
   manager="paulettm"
   editor="cgronlun"
	tags="azure-portal"/>

<tags
   ms.service="hdinsight"
   ms.date="08/12/2015"
   wacn.date=""/>

# Information about using HDInsight on Linux

Linux-based Azure HDInsight clusters provide Hadoop on a familiar Linux environment, running in the Azure cloud. For most things, it should work exactly as any other Hadoop-on-Linux installation. This document calls out specific differences that you should be aware of.

## Domain names

The fully qualified domain name (FQDN) to use when connecting to the cluster is **&lt;clustername>.azurehdinsight.cn** or (for SSH only) **&lt;clustername-ssh>.azurehdinsight.cn**.


## Remote access to services

* **Ambari (web)** - https://&lt;clustername>.azurehdinsight.cn

	Authenticate by using the cluster administrator user and password, and then log in to Ambari. This also uses the cluster administrator user and password.

	Authentication is plaintext - always use HTTPS to help ensure that the connection is secure.

	> [AZURE.IMPORTANT] While Ambari for your cluster is accessible directly over the Internet, some functionality relies on accessing nodes by the internal domain name used by the cluster. Since this is an internal domain name, and not public, you will receive "server not found" errors when trying to access some features over the Internet.
	>
	> To use the full functionality of the Ambari web UI, use an SSH tunnel to proxy web traffic to the cluster head node. See [Use SSH Tunneling to access Ambari web UI, ResourceManager, JobHistory, NameNode, Oozie, and other web UI's](/documentation/articles/hdinsight-linux-ambari-ssh-tunnel)

* **Ambari (REST)** - https://&lt;clustername>.azurehdinsight.cn/ambari

	> [AZURE.NOTE] Authenticate by using the cluster administrator user and password.
	> 
	> Authentication is plaintext - always use HTTPS to help ensure that the connection is secure.

* **WebHCat (Templeton)** - https://&lt;clustername>.azurehdinsight.cn/templeton

	> [AZURE.NOTE] Authenticate by using the cluster administrator user and password.
	>
	> Authentication is plaintext - always use HTTPS to help ensure that the connection is secure.

* **SSH** - &lt;clustername>-ssh.azurehdinsight.cn on port 22on port 22 or 23. Port 22 is used to connect to headnode0, while 23 is used to connect to headnode1. For more information on the head nodes, see [Availability and reliability of Hadoop clusters in HDInsight](/documentation/articles/hdinsight-high-availability-linux).

	> [AZURE.NOTE] You can only access the cluster head node through SSH from a client machine. Once connected, you can then access the worker nodes by using SSH from the head node.

## File locations

Hadoop-related files can be found on the cluster nodes at `/usr/hdp`. This directory contains the following subdirectories:

* __2.2.4.9-1__: This directory is named for the version of the Hortonworks Data Platform used by HDInsight, so the number on your cluster may be different than the one listed here.
* __current__: This directory contains links to directories under the __2.2.4.9-1__ directory, and exists so that you don't have to type a version number (that might change,) every time you want to access a file.

Example data and JAR files can be found on Hadoop Distributed File System (HDFS) or Azure Blob storage at '/example' or 'wasb:///example'.

## HDFS, Azure Blob storage, and storage best practices

In most Hadoop distributions, HDFS is backed by local storage on the machines in the cluster. While this is efficient, it can be costly for a cloud-based solution where you are charged hourly for compute resources.

HDInsight uses Azure Blob storage as the default store, which provides the following benefits:

* Cheap long-term storage

* Accessibility from external services such as websites, file upload/download utilities, various language SDKs, and web browsers

Since it is the default store for HDInsight, you normally don't have to do anything to use it. For example, the following command will list files in the **/example/data** folder, which is stored on Azure Blob storage:

	hadoop fs -ls /example/data

Some commands may require you to specify that you are using Blob storage. For these, you can prefix the command with **WASB://**.

HDInsight also allows you to associate multiple Blob storage accounts with a cluster. To access data on a non-default Blob storage account, you can use the format **WASB://&lt;container-name>@&lt;account-name>.blob.core.chinacloudapi.cn/**. For example, the following will list the contents of the **/example/data** directory for the specified container and Blob storage account:

	hadoop fs -ls wasb://mycontainer@mystorage.blob.core.chinacloudapi.cn/example/data

### What Blob storage is the cluster using?

During cluster creation, you selected to either use an existing Azure Storage account and container, or create a new one. Then, you probably forgot about it. You can find the default storage account and container by using the Ambari REST API.

1. Use the following command to retrieve HDFS configuration information:

        curl -u admin:PASSWORD -G "https://CLUSTERNAME.azurehdinsight.cn/api/v1/clusters/CLUSTERNAME/configurations/service_config_versions?service_name=HDFS&service_config_version=1"

2. In the JSON data returned, find the `fs.defaultFS` entry. This will contain default container and storage account name in a format similar to the following:

        wasb://CONTAINTERNAME@STORAGEACCOUNTNAME.blob.core.chinacloudapi.cn

> [AZURE.TIP] If you have installed [jq](http://stedolan.github.io/jq/), you can use the following to return just the `fs.defaultFS` entry:
>
> `curl -u admin:PASSWORD -G "https://CLUSTERNAME.azurehdinsight.cn/api/v1/clusters/CLUSTERNAME/configurations/service_config_versions?service_name=HDFS&service_config_version=1" | jq '.items[].configurations[].properties["fs.defaultFS"] | select(. != null)'`

**Azure Management Portal**

1. In the [Azure Management Portal](https://manage.windowsazure.cn/), select your HDInsight cluster.

2. Select **Dashboard** at the top of the page.

3. The Storage account(s) and container(s) are listed in the **linked resources** section of the page.

	![linked resources](./media/hdinsight-hadoop-linux-information/storageportal.png)

### How do I access Blob storage?

Other than through the Hadoop command from the cluster, there are a variety of ways to access blobs:

* [Azure CLI for Mac, Linux and Windows](/documentation/articles/xplat-cli): Command-Line interface commands for working with Azure. After installing, use the `azure storage` command for help on using storage, or `azure blob` for blob-specific commands.

* [blobxfer.py](https://github.com/Azure/azure-batch-samples/tree/master/Python/Storage): A python script for working with blobs in Azure Storage.

* A variety of SDKs:

	* [Java](https://github.com/Azure/azure-sdk-for-java)

	* [Node.js](https://github.com/Azure/azure-sdk-for-node)

	* [PHP](https://github.com/Azure/azure-sdk-for-php)

	* [Python](https://github.com/Azure/azure-sdk-for-python)

	* [Ruby](https://github.com/Azure/azure-sdk-for-ruby)

	* [.NET](https://github.com/Azure/azure-sdk-for-net)

* [Storage REST API](https://msdn.microsoft.com/zh-cn/library/azure/dd135733.aspx)

##<a name="scaling"></a>Scaling your cluster

The cluster scaling feature allows you to change the number of data nodes used by a cluster that is running in Azure HDInsight without having to delete and re-create the cluster.

You can perform scaling operations while other jobs or processes are running on a cluster.

The different cluster types are affected by scaling as follows:

* __Hadoop__: When scaling down the number of nodes in a cluster, some of the services in the cluster are restarted. This can cause jobs running or pending to fail at the completion of the scaling operation. You can resubmit the jobs once the operation is complete.

* __HBase__: Regional servers are automatically balanced within a few minutes after completion of the scaling operation. To manually balance regional servers,use the following steps:

	1. Connect to the HDInsight cluster using SSH. For more information on using SSH with HDInsight, see one of the following documents:

		* [Use SSH with HDInsight from Linux, Unix, and Mac OS X](/documentation/articles/hdinsight-hadoop-linux-use-ssh-unix)

		* [Use SSH with HDInsight from Windows](/documentation/articles/hdinsight-hadoop-linux-use-ssh-windows)

	1. Use the following to start the HBase shell:

			hbase shell

	2. Once the HBase shell has loaded, use the following to manually balance the regional servers:

			balancer

* __Storm__: You should rebalance any running Storm topologies after a scaling operation has been performed. This allows the topology to readjust parallelism settings based on the new number of nodes in the cluster. To rebalance running topologies, use one of the following options:

	* __SSH__: Connect to the server and use the following command to rebalance a topology:

			storm rebalance TOPOLOGYNAME

		You can also specify parameters to override the parallelism hints originally provided by the topology. For example, `storm rebalance mytopology -n 5 -e blue-spout=3 -e yellow-bolt=10` will reconfigure the topology to 5 worker processes, 3 executors for the blue-spout component, and 10 executors for the yellow-bolt component.

	* __Storm UI__: Use the following steps to rebalance a topology using the Storm UI.

		1. [Create an SSH tunnel to the cluster and open the Ambari web UI](/documentation/articles/hdinsight-linux-ambari-ssh-tunnel).

		2. From the list of services on the left of the page, select __Storm__. Then select __Storm UI__ from __Quick Links__.

			![Storm UI entry in quick links](./media/hdinsight-hadoop-linux-information/ambari-storm.png)

			This will display the Storm UI:

			![the storm ui](./media/hdinsight-hadoop-linux-information/storm-ui.png)

		3. Select the topology you wish to rebalance, then select the __Rebalance__ button. Enter the delay before the rebalance operation is performed.

For specific information on scaling your HDInsight cluster, see:

* [Manage Hadoop clusters in HDInsight by using the Azure preview portal](/documentation/articles/hdinsight-administer-use-portal-linux#scaling)

* [Manage Hadoop clusters in HDinsight by using Azure PowerShell](/documentation/articles/hdinsight-administer-use-command-line#scaling)

## How do I install Hue (or other Hadoop component)?

HDInsight is a managed service, which means that nodes in a cluster may be destroyed and reprovisioned automatically by Azure if a problem is detected. Because of this, it is not recommended to manually install components on the cluster nodes.

Instead, use [HDInsight Script Actions](/documentation/articles/hdinsight-hadoop-customize-cluster).

Script Actions are Bash scripts that are ran during cluster provisioning, and can be used to install additional components on the cluster. Example scripts are provided for installing the following components:

* [Hue](/documentation/articles/hdinsight-hadoop-hue-linux)
* [Giraph](/documentation/articles/hdinsight-hadoop-giraph-install-linux)
* [R](/documentation/articles/hdinsight-hadoop-r-scripts-linux)
* [Solr](/documentation/articles/hdinsight-hadoop-solr-install-linux)
* [Spark](/documentation/articles/hdinsight-hadoop-spark-install-linux)

For information on developing your own Script Actions, see [Script Action development with HDInsight](/documentation/articles/hdinsight-hadoop-script-actions-linux).

## Next steps

* [Use Hive with HDInsight](/documentation/articles/hdinsight-use-hive)
* [Use Pig with HDInsight](/documentation/articles/hdinsight-use-pig)
* [Use MapReduce jobs with HDInsight](/documentation/articles/hdinsight-use-mapreduce)

