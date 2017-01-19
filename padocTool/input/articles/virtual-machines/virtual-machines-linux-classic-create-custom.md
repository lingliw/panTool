<properties
    pageTitle="Create a Classic Linux VM using the CLI | Azure"
    description="Learn how to create a Linux virtual machine with the Azure CLI using the Classic deployment model"
    services="virtual-machines-linux"
    documentationcenter=""
    author="iainfoulds"
    manager="timlt"
    editor="tysonn"
    tags="azure-service-management" />
<tags
    ms.assetid="f8071a2e-ed91-4f77-87d9-519a37e5364f"
    ms.service="virtual-machines-linux"
    ms.workload="infrastructure-services"
    ms.tgt_pltfrm="vm-linux"
    ms.devlang="na"
    ms.topic="article"
    ms.date="11/14/2016"
    wacn.date=""
    ms.author="iainfou" />

# How to Create a Linux VM with the Azure CLI
[AZURE.INCLUDE [learn-about-deployment-models](../../includes/learn-about-deployment-models-classic-include.md)]

For the Resource Manager version, see [here](/documentation/articles/virtual-machines-linux-create-cli-complete/).

This topic describes how to create a Linux virtual machine (VM) with the Azure CLI using the Classic deployment model. We use a Linux image from the available **IMAGES** on Azure. The Azure CLI commands give the following configuration choices, among others:

* Connecting the VM to a virtual network
* Adding the VM to an existing cloud service
* Adding the VM to an existing storage account
* Adding the VM to an availability set or location

> [AZURE.IMPORTANT]
> If you want your VM to use a virtual network so you can connect to it directly by hostname or set up cross-premises connections, make sure you specify the virtual network when you create the VM. A VM can be configured to join a virtual network only when you create the VM. For details on virtual networks, see [Azure Virtual Network Overview](https://msdn.microsoft.com/zh-cn/library/azure/jj156007.aspx).
> 
> 

## How to create a Linux VM using the Classic deployment model
[AZURE.INCLUDE [virtual-machines-create-LinuxVM](../../includes/virtual-machines-create-linuxvm.md)]

