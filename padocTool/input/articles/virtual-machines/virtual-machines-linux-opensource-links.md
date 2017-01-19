<properties
    pageTitle="Linux and Open-Source Computing on Azure | Azure"
    description="Lists Linux and Open-Source Computing articles on Azure, including basic Linux usage, some fundamental concepts about running or uploading Linux images on Azure, and other content about specific technologies and optimizations."
    services="virtual-machines-linux"
    documentationcenter=""
    author="squillace"
    manager="timlt"
    editor="tysonn"
    tags="azure-resource-manager,azure-service-management" />
<tags
    ms.assetid="a7e608b5-26ea-41e0-b46b-1a483a257754"
    ms.service="virtual-machines-linux"
    ms.devlang="NA"
    ms.topic="article"
    ms.tgt_pltfrm="vm-linux"
    ms.workload="infrastructure-services"
    ms.date="06/27/2016"
    wacn.date=""
    ms.author="rasquill" />

# Linux and open-source computing on Azure
Find all the documentation you need to create and manage Linux-based virtual machines in the classic deployment model.

[AZURE.INCLUDE [learn-about-deployment-models](../../includes/learn-about-deployment-models-classic-include.md)]

## Get Started
* [Introduction for Linux on Azure](/documentation/articles/virtual-machines-linux-intro-on-azure/)
* [Frequently asked question about Azure Virtual Machines created with the classic deployment model](/documentation/articles/virtual-machines-linux-classic-faq/)
* [About images for virtual machines](/documentation/articles/virtual-machines-linux-classic-about-images/)
* [Uploading your own Distro Image](/documentation/articles/virtual-machines-linux-classic-create-upload-vhd/) (and also instructions using an [Azure-Endorsed Distribution](/documentation/articles/virtual-machines-linux-endorsed-distros/))
* [Log on to a Linux VM Using the Azure Classic Management Portal](/documentation/articles/virtual-machines-linux-mac-create-ssh-keys/)

## Set up
* [Install Azure Command-Line Interface (Azure CLI)](/documentation/articles/xplat-cli-install/)

## Tutorials
* [Install the LAMP Stack on a Linux virtual machine in Azure](/documentation/articles/virtual-machines-linux-create-lamp-stack/)
* [Ruby on Rails Web application on an Azure VM](/documentation/articles/virtual-machines-linux-classic-ruby-rails-web-app/)
* [How to: Install Apache Qpid Proton-C for AMQP and Service Bus](/documentation/articles/service-bus-amqp-apache/)

### Databases
* [Optimize Performance of MySQL on Azure](/documentation/articles/virtual-machines-linux-classic-optimize-mysql/)
* [MySQL Clusters](/documentation/articles/virtual-machines-linux-classic-mysql-cluster/)
* [Running Cassandra with Linux on Azure and Accessing it from Node.js](/documentation/articles/virtual-machines-linux-classic-cassandra-nodejs/)
* [Create a Multi-Master cluster of MariaDbs](/documentation/articles/virtual-machines-linux-classic-mariadb-mysql-cluster/)

### Ubuntu
* [How to: MySQL Clusters](/documentation/articles/virtual-machines-linux-classic-mysql-cluster/)
* [How to: Node.js and Cassandra](/documentation/articles/virtual-machines-linux-classic-cassandra-nodejs/)

### OpenSUSE
* [How to: Install and Run MySQL](/documentation/articles/virtual-machines-linux-classic-mysql-on-opensuse/)

### CoreOS
* [How to: Use CoreOS on Azure](https://coreos.com/os/docs/latest/booting-on-azure.html)

## Planning
* [Azure infrastructure services implementation guidelines](/documentation/articles/virtual-machines-linux-infrastructure-subscription-accounts-guidelines/)
* [Selecting Linux Usernames](/documentation/articles/virtual-machines-linux-usernames/)
* [How to configure an availability set for virtual machines in the classic deployment model](/documentation/articles/virtual-machines-linux-classic-configure-availability/)
* [How to Schedule Planned Maintenance on Azure VMs](/documentation/articles/virtual-machines-linux-planned-maintenance-schedule/)
* [Manage the availability of virtual machines](/documentation/articles/virtual-machines-linux-manage-availability/)
* [Planned maintenance for Linux virtual machines in Azure](/documentation/articles/virtual-machines-linux-planned-maintenance/)

## Deployment
* [Create a custom virtual machine running Linux](/documentation/articles/virtual-machines-linux-classic-createportal/)
* [The basics: Capturing a Linux VM to Make a Template](/documentation/articles/virtual-machines-linux-classic-capture-image/)
* [Information for Non-Endorsed Distributions](/documentation/articles/virtual-machines-linux-create-upload-generic/)

## Management
* [SSH](/documentation/articles/virtual-machines-linux-mac-create-ssh-keys/)
* [How to Reset a Password or SSH Properties for Linux](/documentation/articles/virtual-machines-linux-classic-reset-access/)
* [Using Root](/documentation/articles/virtual-machines-linux-use-root-privileges/)

## Azure Resources
* [The Azure Linux Agent](/documentation/articles/virtual-machines-linux-agent-user-guide/)
* [Azure VM Extensions and Features](/documentation/articles/virtual-machines-windows-extensions-features/)
* [Injecting Custom Data into a VM to use with Cloud-init](/documentation/articles/virtual-machines-windows-classic-inject-custom-data/)

## Storage
* [Attaching a Data Disk to a Linux VM](/documentation/articles/virtual-machines-linux-classic-attach-disk/)
* [Detaching a Data Disk from a Linux VM](/documentation/articles/virtual-machines-linux-classic-detach-disk/)
* [RAID](/documentation/articles/virtual-machines-linux-configure-raid/)

## Networking
* [How to set up endpoints on a classic virtual machine in Azure](/documentation/articles/virtual-machines-linux-classic-setup-endpoints/)

## Troubleshooting
* [Troubleshoot Secure Shell (SSH) connections to a Linux-based Azure virtual machine](/documentation/articles/virtual-machines-linux-troubleshoot-ssh-connection/)
* [Troubleshoot classic deployment issues with creating a new Linux virtual machine in Azure](/documentation/articles/virtual-machines-linux-classic-troubleshoot-deployment-new-vm/)  
* [Troubleshoot classic deployment issues with restarting or resizing an existing Linux Virtual Machine in Azure](/documentation/articles/virtual-machines-linux-classic-restart-resize-error-troubleshooting/) 

## Reference
* [Azure CLI commands in Azure Service Management (asm) mode](/documentation/articles/virtual-machines-command-line-tools/)
* [Azure Service Management REST API](https://msdn.microsoft.com/zh-cn/library/azure/ee460799.aspx)

## General Links
The following links are for Microsoft blogs, Technet pages, and external sites rather than Azure.cn documentation as above. As both Azure and the open-source computing world are fast-moving targets, it is almost certain that the following links are out of date, *despite* the fact that we shall do our best to continually add newer topics and remove out-of-date ones. If we've missed one, please let us know in the comments, or submit a pull request to our [GitHub repo](https://github.com/Azure/azure-content/).

* [Running ASP.NET 5 on Linux using Docker Containers](http://blogs.msdn.com/b/webdev/archive/2015/01/14/running-asp-net-5-applications-in-linux-containers-with-docker.aspx)
* [How to Deploy a CentOS VM Image from OpenLogic](https://azure.microsoft.com/blog/2013/01/11/deploying-openlogic-centos-images-on-windows-azure-virtual-machines/)
* [SUSE Update Infrastructure](https://forums.suse.com/showthread.php?5622-New-Update-Infrastructure)
* [SUSE Linux Enterprise Server for SAP Cloud Appliance  Library](https://azure.microsoft.com/marketplace/partners/suse/suselinuxenterpriseserver11sp3forsapcloudappliance/)
* [Building Highly Available Linux on Azure in 12 Steps](http://blogs.technet.com/b/keithmayer/archive/2014/10/03/quick-start-guide-building-highly-available-linux-servers-in-the-cloud-on-microsoft-azure.aspx)
* [Automate Provisioning Linux on Azure with Azure CLI, node.js, jhawk](http://blogs.technet.com/b/keithmayer/archive/2014/11/24/step-by-step-automated-provisioning-for-linux-in-the-cloud-with-microsoft-azure-xplat-cli-json-and-node-js-part-1.aspx)
* [GlusterFS on Azure](http://dastouri.azurewebsites.net/gluster-on-azure-part-1/)

### FreeBSD
* [Running FreeBSD in Azure](https://azure.microsoft.com/blog/2014/05/22/running-freebsd-in-azure/)
* [Easy Deploy FreeBSD](http://msopentech.com/blog/2014/10/24/easy-deploy-freebsd-microsoft-azure-vm-depot/)
* [Deploying a Customized FreeBSD Image](http://msopentech.com/blog/2014/05/14/deploy-customize-freebsd-virtual-machine-image-microsoft-azure/)
* [Kaspersky AV for Linux File Server](https://azure.microsoft.com/marketplace/partners/kaspersky-lab/kav-for-lfs-kav-for-lfs/)

### NoSQL
* [Slideshare (MSOpenTech): Experiences with CouchDb on Azure](http://www.slideshare.net/brianbenz/experiences-using-couchdb-inside-microsofts-azure-team)
* [Running CouchDB-as-a-Service with node.js, CORS, and Grunt](http://msopentech.com/blog/2013/12/19/tutorial-building-multi-tier-windows-azure-web-application-use-cloudants-couchdb-service-node-js-cors-grunt-2/)
* [Redis on Windows in the Azure Redis Cache Service](http://msopentech.com/blog/2014/05/12/redis-on-windows/)
* [Announcing ASP.NET Session State Provider for Redis Preview Release](http://blogs.msdn.com/b/webdev/archive/2014/05/12/announcing-asp-net-session-state-provider-for-redis-preview-release.aspx)
* [Blog: RavenHQ Now Available in the Azure Marketplace](https://azure.microsoft.com/blog/2014/08/12/ravenhq-now-available-in-the-azure-store/)

### Big Data
* [Installing Hadoop on Azure Linux VMs](http://blogs.msdn.com/b/benjguin/archive/2013/04/05/how-to-install-hadoop-on-windows-azure-linux-virtual-machines.aspx)
* [Azure HDInsight](https://azure.microsoft.com/documentation/learning-paths/hdinsight-self-guided-hadoop-training/)

### Relational database
* [MySQL High Availability Architecture in Azure](http://download.microsoft.com/download/6/1/C/61C0E37C-F252-4B33-9557-42B90BA3E472/MySQL_HADR_solution_in_Azure.pdf)
* [Installing Postgres with corosync, pg_bouncer using ILB](https://github.com/chgeuer/postgres-azure)

### Linux high performance computing (HPC)
* [Quickstart template: Spin up a SLURM cluster](https://github.com/Azure/azure-quickstart-templates/tree/master/slurm)
  (and [blog post](http://blogs.technet.com/b/windowshpc/archive/2015/06/06/deploy-a-slurm-cluster-on-azure.aspx))
* [Quickstart template: Create an HPC cluster with Linux compute nodes](https://github.com/Azure/azure-quickstart-templates/tree/master/create-hpc-cluster-linux-cn/)

### Devops, management, and optimization
As the world of devops, management, and optimization is quite expansive and changing very quickly, you should consider the list below a starting point.

* [Video: Azure Virtual Machines : Using Chef, Puppet and Docker for managing Linux VMs](https://azure.microsoft.com/blog/2014/12/15/azure-virtual-machines-using-chef-puppet-and-docker-for-managing-linux-vms/)
* [Complete guide to automated Kubernetes cluster deployment with CoreOS and Weave](https://github.com/GoogleCloudPlatform/kubernetes/blob/master/docs/getting-started-guides/coreos/azure/README.md#kubernetes-on-azure-with-coreos-and-weave)
* [Kubernetes Visualizer](https://azure.microsoft.com/blog/2014/08/28/hackathon-with-kubernetes-on-azure/)
* [Jenkins Slave Plug-in for Azure](http://msopentech.com/blog/2014/09/23/announcing-jenkins-slave-plugin-azure/)
* [GitHub repo: Jenkins Storage Plug-in for Azure](https://github.com/jenkinsci/windows-azure-storage-plugin)
* [Third Party: Hudson Slave Plug-in for Azure](http://wiki.hudson-ci.org/display/HUDSON/Azure+Slave+Plugin)
* [Third Party: Hudson Storage Plug-in for Azure](https://github.com/hudson3-plugins/windows-azure-storage-plugin)
* [Video: What is Chef and How does it Work?](https://msopentech.com/blog/2014/03/31/using-chef-to-manage-azure-resources/)
* [Video: How to Use Azure Automation with Linux VMs](http://channel9.msdn.com/Shows/Azure-Friday/Azure-Automation-104-managing-Linux-and-creating-Modules-with-Joe-Levy)
* [Blog: How to do Powershell DSC for Linux](http://blogs.technet.com/b/privatecloud/archive/2014/05/19/powershell-dsc-for-linux-step-by-step.aspx)
* [GitHub: Docker Client DSC](https://github.com/anweiss/DockerClientDSC)
* [Packer plugin for Azure](https://github.com/msopentech/packer-azure)

