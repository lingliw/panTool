<properties
	pageTitle="Move web site Resources to another Resource Group"
	description="Describes the scenarios where you can move web sites and Azure Websitess from one Resource Group to another."
	services="app-service"
	documentationCenter=""
	authors="ZainRizvi"
	manager="wpickett"
	editor=""/>

<tags
	ms.service="app-service"
	ms.date="10/29/2015"
	wacn.date=""/>
	
# Supported Move Configurations

You can move Azure web site resources using the [ARM Move Resources Api](/documentation/articles/resource-group-move-resources).

Azure web sites currently supports the following move scenarios:

* Moving the entire contents of a resource group (web sites, app service plans, and certificates) to another resource group 
	* Note: The destination resource group can not contain any Microsoft.Web resources in this scenario
* Moving individual web sites to a different resource group, while still hosting them in their current app service plan (the app service plan stays in the old resource group)
