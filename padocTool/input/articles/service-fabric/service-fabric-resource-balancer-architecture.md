<properties
   pageTitle="Resource Balancer Architecture"
   description="An architectural overview of Service Fabric's Resource Balancer"
   services="service-fabric"
   documentationCenter=".net"
   authors="abhic"
   manager="timlt"
   editor=""/>

<tags
   ms.service="Service-Fabric"
   ms.date="09/03/2015"
   wacn.date=""/>

# Resource Balancer Architecture Overview

![Resource Balancer Architecture][Image1]

The Service Fabric Resource Balancer consists of a single centralized Resource Balancing service and a component that exists on every node, which are conceptually collocated with the Service Fabric Failover Manager and with the local Service Fabric node, respectively.

The local agent is responsible for collecting and buffering load reports from the services that are running on the local node, for sending them to the Resource Balancer service, and also for reporting failures and other events to the Failover Manager and Resource Balancer (1 and 2 above). The Resource Balancer service and the Failover Manager collaborate to respond to load events and other events in the system, such as replica or node failures, load reports, and services and applications that are created and deleted. For example, when a replica fails, the Failover Manager requests that the Service Fabric Resource Balancer suggest a location for the replacement that is based on load data from the different nodes. Similarly, when a new service request is received, the Failover Manager requests recommendations from the Resource Balancer for where to place that service. In all these cases, the Resource Balancer responds with changes to various service configurations (3), which are then enacted by the Failover Manager. In the preceding example, the Failover Manager creates a new replica on the node, which results in the best overall balance (4).

<!--Every topic should have next steps and links to the next logical set of content to keep the customer engaged-->
## Next steps

Resource Balancing Features:

- [Describe the Cluster](/documentation/articles/service-fabric-resource-balancer-cluster-description)
- [Describe Services](/documentation/articles/service-fabric-resource-balancer-service-description)
- [Report Dynamic Load](/documentation/articles/service-fabric-resource-balancer-dynamic-load-reporting)
- [Proactive Metric Packing](/documentation/articles/service-fabric-resource-balancer-proactive-metric-packing)
- [Node Buffer Percentage](/documentation/articles/service-fabric-resource-balancer-node-buffer-percentage)

[Image1]: media/service-fabric-resource-balancer-architecture/Service-Fabric-Resource-Balancer-Architecture.png
 