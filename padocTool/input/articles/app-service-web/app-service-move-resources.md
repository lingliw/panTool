<!-- not suitable for Mooncake -->

<properties
	pageTitle="Move Web App Resources to another Resource Group"
	description="Describes the scenarios where you can move Web Apps and Azure Websites from one Resource Group to another."
	services="app-service"
	documentationCenter=""
	authors="ZainRizvi"
	manager="wpickett"
	editor=""/>

<tags
	ms.service="app-service"
	ms.date="07/28/2015"
	wacn.date=""/>
	
# Supported Move Configurations

You can move Azure Web App resources using the [ARM Move Resources Api](/documentation/articles/resource-group-move-resources).

Azure Web Apps currently supports the following move scenarios:

* Moving the entire contents of a resource group (web apps, app service plans, and certificates) to another resource group 
	* Note: The destination resource group can not contain any Microsoft.Web resources in this scenario
* Moving individual web apps to a different resource group, while still hosting them in their current app service plan (the app service plan stays in the old resource group)
