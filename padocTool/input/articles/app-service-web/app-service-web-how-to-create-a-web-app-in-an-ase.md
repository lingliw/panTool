<!-- not suitable for Mooncake -->

<properties
	pageTitle="How to Create a Web App in an Azure Websites Environment"
	description="Creation flow for web apps and app service plans examined for an app service environment"
	services="app-service"
	documentationCenter=""
	authors="ccompy"
	manager="stefsch"
	editor=""/>

<tags
	ms.service="app-service"
	ms.date="09/15/2015"
	wacn.date=""/>

# How to Create a Web App in an Azure Websites Environment #

Creating web apps is nearly the same in an Azure Websites Environments (ASE) as it is normally.  If you are unfamiliar with the Azure Websites Environment capability then read the document here [What is an Azure Websites Environment](/documentation/articles/app-service-app-service-environment-intro).

To create an web app in an ASE you need to first start by having an ASE.   For details around creating an ASE read the document here: [How to Create an Azure Websites Environment](/documentation/articles/app-service-web-how-to-create-an-app-service-environment).

The first step to creating a web app is selecting your Subscription.  If you have multiple subscriptions be aware that to create an app in your ASE, you need to use the same subscription that you used when creating the ASE. The next step involves selecting or creating a resource group.  If you are unfamiliar with resource groups there is more information here: [Managing your Azure resources][ResourceGroups].  Beyond helping to manage your resources, resource groups are also important when establishing RBAC rules for your apps.  

After you have selected your subscription and resource group you then need to create or select an App Service Plan (ASP).  If you need to create a new ASP in your ASE then you will need to provide a name for the ASP, select the ASE you want from Locations and to select the Worker Pool you want the ASP to be in.  This is described in greater detail below.  If you are selecting an ASP in an ASE the app creation flow is the same as creating an app normally.  This is by going through the web app creation flow starting with New -> Web + Mobile -> Web App.

![][1]


If you are using an App Service Plan that you have already created in your Azure Websites Environment, simply select that plan, enter the name for your web app and select Create.  It's the same flow as when you create a web app normally.  You can identify the ASPs in your ASE by looking at the location that is noted under the ASP name.  

![][5]

When you create an app it will will be reached at:

[*sitename*].[*name of your Azure Websites Environment*].p.chinacloudsites.cn

instead of

[*sitename*].chinacloudsites.cn

For now, your web app name needs to be unique across the entire Azure Websites.  This means you if you want to create a web app named "thisismywebapp" then there currently cannot be any other web app named "thisismywebapp" in the Azure Websites.  

### App Service Plans ###

App Service Plans are a managed set of your web apps.  When you select pricing, the price charged is applied to the App Service Plan rather than to the individual apps.  To scale up the number of instances of a web app you scale up the instances of your ASP and it affects all of the web apps in that plan.  Some features such as site slots or VNET Integration also have quantity restrictions within the plan.  You can learn more about App Service Plans from the document here: [App Service plans in-depth](/documentation/articles/azure-web-sites-web-hosting-plans-in-depth-overview)

If you are making a new App Service Plan, there are some differences to creating an ASP in an Azure Websites Environment.  Among other things, your worker choices are different as there are no shared workers in an ASE.  The workers you have to use are the ones that have been allocated to the ASE by the admin.  This means that to create a new ASP, you need to have more workers allocated to your ASE worker pool than the total number of instances across all of your ASPs already in that worker pool.  If you don't have enough workers in your ASE worker pool to create your ASP, you need to work with your ASE admin to get them added.

Another difference with Azure Websites Environment hosted ASPs is the lack of pricing selection.  When you have an Azure Websites Environment you are paying compute resources used by the system and do not have added charges for the ASPs in that environment.  Normally when you create an ASP you select a pricing plan which determines your billing.  An Azure Websites Environment is essentially a private location where you can create content.  You pay for the environment and not to host your content.

### Creating an ASP for your Azure Websites Environment ###

To create an ASP in an ASE you start by selecting Create New in the ASP selection UI and provide a name for your ASP just as you normally would outside of an ASE.  The next step is to select the ASE you wish to use from your location picker.  Because an Azure Websites Environment is essentially a private deployment location, it shows under Location. 

![][2]

After selection of an ASE in the location picker, the ASP creation UI will update.  The location will now show the name of the ASE system and the region it is in and the pricing plan picker is replaced with a worker pool picker.  

![][3]

### Selecting your worker pool ###

Normally in the Azure Websites and outside of an Azure Websites Environment, there are 3 compute sizes that are available with the selection of a dedicated price plan.  In a similar fashion, customers that own an ASE can define up to 3 pools of workers and specify the compute size that is used for that worker pool.  What that means for tenants is that instead of selecting a pricing plan with compute size for your ASP, you select what is called a Worker Pool.  

The worker pool selection UI shows the compute size used for that worker pool below the name.  The quantity available refers to how many compute instances are available for use in that pool.  The total pool may actually have more instances than this number but this value refers to simply how many are not in use.  If you need to adjust your Azure Websites Environment to add more compute resources see the doc here [Configuring your Azure Websites Environment](/documentation/articles/app-service-web-configure-an-app-service-environment).

![][4]

In this example you can see only two worker pools available. That is because the ASE administrator only allocated hosts into those two worker pools.  The third would show up when there are VMs allocated into it.  

### After web app creation ###

There are a few considerations to running web apps and managing ASPs in an ASE that need to be taken into account.  

As noted earlier, the owner of the ASE is responsible for the size of the system and as a result they are also responsible for ensuring that there is sufficient capacity to host the desired ASPs. If there are no available workers then you will not be able to create your ASP.  This is also true to scaling up your web app.  If you need more instances then you would have to get your Azure Websites Environment admin to add more workers.

After creating your web app and ASP it is a good idea to scale it up.  In an ASE you always need to have at least 2 instances of your ASP to provide fault tolerance for your apps.  Scaling an ASP in an ASE is the same as normal through the ASP UI.  For more details around scaling read the document here [How to scale a web app in an Azure Websites Environment](/documentation/articles/app-service-web-scale-a-web-app-in-an-app-service-environment)


[AZURE.INCLUDE [app-service-web-whats-changed](../includes/app-service-web-whats-changed.md)]

[AZURE.INCLUDE [app-service-web-try-app-service](../includes/app-service-web-try-app-service.md)]

<!--Image references-->
[1]: ./media/app-service-web-how-to-create-a-web-app-in-an-ase/createaspnewwebapp.png
[2]: ./media/app-service-web-how-to-create-a-web-app-in-an-ase/createasplocation.png
[3]: ./media/app-service-web-how-to-create-a-web-app-in-an-ase/createaspselected.png
[4]: ./media/app-service-web-how-to-create-a-web-app-in-an-ase/createaspworkerpool.png
[5]: ./media/app-service-web-how-to-create-a-web-app-in-an-ase/selectaspinase.png

<!--Links-->
[WhatisASE]: /documentation/articles/app-service-app-service-environment-intro/
[Appserviceplans]: /documentation/articles/azure-web-sites-web-hosting-plans-in-depth-overview/
[HowtoCreateASE]: /documentation/articles/app-service-web-how-to-create-an-app-service-environment/
[HowtoScale]: /documentation/articles/app-service-web-scale-a-web-app-in-an-app-service-environment
[HowtoConfigureASE]: /documentation/articles/app-service-web-configure-an-app-service-environment
[ResourceGroups]: /documentation/articles/resource-group-portal/
[AzurePowershell]: /documentation/articles/powershell-install-configure/
