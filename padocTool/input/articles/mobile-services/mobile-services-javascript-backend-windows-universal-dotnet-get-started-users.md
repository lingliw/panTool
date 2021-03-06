<properties 
	pageTitle="Add authentication to your universal Windows 8.1 app | Azure Mobile Services"
	description="Learn how to use Mobile Services to authenticate users of your Windows Store app through a variety of identity providers, including Google, Facebook, Twitter, and Microsoft." 
	services="mobile-services" 
	documentationCenter="windows" 
	authors="ggailey777" 
	manager="dwrede" 
	editor=""/>

<tags 
	ms.service="mobile-services" 
	ms.date="09/14/2015" 
	wacn.date=""/>

# Add authentication to your universal Windows 8.1 app

[AZURE.INCLUDE [mobile-services-selector-get-started-users](../includes/mobile-services-selector-get-started-users.md)]		

This topic shows you how to authenticate users in Azure Mobile Services from your universal Windows 8.1 app. In this tutorial, you add authentication to the quickstart project using an identity provider that is supported by Mobile Services. After being successfully authenticated and authorized by Mobile Services, the user ID value is displayed.

This tutorial is based on the Mobile Services quickstart. You must also first complete the tutorial [Get started with Mobile Services] or [Add Mobile Services to an existing app](/documentation/articles/mobile-services-javascript-backend-windows-universal-dotnet-get-started-data). 

>[AZURE.NOTE]This tutorial shows you how to authenticate users in Windows Store and Windows Phone Store 8.1 apps. For a Windows Phone 8.0 or Windows Phone Silverlight 8.1 app, see this version of [Get started with authentication in Mobile Services](/documentation/articles/mobile-services-windows-phone-get-started-users).

>This tutorial demonstrates a service-managed authentication flow using a variety of identity providers. This method is easy to configure and supports multiple providers. To instead use a client-managed flow using Live SDK in your Windows Store app, see the topic [Authenticate your Windows Store app with client managed authentication using Microsoft account](/documentation/articles/mobile-services-windows-store-dotnet-single-sign-on). 

##<a name="register"></a> Register your app for authentication and configure Mobile Services

[AZURE.INCLUDE [mobile-services-register-authentication](../includes/mobile-services-register-authentication.md)] 

##<a name="permissions"></a> Restrict permissions to authenticated users

[AZURE.INCLUDE [mobile-services-restrict-permissions-windows](../includes/mobile-services-restrict-permissions-windows.md)] 

>[AZURE.NOTE] When you use Visual Studio tools to connect your app to a Mobile Service, the tool generate two sets of **MobileServiceClient** definitions, one for each client platform. This is a good time to simplify the generated code by unifying the `#if...#endif` wrapped **MobileServiceClient** definitions into a single unwrapped definition used by both versions of the app. You won't need to do this if you downloaded the quickstart app from the Azure Management portal.

##<a name="add-authentication"></a> Add authentication to the app

[AZURE.INCLUDE [mobile-services-windows-universal-dotnet-authenticate-app](../includes/mobile-services-windows-universal-dotnet-authenticate-app.md)] 

Now, any user authenticated by your trusted identity providers can access the *TodoItem* table. To better secure user-specific data, you must also implement authorization. To do this you get the user ID of a given user, which can then be used to determine what level of access that user should have for a given resource.

##<a name="tokens"></a>Store the authorization token on the client

[AZURE.INCLUDE [mobile-services-windows-store-dotnet-authenticate-app-with-token](../includes/mobile-services-windows-store-dotnet-authenticate-app-with-token.md)] 

## <a name="next-steps"> </a>Next steps

In the next tutorial, [Service-side authorization of Mobile Services users](/documentation/articles/mobile-services-javascript-backend-service-side-authorization), you will take the user ID value provided by Mobile Services based on an authenticated user and use it to filter the data returned by Mobile Services. 

##See also

+ [Enhanced users feature](http://go.microsoft.com/fwlink/p/?LinkId=506605)<br/>
You can get additional user data maintained by the identity provider in your mobile service by by calling the **user.getIdentities()** function in server scripts. 

+ [Mobile Services .NET How-to Conceptual Reference]<br/>Learn more about how to use Mobile Services with a .NET client.


<!-- Anchors. -->
[Register your app for authentication and configure Mobile Services]: #register
[Restrict table permissions to authenticated users]: #permissions
[Add authentication to the app]: #add-authentication
[Store authentication tokens on the client]: #tokens
[Next Steps]:#next-steps


<!-- URLs. -->
[Submit an app page]: http://go.microsoft.com/fwlink/p/?LinkID=266582
[My Applications]: http://go.microsoft.com/fwlink/p/?LinkId=262039
[Live SDK for Windows]: http://go.microsoft.com/fwlink/p/?LinkId=262253

[Get started with Mobile Services]: /documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started
[Get started with data]: /documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started-data
[Get started with authentication]: /documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started-users
[Get started with push notifications]: vmobile-services-javascript-backend-windows-store-dotnet-get-started-push
[Authorize users with scripts]: /documentation/articles/mobile-services-windows-store-dotnet-authorize-users-in-scripts
[JavaScript and HTML]: /documentation/articles/mobile-services-windows-store-javascript-get-started-users
[Azure Management Portal]: https://manage.windowsazure.cn/
[Mobile Services .NET How-to Conceptual Reference]: /documentation/articles/mobile-services-windows-dotnet-how-to-use-client-library
[Register your Windows Store app package for Microsoft authentication]: /documentation/articles/mobile-services-how-to-register-store-app-package-microsoft-authentication
