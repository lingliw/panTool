<properties
   pageTitle="Use Hadoop Sqoop with Curl in HDInsight | Azure"
   description="Learn how to remotely submit Sqoop jobs to HDInsight using Curl."
   services="hdinsight"
   documentationCenter=""
   authors="mumian"
   manager="paulettm"
   editor="cgronlun"
	tags="azure-portal"/>

<tags
	ms.service="hdinsight"
	ms.date="05/27/2016"
	wacn.date=""/>

#Run Sqoop jobs with Hadoop in HDInsight with Curl

> [AZURE.SELECTOR]
- [Overview](/documentation/articles/hdinsight-use-sqoop/)
- [Curl](/documentation/articles/hdinsight-hadoop-use-sqoop-curl/)
- [PowerShell](/documentation/articles/hdinsight-hadoop-use-sqoop-powershell/)
- [.NET](/documentation/articles/hdinsight-hadoop-use-sqoop-dotnet-sdk/)


In this document, you will learn how to use Curl to run Sqoop jobs on a Hadoop on Azure HDInsight cluster.

Curl is used to demonstrate how you can interact with HDInsight by using raw HTTP requests to run, monitor, and retrieve the results of Sqoop jobs. This works by using the WebHCat REST API (formerly known as Templeton) provided by your HDInsight cluster.

##Prerequisites

To complete the steps in this article, you will need the following:

* A Hadoop on HDInsight cluster (Windows-based)

* [Curl](http://curl.haxx.se/)

* [jq](http://stedolan.github.io/jq/)

##Submit Sqoop jobs by using Curl

> [AZURE.NOTE] When using Curl or any other REST communication with WebHCat, you must authenticate the requests by providing the user name and password for the HDInsight cluster administrator. You must also use the cluster name as part of the Uniform Resource Identifier (URI) used to send the requests to the server.
><p> For the commands in this section, replace **USERNAME** with the user to authenticate to the cluster, and replace **PASSWORD** with the password for the user account. Replace **CLUSTERNAME** with the name of your cluster.
><p> The REST API is secured via [basic authentication](http://en.wikipedia.org/wiki/Basic_access_authentication). You should always make requests by using Secure HTTP (HTTPS) to help ensure that your credentials are securely sent to the server.

1. From a command line, use the following command to verify that you can connect to your HDInsight cluster:

        curl -u USERNAME:PASSWORD -G https://CLUSTERNAME.azurehdinsight.cn/templeton/v1/status

    You should receive a response similar to the following:

        {"status":"ok","version":"v1"}

    The parameters used in this command are as follows:

    * **-u** - The user name and password used to authenticate the request.
    * **-G** - Indicates that this is a GET request.

    The beginning of the URL, **https://CLUSTERNAME.azurehdinsight.cn/templeton/v1**, will be the same for all requests. The path, **/status**, indicates that the request is to return a status of WebHCat (also known as Templeton) for the server. 

2. Use the following to submit a sqoop job:


        curl -u USERNAME:PASSWORD -d user.name=USERNAME -d command="export --connect jdbc:sqlserver://SQLDATABASESERVERNAME.database.chinacloudapi.cn;user=USERNAME@SQLDATABASESERVERNAME;password=PASSWORD;database=SQLDATABASENAME --table log4jlogs --export-dir /tutorials/usesqoop/data --input-fields-terminated-by \0x20 -m 1" -d statusdir="wasb:///example/curl" https://CLUSTERNAME.azurehdinsight.cn/templeton/v1/sqoop

    The parameters used in this command are as follows:

    * **-d** - Since `-G` is not used, the request defaults to the POST method. `-d` specifies the data values that are sent with the request.

        * **user.name** - The user that is running the command.

        * **command** - The Sqoop command to execute.

        * **statusdir** - The directory that the status for this job will be written to.

    This command should return a job ID that can be used to check the status of the job.

        {"id":"job_1415651640909_0026"}

3. To check the status of the job, use the following command. Replace **JOBID** with the value returned in the previous step. For example, if the return value was `{"id":"job_1415651640909_0026"}`, then **JOBID** would be `job_1415651640909_0026`.

        curl -G -u USERNAME:PASSWORD -d user.name=USERNAME https://CLUSTERNAME.azurehdinsight.cn/templeton/v1/jobs/JOBID | jq .status.state

	If the job has finished, the state will be **SUCCEEDED**.

    > [AZURE.NOTE] This Curl request returns a JavaScript Object Notation (JSON) document with information about the job; jq is used to retrieve only the state value.

4. Once the state of the job has changed to **SUCCEEDED**, you can retrieve the results of the job from Azure Blob storage. The `statusdir` parameter passed with the query contains the location of the output file; in this case, **wasb:///example/curl**. This address stores the output of the job in the **example/curl** directory on the default storage container used by your HDInsight cluster.

    You can list and download these files by using the [Azure CLI](/documentation/articles/xplat-cli-install/). For example, to list files in **example/curl**, use the following command:

		azure storage blob list <container-name> example/curl

	To download a file, use the following:

		azure storage blob download <container-name> <blob-name> <destination-file>

	> [AZURE.NOTE] You must either specify the storage account name that contains the blob by using the `-a` and `-k` parameters, or set the **AZURE\_STORAGE\_ACCOUNT** and **AZURE\_STORAGE\_ACCESS\_KEY** environment variables. See <a href="/documentation/articles/hdinsight-upload-data/" target="_blank" for more information.


##Summary

As demonstrated in this document, you can use a raw HTTP request to run, monitor, and view the results of Sqoop jobs on your HDInsight cluster.

For more information on the REST interface used in this article, see the <a href="https://sqoop.apache.org/docs/1.99.3/RESTAPI.html" target="_blank">Sqoop REST API guide</a>.

##Next steps

For general information on Hive with HDInsight:

* [Use Sqoop with Hadoop on HDInsight](/documentation/articles/hdinsight-use-sqoop/)

For information on other ways you can work with Hadoop on HDInsight:

* [Use Hive with Hadoop on HDInsight](/documentation/articles/hdinsight-use-hive/)

* [Use Pig with Hadoop on HDInsight](/documentation/articles/hdinsight-use-pig/)

* [Use MapReduce with Hadoop on HDInsight](/documentation/articles/hdinsight-use-mapreduce/)

[hdinsight-sdk-documentation]: http://msdn.microsoft.com/zh-cn/library/dn479185.aspx

[azure-purchase-options]: /pricing/overview/
[azure-member-offers]: /pricing/member-offers/
[azure-trial]: /pricing/1rmb-trial/

[apache-tez]: http://tez.apache.org
[apache-hive]: http://hive.apache.org/
[apache-log4j]: http://zh.wikipedia.org/wiki/Log4j
[hive-on-tez-wiki]: https://cwiki.apache.org/confluence/display/Hive/Hive+on+Tez
[import-to-excel]: /documentation/articles/hdinsight-connect-excel-power-query/


[hdinsight-use-oozie]: /documentation/articles/hdinsight-use-oozie/
[hdinsight-analyze-flight-data]: /documentation/articles/hdinsight-analyze-flight-delay-data/




[hdinsight-provision]: /documentation/articles/hdinsight-provision-clusters-v1/
[hdinsight-submit-jobs]: /documentation/articles/hdinsight-submit-hadoop-jobs-programmatically/
[hdinsight-upload-data]: /documentation/articles/hdinsight-upload-data/

[powershell-here-strings]: http://technet.microsoft.com/zh-cn/library/ee692792.aspx


