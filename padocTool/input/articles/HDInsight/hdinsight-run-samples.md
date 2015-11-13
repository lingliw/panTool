<properties
	pageTitle="Run the Hadoop samples in HDInsight | Windows Azure"
	description="Get started using the Azure HDInsight service with the samples provided. Use PowerShell scripts that run MapReduce programs on data clusters."
	services="hdinsight"
	documentationCenter=""
	tags="azure-portal"
	authors="mumian"
	manager="paulettm"
	editor="cgronlun"/>

<tags
	ms.service="hdinsight"
	ms.date="10/15/2015"
	wacn.date=""/>

#Run the Hadoop samples in HDInsight

[AZURE.INCLUDE [samples-selector](../includes/hdinsight-run-samples-selector.md)]

A set of samples are provided to help you get started running MapReduce jobs on Hadoop clusters using Azure HDInsight. These samples are made available on each of the HDInsight managed clusters that you create. Running these samples will familiarize you with using Azure PowerShell cmdlets to run jobs on Hadoop clusters.

MapReduce programs can also be run programmatically from an application by using the Microsoft .NET API for HDInsight. For more information about using the HDInsight APIs for job submission, see [Submit Hadoop Jobs in HDInsight] [hdinsight-submit-jobs].

Much additional documentation exists on the web for Hadoop-related technologies, such as Java-based MapReduce programming and streaming, and documentation about the cmdlets that are used in Windows PowerShell scripting. For more information about these resources, see the final **Resources for HDInsight** section of [Introduction to Azure HDInsight][hdinsight-introduction].

**What these samples are**

<p>These samples are intended to get you up to speed quickly on how to deploy Hadoop jobs and to provide you with an extensible testing bed to work with the concepts and scripting procedures that are used by the service. They provide you with examples of common tasks, such as creating and importing data sets of various sizes, running and composing jobs sequentially, and examining the results of your jobs. The data sets that you use can be varied in size, which allows you to observe the effects that data sets of various size have on job performance.</p>


**Prerequisites**:

- **An Azure subscription**. See [Get Azure trial](/pricing/1rmb-trial/).
- **an HDInsight cluster**. For instructions on the various ways in which such clusters can be created, see [Provision HDInsight Clusters](/documentation/articles/hdinsight-provision-clusters).
- **A workstation with Azure PowerShell**. See [Install and use Azure PowerShell](/documentation/articles/install-configure-powershell).



## The samples ##

HDInsight ships with the following samples:

- [**The pi estimator Hadoop sample**][hdinsight-sample-pi-estimator]: Shows how to run a MapReduce program with HDInsight that uses a statistical (quasi-Monte Carlo) method to estimate the value of pi.
- [**Run a MapReduce word count example on an Hadoop cluster**][hdinsight-sample-wordcount]: Shows how to use an HDInsight cluster to run a MapReduce program that counts word occurrences in a text file.
- [**The 10-GB Graysort Hadoop sample**][hdinsight-sample-10gb-graysort]: Shows how to run a general purpose GraySort on a 10 GB file by using HDInsight. There are three jobs to run: Teragen to generate the data, Terasort to sort the data, and Teravalidate to confirm that the data has been properly sorted.
- [**The C# streaming wordcount MapReduce sample in Hadoop**][hdinsight-sample-csharp-streaming]: Shows how to use C# to write a MapReduce program that uses the Hadoop streaming interface.


## How to run the samples ##

The samples can be run by using Azure PowerShell. Instructions about how to do this are provided for each of the previous samples.

##Next steps ##

From this article and the articles in each of the samples, you learned how to run the samples included with the HDInsight clusters by using Azure PowerShell. For tutorials about using Pig, Hive, and MapReduce with HDInsight, see the following topics:

* [Get started using Hadoop with Hive in HDInsight to analyze mobile handset use][hdinsight-get-started]
* [Use Pig with Hadoop on HDInsight][hdinsight-use-pig]
* [Use Hive with Hadoop on HDInsight][hdinsight-use-hive]
* [Submit Hadoop Jobs in HDInsight] [hdinsight-submit-jobs]
* [Azure HDInsight SDK documentation][hdinsight-sdk-documentation]
* [Debug Hadoop in HDInsight: Error messages] [hdinsight-errors]


[hdinsight-errors]: /documentation/articles/hdinsight-debug-jobs
[hdinsight-sdk-documentation]: https://msdn.microsoft.com/zh-cn/library/azure/dn479185.aspx

[hdinsight-submit-jobs]: /documentation/articles/hdinsight-submit-hadoop-jobs-programmatically
[hdinsight-introduction]: /documentation/articles/hdinsight-hadoop-introduction
[powershell-install-configure]: /documentation/articles/install-configure-powershell
[hdinsight-get-started]: /documentation/articles/hdinsight-get-started
[hdinsight-samples]: /documentation/articles/hdinsight-run-samples
[hdinsight-sample-10gb-graysort]: /documentation/articles/hdinsight-sample-10gb-graysort
[hdinsight-sample-csharp-streaming]: /documentation/articles/hdinsight-sample-csharp-streaming
[hdinsight-sample-pi-estimator]: /documentation/articles/hdinsight-sample-pi-estimator
[hdinsight-sample-wordcount]: /documentation/articles/hdinsight-sample-wordcount
[hdinsight-use-hive]: /documentation/articles/hdinsight-use-hive
[hdinsight-use-pig]: /documentation/articles/hdinsight-use-pig