<properties
    pageTitle="Navigate and select Windows VM images | Azure"
    description="Learn how to determine the publisher, offer, and SKU for images when creating a Windows virtual machine with the Resource Manager deployment model."
    services="virtual-machines-windows"
    documentationcenter=""
    author="squillace"
    manager="timlt"
    editor=""
    tags="azure-resource-manager" />
<tags
    ms.assetid="188b8974-fabd-4cd3-b7dc-559cbb86b98a"
    ms.service="virtual-machines-windows"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="vm-windows"
    ms.workload="infrastructure"
    ms.date="08/23/2016"
    wacn.date=""
    ms.author="rasquill" />

# Navigate and select Windows virtual machine images in Azure with PowerShell or the CLI
This topic describes how to find VM image publishers, offers, skus, and versions for each location into which you might deploy. To give an example, some commonly used Windows VM images are:

## Table of commonly used Windows images
| PublisherName | Offer | Sku |
|:--- |:--- |:--- |:--- |
| MicrosoftSQLServer |SQL2014-WS2012R2 |Enterprise-Optimized-for-DW |
| MicrosoftSQLServer |SQL2014-WS2012R2 |Enterprise-Optimized-for-OLTP |
| MicrosoftWindowsServer |WindowsServer |2012-R2-Datacenter |
| MicrosoftWindowsServer |WindowsServer |2012-Datacenter |
| MicrosoftWindowsServer |WindowsServer |2008-R2-SP1 |
| MicrosoftWindowsServer |WindowsServer |Windows-Server-Technical-Preview |
| MicrosoftWindowsServerHPCPack |WindowsServerHPCPack |2012R2 |

[AZURE.INCLUDE [virtual-machines-common-cli-ps-findimage](../../includes/virtual-machines-common-cli-ps-findimage.md)]

