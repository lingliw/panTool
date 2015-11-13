<properties
	pageTitle="SharePoint Server 2013 farms in Azure | Windows Azure"
	description="Find the articles that describe how to set up a dev/test environment or a production SharePoint Server 2013 farm in Microsoft Azure."
	documentationCenter=""
	services="virtual-machines"
	authors="JoeDavies-MSFT"
	manager="timlt"
	editor=""
	tags="azure-service-management,azure-resource-manager"/>

<tags
	ms.service="virtual-machines"
	ms.date="09/08/2015"
	wacn.date=""/>

# SharePoint farms hosted in Azure infrastructure services

[AZURE.INCLUDE [learn-about-deployment-models](../includes/learn-about-deployment-models-include.md)] This article covers creating resources with the Resource Manager deployment model or the classic deployment model.

Set up your first or next dev/test or production SharePoint farm in Microsoft Azure infrastructure services, where you can take advantage of ease of configuration and the ability to quickly expand the farm to include new capacity or optimization of key functionality.

> [AZURE.NOTE] Microsoft has released the SharePoint Server 2016 IT Preview. To make this preview easy to install and test, you can use an Azure virtual machine gallery image with SharePoint Server 2016 IT Preview and its prerequisites pre-installed. For more information, see [Test the SharePoint Server 2016 IT Preview in Azure](http://azure.microsoft.com/blog/test-sharepoint-server-2016-it-preview-4/).

## Basic SharePoint dev/test farm

For virtual machines created using the classic deployment model, use the [SharePoint Server Farm](/documentation/articles/virtual-machines-sharepoint-farm-azure-preview) feature of the Azure preview portal to create a basic dev/test farm for an Internet-facing SharePoint website.

The automatically created environment consists of three servers for a domain controller, a SQL server, and the SharePoint server in a cloud-only Azure virtual network.

To create a similar configuration with the Resource Manager deployment model, use a template. See [Deploy a three-server SharePoint farm](/documentation/articles/virtual-machines-workload-template-sharepoint/#deploy-a-three-server-sharepoint-farm).

## High-availability SharePoint dev/test farm

For classic virtual machines, use the [SharePoint Server Farm](/documentation/articles/virtual-machines-sharepoint-farm-azure-preview) feature of the Azure preview portal to create a high-availability SharePoint dev/test farm for an Internet-facing SharePoint website.

The automatically created environment consists of nine servers in a cloud-only Azure virtual network: two for domain controllers, three for a SQL server cluster, two application-tier SharePoint servers, and two web-tier SharePoint servers.

To create a similar configuration with Resource Manager virtual machines, use a template. See [Deploy a nine-server SharePoint farm](/documentation/articles/virtual-machines-workload-template-sharepoint/#deploy-a-nine-server-sharepoint-farm).

## Hybrid cloud dev/test farm

With the [SharePoint intranet farm in a hybrid cloud dev/test environment](/documentation/articles/virtual-networks-setup-sharepoint-hybrid-cloud-testing), you create a simulated hybrid cloud configuration that hosts a simple, two-tier SharePoint farm, which you can use to test an intranet SharePoint farm hosted in Azure from your location on the Internet.

This configuration uses classic virtual machines.

## High-availability, intranet SharePoint production farm

With the deployment of [SharePoint 2013 with SQL Server AlwaysOn Availability Groups in Azure](/documentation/articles/virtual-machines-workload-intranet-sharepoint-overview), you build out a production-ready, high-availability, intranet SharePoint Server 2013 farm in Azure.

This configuration uses classic virtual machines.

## Additional resources

See these resources for additional SharePoint in Azure information and configurations:

- [Windows Azure Architectures for SharePoint 2013](https://technet.microsoft.com/zh-cn/library/dn635309.aspx)

- [Internet Sites in Windows Azure using SharePoint Server 2013](https://technet.microsoft.com/zh-cn/library/dn635307.aspx)

- [SharePoint Server 2013 Disaster Recovery in Windows Azure](https://technet.microsoft.com/zh-cn/library/dn635313.aspx)

- [Using Windows Azure Active Directory for SharePoint 2013 authentication](https://technet.microsoft.com/zh-cn/library/dn635311.aspx)

- [Deploy Office 365 Directory Synchronization (DirSync) in Windows Azure](https://technet.microsoft.com/zh-cn/library/dn635310.aspx)