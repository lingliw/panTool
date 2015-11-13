<!-- not suitable for mooncake-->

<properties 
	pageTitle="Apache Spark Job Server on HDInsight | Azure" 
	description="Learn how to use the Spark Job Server to remotely submit and manage jobs on a Spark cluster." 
	services="hdinsight" 
	documentationCenter="" 
	authors="nitinme" 
	manager="paulettm" 
	editor="cgronlun"/>

<tags 
	ms.service="hdinsight" 
	ms.date="07/10/2015" 
	wacn.date=""/>


# Spark Job Server on Azure HDInsight clusters

Apache Spark cluster on Azure HDInight packages the Spark Job Server as part of the cluster deployment. Spark Job Server provides REST APIs to create Spark context, submit Spark application to context, check job status, kill context, etc. This article provides some examples on how to use Curl to perform some common tasks on a Spark cluster using a Job Server.

>[AZURE.NOTE] For complete documentation for the Spark Job Server, see [https://github.com/spark-jobserver/spark-jobserver](https://github.com/spark-jobserver/spark-jobserver). 

## <a name="uploadjar"></a>Upload a jar to a Spark cluster

	curl.exe -k -u "<hdinsight user>:<user password>" --data-binary @<location of jar on the computer> https://<cluster name>.azurehdinsight.cn/sparkjobserver/jars/<application name>

Example:
	
	curl.exe -k -u "myuser:myPass@word1" --data-binary @C:\mylocation\eventhubs-examples\target\spark-streaming-eventhubs-example-0.1.0-jar-with-dependencies.jar https://mysparkcluster.azurehdinsight.cn/sparkjobserver/jars/streamingjar


##<a name="createcontext"></a>Create new persistent context in job server

	curl.exe -k -u "<hdinsight user>:<user password>" -d "" "https://<cluster name>.azurehdinsight.cn/sparkjobserver/contexts/<context name>?num-cpu-cores=<value>&memory-per-node=<value>"

Example:

	curl.exe -k -u "myuser:myPass@word1" -d "" "https://mysparkcluster.azurehdinsight.cn/sparkjobserver/contexts/mystreaming?num-cpu-cores=4&memory-per-node=1024m"


##<a name="submitapp"></a>Submit an application to the cluster

	curl.exe -k -u "<hdinsight user>:<user password>" -d @<input file name> "https://<cluster name>.azurehdinsight.cn/sparkjobserver/jobs?appName=<app name>&classPath=<class path>&context=<context>"

Example:

	curl.exe -k -u "myuser:myPass@word1" -d @mypostdata.txt "https://mysparkcluster.azurehdinsight.cn/sparkjobserver/jobs?appName=streamingjar&classPath=org.apache.spark.streaming.eventhubs.example.EventCountJobServer&context=mystreaming"

where mypostdata.txt defines your application.


##<a name="submitapp"></a>Delete a job

	curl.exe -X DELETE -k -u "<hdinsight user>:<user password>" "https://<cluster name>.azurehdinsight.cn/sparkjobserver/contexts/<context>"

Example:

	curl.exe -X DELETE -k -u "myuser:myPass@word1" "https://mysparkcluster.azurehdinsight.cn/sparkjobserver/contexts/mystreaming"


##<a name="seealso"></a>See also

* [Overview: Apache Spark on Azure HDInsight](/documentation/articles/hdinsight-apache-spark-overview)
* [Provision a Spark on HDInsight cluster](/documentation/articles/hdinsight-apache-spark-provision-clusters)
* [Perform interactive data analysis using Spark in HDInsight with BI tools](/documentation/articles/hdinsight-apache-spark-use-bi-tools)
* [Use Spark in HDInsight for building machine learning applications](/documentation/articles/hdinsight-apache-spark-ipython-notebook-machine-learning)
* [Use Spark in HDInsight for building real-time streaming applications](/documentation/articles/hdinsight-apache-spark-csharp-apache-zeppelin-eventhub-streaming)
* [Manage resources for the Apache Spark cluster in Azure HDInsight](/documentation/articles/hdinsight-apache-spark-resource-manager)


[hdinsight-versions]: /documentation/articles/hdinsight-component-versioning
[hdinsight-upload-data]: /documentation/articles/hdinsight-upload-data
[hdinsight-storage]: /documentation/articles/hdinsight-use-blob-storage
[azure-purchase-options]: http://www.windowsazure.cn/pricing/overview/
[azure-trial]: http://www.windowsazure.cn/pricing/1rmb-trial/
[azure-management-portal]: https://manage.windowsazure.cn/
[azure-create-storageaccount]: /documentation/articles/storage-create-storage-account
