<properties
	pageTitle="How to use Azure Redis Cache with Node.js | Windows Azure"
	description="Get started with Azure Redis Cache using Node.js and node_redis."
	services="redis-cache"
	documentationCenter=""
	authors="steved0x"
	manager="dwrede"
	editor="v-lincan"/>

<tags
	ms.service="cache"
	ms.date="12/03/2015"
	wacn.date=""/>

# How to use Azure Redis Cache with Node.js

> [AZURE.SELECTOR]
- [.Net](/documentation/articles/cache-dotnet-how-to-use-azure-redis-cache)
- [Node.js](/documentation/articles/cache-nodejs-get-started)
- [Java](/documentation/articles/cache-java-get-started)
- [Python](/documentation/articles/cache-python-get-started)

Azure Redis Cache gives you access to a secure, dedicated Redis cache, managed by Microsoft. Your cache is accessible from any application within Windows Azure.

This topic shows you how to get started with Azure Redis Cache using Node.js. For another example of using Azure Redis Cache with Node.js, see [Build a Node.js Chat Application with Socket.IO on an Azure Website][].


## Prerequisites

Install [node_redis](https://github.com/mranney/node_redis):

    npm install redis

This tutorial uses [node_redis](https://github.com/mranney/node_redis), but you can use any Node.js client listed at [http://redis.io/clients](http://redis.io/clients).

## Create a Redis cache on Azure

In Windows Azure China, Redis Cache can only be managed by Azure PowerShell or Azure CLI

> [AZURE.NOTE]
> In order to use the China Cloud Environment, the following Azure PowerShell commands need to add **"-Environment"** parameter.
> 
>	`Add-AzureRmAccount` <br />
>	`Login-AzureRmAccount` <br />
>	
>For example, `Login-AzureRmAccount` should become `$china = Get-AzureRmEnvironment -Name AzureChinaCloud; Login-AzureRmAccount -Environment $china` if you are using Azure PowerShell 1.0.0 or 1.0.1, or `Login-AzureRmAccount -EnvironmentName AzureChinaCloud` if you are using Azure PowerShell 1.0.2 or greater.
> 

Use the following PowerShell Script to create a cache:

	$VerbosePreference = "Continue"

	# Create a new cache with date string to make name unique. 
	$cacheName = "MovieCache" + $(Get-Date -Format ('ddhhmm')) 
	$location = "China North"
	$resourceGroupName = "Default-Web-ChinaNorth"
	
	$movieCache = New-AzureRmRedisCache -Location $location -Name $cacheName  -ResourceGroupName $resourceGroupName -Size 250MB -Sku Basic

## Enable the non-SSL endpoint

You can use the following PowerShell command to enable the non-SSL endpoint

	Set-AzureRmRedisCache -Name "<your cache name>" -ResourceGroupName "<your resource group name>" -EnableNonSslPort $true

## Add something to the cache and retrieve it

	var redis = require("redis");

	// Add your cache name and access key.
	var client = redis.createClient(6379,'<name>.redis.cache.chinacloudapi.cn', {auth_pass: '<key>' });

	client.set("foo", "bar", function(err, reply) {
	    console.log(reply);
	});

	client.get("foo",  function(err, reply) {
	    console.log(reply);
	});


Output:

	OK
	bar


## Next steps

- Read the official [Redis documentation](http://redis.io/documentation).


<!--Image references-->
[1]: ./media/cache-nodejs-get-started/cache01.png
[2]: ./media/cache-nodejs-get-started/cache02.png
[3]: ./media/cache-nodejs-get-started/cache03.png
[4]: ./media/cache-nodejs-get-started/cache04.png

[Build a Node.js Chat Application with Socket.IO on an Azure Website]: /documentation/articles/web-sites-nodejs-chat-app-socketio 
