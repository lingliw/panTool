<properties
	pageTitle="Use Python with Hive and Pig in HDInsight | Azure"
	description="Learn how to use Python User Defined Functions (UDF) from Hive and Pig in HDInsight, the Hadoop technology stack on Azure."
	services="hdinsight"
	documentationCenter=""
	authors="Blackmist"
	manager="jhubbard"
	editor="cgronlun"
	tags="azure-portal"/>

<tags
	ms.service="hdinsight"
	ms.workload="big-data"
	ms.tgt_pltfrm="na"
	ms.devlang="python"
	ms.topic="article"
	ms.date="09/07/2016"
	wacn.date="" 
	ms.author="larryfr"/>

#Use Python with Hive and Pig in HDInsight

Hive and Pig are great for working with data in HDInsight, but sometimes you need a more general purpose language. Both Hive and Pig allow you to create User Defined Functions (UDF) using a variety of programming languages. In this article, you will learn how to use a Python UDF from Hive and Pig.

##Requirements

* An HDInsight cluster (Windows-based)

* A text editor
 
##<a name="python"></a>Python on HDInsight

Python2.7 is installed by default on HDInsight 3.0 and later clusters. Hive can be used with this version of Python for stream processing (data is passed between Hive and Python using STDOUT/STDIN).

HDInsight also includes Jython, which is a Python implementation written in Java. Pig understands how to talk to Jython without having to resort to streaming, so it's preferable when using Pig. However, you can also use normal Python (C Python,) with Pig as well.

##<a name="hivepython"></a>Hive and Python

Python can be used as a UDF from Hive through the HiveQL **TRANSFORM** statement. For example, the following HiveQL invokes a Python script stored in the **streaming.py** file.

**Windows-based HDInsight**

	add file wasbs:///streaming.py;

	SELECT TRANSFORM (clientid, devicemake, devicemodel)
	  USING 'D:\Python27\python.exe streaming.py' AS
	  (clientid string, phoneLable string, phoneHash string)
	FROM hivesampletable
	ORDER BY clientid LIMIT 50;

> [AZURE.NOTE] On Windows-based HDInsight clusters, the **USING** clause must specify the full path to python.exe. This is always `D:\Python27\python.exe`.

Here's what this example does:

1. The **add file** statement at the beginning of the file adds the **streaming.py** file to the distributed cache, so it's accessible by all nodes in the cluster.

2. The  **SELECT TRANSFORM ... USING** statement selects data from the **hivesampletable**, and passes clientid, devicemake, and devicemodel to the **streaming.py** script.

3. The **AS** clause describes the fields returned from **streaming.py**

<a name="streamingpy"></a>
Here's the **streaming.py** file used by the HiveQL example.

	#!/usr/bin/env python

	import sys
	import string
	import hashlib

	while True:
	  line = sys.stdin.readline()
	  if not line:
	    break

	  line = string.strip(line, "\n ")
	  clientid, devicemake, devicemodel = string.split(line, "\t")
	  phone_label = devicemake + ' ' + devicemodel
	  print "\t".join([clientid, phone_label, hashlib.md5(phone_label).hexdigest()])

Since we are using streaming, this script has to do the following:

1. Read data from STDIN. This is accomplished by using `sys.stdin.readline()` in this example.

2. The trailing newline character is removed using `string.strip(line, "\n ")`, since we just want the text data and not the end of line indicator.

2. When doing stream processing, a single line contains all the values with a tab character between each value. So `string.split(line, "\t")` can be used to split the input at each tab, returning just the fields.

3. When processing is complete, the output must be written to STDOUT as a single line, with a tab between each field. This is accomplished by using `print "\t".join([clientid, phone_label, hashlib.md5(phone_label).hexdigest()])`.

4. This all occurs within a `while` loop, that will repeat until no `line` is read, at which point `break` exits the loop and the script terminates.

Beyond that, the script just concatenates the input values for `devicemake` and `devicemodel`, and calculates a hash of the concatenated value. Pretty simple, but it describes the basics of how any Python script invoked from Hive should function: Loop, read input until there is no more, break each line of input apart at the tabs, process, write a single line of tab delimited output.

See [Running the examples](#running) for how to run this example on your HDInsight cluster.

##<a name="pigpython"></a>Pig and Python

A Python script can be used as a UDF from Pig through the **GENERATE** statement. There's two ways to accomplish this; using Jython (Python implemented on the Java Virtual Machine,) and C Python (regular Python). 

The primary difference between these are that Jython runs on the JVM and can natively be called from Pig (also running on the JVM.) C Python is an external process (written in C.) So the data from Pig on the JVM is sent out to the script running in a Python process, then the output of that is sent back into Pig.

To determine whether Pig uses Jython or C Python to run the script, use __register__ when referencing the Python script from Pig Latin. This tells Pig which interpreter to use and what alias to create for the script. The following examples register scripts with Pig as __myfuncs__:

* __To use Jython__: `register '/path/to/pig_python.py' using jython as myfuncs;`
* __To use C Python__: `register '/path/to/pig_python.py' using streaming_python as myfuncs;`

> [AZURE.IMPORTANT] When using Jython, the path to the pig_jython file can be either a local path or a WASB:// path. However, when using C Python, you must reference a file on the local file system of the node that you are using to submit the Pig job.

Once past registration, the Pig Latin for this example is the same for both:

    LOGS = LOAD 'wasbs:///example/data/sample.log' as (LINE:chararray);
    LOG = FILTER LOGS by LINE is not null;
    DETAILS = FOREACH LOG GENERATE myfuncs.create_structure(LINE);
    DUMP DETAILS;

Here's what this example does:

1. The first line loads the sample data file, **sample.log** into **LOGS**. Since this log file doesn't have a consistent schema, it also defines each record (**LINE** in this case,) as a **chararray**. Chararray is, essentially, a string.

2. The next line filters out any null values, storing the result of the operation into **LOG**.

3. Next, it iterates over the records in **LOG** and uses **GENERATE** to invoke the **create_structure** method contained in the Python/Jython script loaded as **myfuncs**.  **LINE** is used to pass the current record to the function.

4. Finally, the outputs are dumped to STDOUT using the **DUMP** command. This is just to immediately show the results after the operation completes; in a real script you would normally **STORE** the data into a new file.

The actual Python script file is also similar between C Python and Jython, the only real difference being that you must import from __pig\_util__ when using C Python. Here's the __pig\_python.py__ script:

# <a name="streamingpy"></a> Uncomment the following if using C Python
    #from pig_util import outputSchema

    @outputSchema("log: {(date:chararray, time:chararray, classname:chararray, level:chararray, detail:chararray)}")
    def create_structure(input):
    if (input.startswith('java.lang.Exception')):
        input = input[21:len(input)] + ' - java.lang.Exception'
    date, time, classname, level, detail = input.split(' ', 4)
    return date, time, classname, level, detail

> [AZURE.NOTE] 'pig_util' isn't something you need to worry about installing; it's automatically available to the script.

Remember that we previously just defined the **LINE** input as a chararray because there was no consistent schema for the input? What the Python script does is to transform the data into a consistent schema for output. It works like this:

1. The **@outputSchema** statement defines the format of the data that will be returned to Pig. In this case, it's a **data bag**, which is a Pig data type. The bag contains the following fields, all of which are chararray (strings):

	* date - the date the log entry was created
	* time - the time the log entry was created
	* classname - the class name the entry was created for
	* level - the log level
	* detail - verbose details for the log entry

2. Next, the **def create_structure(input)** defines the function that Pig will pass line items to.

3. The example data, **sample.log**, mostly conforms to the date, time, classname, level, and detail schema we want to return. But it also contains a few lines that begin with the string '*java.lang.Exception*' that need to be modified to match the schema. The **if** statement checks for those, then massages the input data to move the '*java.lang.Exception*' string to the end, bringing the data in-line with our expected output schema.

4. Next, the **split** command is used to split the data at the first four space characters. This results in five values, which are assigned into **date**, **time**, **classname**, **level**, and **detail**.

5. Finally, the values are returned to Pig.

When the data is returned to Pig, it will have a consistent schema as defined in the **@outputSchema** statement.

##<a name="running"></a>Running the examples

If you are using a Windows-based HDInsight cluster and a Windows client, use the **PowerShell** steps.

####Hive

1. Use the `hive` command to start the hive shell. You should see a `hive>` prompt once the shell has loaded.

2. Enter the following at the `hive>` prompt.

		add file wasbs:///streaming.py;
		SELECT TRANSFORM (clientid, devicemake, devicemodel)
		  USING 'python streaming.py' AS
		  (clientid string, phoneLabel string, phoneHash string)
		FROM hivesampletable
		ORDER BY clientid LIMIT 50;

3. After entering the last line, the job should start. Eventually it will return output similar to the following.

		100041	RIM 9650	d476f3687700442549a83fac4560c51c
		100041	RIM 9650	d476f3687700442549a83fac4560c51c
		100042	Apple iPhone 4.2.x	375ad9a0ddc4351536804f1d5d0ea9b9
		100042	Apple iPhone 4.2.x	375ad9a0ddc4351536804f1d5d0ea9b9
		100042	Apple iPhone 4.2.x	375ad9a0ddc4351536804f1d5d0ea9b9

####Pig

1. Use the `pig` command to start the shell. You should see a `grunt>` prompt once the shell has loaded.

2. Enter the following statements at the `grunt>` prompt to run the Python script using the Jython interpreter.

		Register wasbs:///pig_python.py using jython as myfuncs;
	    LOGS = LOAD 'wasbs:///example/data/sample.log' as (LINE:chararray);
	    LOG = FILTER LOGS by LINE is not null;
	    DETAILS = foreach LOG generate myfuncs.create_structure(LINE);
	    DUMP DETAILS;

3. After entering the following line,the job should start. Eventually it will return output similar to the following.

		((2012-02-03,20:11:56,SampleClass5,[TRACE],verbose detail for id 990982084))
		((2012-02-03,20:11:56,SampleClass7,[TRACE],verbose detail for id 1560323914))
		((2012-02-03,20:11:56,SampleClass8,[DEBUG],detail for id 2083681507))
		((2012-02-03,20:11:56,SampleClass3,[TRACE],verbose detail for id 1718828806))
		((2012-02-03,20:11:56,SampleClass3,[INFO],everything normal for id 530537821))

4. Use `quit` to exit the Grunt shell, and then use the following to edit the pig_python.py file on the local file system:

    nano pig_python.py

5. Once in the editor, uncomment the following line by removing the `#` character from the beginning of the line:

        #from pig_util import outputSchema

    Once the change has been made, use Ctrl+X to exit the editor. Select Y, and then enter to save the changes.

6. Use the `pig` command to start the shell again. Once you are at the `grunt>` prompt, use the following to run the Python script using the C Python interpreter.

        Register 'pig_python.py' using streaming_python as myfuncs;
	    LOGS = LOAD 'wasbs:///example/data/sample.log' as (LINE:chararray);
	    LOG = FILTER LOGS by LINE is not null;
	    DETAILS = foreach LOG generate myfuncs.create_structure(LINE);
	    DUMP DETAILS;

    Once this job completes, you should see the same output as when you previously ran the script using Jython.

###PowerShell

These steps use Azure PowerShell. If this is not already installed and configured on your development machine, see [How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure/) before using the following steps.

> [AZURE.IMPORTANT] Currently, HDInsight in Azure China is only manageable by Azure Service Manager (ASM). Azure Resource Manager (ARM) model for HDInsight is not available yet.
><p> Please follow the steps in [Install and configure Azure PowerShell](/documentation/articles/powershell-install-configure/) to install the latest version of Azure PowerShell.


1. Using the Python examples [streaming.py](#streamingpy) and [pig_python.py](#jythonpy), create local copies of the files on your development machine.

2. Use  the following PowerShell script to upload the **streaming.py** and **pig\_python.py** files to the server. Substitute the name of your Azure HDInsight cluster, and the path to the **streaming.py** and **pig\_python.py** files on the first three lines of the script.

		$clusterName = YourHDIClusterName
		$pathToStreamingFile = "C:\path\to\streaming.py"
		$pathToJythonFile = "C:\path\to\pig_python.py"

		$hdiStore = get-azurehdinsightcluster -name $clusterName
		$storageAccountName = $hdiStore.DefaultStorageAccount.StorageAccountName.Split(".",2)[0]
		$storageAccountKey = $hdiStore.defaultstorageaccount.storageaccountkey
		$defaultContainer = $hdiStore.DefaultStorageAccount.StorageContainerName

		$destContext = new-azurestoragecontext -storageaccountname $storageAccountName -storageaccountkey $storageAccountKey
		set-azurestorageblobcontent -file $pathToStreamingFile -Container $defaultContainer -Blob "streaming.py" -context $destContext
		set-azurestorageblobcontent -file $pathToJythonFile -Container $defaultContainer -Blob "jython.py" -context $destContext

	This script retrieves information for your HDInsight cluster, then extracts the account and key for the default storage account, and uploads the files to the root of the container.

	> [AZURE.NOTE] Other methods of uploading the scripts can be found in the [Upload data for Hadoop jobs in HDInsight](/documentation/articles/hdinsight-upload-data/) document.

After uploading the files, use the following PowerShell scripts to start the jobs. When the job completes, the output should be written to the PowerShell console.

####Hive

    # Replace 'YourHDIClusterName' with the name of your cluster
	$clusterName = YourHDIClusterName
    # If using a Windows-based HDInsight cluster, change the USING statement to:
    # "USING 'D:\Python27\python.exe streaming.py' AS " +
	$HiveQuery = "add file wasbs:///streaming.py;" +
	             "SELECT TRANSFORM (clientid, devicemake, devicemodel) " +
	               "USING 'python streaming.py' AS " +
	               "(clientid string, phoneLabel string, phoneHash string) " +
	             "FROM hivesampletable " +
	             "ORDER BY clientid LIMIT 50;"

	$jobDefinition = New-AzureHDInsightHiveJobDefinition -Query $HiveQuery -StatusFolder '/hivepython'

	$job = Start-AzureHDInsightJob -Cluster $clusterName -JobDefinition $jobDefinition
	Write-Host "Wait for the Hive job to complete ..." -ForegroundColor Green
	Wait-AzureHDInsightJob -Job $job
    # Uncomment the following to see stderr output
    # Get-AzureHDInsightJobOutput -StandardError -JobId $job.JobId -Cluster $clusterName
	Write-Host "Display the standard output ..." -ForegroundColor Green
	Get-AzureHDInsightJobOutput -Cluster $clusterName -JobId $job.JobId -StandardOutput

The output for the **Hive** job should appear similar to the following:

	100041	RIM 9650	d476f3687700442549a83fac4560c51c
	100041	RIM 9650	d476f3687700442549a83fac4560c51c
	100042	Apple iPhone 4.2.x	375ad9a0ddc4351536804f1d5d0ea9b9
	100042	Apple iPhone 4.2.x	375ad9a0ddc4351536804f1d5d0ea9b9
	100042	Apple iPhone 4.2.x	375ad9a0ddc4351536804f1d5d0ea9b9

####Pig (Jython)
> [AZURE.NOTE] When remotely submitting a job using PowerShell, it is not possible to use C Python as the interpreter.

	# Replace 'YourHDIClusterName' with the name of your cluster
	$clusterName = YourHDIClusterName
	$PigQuery = "Register wasbs:///jython.py using jython as myfuncs;" +
	            "LOGS = LOAD 'wasbs:///example/data/sample.log' as (LINE:chararray);" +
	            "LOG = FILTER LOGS by LINE is not null;" +
	            "DETAILS = foreach LOG generate myfuncs.create_structure(LINE);" +
	            "DUMP DETAILS;"

	$jobDefinition = New-AzureHDInsightPigJobDefinition -Query $PigQuery -StatusFolder '/pigpython'

	$job = Start-AzureHDInsightJob -Cluster $clusterName -JobDefinition $jobDefinition
	Write-Host "Wait for the Pig job to complete ..." -ForegroundColor Green
	Wait-AzureHDInsightJob -Job $job
    # Uncomment the following to see stderr output
    # Get-AzureHDInsightJobOutput -StandardError -JobId $job.JobId -Cluster $clusterName
	Write-Host "Display the standard output ..." -ForegroundColor Green
	Get-AzureHDInsightJobOutput -Cluster $clusterName -JobId $job.JobId -StandardOutput

The output for the **Pig** job should appear similar to the following:

	((2012-02-03,20:11:56,SampleClass5,[TRACE],verbose detail for id 990982084))
	((2012-02-03,20:11:56,SampleClass7,[TRACE],verbose detail for id 1560323914))
	((2012-02-03,20:11:56,SampleClass8,[DEBUG],detail for id 2083681507))
	((2012-02-03,20:11:56,SampleClass3,[TRACE],verbose detail for id 1718828806))
	((2012-02-03,20:11:56,SampleClass3,[INFO],everything normal for id 530537821))

##<a name="troubleshooting"></a>Troubleshooting

###Errors when running jobs

When running the hive job, you may encounter an error similar to the following:

    Caused by: org.apache.hadoop.hive.ql.metadata.HiveException: [Error 20001]: An error occurred while reading or writing to your custom script. It may have crashed with an error.
    
This problem may be caused by the line endings in the streaming.py file. Many Windows editors default to using CRLF as the line ending, but Linux applications usually expect LF.

If you are using an editor that cannot create LF line endings, or are unsure what line endings are being used, use the following PowerShell statements to remove the CR characters before uploading the file to HDInsight:

    $original_file ='c:\path\to\streaming.py'
    $text = [IO.File]::ReadAllText($original_file) -replace "`r`n", "`n"
    [IO.File]::WriteAllText($original_file, $text)

###PowerShell scripts

Both of the example PowerShell scripts used to run the examples contain a commented line that will display error output for the job. If you are not seeing the expected output for the job, uncomment the following line and see if the error information indicates a problem.

	# Get-AzureHDInsightJobOutput -StandardError -JobId $job.JobId -Cluster $clusterName

The error information (STDERR,) and the result of the job (STDOUT,) are also logged to the default blob container for your clusters at the following locations.

For this job..|Look at these files in the blob container
---|---
Hive|/HivePython/stderr<p>/HivePython/stdout
Pig|/PigPython/stderr<p>/PigPython/stdout

##<a name="next"></a>Next steps

If you need to load Python modules that aren't provided by default, see [How to deploy a module to Azure HDInsight](http://blogs.msdn.com/b/benjguin/archive/2014/03/03/how-to-deploy-a-python-module-to-windows-azure-hdinsight.aspx) for an example of how to do this.

For other ways to use Pig, Hive, and to learn about using MapReduce, see the following.

* [Use Hive with HDInsight](/documentation/articles/hdinsight-use-hive/)

* [Use Pig with HDInsight](/documentation/articles/hdinsight-use-pig/)

* [Use MapReduce with HDInsight](/documentation/articles/hdinsight-use-mapreduce/)
