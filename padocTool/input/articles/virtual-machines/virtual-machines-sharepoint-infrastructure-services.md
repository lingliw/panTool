<!-- rename to virtual-machines-windows-sharepoint-farm-structure -->

<properties
	pageTitle="SharePoint Server 2013 farms in Azure | Azure"
	description="Find the articles that describe how to set up a dev/test environment or a production SharePoint Server 2013 farm in Azure."
	documentationCenter=""
	services="virtual-machines"
	authors="JoeDavies-MSFT"
	manager="timlt"
	editor=""
	tags="azure-service-management,azure-resource-manager"/>

<tags
	ms.service="virtual-machines"
	ms.date="01/21/2016"
	wacn.date=""/>

# SharePoint farms hosted in Azure infrastructure services

[AZURE.INCLUDE [learn-about-deployment-models-both-include](../../includes/learn-about-deployment-models-both-include.md)]

Set up your first or next dev/test or production SharePoint Server 2013 farm in Azure infrastructure services, where you can take advantage of ease of configuration and the ability to quickly expand the farm to include new capacity or optimization of key functionality.

> [AZURE.NOTE] Microsoft has released the SharePoint Server 2016 IT Preview. To make this preview easy to install and test, you can use an Azure virtual machine gallery image with SharePoint Server 2016 IT Preview and its prerequisites pre-installed. For more information, see [Test the SharePoint Server 2016 IT Preview in Azure](https://azure.microsoft.com/blog/test-sharepoint-server-2016-it-preview-4/).

## Basic SharePoint dev/test farm

This automatically-created environment consists of three servers in a cloud-only Azure virtual network: a domain controller, a SQL server, and the SharePoint server.

See the [SharePoint 2013 non-HA Farm](https://azure.microsoft.com/marketplace/partners/sharepoint2013/sharepoint2013farmsharepoint2013-nonha/) item in the Azure gallery of the Azure portal. This creates a basic dev/test farm for an Internet-facing SharePoint website. See [Create SharePoint server farms](/documentation/articles/virtual-machines-sharepoint-farm-azure-preview/) for additional details.

You can also use an Azure Resource Manager template. See [SharePoint](/documentation/articles/virtual-machines-app-frameworks/).

> [AZURE.NOTE] The **SharePoint Server Farm** item in the Azure gallery of the Azure portal has been removed.

## High-availability SharePoint dev/test farm

This automatically-created environment consists of nine servers in a cloud-only Azure virtual network: two for domain controllers, three for a SQL server cluster, two application-tier SharePoint servers, and two web-tier SharePoint servers.

See the [SharePoint 2013 HA Farm](https://azure.microsoft.com/marketplace/partners/sharepoint2013/sharepoint2013farmsharepoint2013-ha/) item in the Azure gallery of the Azure portal. This creates a high-availability dev/test farm for an Internet-facing SharePoint website. See [Create SharePoint server farms](/documentation/articles/virtual-machines-sharepoint-farm-azure-preview/) for additional details.

You can also use an Azure Resource Manager template. See [Deploy a nine-server SharePoint farm](/documentation/articles/virtual-machines-workload-template-sharepoint/#deploy-a-nine-server-sharepoint-farm).

> [AZURE.NOTE] The **SharePoint Server Farm** item in the Azure gallery of the Azure portal has been removed.

## Hybrid cloud dev/test farm

With the [SharePoint intranet farm in a hybrid cloud dev/test environment](/documentation/articles/virtual-networks-setup-sharepoint-hybrid-cloud-testing/), you create a simulated hybrid cloud configuration that hosts a simple, two-tier SharePoint farm, which you can use to test an intranet SharePoint farm hosted in Azure from your location on the Internet.

This configuration uses the classic deployment model.

## High-availability, intranet SharePoint production farm

With the deployment of [SharePoint 2013 with SQL Server AlwaysOn Availability Groups in Azure](/documentation/articles/virtual-machines-workload-intranet-sharepoint-overview/), you build out a production-ready, high-availability, intranet SharePoint Server 2013 farm in Azure.

This configuration uses the classic deployment model.

## Next Step

- Discover additional [SharePoint 2013](https://technet.microsoft.com/zh-cn/library/dn635309.aspx) configurations in Azure infrastructure services.
