<properties 
	pageTitle="Register for Twitter authentication - Mobile Services" 
	description="Learn how to use Twitter authentication with your Azure Mobile Services application." 
	services="mobile-services" 
	documentationCenter="" 
	authors="ggailey777" 
	manager="dwrede" 
	editor=""/>

<tags 
	ms.service="mobile-services" 
	ms.date="08/08/2015" 
	wacn.date=""/>

#Register your apps for Twitter login with Mobile Services

[AZURE.INCLUDE [mobile-services-selector-register-identity-provider](../includes/mobile-services-selector-register-identity-provider.md)]

This topic shows you how to register your apps to be able to use Twitter to authenticate with Azure Mobile Services.

>[AZURE.NOTE] This tutorial is about [Azure Mobile Services](http://azure.microsoft.com/services/mobile-services/), a solution to help you build scalable mobile applications for any platform. Mobile Services makes it easy to sync data, authenticate users, and send push notifications. This page supports the <a href="http://azure.microsoft.com/documentation/articles/mobile-services-ios-get-started-users/">Get Started with Authentication</a> tutorial which shows how to log users into your app. If this is your first experience with Mobile Services, please complete the tutorial <a href="http://azure.microsoft.com/documentation/articles/mobile-services-ios-get-started/">Get Started with Mobile Services</a>.

To complete the procedure in this topic, you must have a Twitter account that has a verified email address. To create a new Twitter account, go to <a href="http://go.microsoft.com/fwlink/p/?LinkID=268287" target="_blank">twitter.com</a>.

1. Navigate to the <a href="http://go.microsoft.com/fwlink/p/?LinkId=268300" target="_blank">Twitter Developers</a> website, sign-in with your Twitter account credentials, and click **Create a new application**.

   	![][1]

2. Type the **Name**, **Description**, and **Website** values for your app, then type the URL of your mobile service appended with the path _/login/twitter_ in **Callback URL**.

	>[AZURE.NOTE]For a .NET backend mobile service published to Azure by using Visual Studio, the redirect URL is the URL of your mobile service appended with the path _signin-twitter_ your mobile service as a .NET service, such as <code>https://todolist.azure-mobile.net/signin-twitter</code>.

   	![][2]

3.  At the bottom the page, read and accept the terms, and then click **Create your Twitter application**. 



   	This registers the app displays the application details.

6. Click the **Keys and Access Tokens** tab in your app dashboard and make a note of the values of **Consumer key** and **Consumer secret**. 



    > [AZURE.NOTE] The consumer secret is an important security credential. Do not share this secret with anyone or distribute it with your app.

7. Click the **Settings** tab, scroll down and make sure the **Allow this application to be used to sign in with Twitter**, then click **Update this Twitter application's settings**.



You are now ready to use a Twitter login for authentication in your app by providing the consumer key and consumer secret values to Mobile Services.

<!-- Anchors. -->

<!-- Images. -->
[1]: ./media/mobile-services-how-to-register-twitter-authentication/mobile-services-twitter-developers.png
[2]: ./media/mobile-services-how-to-register-twitter-authentication/mobile-services-twitter-register-app1.png


<!-- URLs. -->

[Twitter Developers]: http://go.microsoft.com/fwlink/p/?LinkId=268300
[Get started with authentication]: /documentation/articles/mobile-services-javascript-backend-windows-universal-dotnet-get-started-users/

[Azure Management Portal]: https://manage.windowsazure.cn
 