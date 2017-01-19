<properties
	pageTitle="How to use Azure Redis Cache with Python | Windows Azure"
	description="Get started with Azure Redis Cache using Python"
	services="redis-cache"
	documentationCenter=""
	authors="steved0x"
	manager="dwrede"
	editor="v-lincan"/>

<tags
	ms.service="cache"
	ms.date="12/03/2015"
	wacn.date=""/>

# How to use Azure Redis Cache with Python

> [AZURE.SELECTOR]
- [.Net](/documentation/articles/cache-dotnet-how-to-use-azure-redis-cache)
- [Node.js](/documentation/articles/cache-nodejs-get-started)
- [Java](/documentation/articles/cache-java-get-started)
- [Python](/documentation/articles/cache-python-get-started)

This topic shows you how to get started with Azure Redis Cache using Python.


## Prerequisites

Install [redis-py](https://github.com/andymccurdy/redis-py).


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


## Add something to the cache and retrieve it

	>>> import redis
	>>> r = redis.StrictRedis(host='<name>.redis.cache.chinacloudapi.cn',
          port=6380, db=0, password='<key>', ssl=True)
    >>> r.set('foo', 'bar')
    True
    >>> r.get('foo')
    b'bar'

Replace *&lt;name&gt;* with your cache name and *&lt;key&gt;* with your access key.


<!--Image references-->
[1]: ./media/cache-python-get-started/cache01.png
[2]: ./media/cache-python-get-started/cache02.png
