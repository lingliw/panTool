<!-- not suitable for Mooncake -->

<properties 
	pageTitle="Introduction to Azure Websites Environment" 
	description="Learn about the Azure Websites Environment feature that provides secure, VNet-joined, dedicated scale units for running all of your apps." 
	services="app-service" 
	documentationCenter="" 
	authors="ccompy" 
	manager="wpickett" 
	editor=""/>

<tags
	ms.service="app-service"
	ms.date="10/06/2015"
	wacn.date=""/>

# Introduction to Azure Websites Environment

## Overview ##
An Azure Websites Environment is a [Premium][PremiumTier] service plan option of Azure Websites that provides a fully isolated and dedicated environment for securely running Azure Websites apps at high scale, including [Web Apps][WebApps], [Mobile Apps][MobileApps], and [API Apps][APIApps].  

Azure Websites Environments are ideal for application workloads requiring:

- Very high scale
- Isolation and secure network access

Customers can create multiple Azure Websites Environments within a single Azure region, as well as across multiple Azure regions.  This makes Azure Websites Environments ideal for horizontally scaling state-less application tiers in support of high RPS workloads.

Azure Websites Environments are isolated to running only a single customer's applications, and are always deployed into a virtual network.  Customers have fine-grained control over both inbound and outbound application network traffic, and applications can establish high-speed secure connections over virtual networks to on-premises corporate resources.

For an overview of how Azure Websites Environments enable high scale and secure network access, see the [AzureCon Deep Dive][AzureConDeepDive] on Azure Websites Environments!

For a deep-dive on horizontally scaling using multiple Azure Websites Environments see the article on how to setup a [geo-distributed app footprint][GeodistributedAppFootprint].

To see how the security architecture shown in the AzureCon Deep Dive was configured, see the article on implementing a [layered security architecture](/documentation/articles/app-service-app-service-environment-layered-security) with Azure Websites Environments.

[AZURE.INCLUDE [app-service-web-to-api-and-mobile](../includes/app-service-web-to-api-and-mobile.md)] 

## Dedicated Compute Resources ##
All of the compute resources in an Azure Websites Environment are dedicated exclusively to a single subscription, and an Azure Websites Environment can be configured with up to fifty (50) compute resources for exclusive use by a single application.

An Azure Websites Environment is composed of a front-end compute resource pool, as well as one to three worker compute resource pools. 

The front-end pool contains compute resources responsible for SSL termination as well automatic load balancing of app requests within an Azure Websites Environment. 

Each worker pool contains compute resources allocated to [App Service Plans][AppServicePlan], which in turn contain one or more Azure Websites apps.  Since there can be up to three different worker pools in an Azure Websites Environment, you have the flexibility to choose different compute resources for each worker pool.  

For example this allows you to create one worker pool with less powerful compute resources for App Service Plans intended for development or test apps.  A second (or even third) worker pool could use more powerful compute resources intended for App Service Plans running production apps.

For more details on the quantity of compute resources available to the front-end and worker pools, see [How To Configure an Azure Websites Environment][HowToConfigureanAppServiceEnvironment].  

For details on the available compute resource sizes supported in an Azure Websites Environment, consult the [Azure Websites Pricing][AppServicePricing] page and review the available options for Azure Websites Environments in the Premium pricing tier.

## Virtual Network Support ##
An Azure Websites Environment can either be created in a pre-existing regional classic "v1" virtual network, or a new regional classic "v1" virtual network ([more info on virtual networks][MoreInfoOnVirtualNetworks]).  Since an Azure Websites Environment always exists in a regional virtual network, and more precisely within a subnet of a regional virtual network, you can leverage the security features of virtual networks to control both inbound and outbound network communications.  

You can use [network security groups][NetworkSecurityGroups] to restrict inbound network communications to the subnet where an Azure Websites Environment resides.  This allows you to run apps behind upstream devices and services such as web application firewalls, and network SaaS providers.  

Apps also frequently need to access corporate resources such as internal databases and web services.  A common approach is to make these endpoints available only to internal network traffic flowing within an Azure virtual network.  Once an Azure Websites Environment is joined to the same virtual network as the internal services, apps running in the environment can access them, including endpoints reachable via [Site-to-Site][SiteToSite] and [Azure ExpressRoute][ExpressRoute] connections.

For more details on how Azure Websites Environments work with virtual networks and on-premises networks consult the following articles on [Network Architecture][NetworkArchitectureOverview], [Controlling Inbound Traffic][ControllingInboundTraffic], and [Securely Connecting to Backends][SecurelyConnectingToBackends]. 

**Note:**  An Azure Websites Environment cannot be created in a "v2" virtual network.

## Getting started

To get started with Azure Websites Environments, see [How To Create An Azure Websites Environment][HowToCreateAnAppServiceEnvironment]

For more information about the Azure Websites platform, see [Azure Websites][AzureAppService].

For an overview of the Azure Websites Environment network architecture, see the [Network Architecture Overview][NetworkArchitectureOverview] article.

For details on using an Azure Websites Environment with ExpressRoute, see the following article on [Express Route and Azure Websites Environments][NetworkConfigDetailsForExpressRoute].

[AZURE.INCLUDE [app-service-web-whats-changed](../includes/app-service-web-whats-changed.md)]

[AZURE.INCLUDE [app-service-web-try-app-service](../includes/app-service-web-try-app-service.md)]

<!-- LINKS -->
[PremiumTier]: /home/features/app-service/#price
[MoreInfoOnVirtualNetworks]: /documentation/articles/virtual-networks-faq/
[AppServicePlan]: /documentation/articles/azure-web-sites-web-hosting-plans-in-depth-overview/
[Azure preview portal]: http://manage.windowsazure.cn
[HowToCreateAnAppServiceEnvironment]: /documentation/articles/app-service-web-how-to-create-an-app-service-environment/
[AzureAppService]: /documentation/articles/app-service-value-prop-what-is/
[WebApps]: /documentation/articles/app-service-web-overview/
[MobileApps]: /documentation/articles/app-service-mobile-value-prop-preview/
[APIApps]: /documentation/articles/app-service-api-apps-why-best-platform/
[LogicApps]: /documentation/articles/app-service-logic-what-are-logic-apps/
[AzureConDeepDive]:  https://azure.microsoft.com/documentation/videos/azurecon-2015-deploying-highly-scalable-and-secure-web-and-mobile-apps/
[GeodistributedAppFootprint]:  /documentation/articles/app-service-app-service-environment-geo-distributed-scale/
[NetworkSecurityGroups]: /documentation/articles/virtual-networks-nsg/
[SiteToSite]: /documentation/articles/vpn-gateway-site-to-site-create/
[ExpressRoute]: http://azure.microsoft.com/services/expressroute/
[HowToConfigureanAppServiceEnvironment]:  /documentation/articles/app-service-web-configure-an-app-service-environment/
[ControllingInboundTraffic]:  /documentation/articles/app-service-app-service-environment-control-inbound-traffic/
[SecurelyConnectingToBackends]:  /documentation/articles/app-service-app-service-environment-securely-connecting-to-backend-resources/
[NetworkArchitectureOverview]:  /documentation/articles/app-service-app-service-environment-network-architecture-overview/
[NetworkConfigDetailsForExpressRoute]:  /documentation/articles/app-service-app-service-environment-network-configuration-expressroute/
[AppServicePricing]: /home/features/app-service/#price 

<!-- IMAGES -->

 
