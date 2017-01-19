<properties
	pageTitle="如何将 Azure Redis 缓存与 Python 配合使用 | Microsoft Azure"
	description="开始将 Azure Redis 缓存与 Python 配合使用"
	services="redis-cache"
	documentationCenter=""
	authors="steved0x"
	manager="dwrede"
	editor="v-lincan"/>

<tags
	ms.service="cache"
	ms.date="08/17/2015"
	wacn.date=""/>

# 如何将 Azure Redis 缓存与 Python 配合使用

本主题说明如何开始将 Azure Redis 缓存与 Python 配合使用。


## 先决条件

安装 [redis-py](https://github.com/andymccurdy/redis-py)。


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

## 在缓存中添加一些内容并检索此内容

    >>> import redis
    >>> r = redis.StrictRedis(host='<name>.redis.cache.windows.net',
          port=6380, db=0, password='<key>', ssl=True)
    >>> r.set('foo', 'bar')
    True
    >>> r.get('foo')
    b'bar'

将 *&lt;name&gt;* 替换为你的缓存名称，将 *&lt;key&gt;* 替换为你的缓存访问密钥。


<!--Image references-->
[1]: ./media/cache-python-get-started/cache01.png
[2]: ./media/cache-python-get-started/cache02.png

<!---HONumber=71-->