<properties 
	pageTitle="Provision Web App with Redis Cache" 
	description="Use Azure Resource Manager template to deploy web app with Redis Cache." 
	services="app-service" 
	documentationCenter="" 
	authors="tfitzmac" 
	manager="wpickett" 
	editor=""/>

<tags
	ms.service="app-service"
	ms.date="07/08/2015"
	wacn.date=""/>

# Create a Web App plus Redis Cache using a template

In this topic, you will learn how to create an Azure Resource Manager template that deploys an Azure Web App with Redis cache. You will learn how to define which resources are deployed and 
how to define parameters that are specified when the deployment is executed. You can use this template for your own deployments, or customize it to meet your requirements.

For more information about creating templates, see [Authoring Azure Resource Manager Templates](/documentation/articles/resource-group-authoring-templates).

For the complete template, see [Web App with Redis Cache template](https://github.com/Azure/azure-quickstart-templates/blob/master/201-web-app-with-redis-cache/azuredeploy.json).

## What you will deploy

In this template, you will deploy:

- Azure Web App
- Azure Redis Cache.

To run the deployment automatically, click the following button:

<!-- deleted by customization
[![Deploy to Azure](http://azuredeploy.net/deploybutton.png)](https://manage.windowsazure.cn/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2F201-web-app-with-redis-cache%2Fazuredeploy.json)
-->
<!-- keep by customization: begin -->
![Deploy to Azure](http://azuredeploy.net/deploybutton.png)
<!-- keep by customization: end -->

## Parameters to specify


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

### Redis Cache

Creates the Azure Redics Cache that is used with the web app. The name of the cache is specified in the **redisCacheName** parameter.

The template creates the cache in the same location as the web app, which is recommended for best performance. 

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

### Web app

Creates the web app with name specified in the **siteName** parameter.

Notice that the web app is configured with app setting properties that enable it to work with the Redis Cache. This app settings are dynamically created based on values provided during deployment.
        
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

    New-AzureResourceGroupDeployment -TemplateUri https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/201-web-app-with-redis-cache/azuredeploy.json -ResourceGroupName ExampleDeployGroup

### Azure CLI

    azure group deployment create --template-uri https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/201-web-app-with-redis-cache/azuredeploy.json -g ExampleDeployGroup


