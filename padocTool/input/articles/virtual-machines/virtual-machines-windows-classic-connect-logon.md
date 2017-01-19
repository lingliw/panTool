<properties
    pageTitle="Log on to a classic Azure VM | Azure"
    description="Use the Azure Classic Management Portal to log on to a Windows virtual machine created with the classic deployment model."
    services="virtual-machines-windows"
    documentationcenter=""
    author="cynthn"
    manager="timlt"
    editor="tysonn"
    tags="azure-service-management" />
<tags
    ms.assetid="3c1239ed-07dc-48b8-8b3d-dc8c5f0ab20e"
    ms.service="virtual-machines-windows"
    ms.workload="infrastructure-services"
    ms.tgt_pltfrm="vm-windows"
    ms.devlang="na"
    ms.topic="article"
    ms.date="07/28/2016"
    wacn.date=""
    ms.author="cynthn" />

# Log on to a Windows virtual machine using the Azure Classic Management Portal
In the Azure Classic Management Portal, you use the **Connect** button to start a Remote Desktop session and log on to a Windows VM.

Do you want to connect to a Linux VM? See [How to log on to a virtual machine running Linux](/documentation/articles/virtual-machines-linux-mac-create-ssh-keys/).

Learn how to [perform these steps using new Azure portal preview](/documentation/articles/virtual-machines-windows-connect-logon/).

[AZURE.INCLUDE [learn-about-deployment-models](../../includes/learn-about-deployment-models-classic-include.md)]

For information about how to log on to a VM using the Resource Manager model, see [here](/documentation/articles/virtual-machines-windows-connect-logon/).

## Connect to the virtual machine
1. Sign in to the Azure Classic Management Portal.
2. Click **Virtual Machines**, and then select the virtual machine.
3. On the command bar at the bottom of the page, click **Connect**.
   
    ![Log on to the virtual machine](./media/virtual-machines-windows-classic-connect-logon/connectwindows.png)

> [AZURE.TIP]
> If the **Connect** button isn't available, see the troubleshooting tips at the end of this article.
> 
> 

## Log on to the virtual machine
[AZURE.INCLUDE [virtual-machines-log-on-win-server](../../includes/virtual-machines-log-on-win-server.md)]

## Next steps
* If the **Connect** button is inactive or you are having other problems with the Remote Desktop connection, try resetting the configuration. From the virtual machine dashboard, under **Quick Glance**, click **Reset remote configuration**.
* For problems with your password, try resetting it. From the virtual machine dashboard, under **Quick Glance**, click **Reset password**.

If those tips don't work or aren't what you need, see [Troubleshoot Remote Desktop connections to a Windows-based Azure Virtual Machine](/documentation/articles/virtual-machines-windows-troubleshoot-rdp-connection/). This article walks you through diagnosing and resolving common problems.

