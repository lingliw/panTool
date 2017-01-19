<properties
    pageTitle="Troubleshooting Windows VM allocation failures | Azure"
    description="Troubleshoot allocation failures when you create, restart, or resize a Windows VM in Azure"
    services="virtual-machines-windows, azure-resource-manager"
    documentationcenter=""
    author="JiangChen79"
    manager="felixwu"
    editor=""
    tags="top-support-issue,azure-resource-manager,azure-service-management" />
<tags
    ms.assetid="bb939e23-77fc-4948-96f7-5037761c30e8"
    ms.service="virtual-machines-windows"
    ms.workload="na"
    ms.tgt_pltfrm="vm-windows"
    ms.devlang="na"
    ms.topic="article"
    ms.date="02/02/2016"
    wacn.date=""
    ms.author="cjiang" />

# Troubleshoot allocation failures when you create, restart, or resize Windows VMs in Azure
When you create a VM, restart stopped (deallocated) VMs, or resize a VM, Azure allocates compute resources to your subscription. You may occasionally receive errors when performing these operations -- even before you reach the Azure subscription limits. This article explains the causes of some of the common allocation failures and suggests possible remediation. The information may also be useful when you plan the deployment of your services. You can also [troubleshoot allocation failures when you create, restart, or resize Linux VMs in Azure](/documentation/articles/virtual-machines-linux-allocation-failure/).

[AZURE.INCLUDE [virtual-machines-common-allocation-failure](../../includes/virtual-machines-common-allocation-failure.md)]

