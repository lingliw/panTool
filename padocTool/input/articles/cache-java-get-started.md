<properties
	pageTitle="如何将 Azure Redis 缓存与 Java 配合使用"
	description="开始将 Azure Redis 缓存与 Java 配合使用"
	services="redis-cache"
	documentationCenter=""
	authors="steved0x"
	manager="dwrede"
	editor=""/>

<tags
	ms.service="cache"
	ms.date="08/17/2015"
	wacn.date=""/>

# 如何将 Azure Redis 缓存与 Java 配合使用

Azure Redis 缓存可让你访问 Microsoft 管理的、专用安全的 Redis 缓存。可从 Microsoft Azure 内部的任何应用程序访问你的缓存。

本主题说明如何开始将 Azure Redis 缓存与 Java 配合使用。


## 先决条件

[Jedis](https://github.com/xetorthio/jedis) - Redis 的 Java 客户端

本教程使用 Jedis，但你可以使用 [http://redis.io/clients](http://redis.io/clients) 中列出的任何 Java 客户端。


## 在 Azure 上创建 Redis 缓存

Windows Azure 中国目前只支持 PowerShell 或者 Azure CLI 对 Redis 缓存进行管理。

> [AZURE.NOTE]
若要使用中国云环境，以下 AzureRm PowerShell 命令需要添加**“-Environment”**参数。
> 
>	`Add-AzureRmAccount`<br />
>	`Login-AzureRmAccount`<br />
>
>例如，`Login-AzureRmAccount` 应变为 `$china = Get-AzureRmEnvironment -Name AzureChinaCloud; Login-AzureRmAccount -Environment $china` (如果你使用的是 Azure PowerShell 1.0.0 或者 1.0.1)，或者 `Login-AzureRmAccount -EnvironmentName AzureChinaCloud` (如果你使用的是 Azure PowerShell 1.0.2 或者 更高)
> 


使用以下的 PowerShell 脚本创建缓存：

	$VerbosePreference = "Continue"

	# Create a new cache with date string to make name unique. 
	$cacheName = "MovieCache" + $(Get-Date -Format ('ddhhmm')) 
	$location = "China North"
	$resourceGroupName = "Default-Web-ChinaNorth"
	
	$movieCache = New-AzureRmRedisCache -Location $location -Name $cacheName  -ResourceGroupName $resourceGroupName -Size 250MB -Sku Basic


## 启用非 SSL 终结点


你可以使用以下的 PowerShell 命令行启用非 SSL 终结点

	Set-AzureRmRedisCache -Name "<your cache name>" -ResourceGroupName "<your resource group name>" -EnableNonSslPort $true


## 在缓存中添加一些内容并检索此内容

	package com.mycompany.app;
	import redis.clients.jedis.Jedis;
	import redis.clients.jedis.JedisShardInfo;

	/* Make sure your turn on non SSL port in Azure Redis using the Configuration section in the Azure portal */
	public class App
	{
	  public static void main( String[] args )
	  {
        /* In this line, replace <name> with your cache name: */
	    JedisShardInfo shardInfo = new JedisShardInfo("<name>.redis.cache.windows.net", 6379);
	    shardInfo.setPassword("<key>"); /* Use your access key. */
	    Jedis jedis = new Jedis(shardInfo);
     	jedis.set("foo", "bar");
     	String value = jedis.get("foo");
	  }
	}


## 后续步骤

- [启用缓存诊断](https://msdn.microsoft.com/library/azure/dn763945.aspx#EnableDiagnostics)，以便可以[监视](https://msdn.microsoft.com/library/azure/dn763945.aspx)缓存的运行状况。
- 阅读官方 [Redis 文档](http://redis.io/documentation)。


<!--Image references-->
[1]: ./media/cache-java-get-started/cache01.png
[2]: ./media/cache-java-get-started/cache02.png
[3]: ./media/cache-java-get-started/cache03.png
[4]: ./media/cache-java-get-started/cache04.png

<!---HONumber=71-->