<!-- deleted in Global -->

<properties
	pageTitle="SQL Server AlwaysOn with Azure Resource Manager template | Azure"
	description="Easily deploy five servers that support SQL Server AlwaysOn with a Resource Manager template and the Azure Management Portal, Azure PowerShell, or the Azure CLI."
	services="virtual-machines"
	documentationCenter=""
	authors="davidmu1"
	manager="timlt"
	editor=""
	tags="azure-resource-manager"/>

<tags
	ms.service="virtual-machines"
	ms.date="10/08/2015"
	wacn.date=""/>

# Deploy SQL Server AlwaysOn with an Azure Resource Manager template

> [AZURE.NOTE] Azure has two different deployment models for creating and working with resources:  [Resource Manager and classic](/documentation/articles/resource-manager-deployment-model/).  This article covers using the Resource Manager deployment model, which Azure recommends for most new deployments instead of the classic deployment model. You can't create this resource with the classic deployment model.

Use the instructions in this article to deploy SQL Server AlwaysOn using an Azure Resource Manager template. This template creates five virtual machines in a new virtual network on two different subnets.

![](./media/virtual-machines-workload-template-sql-alwayson/five-server-sqlao.png)

You can run the template with the Azure Management Portal, Azure PowerShell, or the Azure CLI.

## Azure Management Portal

To deploy this workload using an Azure Resource Manager template and the Azure Management Portal, click [here](https://manage.windowsazure.cn/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fsql-server-2014-alwayson-dsc%2Fazuredeploy.json).

![](./media/virtual-machines-workload-template-sql-alwayson/azure-portal-template.png)

1.	For the **Template** pane, click **Save**.
2.	Click **Parameters**. On the **Parameters** pane, enter new values, select from allowed values, or accept default values, and then click **OK**.
3.	If needed, click **Subscription** and select the correct Azure subscription.
4.	Click **Resource group** and select an existing resource group. Alternately, click **Or create new** to create a new one for this workload.
5.	If needed, click **Resource group location** and select the correct Azure location.
6.	If needed, click **Legal terms** to review the terms and agreement for using the template.
7.	Click **Create**.

Depending on the template, it can take some time for Azure to build the workload. When the template execution is complete, you have a new five-server SQL Server AlwaysOn configuration in your existing or new resource group.

## Azure PowerShell

[AZURE.INCLUDE [powershell-preview](../../includes/powershell-preview-inline-include.md)]

Fill in an Azure deployment name, a new Resource Group name, and an Azure datacenter location in the following set of commands. Remove everything within the quotes, including the < and > characters.

	$deployName="<deployment name>"
	$RGName="<resource group name>"
	$locName="<Azure location, such as China North>"
	$templateURI="https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/sql-server-2014-alwayson-dsc/azuredeploy.json"
	New-AzureRmResourceGroup -Name $RGName -Location $locName
	New-AzureRmResourceGroupDeployment -Name $deployName -ResourceGroupName $RGName -TemplateUri $templateURI

Here is an example.

	$deployName="TestDeployment"
	$RGName="TestRG"
	$locname="China North"
	$templateURI="https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/sql-server-2014-alwayson-dsc/azuredeploy.json"
	New-AzureRmResourceGroup -Name $RGName -Location $locName
	New-AzureRmResourceGroupDeployment -Name $deployName -ResourceGroupName $RGName -TemplateUri $templateURI

Next, run your command block in the Azure PowerShell prompt.

When you run the **New-AzureRmResourceGroupDeployment** command, you will be prompted to supply the values for a series of parameters. When you have specified all the parameter values, **New-AzureRmResourceGroupDeployment** creates and configures the virtual machines.

When the template execution is complete, you have a new five-server SQL Server AlwaysOn configuration in your new resource group.

## Azure CLI

Before you begin, make sure you have the right version of Azure CLI installed, you have logged in, and you have switched to the new Resource Manager mode. For the details, click [here](/documentation/articles/virtual-machines-deploy-rmtemplates-azure-cli/#getting-ready).

First, you create a new resource group. Use the following command and specify the name of the group and the Azure data center location into which you want to deploy.

	azure group create <group name> <location>

Next, use the following command and specify the name of your new resource group and the name of an Azure deployment.

	azure group deployment create --template-uri https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/sql-server-2014-alwayson-dsc/azuredeploy.json <group name> <deployment name>

Here is an example.

	azure group create sqlao chinaeast2
	azure group deployment create --template-uri https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/sql-server-2014-alwayson-dsc/azuredeploy.json sqlao sqldevtest

When you run the **azure group deployment create** command, you will be prompted to supply the values for a series of parameters. When you have specified all the parameter values, Azure creates and configures the virtual machines.

When the template execution is complete, you have a new five-server SQL Server AlwaysOn configuration in your new resource group.


## Additional resources

[Deploy and manage virtual machines using Azure Resource Manager templates and Azure PowerShell](/documentation/articles/virtual-machines-deploy-rmtemplates-powershell/)

[Azure Compute, Network and Storage providers under Azure Resource Manager](/documentation/articles/virtual-machines-azurerm-versus-azuresm/)

[Azure Resource Manager overview](/documentation/articles/resource-group-overview/)

[Deploy and manage Virtual Machines using Azure Resource Manager templates and the Azure CLI](/documentation/articles/virtual-machines-deploy-rmtemplates-azure-cli/)

[Virtual machines documentation](/documentation/services/virtual-machines/)

[How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure/)
