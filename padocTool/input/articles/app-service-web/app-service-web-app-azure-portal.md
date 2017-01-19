<properties
	pageTitle="Reference for navigating the Azure Portal Preview"
	description="Learn the different user experiences for App Service Web between the management portal and the Azure Portal Preview"
	services="app-service"
	documentationCenter=""
	authors="jaime-espinosa"
	manager="wpickett"
	editor="jimbe"/>

<tags
	ms.service="app-service"
	ms.workload="na"
	ms.tgt_pltfrm="na"
	ms.devlang="na"
	ms.topic="article"
	ms.date="02/26/2016"
	wacn.date=""
	ms.author="jaime-espinosa"/>

# Reference for navigating the Azure Portal Preview

Azure Websites are now called [App Service Web Apps](/documentation/articles/app-service-changes-existing-services/). We're updating all of our documentation to reflect this name change and to provide instructions for the Azure Portal Preview. Until that process is done, you can use this document as a guide for working with Web Apps in the Azure Portal Preview.

> [AZURE.NOTE] Although this article refers to web apps, it also applies to API apps and mobile apps.
 
 
## The future of the Azure Classic Management Portal

While you will notice the branding changes on the Azure Classic Management Portal, that portal is in the process of being replaced by the Azure Portal Preview. As the Classic Management Portal is being phased out, the focus for new development is shifting to the Azure Portal Preview. All upcoming new features for Web Apps will come in the Azure Portal Preview. Start using the Azure Portal Preview to take advantage of the latest and greatest that Web Apps have to offer.

## Layout differences between the Azure Classic Management Portal and Azure Portal Preview

In the Classic Management Portal, all the Azure services are listed on the left hand side. Navigation in the Classic Management Portal follows a tree structure, where you start from the service and navigate into each element. This structure works well when managing independent components. However, applications built on Azure are a collection of interconnected services, and this tree structure isn't ideal for working with collections of services. 

The Azure Portal Preview makes it easy to build applications end-to-end with components from multiple services. The portal is organized as *journeys*. A *journey* is a series of *blades*, which are containers for the different components. For example, setting up auto-scaling for a web app is a *journey* which takes you several blades as shown in the following example: the **web-site** blade (that blade title has not yet been updated to use the new terminology), the **Settings** blade, and the **Scale out** blade. In the example, auto scaling is being set up to depend on CPU usage, so there is also a **CPU Percentage** blade. The components within the *blades* are called *parts*, which look like tiles. 

![](./media/app-service-web-app-azure-portal/AutoScaling.png)

## Navigation example: create a web app

Creating new web apps is still as easy as 1-2-3. The following image shows the Classic Management Portal and the portal side-by-side to demonstrate that not much has changed in the number of steps needed to get a web app up and running. 

![](./media/app-service-web-app-azure-portal/CreateWebApp.png)

In the portal you can choose from the most common types of web apps, including popular gallery applications like WordPress. For a full list of available applications, visit the [Azure Marketplace].

When you create a web app, you specify URL, App Service plan, and location in the portal just as you do in the Classic Management Portal. 

![](./media/app-service-web-app-azure-portal/CreateWebAppSettings.png)

In addition, the portal lets you define other common settings. For example, [resource groups](/documentation/articles/resource-group-overview/) make it simple to see and manage related Azure resources. 

## Navigation example: settings and features

All the settings and features are now logically grouped in a single blade, from which you can navigate.

![](./media/app-service-web-app-azure-portal/WebAppSettings.png)

For example, you can create custom domains by clicking **Custom domains and SSL** in the **Settings** blade.

![](./media/app-service-web-app-azure-portal/ConfigureWebApp.png)

To set up a monitoring alert, click **Requests and errors** and then **Add Alert**.

![](./media/app-service-web-app-azure-portal/Monitoring.png)

To enable diagnostics, click **Diagnostics logs** in the **Settings** blade.

![](./media/app-service-web-app-azure-portal/Diagnostics.png)
 
To configure application settings, click **Application settings** in the **Settings** blade. 

![](./media/app-service-web-app-azure-portal/AppSettingsPreview.png)

Other than the brand name, a few things in the portal have been renamed or grouped differently to make it easier to find them. For example, below is a screenshot of the corresponding page for app settings (**Configure**) in the Classic Management Portal.

![](./media/app-service-web-app-azure-portal/AppSettings.png)

## More Resources

[Azure Portal Preview]: https://portal.azure.cn
[Azure Marketplace]: /marketplace/

## What's changed
* For a guide to the change from Websites to App Service see: [Azure App Service and Its Impact on Existing Azure Services](/documentation/articles/app-service-changes-existing-services/)
 
