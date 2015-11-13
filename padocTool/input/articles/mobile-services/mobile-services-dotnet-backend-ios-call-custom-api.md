<properties
	pageTitle="How to call a custom API from an iOS client"
	description="Learn how to define a custom API and then call it from an iOS app that uses Azure Mobile Services."
	services="mobile-services"
	documentationCenter="ios"
	authors="krisragh"
	writer="krisragh"
	manager="dwrede"
	editor=""/>

<tags
	ms.service="mobile-services"
	ms.date="06/03/2015"
	wacn.date=""/>


# How to call a custom API from an iOS client (.NET backend)

[AZURE.INCLUDE [mobile-services-selector-call-custom-api](../includes/mobile-services-selector-call-custom-api.md)]

This topic shows you how to call a custom API from an iOS app. A custom API lets you define custom endpoints with server functionality, but it does not map to a database insert, update, delete, or read operation. By using a custom API, you have more control over messaging, including HTTP headers and body format.

## <a name="define-custom-api"></a>Define Custom API

[AZURE.INCLUDE [mobile-services-dotnet-backend-create-custom-api](../includes/mobile-services-dotnet-backend-create-custom-api.md)]

[AZURE.INCLUDE [mobile-services-ios-call-custom-api](../../includes/mobile-services-ios-call-custom-api.md)]

This topic showed how to use the **invokeApi** method to call a fairly simple custom API from your iOS app. To learn more about using the **invokeApi** method, see the post [Custom API in Azure Mobile Services](http://blogs.msdn.com/b/carlosfigueira/archive/2013/06/19/custom-api-in-azure-mobile-services-client-sdks.aspx).  

<!-- Anchors. -->
[Define the custom API]: #define-custom-api
[Update the app to call the custom API]: #update-app
[Test the app]: #test-app
[Next Steps]: #next-steps

<!-- Images. -->

<!-- URLs. -->
[Windows Push Notifications & Live Connect]: http://go.microsoft.com/fwlink/?LinkID=257677
[Mobile Services server script reference]: /zh-cn/documentation/articles/mobile-services-how-to-use-server-scripts
[My Apps dashboard]: http://go.microsoft.com/fwlink/?LinkId=262039
[Get started with Mobile Services]: /documentation/articles/mobile-services-dotnet-backend-ios-get-started
[Mobile Services Quick Start]: /documentation/articles/mobile-services-dotnet-backend-ios-get-started
[Get started with data]: /documentation/articles/mobile-services-dotnet-backend-ios-get-started-data
[Get started with authentication]: /documentation/articles/mobile-services-dotnet-backend-ios-get-started-users
[Get started with push notifications]: /documentation/articles/mobile-services-dotnet-backend-ios-get-started-push
[Store server scripts in source control]: /documentation/articles/mobile-services-store-scripts-source-control
