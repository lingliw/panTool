<properties 
   pageTitle="Network interfaces | Azure"
   description="Learn about Azure network interfaces in Azure Resource Manager."
   services="virtual-network"
   documentationCenter="na"
   authors="jimdial"
   manager="carmonm"
   editor=""
   tags="azure-resource-manager"
/>
<tags 
   ms.service="virtual-network"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="infrastructure-services"
   ms.date="09/23/2016"
   wacn.date=""
   ms.author="jdial" />

# Network interfaces

A network interface (NIC) is the interconnection between a Virtual Machine (VM) and the underlying software network. This article explains what a network interface is and how it's used in the Azure Resource Manager deployment model.

Azure recommends deploying new resources using the Resource Manager deployment model, but you can also deploy VMs with network connectivity in the [classic](/documentation/articles/virtual-network-ip-addresses-overview-classic/) deployment model. If you're familiar with the classic model, there are important differences in VM networking in the Resource Manager deployment model. Learn more about the differences by reading the [Virtual machine networking - Classic](/documentation/articles/virtual-network-ip-addresses-overview-classic/#differences-between-resource-manager-and-classic-deployments) article.

In Azure, a network interface:

1. Is a resource that can be created, deleted, and has its own configurable settings.
2. Must be connected to one subnet in one Azure Virtual Network (VNet) when it's created. If you're not familiar with VNets, learn more about them by reading the [Virtual network overview](/documentation/articles/virtual-networks-overview/) article. The NIC must be connected to a VNet that exists in the same Azure [location](https://azure.microsoft.com/regions) and [subscription](/documentation/articles/azure-glossary-cloud-terminology/#subscription) as the NIC. After a NIC is created, you can change the subnet it's connected to, but you cannot change the VNet it's connected to.
3. Has a name assigned to it that cannot be changed after the NIC is created. The name must be unique within an Azure [resource group](/documentation/articles/resource-group-overview/#resource-groups), but doesn't have to be unique within the subscription, the Azure location it's created in, or the VNet it's connected to. Several NICs are typically created within an Azure subscription. It's recommended that you devise a naming convention that makes managing multiple NICs easier than using default names.
4. May be attached to a VM, but can only be attached to a single VM that exists in the same location as the NIC.
5. Has a MAC address, which is persisted with the NIC for as long as it remains attached to a VM. The MAC address is persisted whether the VM is restarted (from within the operating system) or stopped (de-allocated) and started using the Azure Portal Preview, Azure PowerShell, or the Azure Command-Line Interface. If it's detached from a VM and attached to a different VM, the NIC receives a different MAC address. If the NIC is deleted, the MAC address is assigned to other NICs.
6. Must have one primary **private** *IPv4* static or dynamic IP address assigned to it.
8. May have one public IP address resource associated to it.
10. Can receive traffic not destined to private IP addresses assigned to it if IP forwarding is enabled for the NIC. If a VM is running firewall software for example, it routes packets not destined for its own IP addresses. The VM must still run software capable of routing or forwarding traffic, but to do so, IP forwarding must be enabled for a NIC.
11. Is often created in the same resource group as the VM it's attached to or the same VNet that it's connected to, though it isn't required to be.

Multiple NICs can be attached to the same VM, provided the VM size supports it. To learn more about which VM sizes support multiple NIC, read the [Windows Server VM sizes](/documentation/articles/virtual-machines-windows-sizes/) or [Linux VM sizes](/documentation/articles/virtual-machines-linux-sizes/) articles.

## Next steps

- Learn how to create a VM with a single NIC by reading the [Create a VM](/documentation/articles/virtual-machines-windows-hero-tutorial/) article.
- Learn how to create a VM with multiple NICs by reading the [Deploy a VM with multiple NIC](/documentation/articles/virtual-network-deploy-multinic-arm-ps/) article.
- Learn how to create a NIC with multiple IP configurations by reading the [Multiple IP addresses for Azure virtual machines](/documentation/articles/virtual-network-multiple-ip-addresses-powershell/) article.
