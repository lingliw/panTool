<properties
	pageTitle="Web Apps overview | Azure"
	description="Learn how Azure App Service helps you develop and host web applications"
	services="app-service\web"
	documentationCenter=""
	authors="jaime-espinosa"
	manager="wpickett"
	editor=""/>

<tags
	ms.service="app-service-web"
	ms.workload="web"
	ms.tgt_pltfrm="na"
	ms.devlang="na"
	ms.topic="get-started-article"
	ms.date="08/26/2016"
	wacn.date=""
	ms.author="rachelap"/>

# Web Apps overview

*App Service Web Apps* is a fully managed compute platform that is optimized for hosting websites and web applications. This [platform-as-a-service](https://en.wikipedia.org/wiki/Platform_as_a_service) (PaaS) offering of Azure lets you focus on your business logic while Azure takes care of the infrastructure to run and scale your apps.

## What is a web app in App Service?

In App Service, a *web app* is the compute resources that Azure provides for hosting a website or web application.  

The compute resources may be on shared or dedicated virtual machines (VMs), depending on the pricing tier that you choose. Your application code runs in a managed VM that is isolated from other customers.

Your code can be in any language or framework that is supported by [Azure App Service](/documentation/articles/app-service-value-prop-what-is/), such as ASP.NET, Node.js, Java, PHP, or Python. You can also run scripts that use [PowerShell and other scripting languages](/documentation/articles/web-sites-create-web-jobs/#acceptablefiles) in a web app.

For examples of typical application scenarios that you can use Web Apps for, see the **Scenarios and recommendations** section of [Azure App Service, Virtual Machines, Service Fabric, and Cloud Services comparison](/documentation/articles/choose-web-site-cloud-service-vm/#scenarios).

## Why use Web Apps?

Here are some key features of App Service that apply to Web Apps:

- **Multiple languages and frameworks** - App Service has first-class support for ASP.NET, Node.js, Java, PHP, and Python. You can also run [PowerShell and other scripts or executables](/documentation/articles/web-sites-create-web-jobs/) on App Service VMs.

- **DevOps optimization** - Set up [continuous integration and deployment](/documentation/articles/app-service-continuous-deployment/) with Visual Studio Team Services, GitHub, or BitBucket. Promote updates through [test and staging environments](/documentation/articles/web-sites-staged-publishing/). Perform [A/B testing](/documentation/articles/app-service-web-test-in-production-get-start/). Manage your apps in App Service by using [Azure PowerShell](/documentation/articles/powershell-install-configure/) or the [cross-platform command-line interface (CLI)](/documentation/articles/xplat-cli-install/).
 
- **Global scale with high availability** - Scale [up](/documentation/articles/web-sites-scale/) or [out](/documentation/articles/insights-how-to-scale/) manually or automatically. Host your apps anywhere in Microsoft's global datacenter infrastructure, and the App Service [SLA](/support/sla/app-service/) promises high availability.

- **Connections to SaaS platforms and on-premises data** - Choose from more than 50 [connectors](/documentation/articles/apis-list/) for enterprise systems (such as SAP, Siebel, and Oracle), SaaS services (such as Salesforce and Office 365), and internet services. Access on-premises data using [Hybrid Connections](/documentation/articles/integration-hybrid-connection-overview/) and [Azure Virtual Networks](/documentation/articles/web-sites-integrate-with-vnet/).

- **Security and compliance** - App Service is [ISO, SOC, and PCI compliant](https://www.trustcenter.cn/).

- **Visual Studio integration** - Dedicated tools in Visual Studio streamline the work of creating, deploying, and debugging.

In addition, a web app can take advantage of features offered by [API Apps](/documentation/articles/app-service-api-apps-why-best-platform/) (such as CORS support) and [Mobile Apps](/documentation/articles/app-service-mobile-value-prop/) (such as push notifications). For more information about app types in App Service, see [Azure App Service overview](/documentation/articles/app-service-value-prop-what-is/).

Besides Web Apps in App Service, Azure offers other services that can be used for hosting websites and web applications. For most scenarios, Web Apps is the best choice.  For microservice architecture, consider [Service Fabric](/documentation/services/service-fabric), and if you need more control over the VMs that your code runs on, consider [Azure Virtual Machines](/documentation/services/virtual-machines/). For more information about how to choose between these Azure services, see [Azure App Service, Virtual Machines, Service Fabric, and Cloud Services comparison](/documentation/articles/choose-web-site-cloud-service-vm/).

## Getting started

To get started by deploying sample code to a new web app in App Service, follow the [Deploy your first web app to Azure in 5 minutes](/documentation/articles/app-service-web-get-started/) tutorial. You'll need a free Azure account.
