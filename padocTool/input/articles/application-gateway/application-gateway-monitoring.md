<properties 
   pageTitle="使用 Azure Resource Manager 配置应用程序网关以进行自定义探测 | Microsoft Azure"
   description="本页提供有关使用 Azure Resource Manager 配置应用程序网关自定义探测的说明"
   documentationCenter="na"
   services="application-gateway"
   authors="joaoma"
   manager="carmonm"
   editor="tysonn"/>
<tags 
   ms.service="application-gateway"
   ms.date="11/24/2015"
   wacn.date=""/>

# 运行状况监视和自定义探测 


Azure 应用程序网关会监视其后端池中所有资源的运行状况，并自动从池中删除任何被视为不正常的资源。

你可以使用下述两种类型的探测来配置运行状况监视：默认的运行状况探测和自定义探测。

## 默认的运行状况探测

如果你未设置任何自定义探测配置，应用程序网关将自动配置默认运行状况探测。进行监视时，可以向针对后端池配置的 IP 地址发出 HTTP 请求，以及向应用程序网关后端 HTTP 设置中配置的端口发出 HTTP 请求。

例如，可将应用程序网关配置为使用 A、B、C 后端服务器来接收端口 80 上的 HTTP 网络流量。默认运行状况监视每隔 30 秒对三台服务器进行测试，以获取正常的 HTTP 响应。正常的 HTTP 响应具有 200 到 399 的[状态代码](https://msdn.microsoft.com/zh-cn/library/aa287675.aspx)。

如果服务器 A 的默认探测检查失败，应用程序网关会从后端池删除该服务器，并且网络流量不再流向该服务器。默认探测仍继续每隔 30 秒检查服务器 A。当服务器 A 成功响应默认运行状况探测发出的请求时，将变为正常状态并重新加回到后端池，而流量也开始再次流向该服务器。

默认探测仅使用 IP 地址来检查状态。若要通过测试 URL 连接性来验证运行状况，必须使用自定义探测。


## 自定义探测 

自定义探测可让你更精细地控制运行状况监视。使用自定义探测时，你可以配置探测检查间隔、要测试的 URL 和路径，以及在将后端池实例标记为不正常之前可接受的失败响应次数。


自定义探测设置：

- **探测间隔** - 配置探测检查间隔。
- **探测超时** - 定义 HTTP 请求检查的探测超时。
- **不正常阈值** - 指定在出现多少次请求失败的情况下才能将实例标记为不正常。  
- **主机名称和路径** - 如果你的网站或 Web 场没有针对 IP 地址的 HTTP 响应，则需配置探测主机名称和路径才能进行有效且良好的 HTTP 响应。例如，你的网站为 http://contoso.com/， 但该网站不能进行有效的 HTTP 响应。必须配置主机名称和路径，以便提供有效且良好的 HTTP 响应以验证 Web 服务器实例是否处于正常状态。在本示例中，可以为“http://contoso.com/path/custompath.htm” 配置自定义探测，使探测检查能够获得成功的 HTTP 响应。 



>[AZURE.NOTE] 只能使用 PowerShell 来配置自定义探测

<!---HONumber=Mooncake_0307_2016-->