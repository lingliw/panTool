﻿<!-- not suitable for Mooncake -->

<properties
    pageTitle="HPC Pack 2016 cluster in Azure | Azure"
    description="Learn how to deploy an HPC Pack 2016 cluster in Azure"
    services="virtual-machines-windows"
    documentationcenter=""
    author="dlepow"
    manager="timlt"
    editor=""
    tags="azure-resource-manager" />
<tags
    ms.assetid="3dde6a68-e4a6-4054-8b67-d6a90fdc5e3f"
    ms.service="virtual-machines-windows"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="vm-multiple"
    ms.workload="big-compute"
    ms.date="11/14/2016"
    wacn.date=""
    ms.author="danlep" />

# Deploy an HPC Pack 2016 cluster in Azure

Follow the steps in this article to deploy a [Microsoft HPC Pack 2016](https://technet.microsoft.com/zh-cn/library/cc514029) cluster in Azure virtual machines. HPC Pack is Microsoft's free HPC solution built on Azure and Windows Server technologies and supports a wide range of HPC workloads.

Use one of the [Azure Resource Manager templates](https://github.com/MsHpcPack/HPCPack2016) to deploy the HPC Pack 2016 cluster. You have several choices of cluster topology with different numbers of cluster head nodes, and with either Linux or Windows compute nodes.

## Prerequisites

### PFX certificate

A Microsoft HPC Pack 2016 cluster requires a Personal Information Exchange (PFX) certificate to secure the communication between the HPC nodes. The certificate must meet the following requirements:

* It must have a private key capable of key exchange
* Key usage includes Digital Signature and Key Encipherment
* Enhanced key usage includes Client Authentication and Server Authentication

Before deploying the HPC cluster, upload the certificate to an [Azure key vault](/documentation/articles/index/) as a secret, and record the following information for use during the deployment: **Vault name**, **Vault resource group**, **Certificate URL**, and **Certificate thumbprint**.

A sample PowerShell script to upload the certificate follows. For more information about uploading a certificate to an Azure key vault, see [Get started with Azure Key Vault](/documentation/articles/key-vault-get-started/).

    #Give the following values
    $VaultName = "mytestvault"
    $SecretName = "hpcpfxcert"
    $VaultRG = "myresourcegroup"
    $location = "chinanorth"
    $PfxFile = "c:\Temp\mytest.pfx"
    $Password = "yourpfxkeyprotectionpassword"
    #Validate the pfx file
    try {
        $pfxCert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2 -ArgumentList $PfxFile, $Password
    }
    catch [System.Management.Automation.MethodInvocationException]
    {
        throw $_.Exception.InnerException
    }
    $thumbprint = $pfxCert.Thumbprint
    $pfxCert.Dispose()
    # Create and encode the JSON object
    $pfxContentBytes = Get-Content $PfxFile -Encoding Byte
    $pfxContentEncoded = [System.Convert]::ToBase64String($pfxContentBytes)
    $jsonObject = @"
    {
    "data": "$pfxContentEncoded",
    "dataType": "pfx",
    "password": "$Password"
    }
    "@
    $jsonObjectBytes = [System.Text.Encoding]::UTF8.GetBytes($jsonObject)
    $jsonEncoded = [System.Convert]::ToBase64String($jsonObjectBytes)
    #Create an Azure key vault and upload the certificate as a secret
    $secret = ConvertTo-SecureString -String $jsonEncoded -AsPlainText -Force
    $rg = Get-AzureRmResourceGroup -Name $VaultRG -Location $location -ErrorAction SilentlyContinue
    if($null -eq $rg)
    {
        $rg = New-AzureRmResourceGroup -Name $VaultRG -Location $location
    }
    $hpcKeyVault = New-AzureRmKeyVault -VaultName $VaultName -ResourceGroupName $VaultRG -Location $location -EnabledForDeployment -EnabledForTemplateDeployment
    $hpcSecret = Set-AzureKeyVaultSecret -VaultName $VaultName -Name $SecretName -SecretValue $secret
    "The following Information will be used in the deployment template"
    "Vault Name             :   $VaultName"
    "Vault Resource Group   :   $VaultRG"
    "Certificate URL        :   $($hpcSecret.Id)"
    "Certificate Thumbprint :   $thumbprint"


## Supported topologies

Choose one of the [Azure Resource Manager templates](https://github.com/MsHpcPack/HPCPack2016) to deploy the HPC Pack 2016 cluster. Following are high-level architectures of three supported cluster topologies. High-availability topologies include multiple cluster head nodes.

1. High-availability cluster with Active Directory domain

    ![HA cluster in AD domain](./media/virtual-machines-windows-hpcpack-2016-cluster/haad.png)



2. High-availability cluster without Active Directory domain

    ![HA cluster without AD domain](./media/virtual-machines-windows-hpcpack-2016-cluster/hanoad.png)

3. Cluster with a single head node

   ![Cluster with single head node](./media/virtual-machines-windows-hpcpack-2016-cluster/singlehn.png)


## Deploy a cluster

To create the cluster, choose a template and click **Deploy to Azure**. In the [Azure portal preview](https://portal.azure.cn), specify parameters for the template as described in the following steps. Each template creates all Azure resources required for the HPC cluster infrastructure. Resources include an Azure virtual network, public IP address, load balancer (only for a high-availability cluster), network interfaces, availability sets, storage accounts, and virtual machines.

### Step 1: Select the subscription, location, and resource group

The **Subscription** and the **Location** must be same that you specified when you uploaded your PFX certificate (see Prerequisites). We recommend that you create a **Resource group** for the deployment.

### Step 2: Specify the parameter settings

Enter or modify values for the template parameters. Click the icon next to each parameter for help information. Also see the guidance for [available VM sizes](/documentation/articles/virtual-machines-windows-sizes/).

Specify the values you recorded in the Prerequisites for the following parameters: **Vault name**, **Vault resource group**, **Certificate URL**, and **Certificate thumbprint**.

###Step 3. Review legal terms and create
Click **Review legal terms** to review the terms. If you agree, click **Purchase**, and then click **Create** to start the deployment.

## Connect to the cluster
1. After the HPC Pack cluster is deployed, go to the [Azure portal preview](https://portal.azure.cn). Click **Resource groups**, and find the resource group in which the cluster was deployed. You can find the head node virtual machines.

    ![Cluster head nodes in the portal](./media/virtual-machines-windows-hpcpack-2016-cluster/clusterhns.png)

2. Click one head node (in a high-availability cluster, click any of the head nodes). In **Essentials**, you can find the public IP address or full DNS name of the cluster.

    ![Cluster connection settings](./media/virtual-machines-windows-hpcpack-2016-cluster/clusterconnect.png)

3. Click **Connect** to log on to any of the head nodes using Remote Desktop with your specified administrator user name. If the cluster you deployed is in an Active Directory Domain, the user name is of the form <privateDomainName>\<adminUsername> (for example, hpc.local\hpcadmin).

## Next steps
* Submit jobs to your cluster. See [Submit jobs to HPC an HPC Pack cluster in Azure](/documentation/articles/virtual-machines-windows-hpcpack-cluster-submit-jobs/) and [Manage an HPC Pack 2016 cluster in Azure using Azure Active Directory](/documentation/articles/virtual-machines-windows-hpcpack-cluster-active-directory/).

