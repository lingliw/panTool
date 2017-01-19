<properties
	pageTitle="Deploy an ASP.NET app to Azure using Visual Studio | Azure"
	description="Learn how to deploy an ASP.NET web project to a new web app in Azure, using Visual Studio."
	services="app-service\web"
	documentationCenter=".net"
	authors="tdykstra"
	manager="wpickett"
	editor=""/>

<tags
	ms.service="app-service-web"
	ms.date="04/22/2016"
	wacn.date=""/>

# Deploy an ASP.NET web app to Azure, using Visual Studio

> [AZURE.SELECTOR]
- [.NET](/documentation/articles/web-sites-dotnet-get-started)
- [Node.js](/documentation/articles/app-service-web-nodejs-get-started)
- [Python](/documentation/articles/web-sites-python-ptvs-django-mysql)
- [Java](/documentation/articles/web-sites-java-get-started)


## Overview

This tutorial shows how to deploy an ASP.NET web application to a [web app in Azure](/home/features/web-site) by using Visual Studio 2015.

The tutorial assumes that you are an ASP.NET developer who has no previous experience with using Azure. When you're finished, you'll have a simple web application up and running in the cloud.

You'll learn:

* How to create a new web project in Visual Studio.
* How to deploy a web project to an Azure web app by using Visual Studio.

At the end of the tutorial, a [Troubleshooting](#troubleshooting) section gives ideas on what to do if something doesn't work, and a [Next steps](#next-steps) section provides links to other tutorials that go into more depth about how to use Azure Web App.

As this is a getting-started tutorial, the web project it shows how to deploy is a simple one that doesn't use a database and doesn't do authentication or authorization. For links to more advanced deployment topics, see [How to deploy an Azure web app](/documentation/articles/web-sites-deploy).

Apart from the time required to install the Azure SDK for .NET, this tutorial will take about 10-15 minutes to complete.

## Prerequisites

* The tutorial assumes you have worked with ASP.NET MVC and Visual Studio. If you need an introduction, see [Getting Started with ASP.NET MVC 5](http://www.asp.net/mvc/overview/getting-started/introduction/getting-started).

* You need an Azure account. You can [open a trial Azure account](/pricing/1rmb-trial/?WT.mc_id=A261C142F). 

## <a name="setupdevenv"></a>Set up the development environment

The tutorial is written for Visual Studio 2015 with the Azure SDK for .NET 2.9 or later. 

* [Download the latest Azure SDK for Visual Studio 2015](http://go.microsoft.com/fwlink/?linkid=518003). The SDK installs Visual Studio 2015 if you don't already have it.

	>[AZURE.NOTE] Depending on how many of the SDK dependencies you already have on your machine, installing the SDK could take a long time, from several minutes to a half hour or more.

If you have Visual Studio 2013 and prefer to use that, you can [download the latest Azure SDK for Visual Studio 2013](http://go.microsoft.com/fwlink/?LinkID=324322). Some screens may look different from the illustrations.

## Configure a new web project

Your next step is to create a web project in Visual Studio and a web app in Azure. In this section of the tutorial you configure the new web project. 

1. Open Visual Studio 2015.

2. Click **File > New > Project**.

3. In the **New Project** dialog box, click **Visual C# > Web > ASP.NET Web Application**.

3. Make sure that **.NET Framework 4.5.2** is selected as the target framework.

4. Name the application **MyExample**, and then click **OK**.

	![New Project dialog box](./media/web-sites-dotnet-get-started/GS13newprojdb.png)

5. In the **New ASP.NET Project** dialog box, select the **MVC** template, and then click **Change Authentication**.

	For this tutorial, you deploy an ASP.NET MVC web project. If you want to learn how to deploy an ASP.NET Web API project, see the [Next steps](#next-steps) section. 

	![New ASP.NET Project dialog box](./media/web-sites-dotnet-get-started/GS13changeauth.png)

6. In the **Change Authentication** dialog box, click **No Authentication**, and then click **OK**.

	![No Authentication](./media/web-sites-dotnet-get-started/GS13noauth.png)

	For this getting-started tutorial you're deploying a simple app that doesn't do user log-in.

5. In the **Azure** section of the **New ASP.NET Project** dialog box, make sure that **Host in the cloud** is NOT selected.

	![New ASP.NET Project dialog box](./media/web-sites-dotnet-get-started/GS13newaspnetprojdb.png)

	Azure China currently does not support create or manage websits in Visual Studio. Hence, you need to go to the [Management Portal](https://manage.windowsazure.cn/) to create a new Azure web app

6. Click **OK**

##<a name="deploy-the-application-to-azure"></a> Deploy the project to the web site

In this section you deploy web project to the web app.

1. In the [Management Portal](https://manage.windowsazure.cn/), create a new website or choose an exited website.

2. Click the **Dashboard** of the website. Under the **quick glance**, click **Download publish profile**.

3. In Visual Studio, right click you project and choose **Publish**

	![choose "publish"](./media/web-sites-dotnet-get-started/choosepublish.png)

	In a few seconds, the **Publish Web** wizard appears.

4. In **Publish Profile**, click **Import**, and choose the publish profile downloaded above.

	Settings that Visual Studio needs to deploy your project to Azure have been imported. You can use the wizard to review and change those settings.

8. On the **Connection** tab of the **Publish Web** wizard, click **Next**.

	![Successfully validated connection](./media/web-sites-dotnet-get-started/GS13ValidateConnection.png)

10. On the **Settings** tab, click **Next**.

	You can accept the default values for **Configuration** and **File Publish Options**.

	You can use the **Configuration** drop-down to deploy a Debug build for remote debugging. The [Next steps](#next-steps) section links to a tutorial that shows how to run Visual Studio in debug mode remotely.

	![Settings tab](./media/web-sites-dotnet-get-started/GS13SettingsTab.png)

11. On the **Preview** tab, click **Publish**.

	![Preview tab of Publish Web wizard](./media/web-sites-dotnet-get-started/GS13previewoutput.png)

	When you click **Publish**, Visual Studio begins the process of copying the files to the Azure server. This may take a minute or two.

	The **Output** and **Azure Activity** windows show what deployment actions were taken and report successful completion of the deployment.

	![Visual Studio Output window reporting successful deployment](./media/web-sites-dotnet-get-started/PublishOutput.png)

	Upon successful deployment, the default browser automatically opens to the URL of the deployed web app, and the application that you created is now running in the cloud. The URL in the browser address bar shows that the web app is loaded from the Internet.

	![Web app running in Azure](./media/web-sites-dotnet-get-started/GS13deployedsite.png)

	> [AZURE.TIP] You can enable the **Web One Click Publish** toolbar for quick deployment. Click **View > Toolbars**, and then select **Web One Click Publish**. You can use the toolbar to select a profile, click a button to publish, or click a button to open the **Publish Web** wizard.
	> ![Web One Click Publish Toolbar](./media/web-sites-dotnet-get-started/weboneclickpublish.png)

## Troubleshooting

If you run into a problem as you go through this tutorial, make sure that you're using the latest version of the Azure SDK for .NET. The easiest way to do that is to [download the Azure SDK for Visual Studio 2015](http://go.microsoft.com/fwlink/?linkid=518003). If you have the current version installed, the Web Platform Installer lets you know that no installation is needed.

If you're on a corporate network and are trying to deploy to Azure through a firewall, make sure that ports 443 and 8172 are open for Web Deploy. If you can't open those ports, see the following Next steps section for other deployment options.

After you have your ASP.NET web app running in Azure Web App, you might want to learn more about Visual Studio features that simplify troubleshooting. For information about logging, remote debugging, and more, see  [Troubleshooting Azure web apps in Visual Studio](/documentation/articles/web-sites-dotnet-troubleshoot-visual-studio).

##<a name="next-steps"></a> Next steps

In this tutorial, you've seen how to create a simple web application and deploy it to an Azure web app. Here are some related topics and resources for learning more about Azure Web App:

* Monitor and manage your web app in the [Azure Classic Portal](https://manage.windowsazure.cn/). 

	For more information, see [Configure web apps in Azure](/documentation/articles/web-sites-configure).

* Deploy a web project from source control

	For information about [automating deployment](http://www.asp.net/aspnet/overview/developing-apps-with-windows-azure/building-real-world-cloud-apps-with-windows-azure/continuous-integration-and-continuous-delivery) from a [source control system](http://www.asp.net/aspnet/overview/developing-apps-with-windows-azure/building-real-world-cloud-apps-with-windows-azure/source-control), see [Get started with web apps in Azure](/documentation/articles/app-service-web-get-started) and [How to deploy an Azure web app](/documentation/articles/web-sites-deploy).

* Deploy an ASP.NET Web API to an API app in Azure

	You've seen how to create an instance of Azure that is mainly intended to host a website. Azure also offers features for hosting Web APIs, such as CORS support and API metadata support for client code generation. You can use API features in a web app, but if you mainly want to host an API in an instance of Azure Web App, an **API app** would be a better choice.

* Add a custom domain name and SSL

	For information about how to use SSL and your own domain (for example, www.contoso.com instead of contoso.chinacloudsites.cn), see the following resources:

	* [Configure a custom domain name in Azure Web App](/documentation/articles/web-sites-custom-domain-name)
	* [Enable HTTPS for an Azure website](/documentation/articles/web-sites-configure-ssl-certificate)

* Delete the resource group that contains your web app and any related Azure resources when you're done with them.

	For information about how to work with resource groups in the Azure portal, see [Using the Azure Portal to deploy and manage your Azure resources](/documentation/articles/resource-group-portal).