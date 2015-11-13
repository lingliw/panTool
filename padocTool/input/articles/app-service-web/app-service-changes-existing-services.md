<!-- not suitable for Mooncake -->

<properties 
	pageTitle="Azure Websites and its impact on existing Azure services" 
	description="Explains how the new Azure Websites and its features impact existing services in Azure." 
	authors="yochayk" 
	writer="yochayk" 
	editor="yochayk" 
	manager="nirma" 
	services="app-service" 
	documentationCenter=""/>

<tags
	ms.service="app-service"
	ms.date="09/15/2015"
	wacn.date=""/>


# Azure Websites and existing Azure services

This article outlines the changes to existing Azure services as part of the change to bring together several Azure services into [Azure Websites](/home/features/app-service/), a new integrated offering.

[AZURE.INCLUDE [app-service-web-to-api-and-mobile](../includes/app-service-web-to-api-and-mobile.md)] 

## Overview 

[Azure Websites](/home/features/app-service/) is a new and unique cloud service that enables developers to create web and mobile apps for any platform and any device. Azure Websites is an integrated solution designed to streamline repeated coding functions, integrate with enterprise and SaaS systems, and automate business processes while meeting your needs for security, reliability, and scalability.

Azure Websites brings together the following existing Azure services - [Websites](/home/features/websites/), [Mobile Services](/home/features/mobile-services/), and [Biztalk Services](/home/features/biztalk-services/) into a single combined service, while adding powerful new capabilities.  Azure Websites allows you to host the following app types: 

-   Web Apps
-   Mobile Apps
-   API Apps
-   Logic Apps

The following table explains how existing Azure services map to Azure Websites and the app types available within it.

<table>
<thead>
<tr class="header">
<th align="left", style="width:10%">Existing Azure Service</th>
<th align="left", style="width:10%">Azure Websites</th>
<th align="left", style="width:80%">What changed</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Azure Websites</td>
<td align="left">Web Apps</td>
<td align="left"><li>For Azure Websites, Azure Websites is strictly limited to changing the name  Websites to Web Apps.
<p><li>All your existing instances of Websites are now Web Apps in Azure Websites.</p>
<p><li>You can access your existing websites via the <a href="https://manage.windowsazure.cn/">Azure Management Portal</a>, where you will find all your existing sites under <em>Web Apps</em>.</p>
<p><li><em>Web Hosting Plan</em> is now <em>App Service Plan</em>. An <em>App Service Plan</em> can host any app type of Azure Websites, such as Web, Mobile, Logic, or API apps.</p>
<p><li>Azure Websites is in General Availability.</p>
<p><li><a href="/home/features/app-service/web/">Learn more about Web Apps</a>.</p></td>
</tr>
<tr class="even">
<td align="left">Azure Mobile Services</td>
<td align="left">Mobile Apps</td>
<td align="left"><p><li>Mobile Services continue to be available as a standalone service and remain fully supported.</p>
<p><li>Mobile Apps is a new app type in Azure Websites, which integrates all of the functionality of Mobile Services and more. Mobile Apps is in public preview.</p>
<p><li>It is easy to <a href="/documentation/articles/app-service-mobile-dotnet-backend-migrating-from-mobile-services-preview/">migrate from Mobile Services to Mobile Apps</a>. Since Mobile Apps are still in preview it is not yet recommended for running production apps.</p>
<p><li>As part of Azure Websites, Mobile Apps get new capabilities beyond Mobile Services, such as  integration with on-premises and SaaS systems, staging slots, WebJobs, better scaling options, and more.</p>
<p><li><a href="/home/features/app-service/mobile/">Learn more about Mobile Apps</a>.</p>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left">API Apps</td>
<td align="left">
<p><li>API Apps is a new app type in Azure Websites that lets you easily build and consume APIs in the cloud.</p>
<p><li><a href="/home/features/app-service/api/">Learn more about API Apps</a>.</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left">Logic Apps</td>
<td align="left">
<p><li>Logic Apps is a new app type in Azure Websites that lets you easily automate business process.</p>
<p><li><a href="/home/features/app-service/logic/">Learn more about Logic Apps</a>.</p></td>
</tr>
<tr class="odd">
<td align="left">Azure BizTalk Services</td>
<td align="left">BizTalk API Apps</td>
<td align="left">
<li><p>BizTalk Services continue to be available as a standalone service and remain fully supported.</p>
<li><p>All the capabilities of BizTalk Services are integrated into Azure Websites as API Apps enabling users to perform enterprise application integration and B2B integration scenarios with any of the app types in Azure Websites</p>
<li><p>With Logic Apps you can now automate business processes using a visual design experience to create workflows</p></td>
</tr>
</tbody>
</table>

To learn more, please visit [Azure Websites documentation](/documentation/services/web-sites/).
 