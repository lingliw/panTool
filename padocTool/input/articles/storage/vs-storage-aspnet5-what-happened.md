<properties 
	pageTitle="Getting Started with Azure Storage" 
	description="Describes what happened when creating an Azure storage in a Visual Studio ASP.NET 5 project" 
	services="storage" 
	documentationCenter="" 
	authors="patshea123" 
	manager="douge" 
	editor="tglee"/>

<tags 
	ms.service="storage" 
	
	ms.date="07/22/2015" 
	wacn.date=""/>

# What happened to my project?

> [AZURE.SELECTOR]
> - [Getting Started](/documentation/articles/vs-storage-aspnet5-getting-started-blobs)
> - [What Happened](/documentation/articles/vs-storage-aspnet5-what-happened)

> [AZURE.SELECTOR]
> - [Blobs](/documentation/articles/vs-storage-aspnet5-getting-started-blobs)
> - [Queues](/documentation/articles/vs-storage-aspnet5-getting-started-queues)
> - [Tables](/documentation/articles/vs-storage-aspnet5-getting-started-tables)

###What happened to my project?</span>

##### References Added

The Azure Storage NuGet package was added to your Visual Studio project.  
This package adds the following .NET references:

- `Microsoft.Data.Edm`
- `Microsoft.Data.OData`
- `Microsoft.Data.Services.Client`
- `Microsoft.WindowsAzure.Configuration`
- `Microsoft.WindowsAzure.Storage`
- `Newtonsoft.Json`
- `System.Data`
- `System.Spatial`

Also, the NuGet package **Microsoft.Framework.Configuration.Json** was added.

#####Connection string for Azure Storage added 
In the config.json file of your project, an element was created with the selected storage account's connection string and key.

For more information, see [ASP.NET 5](http://www.asp.net/vnext).
 