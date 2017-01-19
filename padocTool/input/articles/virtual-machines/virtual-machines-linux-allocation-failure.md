<properties
    pageTitle="Troubleshooting Linux VM allocation failures | Azure"
    description="Troubleshoot allocation failures when you create, restart, or resize a Linux VM in Azure"
    services="virtual-machines-linux, azure-resource-manager"
    documentationcenter=""
    author="JiangChen79"
    manager="felixwu"
    editor=""
    tags="top-support-issue,azure-resourece-manager,azure-service-management" />
<tags
    ms.assetid="1ef41144-6dd6-4a56-b180-9d8b3d05eae7"
    ms.service="virtual-machines-linux"
    ms.workload="na"
    ms.tgt_pltfrm="vm-linux"
    ms.devlang="na"
    ms.topic="article"
    ms.date="02/02/2016"
    wacn.date=""
    ms.author="cjiang" />

# Troubleshoot allocation failures when you create, restart, or resize Linux VMs in Azure
When you create a VM, restart stopped (deallocated) VMs, or resize a VM, Azure allocates compute resources to your subscription. You may occasionally receive errors when performing these operations -- even before you reach the Azure subscription limits. This article explains the causes of some of the common allocation failures and suggests possible remediation. The information may also be useful when you plan the deployment of your services. You can also [troubleshoot allocation failures when you create, restart, or resize Windows VMs in Azure](/documentation/articles/virtual-machines-windows-allocation-failure/).

[AZURE.INCLUDE [virtual-machines-common-allocation-failure](../../includes/virtual-machines-common-allocation-failure.md)]

