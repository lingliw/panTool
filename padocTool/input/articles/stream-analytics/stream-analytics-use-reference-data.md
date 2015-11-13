<properties 
	pageTitle="Use reference data | Windows Azure" 
	description="Use reference data as an input stream" 
	keywords="big data analytics,cloud service,internet of things,managed service,stream processing,streaming analytics,streaming data"
	services="stream-analytics" 
	documentationCenter="" 
	authors="jeffstokes72" 
	manager="paulettm" 
	editor="cgronlun"/>

<tags 
	ms.service="stream-analytics" 
	ms.date="09/09/2015" 
	wacn.date=""/>

# Using reference data as an input

Reference data is a finite data set that is static or slowing changing in nature, used to perform a lookup or to correlate with your data stream. To make use of reference data in your Azure Stream Analytics job you will generally use a [Reference Data Join](https://msdn.microsoft.com/library/azure/dn949258.aspx) in your Query. Stream Analytics uses Azure Blob storage as the storage layer for Reference Data, and with Azure Data Factory reference data can be transformed and/or copied to Azure Blob storage, for use as Reference Data, from [any number of cloud based and on-premises data stores](./articles/data-factory-data-movement-activities.md).

## Configuring reference data

To configure your reference data, you first need to create an input that is of type Reference Data. The table below explains each property that you will need to provide while creating the reference data input with its description:

<table>
<tbody>
<tr>
<td>Property Name</td>
<td>Description</td>
</tr>
<tr>
<td>Input Alias</td>
<td>A friendly name that will be used in the job query to reference this input.</td>
</tr>
<tr>
<td>Storage Account</td>
<td>The name of the storage account where your blob files are located. If it’s in the same subscription as your Stream Analytics Job, you can select it from the drop down.</td>
</tr>
<tr>
<td>Storage Account Key</td>
<td>The secret key associated with the storage account. This gets automatically populated if the storage account is in the same subscription as your Stream Analytics job.</td>
</tr>
<tr>
<td>Storage Container</td>
<td>Containers provide a logical grouping for blobs stored in the Windows Azure Blob service. When you upload a blob to the Blob service, you must specify a container for that blob.</td>
</tr>
<tr>
<td>Path Prefix Pattern [optional]</td>
<td>The file path used to locate your blobs within the specified container. Within the path, you may choose to specify one or more instances of the following 2 variables:<BR>{date}, {time}<BR>Example 1: products/{date}/{time}/product-list.csv<BR>Example 2: products/{date}/product-list.csv
</tr>
<tr>
<td>Date Format [optional]</td>
<td>If you have used {date} within the Path Pattern that you specified, then you can select the date format in which your files are organized from the drop down of supported formats. Example: YYYY/MM/DD</td>
</tr>
<tr>
<td>Time Format [optional]</td>
<td>If you have used {time} within the Path Pattern that you specified, then you can select the time format in which your files are organized from the drop down of supported formats. Example: HH</td>
</tr>
<tr>
<td>Event Serialization Format</td>
<td>To make sure your queries work the way you expect, Stream Analytics needs to know which serialization format you're using for incoming data streams. For Reference Data, the supported formats are CSV and JSON.</td>
</tr>
<tr>
<td>Encoding</td>
<td>UTF-8 is the only supported encoding format at this time</td>
</tr>
</tbody>
</table>

## Generating reference data on a schedule

If your reference data is a slowly changing dataset, then support for refreshing reference data is enabled by specifying a path pattern in the input configuration using the {date} and {time} tokens. Stream Analytics will pick up the updated reference data definitions based on this path pattern. For example, a pattern of ````"/sample/{date}/{time}/products.csv"```` with a date format of “YYYY-MM-DD” and a time format of “HH:mm” tells Stream Analytics to pick up the updated blob ````"/sample/2015-04-16/17:30/products.csv"```` at 5:30 PM on April 16th 2015 UTC time zone.

> [AZURE.NOTE] Currently Stream Analytics jobs look for the blob refresh only when the machine time coincides with the time encoded in the blob name. For example  the job will look for /sample/2015-04-16/17:30/products.csv between 5:30 PM and 5:30:59.9PM on April 16th 2015 UTC time zone. When the machine clock reaches 5:31PM it stops looking for /sample/2015-04-16/17:30/products.csv and starts looking for /sample/2015-04-16/17:31/products.csv. The only time previous reference data blobs are considered is when the job is first started. At that time the job is looking for the most recent blob produced prior to the job start time specified. This is done to ensure that there is a non-empty reference data set when the job start. If one cannot be found, the job will fail and will display a diagnostic notice to the user.

[Azure Data Factory](http://azure.microsoft.com/documentation/services/data-factory/) can be used to orchestrate the task of creating the updated blobs required by Stream Analytics to update reference data definitions . Data Factory is a cloud-based data integration service that orchestrates and automates the movement and transformation of data. Data Factory supports [connecting to a large number of cloud based and on-premises data stores](./articles/data-factory-data-movement-activities.md) and moving data easily on a regular schedule that you specify. For more information and step by step guidance on how to set up a Data Factory pipeline to generate reference data for Stream Analytics which refreshes on a pre-defined schedule, check out this [GitHub sample](https://github.com/Azure/Azure-DataFactory/tree/master/Samples/ReferenceDataRefreshForASAJobs).

## Get help
For further assistance, try our [Azure Stream Analytics forum](https://social.msdn.microsoft.com/Forums/en-US/home?forum=AzureStreamAnalytics)

## Next steps
You've been introduced to Stream Analytics, a managed service for streaming analytics on data from the Internet of Things. To learn more about this service, see:

- [Get started using Azure Stream Analytics](/documentation/articles/stream-analytics-get-started)
- [Scale Azure Stream Analytics jobs](/documentation/articles/stream-analytics-scale-jobs)
- [Azure Stream Analytics Query Language Reference](https://msdn.microsoft.com/library/azure/dn834998.aspx)
- [Azure Stream Analytics Management REST API Reference](https://msdn.microsoft.com/library/azure/dn835031.aspx)

<!--Link references-->
[stream.analytics.developer.guide]: ../stream-analytics-developer-guide.md
[stream.analytics.scale.jobs]: stream-analytics-scale-jobs.md
[stream.analytics.introduction]: stream-analytics-introduction.md
[stream.analytics.get.started]: stream-analytics-get-started.md
[stream.analytics.query.language.reference]: http://go.microsoft.com/fwlink/?LinkID=513299
[stream.analytics.rest.api.reference]: http://go.microsoft.com/fwlink/?LinkId=517301
