<properties
	pageTitle="What is Hadoop in the cloud? Introduction to HDInsight | Azure"
	description="What is Hadoop in the cloud and how is it managed in Azure HDInsight? An introduction to Hadoop components and big data analysis."
	keywords="big data analysis,introduction to hadoop,what is hadoop,hadoop in the cloud,hadoop technology stack,hadoop ecosystem"
	services="hdinsight"
	documentationCenter=""
	authors="cjgronlund"
	manager="paulettm"
	editor="cgronlun"/>

<tags
	ms.service="hdinsight"
	ms.date="07/21/2016"
	wacn.date=""/>


# What is Hadoop in the cloud? An introduction to the Hadoop ecosystem in HDInsight

Get an introduction to Hadoop, its ecosystem, and big data in Azure HDInsight: What is Hadoop in HDInsight and what are the Hadoop components, common terminology, and scenarios for big data analysis? Also, learn about Hadoop tutorials, documentation, and resources for using Hadoop the cloud in HDInsight.

## What is Hadoop in HDInsight?

Azure HDInsight uses the **Hortonworks Data Platform (HDP)** Hadoop distribution. HDInsight deploys and provisions managed Apache Hadoop clusters in the cloud, providing a software framework designed to process, analyze, and report on big data with high reliability and availability.

Hadoop often refers to the entire Hadoop ecosystem of components, which includes Apache HBase and Apache Storm, as well as other technologies under the Hadoop umbrella. See [Overview of the Hadoop ecosystem in HDInsight](#overview) below for details.

## What is big data?

Big data describes any large body of digital information, from the text in a Twitter feed, to the sensor information from industrial equipment, to information about customer browsing and purchases on a website. Big data can be historical (meaning stored data) or real-time (meaning streamed directly from the source). Big data is being collected in ever-escalating volumes, at increasingly higher velocities, and in an expanding variety formats.

For big data to provide actionable intelligence or insight, not only must you collect relevant data and ask the right questions, but also the data must be accessible, cleaned, analyzed, and then presented in a useful way. That's where big data analysis on Hadoop in HDInsight can help.

## <a name="overview"></a>Overview of the Hadoop ecosystem in HDInsight

HDInsight is a cloud implementation on Azure of the rapidly expanding Apache Hadoop technology stack that is the go-to solution for big data analysis. It includes implementations of Apache HBase, Storm, Pig, Hive, Sqoop, Oozie, and so on. HDInsight also integrates with business intelligence (BI) tools such as Power BI, Excel, SQL Server Analysis Services, and SQL Server Reporting Services.

### Hadoop, HBase, Storm, and customized clusters

HDInsight provides cluster configurations for Apache Hadoop, HBase, or Storm. Or, you can [customize clusters with script actions](/documentation/articles/hdinsight-hadoop-customize-cluster-v1/).

* **Hadoop** (the "Query" workload): Provides reliable data storage with [HDFS](#hdfs), and a simple [MapReduce](#mapreduce) programming model to process and analyze data in parallel.

* **<a target="_blank" href="http://hbase.apache.org/">HBase</a>** (the "NoSQL" workload): A NoSQL database built on Hadoop that provides random access and strong consistency for large amounts of unstructured and semi-structured data - potentially billions of rows times millions of columns. See [Overview of HBase on HDInsight](/documentation/articles/hdinsight-hbase-overview/).

* **<a  target="_blank" href="https://storm.incubator.apache.org/">Apache Storm</a>** (the "Stream" workload): A distributed, real-time computation system for processing large streams of data fast. Storm is offered as a managed cluster in HDInsight. See [Analyze real-time sensor data using Storm and Hadoop](/documentation/articles/hdinsight-storm-sensor-data-analysis/).

### Example customization scripts

Script Actions are scripts that run during cluster provisioning, and can be used to install additional components on the cluster. These are Bash scripts.

The following example scripts are provided by the HDInsight team:

* [Giraph](/documentation/articles/hdinsight-hadoop-giraph-install-v1/): Graph processing to model relationships between things or people.

* [R](/documentation/articles/hdinsight-hadoop-r-scripts/): An open-source language and environment for statistical computing used in machine learning.

* [Solr](/documentation/articles/hdinsight-hadoop-solr-install-v1/): An enterprise-scale search platform that allows full-text search on data.

For information on developing your own Script Actions, see [Script Action development with HDInsight](/documentation/articles/hdinsight-hadoop-script-actions/).


## What are the Hadoop components and utilties?

The following components and utilities are included on HDInsight clusters.

* **[Avro](#avro)** (Microsoft .NET Library for Avro): Data serialization for the Microsoft .NET environment.

* **[Hive & HCatalog](#hive)**: Structured Query Language (SQL)-like querying, and a table and storage management layer.

* **[Mahout](#mahout)**: Machine learning.

* **[MapReduce](#mapreduce)**: Legacy framework for Hadoop distributed processing and resource management. See [YARN](#yarn), the next-generation resource framework.

* **[Oozie](#oozie)**: Workflow management.

* **[Phoenix](#phoenix)**: Relational database layer over HBase.

* **[Pig](#pig)**: Simpler scripting for MapReduce transformations.

* **[Sqoop](#sqoop)**: Data import and export.

* **[Tez](#tez)**: Allows data-intensive processes to run efficiently at scale.

* **[YARN](#yarn)**: Part of the Hadoop core library and next generation of the MapReduce software framework.

* **[ZooKeeper](#zookeeper)**: Coordination of processes in distributed systems.

> [AZURE.NOTE] For information on the specific components and version information, see [Hadoop components, versioning, and service offerings in HDInsight][component-versioning]

### <a name="avro"></a>Avro (Microsoft .NET Library for Avro)

The Microsoft .NET Library for Avro implements the Apache Avro compact binary data interchange format for serialization for the Microsoft .NET environment. It uses <a target="_blank" href="http://www.json.org/">JavaScript Object Notation (JSON)</a> to define a language-agnostic schema that underwrites language interoperability, meaning data serialized in one language can be read in another. Detailed information on the format can be found in the <a target=_"blank" href="http://avro.apache.org/docs/current/spec.html">Apache Avro Specification</a>.
The format of Avro files supports the distributed MapReduce programming model. Files are "splittable", meaning you can seek any point in a file and start reading from a particular block. To find out how, see [Serialize data with the Microsoft .NET Library for Avro](/documentation/articles/hdinsight-dotnet-avro-serialization/).


### <a name="HDFS"></a>HDFS

Hadoop Distributed File System (HDFS) is a distributed file system that, with MapReduce and YARN, is the core of the Hadoop ecosystem. HDFS is the standard file system for Hadoop clusters on HDInsight.

### <a name="hive"></a>Hive & HCatalog

<a target="_blank" href="http://hive.apache.org/">Apache Hive</a> is data warehouse software built on Hadoop that allows you to query and manage large datasets in distributed storage by using a SQL-like language called HiveQL. Hive, like Pig, is an abstraction on top of MapReduce. When run, Hive translates queries into a series of MapReduce jobs. Hive is conceptually closer to a relational database management system than Pig, and is therefore appropriate for use with more structured data. For unstructured data, Pig is the better choice. See [Use Hive with Hadoop in HDInsight](/documentation/articles/hdinsight-use-hive/).

<a target="_blank" href="https://cwiki.apache.org/confluence/display/Hive/HCatalog/">Apache HCatalog</a> is a table and storage management layer for Hadoop that presents users with a relational view of data. In HCatalog, you can read and write files in any format for which a Hive SerDe (serializer-deserializer) can be written.

### <a name="mahout"></a>Mahout

<a target="_blank" href="https://mahout.apache.org/">Apache Mahout</a> is a scalable library of machine learning algorithms that run on Hadoop. Using principles of statistics, machine learning applications teach systems to learn from data and to use past outcomes to determine future behavior. See [Generate movie recommendations using Mahout on Hadoop](/documentation/articles/hdinsight-mahout/).

### <a name="mapreduce"></a>MapReduce
MapReduce is the legacy software framework for Hadoop for writing applications to batch process big data sets in parallel. A MapReduce job splits large datasets and organizes the data into key-value pairs for processing.

[YARN](#yarn) is the Hadoop next-generation resource manager and application framework, and is referred to as MapReduce 2.0. MapReduce jobs will run on YARN.

For more information on MapReduce, see <a target="_blank" href="http://wiki.apache.org/hadoop/MapReduce">MapReduce</a> in the Hadoop Wiki.

### <a name="oozie"></a>Oozie
<a target="_blank" href="http://oozie.apache.org/">Apache Oozie</a> is a workflow coordination system that manages Hadoop jobs. It is integrated with the Hadoop stack and supports Hadoop jobs for MapReduce, Pig, Hive, and Sqoop. It can also be used to schedule jobs specific to a system, like Java programs or shell scripts. See [Use Oozie with Hadoop](/documentation/articles/hdinsight-use-oozie/).

### <a name="phoenix"></a>Phoenix
<a  target="_blank" href="http://phoenix.apache.org/">Apache Phoenix</a> is a relational database layer over HBase. Phoenix includes a JDBC driver that allows users to query and manage SQL tables directly. Phoenix translates queries and other statements into native NoSQL API calls - instead of using MapReduce - thus enabling faster applications on top of NoSQL stores. See [Use Apache Phoenix and SQuirreL with HBase clusters](/documentation/articles/hdinsight-hbase-phoenix-squirrel/).


### <a name="pig"></a>Pig
<a  target="_blank" href="http://pig.apache.org/">Apache Pig</a> is a high-level platform that allows you to perform complex MapReduce transformations on very large datasets by using a simple scripting language called Pig Latin. Pig translates the Pig Latin scripts so they'll run within Hadoop. You can create User Defined Functions (UDFs) to extend Pig Latin. See [Use Pig with Hadoop](/documentation/articles/hdinsight-use-pig/).

### <a name="sqoop"></a>Sqoop
<a  target="_blank" href="http://sqoop.apache.org/">Apache Sqoop</a> is tool that transfers bulk data between Hadoop and relational databases such a SQL, or other structured data stores, as efficiently as possible. See [Use Sqoop with Hadoop](/documentation/articles/hdinsight-use-sqoop/).

### <a name="tez"></a>Tez
<a  target="_blank" href="http://tez.apache.org/">Apache Tez</a> is an application framework built on Hadoop YARN that executes complex, acyclic graphs of general data processing. It's a more flexible and powerful successor to the MapReduce framework that allows data-intensive processes, such as Hive, to run more efficiently at scale. See ["Use Apache Tez for improved performance" in Use Hive and HiveQL](/documentation/articles/hdinsight-use-hive/#usetez).

### <a name="yarn"></a>YARN
Apache YARN is the next generation of MapReduce (MapReduce 2.0, or MRv2) and supports data processing scenarios beyond MapReduce batch processing with greater scalability and real-time processing. YARN provides resource management and a distributed application framework. MapReduce jobs will run on YARN.

To learn about YARN, see <a target="_blank" href="http://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html">Apache Hadoop NextGen MapReduce (YARN)</a>.


### <a name="zookeeper"></a>ZooKeeper
<a  target="_blank" href="http://zookeeper.apache.org/">Apache ZooKeeper</a> coordinates processes in large distributed systems by means of a shared hierarchical namespace of data registers (znodes). Znodes contain small amounts of meta information needed to coordinate processes: status, location, configuration, and so on.

## Programming languages on HDInsight

HDInsight clusters--Hadoop, HBase, and Storm clusters--support a number of programming languages, but some aren't installed by default. For libraries, modules, or packages not installed by default, use a script action to install the component. See [Script action development with HDInsight](/documentation/articles/hdinsight-hadoop-script-actions/).

### Default programming language support

By default, HDInsight clusters support:

* Java

* Python

Additional languages can be installed using script actions: [Script action development with HDInsight](/documentation/articles/hdinsight-hadoop-script-actions/).

### Java virtual machine (JVM) languages

Many languages other than Java can be run using a Java virtual machine (JVM); however, running some of these languages may require additional components installed on the cluster.

These JVM-based languages are supported on HDInsight clusters:

* Clojure

* Jython (Python for Java)

* Scala

### Hadoop-specific languages

HDInsight clusters provide support for the following languages that are specific to the Hadoop ecosystem:

* Pig Latin for Pig jobs

* HiveQL for Hive jobs


## <a name="advantage"></a>Advantages of Hadoop in the cloud

As part of the Azure cloud ecosystem, Hadoop in HDInsight offers a number of benefits, among them:

* Automatic provisioning of Hadoop clusters. HDInsight clusters are much easier to create than manually configuring Hadoop clusters. For details, see [Provision Hadoop clusters in HDInsight](/documentation/articles/hdinsight-provision-clusters-v1/).

* State-of-the-art Hadoop components. For details, see [Hadoop components, versioning, and service offerings in HDInsight][component-versioning].

* High availability and reliability of clusters. See [Availability and reliability of Hadoop clusters in HDInsight](/documentation/articles/hdinsight-high-availability/) for details.

* Efficient and economical data storage with Azure Blob storage, a Hadoop-compatible option. See [Use Azure Blob storage with Hadoop in HDInsight](/documentation/articles/hdinsight-hadoop-use-blob-storage/) for details.

* Integration with other Azure services, including [Web apps](/documentation/services/web-sites/) and [SQL Database](/documentation/services/sql-databases/).

* Additional VM sizes and types for running HDInsight clusters. See [Hadoop components, versioning, and service offerings in HDInsight][component-versioning] for details.

* Cluster scaling. Cluster scaling enables you to change the number of nodes of a running HDInsight cluster without having to delete or re-create it.

* Virtual Network support. HDInsight clusters can be used with Azure Virtual Network to support isolation of cloud resources or hybrid scenarios that link cloud resources with those in your datacenter.

* Low entry cost. Start a [trial](/pricing/1rmb-trial/), or consult [HDInsight pricing details](/pricing/details/hdinsight/).

To read more about the advantages on Hadoop in HDInsight, see the  [Azure features page for HDInsight][marketing-page].



## <a id="resources"></a>Resources for learning more about big-data analysis, Hadoop, and HDInsight

Build on this introduction to Hadoop in the cloud and big data analysis with the resources below.


### Hadoop documentation for HDInsight

* [HDInsight documentation](/documentation/services/hdinsight/): The documentation page for Hadoop on Azure HDInsight with links to articles, videos, and more resources.

* [Get started with Hadoop in HDInsight](/documentation/articles/hdinsight-hadoop-tutorial-get-started-windows-v1/): A quick-start tutorial for provisioning HDInsight Hadoop clusters and running sample Hive queries.

* [Provision HDInsight clusters](/documentation/articles/hdinsight-provision-clusters-v1/): Learn how to provision an HDInsight Hadoop cluster through the Azure Portal, Azure CLI, or Azure PowerShell.


### Apache Hadoop

* <a target="_blank" href="http://hadoop.apache.org/">Apache Hadoop</a>: Learn more about the Apache Hadoop software library, a framework that allows for the distributed processing of large datasets across clusters of computers.

* <a target="_blank" href="http://hadoop.apache.org/docs/r1.0.4/hdfs_design.html">HDFS</a>: Learn more about the architecture and design of the Hadoop Distributed File System, the primary storage system used by Hadoop applications.

* <a target="_blank" href="http://hadoop.apache.org/docs/r1.2.1/mapred_tutorial.html">MapReduce Tutorial</a>: Learn more about the programming framework for writing Hadoop applications that rapidly process large amounts of data in parallel on large clusters of compute nodes.


### Microsoft business intelligence

Familiar business intelligence (BI) tools - such as Excel, PowerPivot, SQL Server Analysis Services, and SQL Server Reporting Services - retrieve, analyze, and report data integrated with HDInsight by using either the Power Query add-in or the Microsoft Hive ODBC Driver.

These BI tools can help in your big-data analysis:

* [Connect Excel to Hadoop with Power Query](/documentation/articles/hdinsight-connect-excel-power-query/): Learn how to connect Excel to the Azure Storage account that stores the data associated with your HDInsight cluster by using Microsoft Power Query for Excel. Windows workstation required. Works with Windows-based cluster.

* [Connect Excel to Hadoop with the Microsoft Hive ODBC Driver](/documentation/articles/hdinsight-connect-excel-hive-ODBC-driver/): Learn how to import data from HDInsight with the Microsoft Hive ODBC Driver. Windows workstation required. Works with Windows-based cluster.

* [SQL Server Reporting Services](http://msdn.microsoft.com/zh-cn/library/ms159106.aspx).




[marketing-page]: https://azure.microsoft.com/services/hdinsight/
[component-versioning]: /documentation/articles/hdinsight-component-versioning-v1/
[zookeeper]: http://zookeeper.apache.org/
