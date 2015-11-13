<properties 
	pageTitle="Write Queries| Windows Azure" 
	description="Write Queries learning path segment."
	documentationCenter=""
	services="stream-analytics"
	authors="jeffstokes72" 
	manager="paulettm" 
	editor="cgronlun"/>

<tags 
	ms.service="stream-analytics" 
	ms.date="09/09/2015" 
	wacn.date=""/>

# Write Queries

Stream processing logic in Azure Stream Analytics is implemented as a "standing query" that is defined before a job starts and executed on data as it reaches the job. The data transformation is expressed in a SQL-like query language, which is largely a subset of T-SQL with some added language extensions like [Windowing](https://msdn.microsoft.com/library/azure/dn835019.aspx) used to express temporal semantics.  

## To author a Stream Analytics query: ##

1. In your Stream Analytics Job, click **Query**.

    ![Select Query](./media/stream-analytics-write-queries/1-stream-analytics-write-queries.png)  

2.	New jobs have a query template to help get you started. The query template performs a "pass-through" query that projects all fields from input events into the output.  

    - If you have defined at least one input and output for your job, you can replace the placeholder "[YourOutputAlias]" and "[YourInputAlias]" fields with the aliases of the input and output that you wish use first. In addition, you can still author and test your query in the Azure portal without defining inputs and outputs on the job.
    - If you wish to perform more processing than a simple pass-through, you can edit the query definition. To get started with query authoring, take a look at some common query patterns are captured [here](stream-analytics-query-patterns).  
  
    ![Query Window](./media/stream-analytics-write-queries/2-stream-analytics-write-queries.png)  

## To test a query: ##

You can test that your query behaves as expected by running it in the browser over one or more local JSON files containing test data. This will not start the job or have any billing implications.

1.	Make sure that there are no errors in the query (otherwise the Test button will be disabled) and then click the Test button.  

    ![Query Test](./media/stream-analytics-write-queries/3-stream-analytics-write-queries.png)  

2.	You will be prompted to specify files for each of the inputs referenced in the query. In this example, the template query is left as-is, so the dialog is prompting for an input named "yourinputalias".  

    ![Test Data](./media/stream-analytics-write-queries/4-stream-analytics-write-queries.png)  

3.	Browse to a test file. Several sample files are available on [github](https://github.com/Azure/azure-stream-analytics/tree/master/Sample Data) and you can also retrieve sample data from your own data stream inputs via the Sample Data function on the inputs tab.  

    ![Query Input](./media/stream-analytics-write-queries/5-stream-analytics-write-queries.png)  

4.	After closing the dialog, your query will be run over the test data and you will see the results at the bottom of the Query page.  

    ![Query Summary](./media/stream-analytics-write-queries/6-stream-analytics-write-queries.png)  

## Get help
For further assistance, try our [Azure Stream Analytics forum](https://social.msdn.microsoft.com/Forums/en-US/home?forum=AzureStreamAnalytics)

## Next steps

- [Introduction to Azure Stream Analytics](/documentation/articles/stream-analytics-introduction)
- [Get started using Azure Stream Analytics](/documentation/articles/stream-analytics-get-started)
- [Scale Azure Stream Analytics jobs](/documentation/articles/stream-analytics-scale-jobs)
- [Azure Stream Analytics Query Language Reference](https://msdn.microsoft.com/library/azure/dn834998.aspx)
- [Azure Stream Analytics Management REST API Reference](https://msdn.microsoft.com/library/azure/dn835031.aspx)