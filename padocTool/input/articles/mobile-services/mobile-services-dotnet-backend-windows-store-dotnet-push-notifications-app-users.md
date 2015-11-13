<properties 
	pageTitle="Send push notifications to authenticated users" 
	description="Learn how to send push notifications to specific" 
	services="mobile-services,notification-hubs" 
	documentationCenter="windows" 
	authors="ggailey777" 
	manager="dwrede" 
	editor=""/>

<tags 
	ms.service="mobile-services" 
	ms.date="07/01/2015" 
	wacn.date=""/>

# Send push notifications to authenticated users

[AZURE.INCLUDE [mobile-services-selector-push-users](../includes/mobile-services-selector-push-users.md)]

##Overview

This topic shows you how to send push notifications to an authenticate user on any registered device. Unlike the previous [push notification][Get started with push notifications] tutorial, this tutorial changes your mobile service to require that a user be authenticated before the client can register with the notification hub for push notifications. Registration is also modified to add a tag based on the assigned user ID. Finally, the server code is updated to send the notification only to the authenticated user instead of to all registrations.


 
This tutorial supports both Windows Store and Windows Phone Store apps.

##Prerequisites 

Before you start this tutorial, you must have already completed these Mobile Services tutorials:

+ [Get started with authentication]<br/>Adds a login requirement to the TodoList sample app.

+ [Get started with push notifications]<br/>Configures the TodoList sample app for push notifications by using Notification Hubs. 

After you have completed both tutorials, you can prevent unauthenticated users from registering for push notifications from your mobile service.

##<a name="register"></a>Update the service to require authentication to register

[AZURE.INCLUDE [mobile-services-dotnet-backend-push-notifications-app-users](../includes/mobile-services-dotnet-backend-push-notifications-app-users.md)] 

##<a name="update-app"></a>Update the app to log in before registration

[AZURE.INCLUDE [mobile-services-windows-store-dotnet-push-notifications-app-users](../includes/mobile-services-windows-store-dotnet-push-notifications-app-users.md)] 

##<a name="test"></a>Test the app

[AZURE.INCLUDE [mobile-services-windows-test-push-users](../includes/mobile-services-windows-test-push-users.md)] 


<!-- Anchors. -->
[Updating the service to require authentication for registration]: #register
[Updating the app to log in before registration]: #update-app
[Testing the app]: #test
[Next Steps]:#next-steps


<!-- URLs. -->
[Get started with authentication]: /documentation/articles/mobile-services-dotnet-backend-windows-store-dotnet-get-started-users
[Get started with push notifications]: /documentation/articles/mobile-services-dotnet-backend-windows-store-dotnet-get-started-push

[Azure Management Portal]: https://manage.windowsazure.cn/
