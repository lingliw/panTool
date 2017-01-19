<!-- need to be verified -->

<properties
    pageTitle="Windows HPC Pack cluster options in the cloud | Azure"
    description="Learn about options with Microsoft HPC Pack to create and manage a Windows high performance computing (HPC) cluster in the Azure cloud"
    services="virtual-machines-windows,cloud-services,batch"
    documentationcenter=""
    author="dlepow"
    manager="timlt"
    editor=""
    tags="azure-resource-manager,azure-service-management,hpc-pack" />
<tags
    ms.assetid="02c5566d-2129-483c-9ecf-0d61030442d7"
    ms.service="virtual-machines-windows"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="vm-windows"
    ms.workload="big-compute"
    ms.date="11/17/2016"
    wacn.date=""
    ms.author="danlep" />

# Options with HPC Pack to create and manage a Windows HPC cluster in Azure
[AZURE.INCLUDE [virtual-machines-common-hpcpack-cluster-options](../../includes/virtual-machines-common-hpcpack-cluster-options.md)]

## Run an HPC Pack cluster in Azure VMs
### Azure templates

>[AZURE.NOTE] Templates you downloaded from the GitHub Repo "azure-quickstart-templates" must be modified in order to fit in the Azure China Cloud Environment. For example, replace some endpoints -- "blob.core.chinacloudapi.cn" by "blob.core.chinacloudapi.cn", "chinacloudapp.cn" by "chinacloudapp.cn"; change some unsupported VM images; and, changes some unsupported VM sizes.

* (Quickstart) [Create an HPC cluster](https://github.com/Azure/azure-quickstart-templates/tree/master/create-hpc-cluster)
* (Quickstart) [Create an HPC cluster with custom compute node image](https://github.com/Azure/azure-quickstart-templates/tree/master/create-hpc-cluster-custom-image)

### PowerShell deployment script
* [Create an HPC cluster with the HPC Pack IaaS deployment script](/documentation/articles/virtual-machines-windows-classic-hpcpack-cluster-powershell-script/)

### Tutorials
* [Tutorial: Get started with an HPC Pack cluster in Azure to run Excel and SOA workloads](/documentation/articles/virtual-machines-windows-excel-cluster-hpcpack/)

### Manual deployment with the Azure portal preview
* [Set up the head node of an HPC Pack cluster in an Azure VM](/documentation/articles/virtual-machines-windows-hpcpack-cluster-headnode/)

### Cluster management
* [Manage compute nodes in an HPC Pack cluster in Azure](/documentation/articles/virtual-machines-windows-classic-hpcpack-cluster-node-manage/)
* [Grow and shrink Azure compute resources in an HPC Pack cluster](/documentation/articles/virtual-machines-windows-classic-hpcpack-cluster-node-autogrowshrink/)
* [Submit jobs to an HPC Pack cluster in Azure](/documentation/articles/virtual-machines-windows-hpcpack-cluster-submit-jobs/)
* [Job management in HPC Pack](https://technet.microsoft.com/zh-cn/library/jj899585.aspx)

## Add worker role nodes to an HPC Pack cluster
* [Burst to Azure worker instances with HPC Pack](https://technet.microsoft.com/zh-cn/library/gg481749.aspx)
* [Tutorial: Set up a hybrid cluster with HPC Pack in Azure](/documentation/articles/cloud-services-setup-hybrid-hpcpack-cluster/)
* [Add Azure "burst" nodes to an HPC Pack head node in Azure](/documentation/articles/virtual-machines-windows-classic-hpcpack-cluster-node-burst/)

## Integrate with Azure Batch
* [Burst to Azure Batch with HPC Pack](https://technet.microsoft.com/zh-cn/library/mt612877.aspx)
