To create a cache, first sign in to the [Azure portal Preview](https://portal.azure.cn), and click **New**, **Data + Storage**, **Redis Cache**.

> [AZURE.NOTE]
> If you don't have an Azure account, you can [Open an Azure account](/pricing/1rmb-trial/?WT.mc_id=redis_cache_hero) in just a couple of minutes.
> 
> 

![New cache](./media/redis-cache-create/redis-cache-new-cache-menu.png)

> [AZURE.NOTE]
> In addition to creating caches in the Azure portal Preview, you can also create them using Resource Manager templates, PowerShell, or Azure CLI.
><p>
><p> *	To create a cache using Resource Manager templates, see [Create a Redis cache using a template](/documentation/articles/cache-redis-cache-arm-provision/).
><p> *	To create a cache using Azure PowerShell, see [Manage Azure Redis Cache with Azure PowerShell](/documentation/articles/cache-howto-manage-redis-cache-powershell/).
><p> *	To create a cache using Azure CLI, see [How to create and manage Azure Redis Cache using the Azure Command-Line Interface (Azure CLI)](/documentation/articles/cache-manage-cli/).
> 
> 

In the **New Redis Cache** blade, specify the desired configuration for the cache.

![Create cache](./media/redis-cache-create/redis-cache-cache-create.png) 

* In **Dns name**, enter a cache name to use for the cache endpoint. The cache name must be a string between 1 and 63 characters and contain only numbers, letters, and the `-` character. The cache name cannot start or end with the `-` character, and consecutive `-` characters are not valid.
* For **Subscription**, select the Azure subscription that you want to use for the cache. If your account has only one subscription, it will be automatically selected and the **Subscription** drop-down will not be displayed.
* In **Resource group**, select or create a resource group for your cache. For more information, see [Using Resource groups to manage your Azure resources](/documentation/articles/resource-group-overview). 
* Use **Location** to specify the geographic location in which your cache is hosted. For the best performance, Microsoft strongly recommends that you create the cache in the same region as the cache client application.
* Use **Pricing Tier** to select the desired cache size and features.
* **Redis cluster** allows you to create caches larger than 53 GB and to shard data across multiple Redis nodes. For more information, see [How to configure clustering for a Premium Azure Redis Cache](/documentation/articles/cache-how-to-premium-clustering/).
* **Redis persistence** offers the ability to persist your cache to an Azure Storage account. For instructions on configuring persistence, see [How to configure persistence for a Premium Azure Redis Cache](/documentation/articles/cache-how-to-premium-persistence/).
* **Virtual Network** provides enhanced security and isolation by restricting access to your cache to only those clients within the specified Azure Virtual Network. You can use all the features of VNet such as subnets, access control policies, and other features to further restrict access to Redis. For more information, see [How to configure Virtual Network support for a Premium Azure Redis Cache](/documentation/articles/cache-how-to-premium-vnet/).

Once the new cache options are configured, click **Create**. It can take a few minutes for the cache to be created. To check the status, you can monitor the progress on the startboard. After the cache has been created, your new cache has a **Running** status and is ready for use with [default settings](/documentation/articles/cache-configure/#default-redis-server-configuration).

![Cache created](./media/redis-cache-create/redis-cache-cache-created.png)

