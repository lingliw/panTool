<properties 
	pageTitle="如何为高级 Azure Redis 缓存配置虚拟网络支持" 
	description="了解如何为高级层 Azure Redis 缓存实例创建和管理虚拟网络支持" 
	services="redis-cache" 
	documentationCenter="" 
	authors="steved0x" 
	manager="dwrede" 
	editor=""/>

<tags
	ms.service="cache"
	ms.date="10/01/2015"
	wacn.date=""/>

# 如何为高级 Azure Redis 缓存配置虚拟网络支持
Azure Redis 缓存具有不同的缓存产品（包括新推出的高级级别，目前为预览版），使缓存大小和功能的选择更加灵活。

Azure Redis 缓存高级层包括群集、暂留和虚拟网络 (VNET) 支持。VNET 是你自己的网络在云中的表示形式。使用 VNET 配置 Azure Redis 缓存实例后，该实例不可公开寻址，而只能从 VNET 中的客户端访问。本文说明如何配置高级 Azure Redis 缓存实例的虚拟网络支持。

有关其他高级缓存功能的信息，请参阅[如何配置高级 Azure Redis 缓存的持久性](/documentation/articles/cache-how-to-premium-persistence)和[如何配置高级 Azure Redis 缓存的群集](/documentation/articles/cache-how-to-premium-clustering)。

>[AZURE.NOTE] Azure Redis 缓存高级级别目前处于预览状态。

## 为何使用 VNET？
[Azure 虚拟网络 (VNET)](/home/features/networking/) 部署为 Azure Redis 缓存提供增强的安全性，并提供子网、访问控制策略和进一步限制访问 Azure Redis 缓存的其他功能。

## 虚拟网络支持

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
	
	$movieCache = New-AzureRmRedisCache -Location $location -Name $cacheName  -ResourceGroupName $resourceGroupName -Size 6GB -Sku Premium -VirtualNetwork /subscriptions/{subid}/Microsoft.ClassicNetwork/VirtualNetworks/vnet1 -Subnet Front -StaticIP 10.10.1.5

## Azure Redis 缓存 VNET 常见问题

以下列表包含有关 Azure Redis 缓存缩放的常见问题的解答。

## Azure Redis 缓存和 VNET 有哪些常见的错误配置问题？

以下列表包含一些常见配置错误，它们可能导致 Azure Redis 缓存无法正常运行。

-	已阻止客户端用来连接 Redis 的 TCP 端口（例如 6379 或 6380）。
-	已阻止或拦截来自虚拟网络的传出 HTTPS 流量。Azure Redis 缓存使用了定向到 Azure 服务（尤其是存储空间）的传出 HTTPS 流量。
-	已阻止 Redis 角色实例 VM 在子网内部相互通信。Redis 角色实例应允许在所用的任何端口上使用 TCP 相互通信，这些端口可能会变化，但至少可以假设为 Redis CSDEF 文件中使用的所有端口。
-	已阻止 Azure 负载平衡器在 TCP/HTTP 端口 16001 上连接到 Redis VM。Azure Redis 缓存依赖于默认 Azure 负载平衡器探测来判断哪些角色实例正在运行。默认负载平衡器探测的工作方式是在端口 16001 上 ping Azure 来宾代理。只有响应 ping 的角色实例才会放入轮转实例，以接收 ILB 转发的流量。如果由于端口被阻止导致 ping 失败，因而没有任何实例被放入轮转列表，ILB 将不接受任何传入 TCP 连接。
-	已阻止使用客户端应用程序的 Web 流量进行 SSL 公钥验证。Redis（在虚拟网络中）的客户端必须能够将 HTTP 流量传送到公共 Internet，才能下载 CA 证书和证书吊销列表，以在使用端口 6380 连接到 Redis 并进行 SSL 服务器身份验证时，执行 SSL 证书验证。
-	已阻止 Azure 负载平衡器通过端口 1300x（13000、13001 等）或 1500x（15000、15001 等）上的 TCP 连接到群集中的 Redis VM。在 csdef 文件中配置了 VNet，该文件中包含用于打开这些端口的负载平衡器探测。Azure 负载平衡器需受 NSG 的允许，默认 NSG 使用标记 AZURE\_LOADBALANCER 来执行此操作。Azure 负载平衡器具有单个静态 IP 地址 168.63.126.16。有关详细信息，请参阅[什么是网络安全组 (NSG)？](/documentation/articles/virtual-networks-nsg)。

## 是否可以对标准或基本缓存使用 VNET？

只能对高级缓存使用 VNET。

## 后续步骤
了解如何使用更多的高级版缓存功能。

-	[如何为高级 Azure Redis 缓存配置暂留](/documentation/articles/cache-how-to-premium-persistence)
-	[如何为高级 Azure Redis 缓存配置群集功能](/documentation/articles/cache-how-to-premium-clustering)





  
<!-- IMAGES -->

[redis-cache-new-cache-menu]: ./media/cache-how-to-premium-vnet/redis-cache-new-cache-menu.png

[redis-cache-premium-pricing-tier]: ./media/cache-how-to-premium-vnet/redis-cache-premium-pricing-tier.png

[redis-cache-vnet]: ./media/cache-how-to-premium-vnet/redis-cache-vnet.png

[redis-cache-vnet-select]: ./media/cache-how-to-premium-vnet/redis-cache-vnet-select.png

[redis-cache-vnet-ip]: ./media/cache-how-to-premium-vnet/redis-cache-vnet-ip.png

[redis-cache-vnet-subnet]: ./media/cache-how-to-premium-vnet/redis-cache-vnet-subnet.png

<!---HONumber=82-->