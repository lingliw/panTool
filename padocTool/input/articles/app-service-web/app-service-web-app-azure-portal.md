<!-- not suitable for Mooncake -->

<properties
	pageTitle="Reference for navigating the Azure Management Portal"
	description="Learn the different user experiences for Azure Websites Web between the management portal and the Azure Management Portal"
	services="app-service"
	documentationCenter=""
	authors="jaime-espinosa"
	manager="wpickett"
	editor="jimbe"/>

<tags
	ms.service="app-service"
	ms.date="09/15/2015"
	wacn.date=""/>

# Reference for navigating the Azure Management Portal

Azure Websites is now called [Azure Websites](/documentation/services/web-sites/). We're updating all of our documentation to reflect this name change and to provide instructions for the New Azure Management Portal. Until that process is done, you can use this document as a guide for working with Web Apps in the new Azure Management Portal.

[AZURE.INCLUDE [app-service-web-to-api-and-mobile](../includes/app-service-web-to-api-and-mobile.md)] 
 
## The future of the Management Portal

While you will notice the branding changes on the Management Portal, that portal is in the process of being replaced by the new Azure Management Portal. As the Management Portal is being phased out, the focus for new development is shifting to the new portal. All upcoming new features for Web Apps will come in the new portal. Start using the new portal to take advantage of the latest and greatest that Web Apps have to offer.

## Layout differences between the Management Portal and Azure Management Portal

In the Management Portal, all the Azure services are listed on the left hand side. Navigation in the Management Portal follows a tree structure, where you start from the service and navigate into each element. This structure works well when managing independent components. However, applications built on Azure are a collection of interconnected services, and this tree structure isn't ideal for working with collections of services. 

The new portal makes it easy to build applications end-to-end with components from multiple services. The new Azure Management Portal is organized as *journeys*. A *journey* is a series of *blades*, which are containers for the different components. For example, setting up auto-scaling for a web app is a *journey* which takes you several blades as shown in the following example: the **web-site** blade (that blade title has not yet been updated to use the new terminology), the **Settings** blade, and the **Scale** blade. In the example, auto scaling is being set up to depend on CPU usage, so there is also a **CPU Percentage** blade. The components within the *blades* are called *parts*, which look like tiles. 

![](./media/app-service-web-app-azure-portal/AutoScaling.png)

## Navigation example: create a web app

Creating new web apps is still as easy as 1-2-3. The following image shows the Management Portal and the new portal side-by-side to demonstrate that not much has changed in the number of steps needed to get a web app up and running. 

![](./media/app-service-web-app-azure-portal/CreateWebApp.png)

In the new portal you can choose from the most common types of web apps, including popular gallery applications like WordPress. For a full list of available applications, visit the [Azure Marketplace].

When you create a web app, you specify URL, App Service plan, and location in the new portal just as you do in the Management Portal. 

![](./media/app-service-web-app-azure-portal/CreateWebAppSettings.png)

In addition, the new portal lets you define other common settings. For example, [resource groups](/documentation/articles/resource-group-overview) make it simple to see and manage related Azure resources. 

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

Other than the brand name, a few things in the portal have been renamed or grouped differently to make it easier to find them. For example, below is a screenshot of the corresponding page for app settings (**Configure**) in the Management Portal.

![](./media/app-service-web-app-azure-portal/AppSettings.png)

## More Resources

[The Azure cloud application platform](/documentation/articles/app-service-cloud-app-platform)

[New portal]: https://manage.windowsazure.cn
[Azure Marketplace]: /marketplace/

>[AZURE.NOTE] If you want to get started with Azure Websites before signing up for an Azure account, go to [Try Azure Websites](http://go.microsoft.com/fwlink/?LinkId=523751), where you can immediately create a short-lived starter web app in Azure Websites. No credit cards required; no commitments.

## What's changed
* For a guide to the change from Websites to Azure Websites see: [Azure Websites and Its Impact on Existing Azure Services](/documentation/services/web-sites/)
* For a guide to the change of the Management Portal to the new portal see: [Reference for navigating the new portal](https://manage.windowsazure.cn/)
 
