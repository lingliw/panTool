<!-- not suitable for Mooncake -->

<properties
    pageTitle="About compute-intensive VMs with Windows | Azure"
    description="Get background information and considerations for using the Azure H-series and A8, A9, A10, and A11 compute-intensive sizes for Windows VMs and cloud services"
    services="virtual-machines-windows, cloud-services"
    documentationcenter=""
    author="dlepow"
    manager="timlt"
    editor=""
    tags="azure-resource-manager,azure-service-management" />
<tags
    ms.assetid="28d8e1f2-8e61-4fbe-bfe8-80a68443baba"
    ms.service="virtual-machines-windows"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="vm-windows"
    ms.workload="infrastructure-services"
    ms.date="09/21/2016"
    wacn.date=""
    ms.author="danlep" />

# About H-series and compute-intensive A-series VMs
Here is background information and some considerations for using the newer Azure H-series and the earlier A8, A9, A10, and A11 instances, also known as *compute-intensive* instances. This article focuses on using these instances for Windows VMs. This article is also available for [Linux VMs](/documentation/articles/virtual-machines-linux-a8-a9-a10-a11-specs/).

For basic specs, storage capacities, and disk details, see [Sizes for virtual machines](/documentation/articles/virtual-machines-windows-sizes/).

[AZURE.INCLUDE [virtual-machines-common-a8-a9-a10-a11-specs](../../includes/virtual-machines-common-a8-a9-a10-a11-specs.md)]

## Access to the RDMA network
You can create clusters of RDMA-capable Windows Server instances and deploy one of the supported MPI implementations to take advantage of the Azure RDMA network. This low-latency, high-throughput network is reserved for MPI traffic only.

* **Operating system**
  
  * **Virtual machines** - Windows Server 2012 R2, Windows Server 2012
  * **Cloud services** - Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 Guest OS family
* **MPI** - Microsoft MPI (MS-MPI) 2012 R2 or later, Intel MPI Library 5.x

Supported MPI implementations use the Microsoft Network Direct interface to communicate between instances. See [Set up a Windows RDMA cluster with HPC Pack to run MPI applications](/documentation/articles/virtual-machines-windows-classic-hpcpack-rdma-cluster/) and [Use multi-instance tasks to run Message Passing Interface (MPI) applications in Azure Batch](/documentation/articles/batch-mpi/) for deployment options and sample configuration steps.

> [AZURE.NOTE]
> On RDMA-capable compute-intensive VMs, the HpcVmDrivers extension must be added to the VMs to install Windows network device drivers that are needed for RDMA connectivity. In most deployments, the HpcVmDrivers extension is added automatically. If you need to add the extension yourself, see [Manage VM extensions](/documentation/articles/virtual-machines-windows-classic-manage-extensions/).
> 
> 

## Considerations for HPC Pack and Windows
[Microsoft HPC Pack](https://technet.microsoft.com/zh-cn/library/jj899572.aspx), Microsoft's free HPC cluster and job management solution, is not required for you to use the compute-intensive instances with Windows Server. However, it is one option for you to create a compute cluster in Azure to run Windows-based MPI applications and other HPC workloads. HPC Pack 2012 R2 and later versions include a runtime environment for MS-MPI that can use the Azure RDMA network when deployed on RDMA-capable VMs.

For more information and checklists to use the compute-intensive instances with HPC Pack on Windows Server, see [Set up a Windows RDMA cluster with HPC Pack to run MPI applications](/documentation/articles/virtual-machines-windows-classic-hpcpack-rdma-cluster/).

## Next steps
* For details about availability and pricing of the compute-intensive sizes, see [Virtual Machines pricing](/pricing/details/virtual-machines/#Windows) and [Cloud Services pricing](/pricing/details/cloud-services/).
* For storage capacities and disk details, see [Sizes for virtual machines](/documentation/articles/virtual-machines-linux-sizes/).
* To get started deploying and using compute-intensive instances with HPC Pack on Windows, see [Set up a Windows RDMA cluster with HPC Pack to run MPI applications](/documentation/articles/virtual-machines-windows-classic-hpcpack-rdma-cluster/).
* For information about using A8 and A9 instances to run MPI applications with Azure Batch, see [Use multi-instance tasks to run Message Passing Interface (MPI) applications in Azure Batch](/documentation/articles/batch-mpi/).

