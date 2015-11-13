<!-- not suitable for mooncake -->

<properties 
	pageTitle="Create an Orchard CMS web app from the Azure Marketplace" 
	description="A tutorial that teaches you how to create a new web app in Azure. Also learn how to launch and manage your web app using the Azure Management Portal." 
	tags="azure-portal"
	services="app-service\web" 
	documentationCenter=".net" 
	authors="tfitzmac" 
	manager="wpickett" 
	editor=""/>

<tags 
	ms.service="app-service-web" 
	ms.date="08/03/2015" 
	wacn.date=""/>

# Create an Orchard CMS web app from the Azure Marketplace

## Overview

The Marketplace makes available a wide range of popular web applications developed by Microsoft, third party companies, and open source software initiatives. Web applications created from the Marketplace do not require installation of any software other than the browser used to connect to the [Azure preview portal](https://manage.windowsazure.cn/). For more information about the web applications in the Marketplace, see [Azure Marketplace](/marketplace/).

In this tutorial, you'll learn:

- How to create a new web app from the Marketplace

- How to launch and manage your site from the Management Portal
 
You'll build an Orchard CMS site that uses a default template. [Orchard](http://www.orchardproject.net/) is a free, open-source, .NET-based CMS application that allows you to create customized, content-driven websites. Orchard CMS includes an extensibility framework through which you can [download additional modules and themes](http://gallery.orchardproject.net/) to customize your site. The following illustration shows the Orchard CMS site that you will create.

![Orchard blog][13]

[AZURE.INCLUDE [create-account-and-websites-note](../includes/create-account-and-websites-note)]

## Create an Orchard web app from the Marketplace

1. Login to the [Azure Management Portal](http://manage.windowsazure.cn).

2. Click **New** > **Web + Mobile** > **Azure Marketplace**.
	
	![Create New][1]

3. Click **Web Apps** > **Orchard CMS**. In the next blade, click **Create**.
	
	![Create From Marketplace][2]

4. Configure the web app's URL, App Service plan, resource group, and location. When you're done, click **Create**.
	
	![Configure the app][3]

	Once your web app is created, the **Notifications** button will show a green "SUCCESS" and your web app's blade will be displayed.

## Launch and manage your Orchard web app

1. In your web app's blade, click **Browse** to open your web app's welcome page.

	![browse button][12]

2. Enter the configuration information required by Orchard, and then click **Finish Setup** to complete the configuration and open the web app's home page.

	![login to Orchard][7]

	You'll have a new Orchard web app that looks similar to the screenshot below.  

	![your Orchard web app][13]

3. Follow the details in the [Orchard Documentation](http://docs.orchardproject.net/) to learn more about Orchard and configure your new web app.

## Next steps

* [Create an ASP.NET MVC app with auth and SQL DB and deploy to Azure Websites](/documentation/articles/web-sites-dotnet-deploy-aspnet-mvc-app-membership-oauth-sql-database)-- Learn how to create a new web app in Azure Websites from Visual Studio.


[1]: ./media/web-sites-dotnet-orchard-cms-gallery/orchardgallery-01.png
[2]: ./media/web-sites-dotnet-orchard-cms-gallery/orchardgallery-02.png
[3]: ./media/web-sites-dotnet-orchard-cms-gallery/orchardgallery-03.png
[4]: ./media/web-sites-dotnet-orchard-cms-gallery/orchardgallery-04.png
[5]: ./media/web-sites-dotnet-orchard-cms-gallery/orchardgallery-05.png
[7]: ./media/web-sites-dotnet-orchard-cms-gallery/orchardgallery-07.png
[12]: ./media/web-sites-dotnet-orchard-cms-gallery/orchardgallery-12.png
[13]: ./media/web-sites-dotnet-orchard-cms-gallery/orchardgallery-08.png


