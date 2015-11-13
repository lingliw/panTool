<properties
   pageTitle="Develop a Service Fabric service"
   description="Conceptual information and tutorials that help you understand how to develop a Service Fabric service using the Reliable Actor or Reliable Services programming models."
   services="service-fabric"
   documentationCenter=".net"
   authors="rwike77"
   manager="timlt"
   editor=""/>

<tags
   ms.service="service-fabric"
   ms.date="08/20/2015"
   wacn.date=""/>

# Develop a Service Fabric service
This page has links to overview and conceptual articles and tutorial to help you learn to develop a Service Fabric service. Service Fabric offers two high-level programming models for building services: the reliable actor APIs and the reliable services APIs. While both are built on the same Service Fabric core, they make different trade-offs between simplicity and flexibility in terms of concurrency, partitioning, and communication. It is useful to understand both models so that you can choose the appropriate framework for a particular service within your application.

- [Choose a Programming Model](/documentation/articles/service-fabric-choose-framework)
- [Introduction to the Service Fabric Actor Model](/documentation/articles/service-fabric-reliable-actors-introduction)
- [Reliable Service Programming Model Introduction](/documentation/articles/service-fabric-reliable-services-introduction)

## Reliable Actor programming model
 Reliable Actors provide an asynchronous, single-threaded actor model. The actors represent the unit of state and computation that are distributed throughout the cluster to achieve high scalability. Reliable Actor model leverages the distributed store provided by underlying Service Fabric platform to provide highly available and consistent state management for the application developers.  To learn more, read:

- [Get started with Reliable Actors](/documentation/articles/service-fabric-reliable-actors-get-started)
- [Actor lifecycle and Garbage Collection](/documentation/articles/service-fabric-reliable-actors-lifecycle)
- [How Fabric Actors use the Service Fabric platform](/documentation/articles/service-fabric-reliable-actors-platform)
- [Notes on Azure Service Fabric Actors type serialization](/documentation/articles/service-fabric-reliable-actors-notes-on-actor-type-serialization)

Communicating with Actors is described in:

- [Introduction to the Service Fabric Actor Model](/documentation/articles/service-fabric-reliable-actors-introduction.md#actor-communication).
- [Communicating with services](/documentation/articles/service-fabric-connect-and-communicate-with-services)

These articles discuss useful design patterns and scenarios:

- [Actor Model Design Patterns](/documentation/articles/service-fabric-reliable-actors-patterns-introduction)  
- [Pattern: Smart Cache](/documentation/articles/service-fabric-reliable-actors-pattern-smart-cache)
- [Pattern: Distributed Networks and Graphs](/documentation/articles/service-fabric-reliable-actors-pattern-distributed-networks-and-graphs)
- [Pattern: Resource Governance](/documentation/articles/service-fabric-reliable-actors-pattern-resource-governance)
- [Pattern: Stateful Service Composition](/documentation/articles/service-fabric-reliable-actors-pattern-stateful-service-composition)
- [Pattern: Internet of Things](/documentation/articles/service-fabric-reliable-actors-pattern-internet-of-things)
- [Pattern: Distributed Computation](/documentation/articles/service-fabric-reliable-actors-pattern-distributed-computation)
- [Some Anti-patterns](/documentation/articles/service-fabric-reliable-actors-anti-patterns)

A simple turn-based concurrency is provided for Reliable Actor methods. Concurrency, timers and reminders, and reentrancy are described in these articles:

- [Concurrency](/documentation/articles/service-fabric-reliable-actors-introduction.md#concurrency)
- [Events and performance counters related to concurrency](/documentation/articles/service-fabric-reliable-actors-diagnostics.md)
- [Actor Reentrancy](/documentation/articles/service-fabric-reliable-actors-reentrancy)
- [Actor Timers](/documentation/articles/service-fabric-reliable-actors-timers-reminders)

Information on configuring Reliable Actors is found here:

- [KVSActorStateProvider Configuration](/documentation/articles/service-fabric-reliable-actors-KVSActorstateprovider-configuration)  
- [Configuring Reliable Actors - ReliableDictionaryActorStateProvider](/documentation/articles/service-fabric-reliable-actors-reliabledictionarystateprovider-configuration)

Reliable Actors emit events and performance counters, which can be used to diagnose and monitor your service:

- [Actor Diagnostics](/documentation/articles/service-fabric-reliable-actors-diagnostics)
- [Actor Events](/documentation/articles/service-fabric-reliable-actors-events)


## Reliable Service programming model
Reliable Services gives you a simple, powerful, top-level programming model to help you express what is important to your application. To learn more, read:

- [Get started with Reliable Services](/documentation/articles/service-fabric-reliable-services-quick-start)
- [Programming Model Overview](/documentation/articles/service-fabric-reliable-services-service-overview)  
- [Architecture](/documentation/articles/service-fabric-reliable-services-platform-architecture)
- [Reliable Collections](/documentation/articles/service-fabric-reliable-services-reliable-collections)
- [Configuring Stateful Reliable Services](/documentation/articles/Service-Fabric/service-fabric-reliable-services-configuration)
- [Reliable Services Programming Model Advanced Usage](/documentation/articles/Service-Fabric/service-fabric-reliable-services-advanced-usage)

Communicating with Reliable Services and the abstractions which clients can use to discover and communicate with the service endpoints are described in the following:

- [Communicating with services](/documentation/articles/service-fabric-connect-and-communicate-with-services)
- [Service Communication Model](/documentation/articles/service-fabric-reliable-services-communication)
- [Default communication stack provided by Reliable Services Framework](/documentation/articles/service-fabric-reliable-services-communication-default)
- [WCF based communication stack for Reliable Services](/documentation/articles/service-fabric-reliable-services-communication-wcf)
- [Getting Started with Microsoft Azure Service Fabric Web API services with OWIN self-host (VS 2015 RC)](/documentation/articles/service-fabric-reliable-services-communication-webapi)

Reliable Services emit events and performance counters, which can be used to diagnose and monitor your service:

- [Stateful Reliable Service Diagnostics](/documentation/articles/service-fabric-reliable-services-diagnostics)
