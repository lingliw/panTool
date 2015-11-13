<properties
   pageTitle="Diagnose and troubleshoot a Service Fabric service"
   description="Conceptual information and tutorials that help you diagnose, monitor, and troubleshoot a Service Fabric service."
   services="service-fabric"
   documentationCenter=".net"
   authors="rwike77"
   manager="timlt"
   editor=""/>

<tags
   ms.service="service-fabric"
   ms.date="08/04/2015"
   wacn.date=""/>

# Diagnose and monitor a Service Fabric service
Monitoring, detecting, diagnosing and troubleshooting allows for services to continue with minimal disruption to user experience. To learn more, read:

- [How to Monitor and Diagnose Services locally](documentation/articles/service-fabric-diagnostics-how-to-monitor-and-diagnose-services-locally)
- [Setting up Application Insights for your Service Fabric application](documentation/articles/service-fabric-diagnostics-application-insights-setup)
- [Troubleshooting Application Upgrade Failures](documentation/articles/service-fabric-application-upgrade-troubleshooting)
- [Troubleshooting a failed monitored application upgrade](documentation/articles/service-fabric-application-monitored-upgrade-troubleshooting)
- [Diagnostics and Performance Monitoring for Reliable Actors](documentation/articles/service-fabric-reliable-actors-diagnostics)
- [Diagnostics and Performance Monitoring for Reliable Services](documentation/articles/service-fabric-reliable-services-diagnostics)

## Troubleshoot a cluster
The following information will help you troubleshoot your local development cluster:

- [Troubleshoot your local development cluster setup](documentation/articles/service-fabric-troubleshoot-local-cluster-setup)

## Health model
Service Fabric introduces a health model that provides a rich, flexible and extensible reporting and evaluation functionality for Service Fabric entities. Service Fabric components report health out of the box on all entities. User services can enrich the health data with information specific to their logic, reported on themselves or other entities in the cluster. To learn more, read:

- [Introduction to Service Fabric Health Monitoring](documentation/articles/service-fabric-health-introduction)
- [How to view Service Fabric health reports](documentation/articles/service-fabric-view-entities-aggregated-health)
- [Using System health reports for troubleshooting](documentation/articles/service-fabric-understand-and-troubleshoot-with-system-health-reports)
- [Adding custom Service Fabric health reports](documentation/articles/service-fabric-report-health)
 