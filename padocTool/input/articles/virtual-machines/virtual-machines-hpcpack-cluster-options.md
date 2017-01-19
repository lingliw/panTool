<!-- rename to virtual-machines-windows-hpcpack-cluster-options -->

<properties
 pageTitle="HPC Pack cluster options in the cloud | Azure"
 description="Learn about options with Microsoft HPC Pack to create and manage a high performance computing (HPC) cluster in the Azure cloud."
 services="virtual-machines,cloud-services,batch"
 documentationCenter=""
 authors="dlepow"
 manager="timlt"
 editor=""
 tags="azure-resource-manager,azure-service-management,hpc-pack"/>
<tags
	ms.service="virtual-machines"
	ms.date="02/04/2016"
	wacn.date=""/>

# Options to create and manage a high performance computing (HPC) cluster in Azure with Microsoft HPC Pack

[AZURE.INCLUDE [learn-about-deployment-models](../../includes/learn-about-deployment-models-both-include.md)]


Take advantage of Microsoft HPC Pack and Azure compute and infrastructure services to create and manage a cloud-based high performance computing (HPC) cluster. [HPC Pack](https://technet.microsoft.com/zh-cn/library/jj899572.aspx) is Microsoft's free HPC solution built on Azure and Windows Server technologies and supports both Windows and Linux HPC workloads. A cloud-based HPC Pack cluster provides a cluster administrator or independent software vendor (ISV) a flexible, scalable platform to run compute-intensive applications while reducing investment in an on-premises compute cluster infrastructure.


## Run an HPC Pack cluster in Azure VMs

### PowerShell deployment script

* [Create an HPC cluster with the HPC Pack IaaS deployment script](/documentation/articles/virtual-machines-linux-classic-hpcpack-cluster-powershell-script/)

### Tutorials

* [Tutorial: Get started with Linux compute nodes in an HPC Pack cluster in Azure](/documentation/articles/virtual-machines-linux-classic-hpcpack-cluster/)

* [Tutorial: Run NAMD with Microsoft HPC Pack on Linux compute nodes in Azure](/documentation/articles/virtual-machines-linux-classic-hpcpack-cluster-namd/)

* [Tutorial: Run OpenFOAM with Microsoft HPC Pack on a Linux RDMA cluster in Azure](/documentation/articles/virtual-machines-linux-classic-hpcpack-cluster-openfoam/)

* [Tutorial: Get started with an HPC Pack cluster in Azure to run Excel and SOA workloads](/documentation/articles/virtual-machines-windows-excel-cluster-hpcpack/)



### Manual deployment with the Azure portal

* [Set up the head node of an HPC Pack cluster in an Azure VM](/documentation/articles/virtual-machines-windows-hpcpack-cluster-headnode/)

### Cluster management

* [Manage compute nodes in an HPC Pack cluster in Azure](/documentation/articles/virtual-machines-windows-classic-hpcpack-cluster-node-manage/)


* [Grow and shrink Azure compute resources in an HPC Pack cluster](/documentation/articles/virtual-machines-windows-classic-hpcpack-cluster-node-autogrowshrink/)

* [Submit jobs to an HPC Pack cluster in Azure](/documentation/articles/virtual-machines-windows-hpcpack-cluster-submit-jobs/)


## Add worker role nodes to an HPC Pack cluster


* [Burst to Azure worker instances with HPC Pack](https://technet.microsoft.com/zh-cn/library/gg481749.aspx)

* [Tutorial: Set up a hybrid cluster with HPC Pack in Azure](/documentation/articles/cloud-services-setup-hybrid-hpcpack-cluster/)

* [Add Azure "burst" nodes to an HPC Pack head node in Azure](/documentation/articles/virtual-machines-windows-classic-hpcpack-cluster-node-burst/)

* [Grow and shrink Azure compute resources in an HPC Pack cluster](/documentation/articles/virtual-machines-windows-classic-hpcpack-cluster-node-autogrowshrink/)

## Integrate with Azure Batch 

* [Burst to Azure Batch with HPC Pack](https://technet.microsoft.com/zh-cn/library/mt612877.aspx)

## Create RDMA clusters for MPI workloads

* [Set up a Windows RDMA cluster with HPC Pack to run MPI applications](/documentation/articles/virtual-machines-windows-classic-hpcpack-rdma-cluster/)

* [Tutorial: Run OpenFOAM with Microsoft HPC Pack on a Linux RDMA cluster in Azure](/documentation/articles/virtual-machines-linux-classic-hpcpack-cluster-openfoam/)

* [Set up a Linux RDMA cluster to run MPI applications](/documentation/articles/virtual-machines-linux-classic-rdma-cluster/)
