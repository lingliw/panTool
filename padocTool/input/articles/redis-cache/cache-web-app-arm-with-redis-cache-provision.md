<properties 
	pageTitle="Provision web site with Redis Cache" 
	description="Use Azure Resource Manager template to deploy web site with Redis Cache." 
	services="app-service" 
	documentationCenter="" 
	authors="tfitzmac" 
	manager="wpickett" 
	editor=""/>

<tags
	ms.service="app-service"
	ms.date="12/16/2015"
	wacn.date=""/>

# Create a web site plus Redis Cache using a template

In this topic, you will learn how to create an Azure Resource Manager template that deploys an Azure web site with Redis cache. You will learn how to define which resources are deployed and 
how to define parameters that are specified when the deployment is executed. You can use this template for your own deployments, or customize it to meet your requirements.

For more information about creating templates, see [Authoring Azure Resource Manager Templates](/documentation/articles/resource-group-authoring-templates).

For the complete template, see [web site with Redis Cache template](https://github.com/Azure/azure-quickstart-templates/blob/master/201-web-app-with-redis-cache/azuredeploy.json).

## What you will deploy

In this template, you will deploy:

- Azure web site
- Azure Redis Cache.


## Parameters to specify

With Azure Resource Manager, you define parameters for values you want to specify when the template is deployed. The template includes a section called Parameters that contains all of the parameter values.
You should define a parameter for those values that will vary based on the project you are deploying or based on the 
environment you are deploying to. Do not define parameters for values that will always stay the same. Each parameter value is used in the template to define the resources that are deployed. 

When defining parameters, use the **allowedValues** field to specify which values a user can provide during deployment. Use the **defaultValue** field to assign a value to the parameter, if no value is provided 
during deployment.

We will describe each parameter in the template.

### siteName

The name of the web site that you wish to create.

    "siteName":{
      "type":"string"
    }

### hostingPlanName

The name of the App Service plan to use for hosting the web site.
    
    "hostingPlanName":{
      "type":"string"
    }

### siteLocation

The location to use for creating the web site and hosting plan. It must be one of the Azure locations that support web sites.

    "siteLocation":{
      "type":"string"
    }

### sku

The pricing tier for the hosting plan.

    "sku":{
      "type":"string",
      "allowedValues":[
        "Free",
        "Shared",
        "Basic",
        "Standard"
      ],
      "defaultValue":"Free"
    }

The template defines the values that are permitted for this parameter (Free, Shared, Basic, or Standard), and assigns a default value (Free) if no value is specified.

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



### redisCacheName

The name of the Azure Redis Cache to create.

    "redisCacheName": {
      "type": "string"
    }

### redisCacheSKU

The pricing tier of the new Azure Redis Cache.

    "redisCacheSKU": {
      "type": "string",
      "allowedValues": [ "Basic", "Standard" ],
      "defaultValue": "Standard"
    }

The template defines the values that are permitted for this parameter (Basic or Standard), and assigns a default value (Standard) if no value is specified. Basic provides a single node with multiple sizes available up to 53 GB.
Standard provides two-node Primary/Replica with multiple sizes available up to 53 GB and 99.9% SLA.

### redisCacheFamily

The family for the sku.

    "redisCacheFamily": {
      "type": "string",
      "defaultValue": "C"
    }

### redisCacheCapacity

The size of the new Azure Redis Cache instance. 

    "redisCacheCapacity": {
      "type": "int",
      "allowedValues": [ 0, 1, 2, 3, 4, 5, 6 ],
      "defaultValue": 1
    }

The template defines the values that are permitted for this parameter (0, 1, 2, 3, 4, 5 or 6), and assigns a default value (1) if no value is specified. Those numbers correspond to following cache sizes: 
0 = 250 MB, 1 = 1 GB, 2 = 2.5 GB, 3 = 6 GB, 4 = 13 GB, 5 = 26 GB, 6 = 53 GB

### redisCacheVersion

The Redis server version of the new cache.

    "redisCacheVersion": {
      "type": "string",
      "defaultValue": "2.8"
    }




## Resources to deploy

### App Service plan

Creates the service plan for hosting the web site. You provide the name of the plan through the **hostingPlanName** parameter. The location of the plan is the 
same location used for the web site. The pricing tier and worker size are specified in the **sku** and **workerSize** parameters

    {
      "apiVersion": "2014-06-01",
      "name": "[parameters('hostingPlanName')]",
      "type": "Microsoft.Web/serverfarms",
      "location": "[parameters('siteLocation')]",
      "properties": {
        "name": "[parameters('hostingPlanName')]",
        "sku": "[parameters('sku')]",
        "workerSize": "[parameters('workerSize')]",
        "numberOfWorkers": 1
      }
    },


### Redis Cache

Creates the Azure Redis Cache that is used with the web site. The name of the cache is specified in the **redisCacheName** parameter.

The template creates the cache in the same location as the web site, which is recommended for best performance. 

    {
      "apiVersion": "2014-04-01-preview",
      "name": "[parameters('redisCacheName')]",
      "type": "Microsoft.Cache/Redis",
      "location": "[parameters('siteLocation')]",
      "properties": {
        "sku": {
          "name": "[parameters('redisCacheSKU')]",
          "family": "[parameters('redisCacheFamily')]",
          "capacity": "[parameters('redisCacheCapacity')]"
        },
        "redisVersion": "[parameters('redisCacheVersion')]",
        "enableNonSslPort": true
      }
    }

### web site

Creates the web site with name specified in the **siteName** parameter.

Notice that the web site is configured with app setting properties that enable it to work with the Redis Cache. This app settings are dynamically created based on values provided during deployment.
        
    {
      "apiVersion": "2015-04-01",
      "name": "[parameters('siteName')]",
      "type": "Microsoft.Web/sites",
      "location": "[parameters('siteLocation')]",
      "dependsOn": [
          "[resourceId('Microsoft.Web/serverFarms', parameters('hostingPlanName'))]",
          "[resourceId('Microsoft.Cache/Redis', parameters('redisCacheName'))]"
      ],
      "properties": {
          "serverFarmId": "[parameters('hostingPlanName')]"
      },
      "resources": [
          {
              "apiVersion": "2015-06-01",
              "type": "config",
              "name": "web",
              "dependsOn": [
                  "[resourceId('Microsoft.Web/Sites', parameters('siteName'))]"
              ],
              "properties": {
                  "appSettings": [
                      {
                          "name": "REDIS_HOST",
                          "value": "[concat(parameters('siteName'), '.redis.cache.chinacloudapi.cn:6379')]"
                      },
                      {
                          "name": "REDIS_KEY",
                          "value": "[listKeys(resourceId('Microsoft.Cache/Redis', parameters('redisCacheName')), '2014-04-01').primaryKey]"
                      }
                  ]
              }
          }
      ]
    }



## Commands to run deployment



### PowerShell

    New-AzureRmResourceGroupDeployment -TemplateUri https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/201-web-app-with-redis-cache/azuredeploy.json -ResourceGroupName ExampleDeployGroup

### Azure CLI

    azure group deployment create --template-uri https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/201-web-app-with-redis-cache/azuredeploy.json -g ExampleDeployGroup


