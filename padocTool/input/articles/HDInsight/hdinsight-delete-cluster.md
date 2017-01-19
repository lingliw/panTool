<properties
pageTitle="How to delete an HDInsight cluster | Azure"
description="Information on the various ways that you can delete an HDInsight cluster."
services="hdinsight"
documentationCenter=""
authors="Blackmist"
manager="paulettm"
editor="cgronlun"/>

<tags
	ms.service="hdinsight"
	ms.date="03/07/2016"
	wacn.date=""/>

#How to delete an HDInsight cluster

HDInsight clusters are billed hourly, so you should always delete your cluster when it is no longer in use. In this document, you will learn how to delete a cluster using the Azure Management Portal, Azure PowerShell, and the Azure CLI.

> [AZURE.IMPORTANT] Deleting an HDInsight cluster does not delete the Azure Storage account(s) associated with the cluster. This allows you to preserve and reuse any data stored by the cluster.

##Azure Management Portal

1. Login to the [Azure Management Portal](https://manage.windowsazure.cn), click **HDInsight**, and select the cluster you want to delete.

2. Click the __Delete__ at the bottom. When prompted, select __Yes__ to delete the cluster.

##Azure PowerShell

> [AZURE.NOTE] If you have not installed and configured Azure PowerShell, use the steps in the [Install and Configure Azure PowerShell](/documentation/articles/powershell-install-configure) document.

From a PowerShell prompt, use the following command to delete the cluster:

    Remove-AzureHDInsightCluster -Name CLUSTERNAME

Replace __CLUSTERNAME__ with the name of your HDInsight cluster.

##Azure CLI

> [AZURE.NOTE] If you have not installed and configured the Azure CLI, use the steps in the [Install and configure Azure CLI](/documentation/articles/xplat-cli-install) document.

From a prompt, use the following to delete the cluster:

    azure hdinsight cluster delete CLUSTERNAME
    
Replace __CLUSTERNAME__ with the name of your HDInsight cluster.
