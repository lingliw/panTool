<!-- not suitable for Mooncake -->

<properties 
	pageTitle="How to Configure an Azure Websites Environment" 
	description="Configuration, management and monitoring of Azure Websites Environments" 
	services="app-service" 
	documentationCenter="" 
	authors="ccompy" 
	manager="stefsch" 
	editor=""/>

<tags
	ms.service="app-service"
	ms.date="09/11/2015"
	wacn.date=""/>

# Configuring an Azure Websites Environment #

## Overview ##

Azure Websites Environments is a new Premium Tier capability in the Azure Websites that offers new scaling and network access capabilities.  This new scale capability allows you to place an instance of the Azure Websites into your VNET.  If you are unfamiliar with the Azure Websites Environment (ASE) capability then read the document here [What is an Azure Websites Environment](/documentation/articles/app-service-app-service-environment-intro). For information on how to create an ASE read the document here [How to Create an Azure Websites Environment](/documentation/articles/app-service-web-how-to-create-an-app-service-environment). 

At a high level an Azure Websites Environment consists of several major components:

- Compute resources running in the Azure App Environment Hosted Service
- Storage
- Database
- A classic "v1" Virtual Network with at least one subnet
- subnet with the Azure App Environment hosted service running in it

To help manage and monitor your Azure Websites Environments you can access UI for that purpose from Browse -> Azure Websites Environments in the Azure preview portal. The initial release does have what you need to manage the system and will continue to improve with additional capabilities in coming weeks.  

![][1]

[AZURE.INCLUDE [app-service-web-to-api-and-mobile](../includes/app-service-web-to-api-and-mobile.md)] 

## Monitoring ##

There aren't many metrics capabilities available in the initial Preview release but they will be rolling out shortly.  Those metrics capabilities will help system administrators to make decisions on system scaling and operations.

Even now in the portal you can list all of the App Service Plans in the ASE as well as all of the web apps in the Azure Websites Environment.  To see either list go to Settings and select the item you are interested in.  

![][3]

In both lists you can see the Worker Pool assignment with how many instances and the size of the compute resource that is being used.  Details around the performance within an individual App Service Plan will be available the same as normal which is by opening up the App Service Plan UI.  

![][4]

## Compute Resources ##

The compute resources, Storage and Database are all operated by the Azure Websites.  The quantity and sizes of compute resources though are up to the user to decide.  

Regardless of the size of the compute resources, the minimum footprint has 2 Front End servers and 2 Workers.  An Azure Websites Environment can be configured to use up to 55 total compute resources.  Of those 55 compute resources, only 50 can be used to host workloads. The reason for that is two fold.  There are a minimum of 2 Front End compute resources.  That leaves up to 53 to support worker pool allocation. In order to provide fault tolerance though, you need to have an additional compute resource allocated according to the following rules:

- each worker pool needs at least one additional compute resource which cannot be assigned workload
- when the quantity of compute resources in a pool goes above a certain value then another compute resource is required

Within any single worker pool the fault tolerance requirements are that for a given value of X resources assigned to a worker pool:

- if X is between 2 to 20, the amount of usable compute resources you can use for workloads is X-1
- if X is between 21 to 40, the amount of usable compute resources you can use for workloads is X-2
- if X is between 41 to 53, the amount of usable compute resources you can use for workloads is X-3

In addition to being able to manage the quantity of compute resources that you can assign to a given pool you also have control over the size.  With Azure Websites Environments you can choose from 4 different sizes labeled P1 through P4.  For details around those sizes and their pricing please see here [Azure Websites Pricing](/documentation/articles/app-service-value-prop-what-is) The P1 to P3 compute resource sizes are the same as what is available normally.  The P4 compute resource gives 8 cores with 14 GB of RAM and is only available in an Azure Websites Environment.

As noted earlier, the Azure Websites Environment feature is currently in Preview and as such it still has room to grow.  In addition to additional monitoring capabilities, more management features will be rolled out as Azure Websites Environments moves to GA.  For now there are only a few things that can be managed in this interface:

- Number of compute resources in each pool
- Size of the compute resources in each pool
- Number of IP addresses available

To control these things select the Scale configuration item at the top.  

![][2]

The quantity of compute resources in each pool and their size can be adjusted here.  Before making any changes though it is important to note a few things:

- changes made can take hours to complete depending on how large is the change requested
- when there is already a Azure Websites Environment configuration change in work, you cannot start another change
- if you change the size of the compute resources used in a worker pool you can cause outages for the web apps running in that worker pool

Adding additional instances to a worker pool is a benign operation and does not incur a system impact.  Changing the size of the compute resource used in a worker pool is another story though.  To avoid any app down time during a size change to a worker pool it is best to:

- use an unused worker pool to bring up the instances required in the size desired
- scale the App Service Plans to the new worker pool.  
 
This is much less disruptive to running apps than changing the compute resource size with running workloads.  For details around scaling web apps in an Azure Websites Environment go here [Scaling Web Apps in an Azure Websites Environment](/documentation/articles/app-service-web-scale-a-web-app-in-an-app-service-environment)  

## Virtual Network ##

The [Virtual Network][virtualnetwork] and subnet are all under user control.  Azure Websites Environments does have a few network requirements but the rest is up to the user to control.  Those ASE requirements are:

- a classic "v1" VNET with at least 512 addresses
- a subnet with at least 8 addresses 
- the VNET must be a regional VNET  
 
Administering your VNET is done through the normal Virtual Network UI.

Because this capability places the Azure Websites into your VNET it means that your apps hosted in your ASE can now access resources made available through ExpressRoute or Site to Site VPNs directly.  The apps within your Azure Websites Environments do not require additional networking features to access resources available to the VNET hosting your Azure Websites Environment.  

If desired you can also now control access using Network Security Groups.  This capability allows you to lock down your Azure Websites Environment to just the IP addresses you wish to restrict it to.  For more information around how to do that see the document here [How to Control Inbound Traffic in an Azure Websites Environment](/documentation/articles/app-service-app-service-environment-control-inbound-traffic).

## Deleting an Azure Websites Environment ##

If you want to delete an Azure Websites Environment then simply use the Delete action at the top of the Azure Websites Environment blade.  You cannot delete an ASE though that has content in it.  Be sure to remove all web apps and App Service Plans in order to delete your Azure Websites Environment.  

## Getting started

To get started with Azure Websites Environments, see [How To Create An Azure Websites Environment](/documentation/articles/app-service-web-how-to-create-an-app-service-environment)

For more information about the Azure Websites platform, see [Azure Websites](/documentation/articles/app-service-value-prop-what-is).

[AZURE.INCLUDE [app-service-web-whats-changed](../includes/app-service-web-whats-changed.md)]

[AZURE.INCLUDE [app-service-web-try-app-service](../includes/app-service-web-try-app-service.md)]

<!--Image references-->
[1]: ./media/app-service-web-configure-an-app-service-environment/configureaseblade.png
[2]: ./media/app-service-web-configure-an-app-service-environment/configurescale.png
[3]: ./media/app-service-web-configure-an-app-service-environment/configureasplist.png
[4]: ./media/app-service-web-configure-an-app-service-environment/configurewebapplist.png

<!--Links-->
[WhatisASE]: /documentation/articles/app-service-app-service-environment-intro/
[Appserviceplans]: /documentation/articles/azure-web-sites-web-hosting-plans-in-depth-overview/
[HowtoCreateASE]: /documentation/articles/app-service-web-how-to-create-an-app-service-environment/
[HowtoScale]: /documentation/articles/app-service-web-scale-a-web-app-in-an-app-service-environment/
[ControlInbound]: /documentation/articles/app-service-app-service-environment-control-inbound-traffic/
[virtualnetwork]: /documentation/articles/virtual-networks-faq/
[AppServicePricing]: /home/features/app-service/#price 
[AzureAppService]: /documentation/articles/app-service-value-prop-what-is/
 
