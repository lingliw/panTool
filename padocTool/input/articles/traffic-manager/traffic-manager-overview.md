<properties 
   pageTitle="What is Traffic Manager | Azure"
   description="This article will help you understand what Traffic Manager is, and whether it is the right traffic routing choice for your application"
   services="traffic-manager"
   documentationCenter=""
   authors="jtuliani"
   manager="carmonm"
   editor="tysonn" />
<tags
	ms.service="traffic-manager"
	ms.date="06/09/2016"
	wacn.date=""/>

# What is Traffic Manager?

Azure Traffic Manager allows you to control the distribution of user traffic to your service endpoints running in different datacenters around the world.

Service endpoints supported by Traffic Manager include Azure VMs, Web Apps and cloud services. You can also use Traffic Manager with external, non-Azure endpoints.

Traffic Manager works by using the Domain Name System (DNS) to direct end-user requests to the most appropriate endpoint, based on the configured traffic-routing method and current view of endpoint health.  Clients then connect to the appropriate service endpoint directly.

Traffic Manager supports a [range of traffic-routing methods](/documentation/articles/traffic-manager-routing-methods) to suit different application needs.  Traffic Manager provides [endpoint health checks and automatic endpoint failover](/documentation/articles/traffic-manager-monitoring), enabling you to build high-availability applications that are resilient to failure, including the failure of an entire Azure region.

## Traffic Manager benefits

Traffic Manager can help you:

- **Improve availability of critical applications** - Traffic Manager allows you to deliver high availability for your critical applications by monitoring your endpoints in Azure and providing automatic failover when an endpoint goes down.
- **Improve responsiveness for high performance applications** - Azure allows you to run cloud services or websites in datacenters located around the world. Traffic Manager can improve the responsiveness of your applications by directing end-users to the endpoint with the lowest network latency from the client.
- **Upgrade and perform service maintenance without downtime** - You can seamlessly carry out upgrade and other planned maintenance operations on your applications without downtime for end users by using Traffic Manager to direct traffic to alternative endpoints when maintenance is in progress.
- **Combine on-premises and Cloud-based applications** - Traffic Manager supports external, non-Azure endpoints enabling it to be used with hybrid cloud and on-premises deployments, including the "burst-to-cloud," "migrate-to-cloud," and "failover-to-cloud" scenarios.
- **Distribute traffic for large, complex deployments** - Traffic-routing methods can be combined using [nested Traffic Manager profiles](/documentation/articles/traffic-manager-nested-profiles) to create sophisticated and flexible traffic-routing configurations to meet the needs of larger, more complex deployments. 

## Load Balancer differences

There are different options to distribute network traffic using Azure.  These options work differently from each other, having a different feature set and supports different scenarios.  They can each be used in isolation, or combining them.

- Azure Load Balancer works at the network layer (level 4 in the OSI network reference stack).  It provides network-level distribution of traffic across instances of an application running in the same Azure data center.

- Application Gateway works at the application layer (level 7 in the OSI network reference stack).  It acts as a reverse-proxy service, terminating the client connection and forwarding requests to back-end endpoints.

- 	Traffic Manager works at the DNS level.  It uses DNS responses to direct end-user traffic to globally-distributed endpoints.  Clients then connect to those endpoints directly.
The following table summarizes the features offered by each service:

| Service | Azure Load Balancer | Application Gateway | Traffic Manager |
|---|---|---|---|
|Technology| Network level (level 4) | Application level (level 7) | DNS level |
| Application protocols supported |	Any | HTTP and HTTPS | 	Any (An HTTP/S endpoint is required for endpoint monitoring) |
| Endpoints | Azure VMs and Cloud Services role instances | Any Azure Internal IP address or public internet IP address | Azure VMs, Cloud Services, Azure Web Apps and external endpoints |
| Vnet support | Can be used for both Internet facing and internal (Vnet) applications | Can be used for both Internet facing and internal (Vnet) applications |	Only supports Internet-facing applications |
Endpoint Monitoring | supported via probes | supported via probes | supported via HTTP/HTTPS GET | 
<BR>
Azure Load Balancer and Application Gateway route network traffic to endpoints but they have different usage scenarios to which traffic to handle. The table below helps understanding the difference between the two load balancers:


| Type | Azure Load Balancer | Application Gateway |
|---|---|---|
| Protocols | UDP/TCP | HTTP/ HTTPS |
| IP reservation | Supported | Not supported | 
| Load balancing mode | 5 tuple(source IP, source port, destination IP,destination port, protocol type) | CookieBasedAffinity = false,rules = basic (Round-Robin) | 
| Load balancing mode (source IP /sticky sessions) |  2 tuple (source IP and destination IP), 3 tuple (source IP, destination IP and port). Can scale up or down based on the number of virtual machines | CookieBasedAffinity = true,rules = basic (Roud-Robin) for new connections. |
| health probes | Default: probe interval - 15 secs. Taken out of rotation: 2 Continuous failures. Supports user defined probes | Idle probe interval 30 secs. Taken out after 5 consecutive live traffic failures or a single probe failure in idle mode. Supports user defined probes | 
| SSL offloading | not supported | supported | 




## Next Steps

- Learn more about [how Traffic Manager works](/documentation/articles/traffic-manager-how-traffic-manager-works).

- Learn how to develop high-availability applications using [Traffic Manager endpoint monitoring](/documentation/articles/traffic-manager-monitoring).

- Learn more about the [traffic-routing methods](/documentation/articles/traffic-manager-routing-methods) supported by Traffic Manager.

- [Create a Traffic Manager profile](/documentation/articles/traffic-manager-manage-profiles).
 
