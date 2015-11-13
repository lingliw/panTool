<properties
   pageTitle="Create a virtual network using an ARM template | Windows Azure"
   description="Learn how to create a virtual network using an ARM template | Resource Manager."
   services="virtual-network"
   documentationCenter=""
   authors="telmosampaio"
   manager="carolz"
   editor=""
   tags="azure-resource-manager"/>

<tags
	ms.service="virtual-network"
	ms.date="08/21/2015"
	wacn.date=""/>

# Create a virtual network by using an ARM template

[AZURE.INCLUDE [virtual-networks-create-vnet-selectors-arm-include](../includes/virtual-networks-create-vnet-selectors-arm-include.md)]

[AZURE.INCLUDE [virtual-networks-create-vnet-intro](../includes/virtual-networks-create-vnet-intro-include.md)]

[AZURE.INCLUDE [azure-arm-classic-important-include](../includes/azure-arm-classic-important-include.md)] This document covers creating a VNet by using the Resource Manager deployment model. You can also [create a virtual network in the classic deployment model](/documentation/articles/virtual-networks-create-vnet-classic-pportal).

You will learn how to download and modify and existing ARM template from GitHub, and deploy the template from GitHub, PowerShell, and the Azure CLI.

If you are simply deploying the ARM template directly from GitHub, without any changes, skip to [deploy a template from github](#deploy-the-arm-template-by-using-click-to-deploy).

[AZURE.INCLUDE [virtual-networks-create-vnet-scenario-include](../includes/virtual-networks-create-vnet-scenario-include.md)]

[AZURE.INCLUDE [virtual-networks-create-vnet-arm-template-include](../includes/virtual-networks-create-vnet-arm-template-include.md)]

[AZURE.INCLUDE [virtual-networks-create-vnet-arm-template-ps-include](../includes/virtual-networks-create-vnet-arm-template-ps-include.md)]

[AZURE.INCLUDE [virtual-networks-create-vnet-arm-template-cli-include](../includes/virtual-networks-create-vnet-arm-template-cli-include.md)]

[AZURE.INCLUDE [virtual-networks-create-vnet-arm-template-click-include](../includes/virtual-networks-create-vnet-arm-template-click-include.md)]