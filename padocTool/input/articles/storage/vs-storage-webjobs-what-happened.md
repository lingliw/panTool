<properties
	pageTitle="What happened to my WebJob project (Visual Studio Azure Storage connected service)? | Windows Azure"
	description="Describes what happened in a Azure WebJob project after connecting to a storage account using Visual Studio connected services" 
	services="storage"
	documentationCenter=""
	authors="patshea123"
	manager="douge"
	editor="tglee"/>

<tags 
	ms.service="storage" 
	
	ms.date="09/03/2015"
	wacn.date=""/>
# What happened to my WebJob project (Visual Studio Azure Storage connected service)?

> [AZURE.SELECTOR]
> - [Getting Started](/documentation/articles/vs-storage-webjobs-getting-started-blobs)
> - [What Happened](/documentation/articles/vs-storage-webjobs-what-happened)


##### References Added

The Azure Storage NuGet package was added to or updated in your Visual Studio project.  
This package adds the following .NET references:

- `Microsoft.Data.Edm`
- `Microsoft.Data.OData`
- `Microsoft.Data.Services.Client`
- `Microsoft.WindowsAzure.ConfigurationManager`
- `Microsoft.WindowsAzure.Storage`
- `Newtonsoft.Json`
- `System.Data`
- `System.Spatial`

## Connection string for Azure Storage added
In the App.config file of your project, the **AzureWebJobsStorage** and **AzureWebJobsDashboard** entries were updated with the selected storage account's connection string and key.

For more information, see [Azure WebJobs Recommended Resources](http://www.windowsazure.cn/documentation/articles/websites-webjobs-resources/). 