<properties 
	pageTitle="What happened to my .NET project after adding Mobile Services by using Visual Studio Connected Services | Windows Azure" 
	description="Describes what happened in your Visual Studio .NET project after adding Azure Mobile Services by using Connected Services " 
	services="mobile-services" 
	documentationCenter="" 
	authors="patshea123" 
	manager="douge" 
	editor=""/>

<tags 
	ms.service="mobile-services" 
	ms.date="09/17/2015" 
	wacn.date=""/>

# What happened to my Visual Studio .NET project after adding Azure Mobile Services by using Connected Services?

> [AZURE.SELECTOR]
> - [Getting Started](/documentation/articles/vs-mobile-services-dotnet-getting-started)
> - [What Happened](/documentation/articles/vs-mobile-services-dotnet-what-happened)

## References Added

The Azure Mobile Services NuGet package was added to your project. As a result, the following .NET references were added to your project:

- **Microsoft.WindowsAzure.Mobile**
- **Microsoft.WindowsAzure.Mobile.Ext**
- **Newtonsoft.Json**
- **System.Net.Http.Extensions**
- **System.Net.Http.Primitives** 

## Connection string values for Mobile Services

In your App.xaml.cs file, a **MobileServiceClient** object was created with the selected mobile service’s application URL and application key. 

## Mobile Services project added

If a .NET mobile service is created in the Connected Service Provider, then a mobile services project is created and added to the solution.


[Learn more about mobile services](/services/mobile-services/) 
