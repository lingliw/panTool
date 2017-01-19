<properties
    pageTitle="Connect to a Windows Server VM | Azure"
    description="Learn how to connect and log on to a Windows VM using the Azure portal preview and the Resource Manager deployment model."
    services="virtual-machines-windows"
    documentationcenter=""
    author="cynthn"
    manager="timlt"
    editor="tysonn"
    tags="azure-resource-manager" />
<tags
    ms.assetid="ef62b02e-bf35-468d-b4c3-71b63fe7f409"
    ms.service="virtual-machines-windows"
    ms.workload="infrastructure-services"
    ms.tgt_pltfrm="vm-windows"
    ms.devlang="na"
    ms.topic="get-started-article"
    ms.date="07/28/2016"
    wacn.date=""
    ms.author="cynthn" />

# How to connect and log on to an Azure virtual machine running Windows
You'll use the **Connect** button in the Azure portal preview to start a Remote Desktop (RDP) session. First you connect to the virtual machine, then you log on.

## Connect to the virtual machine
1. If you haven't already done so, sign in to the [Azure portal preview](https://portal.azure.cn/).
2. On the Hub menu, click **Virtual Machines**.
3. Select the virtual machine from the list.
4. On the blade for the virtual machine, click **Connect**.
   
    ![Screenshot of the Azure portal preview showing how to connect to your VM.](./media/virtual-machines-windows-connect-logon/connect.png)
   
   > [AZURE.TIP]
   > If the **Connect** button in the portal is greyed out and you are not connected to Azure via an [Express Route](/documentation/articles/expressroute-introduction/) or [Site-to-Site VPN](/documentation/articles/vpn-gateway-howto-site-to-site-resource-manager-portal/) connection, you need to create and assign your VM a public IP address before you can use RDP. You can read more about [public IP addresses in Azure](/documentation/articles/virtual-network-ip-addresses-overview-arm/).
   > 
   > 

## Log on to the virtual machine
[AZURE.INCLUDE [virtual-machines-log-on-win-server](../../includes/virtual-machines-log-on-win-server.md)]

## Next steps
If you run into trouble when you try to connect, see [Troubleshoot Remote Desktop connections](/documentation/articles/virtual-machines-windows-troubleshoot-rdp-connection/). This article walks you through diagnosing and resolving common problems.

