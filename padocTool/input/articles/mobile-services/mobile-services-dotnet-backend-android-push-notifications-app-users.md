<properties 
	pageTitle="Send push notifications to authenticated users" 
	description="Learn how to send push notifications to specific" 
	services="mobile-services,notification-hubs" 
	documentationCenter="android" 
	authors="wesmc7777" 
	manager="dwrede" 
	editor=""/>

<tags 
	ms.service="mobile-services" 
	ms.date="06/03/2015" 
	wacn.date=""/>

# Send push notifications to authenticated users

[AZURE.INCLUDE [mobile-services-selector-push-users](../includes/mobile-services-selector-push-users.md)]

##Overview

This topic shows you how to send push notifications to an authenticated user on any registered device. Unlike the previous [push notification][Get started with push notifications] tutorial, this tutorial changes your mobile service to require that a user be authenticated before the client can register with the notification hub for push notifications. Registration is also modified to add a tag based on the assigned user ID. Finally, the server code is updated to send the notification only to the authenticated user instead of to all registrations.

 
This tutorial supports Android apps.

##Prerequisites 

Before you start this tutorial, you must have already completed these Mobile Services tutorials:

+ [Add authentication to your Mobile Services app]<br/>Adds a login requirement to the TodoList sample app.

+ [Get started with push notifications]<br/>Configures the TodoList sample app for push notifications by using Notification Hubs. 

After you have completed both tutorials, you can prevent unauthenticated users from registering for push notifications from your mobile service.

##Update the service to require authentication to register

[AZURE.INCLUDE [mobile-services-dotnet-backend-push-notifications-app-users](../includes/mobile-services-dotnet-backend-push-notifications-app-users.md)] 

##Update the app to log in before registration

[AZURE.INCLUDE [mobile-services-android-push-notifications-app-users](../includes/mobile-services-android-push-notifications-app-users.md)] 

##Test the app

[AZURE.INCLUDE [mobile-services-android-test-push-users](../includes/mobile-services-android-test-push-users.md)] 


<!---##Next steps

In the next tutorial, [Service-side authorization of Mobile Services users](/documentation/articles/mobile-services-javascript-backend-service-side-authorization), you will take the user ID value provided by Mobile Services based on an authenticated user and use it to filter the data returned by Mobile Services. Learn more about how to use Mobile Services with .NET in [Mobile Services .NET How-to Conceptual Reference]-->


<!-- URLs. -->
[Add authentication to your Mobile Services app]: /documentation/articles/mobile-services-dotnet-backend-android-get-started-users
[Get started with push notifications]: /documentation/articles/mobile-services-dotnet-backend-android-get-started-push

[Azure Management Portal]: https://manage.windowsazure.cn/
[Mobile Services .NET How-to Conceptual Reference]: /documentation/articles/mobile-services-windows-dotnet-how-to-use-client-library
