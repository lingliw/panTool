<properties 
	pageTitle="Deploy a web app that is linked to a GitHub repository" 
	description="Use an Azure Resource Manager template to deploy a web app that contains a project from a GitHub repository." 
	services="app-service" 
	documentationCenter="" 
	authors="cephalin" 
	manager="wpickett" 
	editor=""/>

<tags 
	ms.service="app-service" 
	ms.workload="na" 
	ms.tgt_pltfrm="na" 
	ms.devlang="na" 
	ms.topic="article" 
	ms.date="04/27/2016" 
	wacn.date="" 
	ms.author="cephalin"/>

# Deploy a web app linked to a GitHub repository

In this topic, you will learn how to create an Azure Resource Manager template that deploys a web app that is linked to a project in a GitHub repository. You will learn how to define which resources are deployed and 
how to define parameters that are specified when the deployment is executed. You can use this template for your own deployments, or customize it to meet your requirements.

For more information about creating templates, see [Authoring Azure Resource Manager Templates](/documentation/articles/resource-group-authoring-templates/).

For the complete template, see [Web App Linked to GitHub template](https://github.com/Azure/azure-quickstart-templates/blob/master/201-web-app-github-deploy/azuredeploy.json).

> [AZURE.NOTE] Although this article refers to web apps, it also applies to API apps and mobile apps.
 

## What you will deploy

With this template, you will deploy a web app that contains the code from a project in GitHub.

## Parameters

With Azure Resource Manager, you define parameters for values you want to specify when the template is deployed. The template includes a section called Parameters that contains all of the parameter values.
You should define a parameter for those values that will vary based on the project you are deploying or based on the 
environment you are deploying to. Do not define parameters for values that will always stay the same. Each parameter value is used in the template to define the resources that are deployed. 

When defining parameters, use the **allowedValues** field to specify which values a user can provide during deployment. Use the **defaultValue** field to assign a value to the parameter, if no value is provided 
during deployment.

We will describe each parameter in the template.

### siteName

The name of the web app that you wish to create.

    "siteName":{
      "type":"string"
    }

### hostingPlanName

The name of the App Service plan to use for hosting the web app.
    
    "hostingPlanName":{
      "type":"string"
    }

### sku

The pricing tier for the hosting plan.

    "sku": {
      "type": "string",
      "allowedValues": [
        "F1",
        "D1",
        "B1",
        "B2",
        "B3",
        "S1",
        "S2",
        "S3",
        "P1",
        "P2",
        "P3",
        "P4"
      ],
      "defaultValue": "S1",
      "metadata": {
        "description": "The pricing tier for the hosting plan."
      }
    }

The template defines the values that are permitted for this parameter, and assigns a default value (S1) if no value is specified.

### workerSize

The instance size of the hosting plan (small, medium, or large).

    "workerSize":{
      "type":"string",
      "allowedValues":[
        "0",
        "1",
        "2"
      ],
      "defaultValue":"0"
    }
    
The template defines the values that are permitted for this parameter (0, 1, or 2), and assigns a default value (0) if no value is specified. The values correspond to small, medium and large.


### repoURL

The URL for GitHub repository that contains the project to deploy. This parameter contains a default value but this value is only intended to show you how to provide the URL for repository. You can use this value when testing the template but you will want to provide the URL your own repository when working with the template.

    "repoURL": {
        "type": "string",
        "defaultValue": "https://github.com/davidebbo-test/Mvc52Application.git"
    }

### branch

The branch of the repository to use when deploying the application. The default value is master, but you can provide the name of any branch in the repository that you wish to deploy.

    "branch": {
        "type": "string",
        "defaultValue": "master"
    }
    
## Resources to deploy

### App Service plan

Creates the service plan for hosting the web app. You provide the name of the plan through the **hostingPlanName** parameter. The location of the plan is the 
same location used for the resource group. The pricing tier and worker size are specified in the **sku** and **workerSize** parameters

    {
      "apiVersion": "2015-08-01",
      "name": "[parameters('hostingPlanName')]",
      "type": "Microsoft.Web/serverfarms",
      "location": "[resourceGroup().location]",
      "sku": {
        "name": "[parameters('sku')]",
        "capacity": "[parameters('workerSize')]"
      },
      "properties": {
        "name": "[parameters('hostingPlanName')]"
      }
    },



### Web app

Creates the web app that is linked to the project in GitHub. 

You specify the name of the web app through the **siteName** parameter, and the location of the web app through the **siteLocation** parameter. In the **dependsOn** element, the template defines the web app 
as dependent on the service hosting plan. Because it is dependent on the hosting plan, the web app is not created until the hosting plan has finished being created. The **dependsOn** element is only used to specify deployment 
order. If you do not mark the web app as dependent on the hosting plan, Azure Resource Mananger will attempt to create both resources at the same time and you may receive an error if the web app is created before the hosting 
plan.

The web app also has a child resource which is defined in **resources** section below. This child resource defines source control for the project deployed with the web app. In this template, the source control 
is linked to a particular GitHub repository. The GitHub repository is defined with the code **"RepoUrl":"https://github.com/davidebbo-test/Mvc52Application.git"** You might hard-code the repository URL when you want to create a template that repeatedly deploys a single project while requiring the minimum number of parameters.
Instead of hard-coding the repository URL, you can add a parameter for the repository URL and use that value for the **RepoUrl** property.

    {
      "apiVersion": "2015-08-01",
      "name": "[parameters('siteName')]",
      "type": "Microsoft.Web/sites",
      "location": "[resourceGroup().location]",
      "dependsOn": [
        "[resourceId('Microsoft.Web/serverfarms', parameters('hostingPlanName'))]"
      ],
      "properties": {
        "serverFarmId": "[parameters('hostingPlanName')]"
      },
      "resources": [
        {
          "apiVersion": "2015-08-01",
          "name": "web",
          "type": "sourcecontrols",
          "dependsOn": [
            "[resourceId('Microsoft.Web/Sites', parameters('siteName'))]"
          ],
          "properties": {
            "RepoUrl": "[parameters('repoURL')]",
            "branch": "[parameters('branch')]",
            "IsManualIntegration": true
          }
        }
      ]
    }

## Commands to run deployment


To deploy the resources to Azure, you must be logged in to your Azure account and you must use the Azure Resource Manager module. To learn about using Azure Resource Manager with either Azure PowerShell or Azure CLI, 
see:

- [Using Azure PowerShell with Azure Resource Manager](/documentation/articles/powershell-azure-resource-manager/)
- [Using the Azure CLI for Mac, Linux, and Windows with Azure Resource Management](/documentation/articles/xplat-cli-azure-resource-manager/).

The following examples assume you already have a resource group in your account with the specified name. 


### PowerShell

    New-AzureRmResourceGroupDeployment -TemplateUri https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/201-web-app-github-deploy/azuredeploy.json -siteName ExampleSite -hostingPlanName ExamplePlan -siteLocation "China North" -ResourceGroupName ExampleDeployGroup

### Azure CLI

    azure group deployment create --template-uri https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/201-web-app-github-deploy/azuredeploy.json


 
