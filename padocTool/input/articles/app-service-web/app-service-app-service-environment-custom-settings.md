<properties
	pageTitle="Custom settings for App Service Environments"
	description="Custom configuration settings for App Service Environments"
	services="app-service"
	documentationCenter=""
	authors="stefsch"
	manager="nirma"
	editor=""/>

<tags
	ms.service="app-service"
	ms.workload="na"
	ms.tgt_pltfrm="na"
	ms.devlang="na"
	ms.topic="article"
	ms.date="08/22/2016"
	wacn.date=""
	ms.author="stefsch"/>

# Custom configuration settings for App Service Environments

## Overview ##
Because App Service Environments are isolated to a single customer, there are certain configuration settings that can be applied exclusively to App Service Environments. This article documents the various specific customizations that are available for App Service Environments.

If you do not have an App Service Environment, see [How to Create an App Service Environment](/documentation/articles/app-service-web-how-to-create-an-app-service-environment/).

You can store App Service Environment customizations by using an array in the new **clusterSettings** attribute. This attribute is found in the "Properties" dictionary of the *hostingEnvironments* Azure Resource Manager entity.

The following abbreviated Resource Manager template snippet shows the **clusterSettings** attribute:


    "resources": [
    {
       "apiVersion": "2015-08-01",
       "type": "Microsoft.Web/hostingEnvironments",
       "name": ...,
       "location": ...,
       "properties": {
          "clusterSettings": [
             {
                 "name": "nameOfCustomSetting",
                 "value": "valueOfCustomSetting"
             }
          ],
          "workerPools": [ ...],
          etc...
       }
    }

The **clusterSettings** attribute can be included in a Resource Manager template to update the App Service Environment.

## Disable TLS 1.0 ##
A recurring question from customers, especially customers who are dealing with PCI compliance audits, is how to explicitly disable TLS 1.0 for their apps.

TLS 1.0 can be disabled through the following **clusterSettings** entry:

        "clusterSettings": [
            {
                "name": "DisableTls1.0",
                "value": "1"
            }
        ],

## Change TLS cipher suite order ##
Another question from customers is if they can modify the list of ciphers negotiated by their server and this can be achieved by modifying the **clusterSettings** as shown below. The list of cipher suites available can be retrieved from [this MSDN article](https://msdn.microsoft.com/zh-cn/library/windows/desktop/aa374757(v=vs.85\).aspx).

        "clusterSettings": [
            {
                "name": "FrontEndSSLCipherSuiteOrder",
                "value": "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384_P256,TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256_P256,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384_P256,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256_P256,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA_P256,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA_P256"
            }
        ],

> [AZURE.WARNING]  If incorrect values are set for the cipher suite that SChannel cannot understand, all TLS communication to your server might stop functioning. In such a case, you will need to remove the *FrontEndSSLCipherSuiteOrder* entry from **clusterSettings** and submit the updated Resource Manager template to revert back to the default cipher suite settings.  Please use this functionality with caution.

## Get started
The Azure Quickstart Resource Manager template site includes a template with the base definition for [creating an App Service Environment](https://github.com/Azure/azure-quickstart-templates/tree/master/201-web-app-ase-create/).


<!-- LINKS -->

<!-- IMAGES -->
