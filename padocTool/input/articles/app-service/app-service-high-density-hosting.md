<properties
    pageTitle="High density hosting on Azure App Service | Azure"
    description="High density hosting on Azure App Service"
    author="btardif"
    manager="wpickett"
    editor=""
    services="app-service\web"
    documentationcenter="" />
<tags
    ms.assetid="a903cb78-4927-47b0-8427-56412c4e3e64"
    ms.service="app-service-web"
    ms.workload="web"
    ms.tgt_pltfrm="na"
    ms.devlang="multiple"
    ms.topic="article"
    ms.date="10/24/2016"
    wacn.date=""
    ms.author="byvinyal" />

# High density hosting on Azure App Service
When using App Service, your application is decoupled from the capacity allocated to it by two concepts:

* **The Application:** Represents the app and its runtime configuration. For example, it includes the version of .NET that the runtime should load, the app settings, etc.
* **The App Service Plan:** Defines the characteristics of the capacity, available feature set, and locality of the application. For example, characteristics might be large (four cores) machine, four instances, Premium features in China East.

An app is always linked to an App Service plan, but an App Service plan can provide capacity to one or more apps.

As a result, the platform provides the flexibility to isolate a
single app or have multiple apps share resources by sharing an
App Service plan.

However, when multiple apps share an App Service plan, an
instance of that app runs on every instance of that
App Service plan.

## Per app scaling
*Per app scaling* is a feature that can be enabled at the
App Service plan level and then used per application.

Per app scaling scales an app independently from the
App Service plan that hosts it. This way, an App Service plan
can be configured to provide 10 instances, but an app can be set to scale to
only 5 of them.

The following Azure Resource Manager template creates an App Service plan that's scaled out to 10
instances and an app that's configured to use per app scaling and scale to
only 5 instances.

The App Service plan is setting the **per-site scaling** property 
to true ( `"perSiteScaling": true`). The app is setting the **number of workers** 
to use to 5 (`"properties": { "numberOfWorkers": "5" }`).

    {
        "$schema": "http://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
        "contentVersion": "1.0.0.0",
        "parameters":{
            "appServicePlanName": { "type": "string" },
            "appName": { "type": "string" }
         },
        "resources": [
        {
            "comments": "App Service Plan with per site perSiteScaling = true",
            "type": "Microsoft.Web/serverFarms",
            "sku": {
                "name": "S1",
                "tier": "Standard",
                "size": "S1",
                "family": "S",
                "capacity": 10
                },
            "name": "[parameters('appServicePlanName')]",
            "apiVersion": "2015-08-01",
            "location": "China North",
            "properties": {
                "name": "[parameters('appServicePlanName')]",
                "perSiteScaling": true
            }
        },
        {
            "type": "Microsoft.Web/sites",
            "name": "[parameters('appName')]",
            "apiVersion": "2015-08-01-preview",
            "location": "China North",
            "dependsOn": [ "[resourceId('Microsoft.Web/serverFarms', parameters('appServicePlanName'))]" ],
            "properties": { "serverFarmId": "[resourceId('Microsoft.Web/serverFarms', parameters('appServicePlanName'))]" },
            "resources": [ {
                    "comments": "",
                    "type": "config",
                    "name": "web",
                    "apiVersion": "2015-08-01",
                    "location": "China North",
                    "dependsOn": [ "[resourceId('Microsoft.Web/Sites', parameters('appName'))]" ],
                    "properties": { "numberOfWorkers": "5" }
             } ]
         }]
    }


## Recommended configuration for high density hosting
Per app scaling is a feature that is enabled in both public Azure regions
and App Service Environments. However, the recommended strategy is to
use App Service Environments to take advantage of their advanced features and the larger
pools of capacity.  

Follow these steps to configure
high density hosting for your apps:

1. Configure the App Service Environment and choose a worker pool that is dedicated to the high density hosting scenario.
2. Create a single App Service plan, and scale it to use all the available
   capacity on the worker pool.
3. Set the per-site scaling flag to true on the App Service plan.
4. New sites are created and assigned to that App Service plan with the
   **numberOfWorkers** property set to **1**. Using this configuration yields the 
   highest density possible on this worker pool.
5. The number of workers can be configured independently per site to grant
   additional resources as needed. For example, a high-use site might set
   **numberOfWorkers** to **3** to have more processing capacity for that app, while
   low-use sites would set **numberOfWorkers** to **1**.

