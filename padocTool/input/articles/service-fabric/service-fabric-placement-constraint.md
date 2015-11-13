<properties
   pageTitle="Service Fabric Cluster Orchestration Placement Constraints"
   description="A conceptual overview of placement constraints in Service Fabric"
   services="service-fabric"
   documentationCenter=".net"
   authors="GaugeField"
   manager="timlt"
   editor=""/>

<tags
   ms.service="Service-Fabric"
   ms.date="09/03/2015"
   wacn.date=""/>

# Placement Constraints Overview

Service Fabric allows developers to constrain the placement of service replicas on to nodes that satisfy particular conditions. These conditions are expressed via a boolean expression that is evaluated with appropriate service-context specific values.


## Capabilities
By using Placement Constraints, you can:

- Confine different type of services on different types of nodes via defining NodeProperties on the nodes.

- Apply certain constraints to primary replicas but not secondary replicas


## Key Concepts
NodeProperty- A user or system defined map from a string to a value, that can vary over each node, i.e NodeName.


<!--Every topic should have next steps and links to the next logical set of content to keep the customer engaged-->
## Next steps

For more information: [Application Scenarios](/documentation/articles/service-fabric-application-scenarios).
 