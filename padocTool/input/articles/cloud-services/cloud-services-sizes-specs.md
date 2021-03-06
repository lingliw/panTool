<properties 
 pageTitle="Sizes for cloud services" 
 description="Lists the different sizes for Azure cloud service web and worker roles." 
 services="cloud-services" 
 documentationCenter="" 
 authors="Thraka" 
 manager="timlt" 
 editor=""/>
<tags 
 ms.service="cloud-services" 
 ms.date="09/14/2015"
 wacn.date=""/>
 
# Sizes for Cloud Services

This topic describes the available sizes and options for Cloud Service role instances (web roles and worker roles). It also provides deployment considerations to be aware of when planning to use these resources.

Azure Virtual Machines and Cloud Services are two of several types of compute resources offered by Azure. For explanations, see [Compute Hosting Options Provided by Azure](/documentation/articles/fundamentals-application-models).

> [AZURE.NOTE]To see related Azure limits, see [Azure Subscription and Service Limits, Quotas, and Constraints](/documentation/articles/azure-subscription-service-limits)

## Sizes for web and worker role instances

The following considerations might help you decide on a size:

* D-series VM instances are designed to run applications that demand higher compute power and temporary disk performance. D-series VMs provide faster processors, a higher memory-to-core ratio, and a solid-state drive (SSD) for the temporary disk. For details, see the announcement on the Azure blog, [New D-Series Virtual Machine Sizes](http://azure.microsoft.com/blog/2014/09/22/new-d-series-virtual-machine-sizes/).  

*   Dv2-series, a follow-on to the original D-series, features a more powerful CPU. The Dv2-series CPU is about 35% faster than the D-series CPU. It is based on the latest generation 2.4 GHz Intel Xeon� E5-2673 v3 (Haswell) processor, and with the Intel Turbo Boost Technology 2.0, can go up to 3.2 GHz. The Dv2-series has the same memory and disk configurations as the D-series.

    Dv2-series regional availability will be based on this schedule:
        Oct'15: US East 2, US Central, US North Central, US West
        Nov'15: US East, Europe North, Europe West
        Jan'16: US South Central, APAC East, APAC Southeast, Japan East, Japan West,
                Australia East, Australia Southeast, Brazil South

* Web roles and worker roles require more temporary disk space than Azure Virtual Machines because of system requirements. The system files reserve 4 GB of space for the Windows page file, and 2 GB of space for the Windows dump file.  

* The OS disk contains the Windows guest OS and includes the Program Files folder (including installations done via startup tasks unless you specify another disk), registry changes, the System32 folder, and the .NET framework.  

* The local resource disk contains Azure logs and configuration files, Azure Diagnostics (which includes your IIS logs), and any local storage resources you define.  

* The apps (application) disk is where your .cspkg is extracted and includes your website, binaries, role host process, startup tasks, web.config, and so on.  

* The A8/A10 and A9/A11 virtual machine sizes have the same capacities. The A8 and A9 virtual machine instances include an additional network adapter that is connected to a remote direct memory access (RDMA) network for fast communication between virtual machines. The A8 and A9 instances are designed for high-performance computing applications that require constant and low-latency communication between nodes during execution, for example, applications that use the Message Passing Interface (MPI). The A10 and A11 virtual machine instances do not include the additional network adapter. A10 and A11 instances are designed for high-performance computing applications that do not require constant and low-latency communication between nodes, also known as parametric or embarrassingly parallel applications.  

|Size|CPU<br>cores|Memory|Disk sizes|
|---|---|---|---|
|ExtraSmall|1|768 MB|OS = Guest OS size<br/>Local resource = 15384 MB<br/>Apps = approx. 1.5 GB|
|Small|1|1.75 GB|OS = Guest OS size<br/>Local resource = 225304 MB<br/>Apps = approx. 1.5 GB|
|Medium|2|3.5 GB|OS = Guest OS size<br/>Local resource = 496664 MB<br/>Apps = approx. 1.5 GB|
|Large|4|7 GB|OS = Guest OS size<br/>Local resource = 1018904 MB<br/>Apps = approx. 1.5 GB|
|ExtraLarge|8|14 GB|OS = Guest OS size<br/>Local resource = 2083864 MB<br/>Apps = approx. 1.5 GB|
|A5|2|14 GB|OS = Guest OS size<br/>Local resource = 496664 MB<br/>Apps = approx. 1.5 GB|
|A6|4|28 GB|OS = Guest OS size<br/>Local resource = 1018904 MB<br/>Apps = approx. 1.5 GB|
|A7|8|56 GB|OS = Guest OS size<br/>Local resource = 2083864 MB<br/>Apps = approx. 1.5 GB
|A8|8|56 GB|OS = Guest OS size<br/>Local resource = 1856172 MB<br/>Apps = approx. 1.5 GB<blockquote> Note: For information and considerations about using this size, see <a href="http://go.microsoft.com/fwlink/p/?linkid=328042">About the A8, A9, A10, and A11 Compute Intensive Instances</a>.</blockquote>|
|A9|16|112 GB|OS = Guest OS size<br/>Local resource = 1856172 MB<br/>Apps = approx. 1.5 GB<blockquote> Note: For information and considerations about using this size, see <a href="http://go.microsoft.com/fwlink/p/?linkid=328042">About the A8, A9, A10, and A11 Compute Intensive Instances</a>.</blockquote>|
|A10|8|56 GB|OS = Guest OS size<br/>Local resource = 1856172 MB<br/>Apps = approx. 1.5 GB<blockquote> Note: For information and considerations about using this size, see <a href="http://go.microsoft.com/fwlink/p/?linkid=328042">About the A8, A9, A10, and A11 Compute Intensive Instances</a>.</blockquote>|
|A11|16|112 GB|OS = Guest OS size<br/>Local resource = 1856172 MB<br/>Apps = approx. 1.5 GB<blockquote> Note: For information and considerations about using this size, see <a href="http://go.microsoft.com/fwlink/p/?linkid=328042">About the A8, A9, A10, and A11 Compute Intensive Instances</a>.</blockquote>|
|Standard_D1|1|3.5 GB|OS = Guest OS size<br/>Local resource = 46104 MB<br/>Apps = approx. 1.5 GB|
|Standard_D2|2|7 GB|OS = Guest OS size<br/>Local resource = 97304 MB<br/>Apps = approx. 1.5 GB|
|Standard_D3|4|14 GB|OS = Guest OS size<br/>Local resource = 199704 MB<br/>Apps = approx. 1.5 GB|
|Standard_D4|8|28 GB|OS = Guest OS size<br/>Local resource = 404504 MB<br/>Apps = approx. 1.5 GB|
|Standard_D11|2|14 GB|OS = Guest OS size<br/>Local resource = 97304 MB<br/>Apps = approx. 1.5 GB|
|Standard_D12|4|28 GB|OS = Guest OS size<br/>Local resource = 199704 MB<br/>Apps = approx. 1.5 GB|
|Standard_D13|8|56 GB|OS = Guest OS size<br/>Local resource = 404504 MB<br/>Apps = approx. 1.5 GB|
|Standard_D14|16|112 GB|OS = Guest OS size<br/>Local resource = 814104 MB<br/>Apps = approx. 1.5 GB|
|Standard_D1_v2|1|3.5 GB|OS = Guest OS size<br/>Local resource = 46104 MB<br/>Apps = approx. 1.5 GB|
|Standard_D2_v2|2|7 GB|OS = Guest OS size<br/>Local resource = 97304 MB<br/>Apps = approx. 1.5 GB|
|Standard_D3_v2|4|14 GB|OS = Guest OS size<br/>Local resource = 199704 MB<br/>Apps = approx. 1.5 GB|
|Standard_D4_v2|8|28 GB|OS = Guest OS size<br/>Local resource = 404504 MB<br/>Apps = approx. 1.5 GB|
|Standard_D5_v2|16|56 GB|OS = Guest OS size<br/>Local resource = 814104 MB<br/>Apps = approx. 1.5 GB|
|Standard_D11_v2|2|14 GB|OS = Guest OS size<br/>Local resource = 97304 MB<br/>Apps = approx. 1.5 GB|
|Standard_D12_v2|4|28 GB|OS = Guest OS size<br/>Local resource = 199704 MB<br/>Apps = approx. 1.5 GB|
|Standard_D13_v2|8|56 GB|OS = Guest OS size<br/>Local resource = 404504 MB<br/>Apps = approx. 1.5 GB|
|Standard_D14_v2|16|112 GB|OS = Guest OS size<br/>Local resource = 814104 MB<br/>Apps = approx. 1.5 GB|
## Configure sizes for Cloud Services

You can specify the Virtual Machine size of a role instance as part of the service model described by the service definition file. The size of the role determines the number of CPU cores, the memory capacity, and the local file system size that is allocated to a running instance. Choose the role size based on your application's resource requirement.

Here is an example for setting the role size to be small for a Web Role instance:


    <WebRole name="WebRole1" vmsize="Small">
    �
    </WebRole>

Ensure that the local resource size specified is less than or equal to the max local resource size in the table above.
## Next steps

[Set Up a Cloud Service for Azure](https://msdn.microsoft.com/zh-cn/library/hh124108)  
