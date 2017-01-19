<properties
    pageTitle="Set up endpoints on a classic Linux VM | Azure"
    description="Learn to set up endpoints for a Linux VM in the Azure Classic Management Portal to allow communication with a Linux virtual machine in Azure"
    services="virtual-machines-linux"
    documentationcenter=""
    author="cynthn"
    manager="timlt"
    editor=""
    tags="azure-service-management" />
<tags
    ms.assetid="f3749738-1109-4a1d-8635-40e4bd220e91"
    ms.service="virtual-machines-linux"
    ms.workload="infrastructure-services"
    ms.tgt_pltfrm="vm-linux"
    ms.devlang="na"
    ms.topic="article"
    ms.date="07/13/2016"
    wacn.date=""
    ms.author="cynthn" />

# How to set up endpoints on a Linux classic virtual machine in Azure
All Linux virtual machines that you create in Azure using the classic deployment model can automatically communicate over a private network channel with other virtual machines in the same cloud service or virtual network. However, computers on the Internet or other virtual networks require endpoints to direct the inbound network traffic to a virtual machine. This article is also available for [Windows virtual machines](/documentation/articles/virtual-machines-windows-classic-setup-endpoints/).

[AZURE.INCLUDE [learn-about-deployment-models](../../includes/learn-about-deployment-models-classic-include.md)]

In the **Resource Manager** deployment model, endpoints are configured using **Network Security Groups (NSGs)**. For more information, see [Opening ports and endpoints](/documentation/articles/virtual-machines-linux-nsg-quickstart/).

When you create a Linux virtual machine in the Azure Classic Management Portal, an endpoint for Secure Shell (SSH) is typically created for you automatically. You can configure additional endpoints while creating the virtual machine or afterwards as needed.

[AZURE.INCLUDE [virtual-machines-common-classic-setup-endpoints](../../includes/virtual-machines-common-classic-setup-endpoints.md)]

## Next steps
* You can also create a VM endpoint by using the [Azure Command-Line Interface](/documentation/articles/virtual-machines-command-line-tools/). Run the **azure vm endpoint create** command.
* If you created a virtual machine in the Resource Manager deployment model, you can use the Azure CLI in Resource Manager mode to [create network security groups](/documentation/articles/virtual-networks-create-nsg-arm-cli/) to control traffic to the VM.

