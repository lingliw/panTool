<!-- rename to virtual-machines-linux-opensource-links -->

<properties
	pageTitle="Linux and Open-Source Computing on Azure | Azure"
	description="Lists Linux and Open-Source Computing articles on Azure, including basic Linux usage, some fundamental concepts about running or uploading Linux images on Azure, and other content about specific technologies and optimizations."
	services="virtual-machines"
	documentationCenter=""
	authors="squillace"
	manager="timlt"
	editor="tysonn"
	tags="azure-resource-manager,azure-service-management"/>

<tags
	ms.service="virtual-machines"
	ms.date="01/03/2016"
	wacn.date=""/>



# Linux and open-source computing on Azure

This document attempts to list in one place all the topics written by Microsoft and its partners about running Linux-based Virtual Machines as well as other open-source compute environments and applications on Azure. Articles that describe the classic deployment model only are noted, as are those that use the Resource Manager deployment model. Articles that lack a deployment model note describe both deployment models.

As both Azure and the open-source computing world are fast-moving targets, it is almost certain that this document is out of date, *despite* the fact that we shall do our best to continually add newer topics and remove out-of-date ones. If we've missed one, please let us know in the comments, or submit a pull request to our [GitHub repo](https://github.com/wacn/techcontent/).

[AZURE.INCLUDE [learn-about-deployment-models](../../includes/learn-about-deployment-models-both-include.md)]


## General notes
The sections are broken down on the right of this page. (Links may occur in more than one section, as topics can be about more than one concept, distro, or technology.) In addition, there are several topics that describe various Linux options, image repositories, case studies, and how-to topics to upload your own custom images:

- [MSOpenTech VM Depot](https://vmdepot.msopentech.com/List/Index)
- [Events and Demonstrations: Microsoft Openness CEE](http://www.opennessatcee.com/)
- \[Classic Deployment]: [How to: Uploading your own Distro Image](/documentation/articles/virtual-machines-linux-classic-create-upload-vhd/) (and also instructions using an [Azure-Endorsed Distribution](/documentation/articles/virtual-machines-linux-endorsed-distros/))
- [Notes: General Linux Requirements to Run in Azure](/documentation/articles/virtual-machines-linux-create-upload-generic/)
- \[Classic Deployment]: [Notes: General Introduction for Linux on Azure](/documentation/articles/virtual-machines-linux-intro-on-azure/)

## Distros

There are tons of Linux distributions, usually broken down by the package management systems: Some are dpkg-based, like Debian and Ubuntu, and others are rpm-based, like CentOS, SUSE, and RedHat. Some companies provide distro images as formal partners of Microsoft and are endorsed. Others are provided by the community. The distros in this section have formal articles about them, even if they were only used in examples of other technologies.

### Ubuntu

Ubuntu is a very popular and Azure-endorsed Linux distribution based on dpkg and apt-get package management.

1. [How to: Upload your own Ubuntu Image](/documentation/articles/virtual-machines-linux-create-upload-ubuntu/)
2. [How to: Ubuntu LAMP Stack](/documentation/articles/virtual-machines-linux-install-lamp-stack/)
3. \[Classic Deployment]: [How to: MySQL Clusters](/documentation/articles/virtual-machines-linux-classic-mysql-cluster/)
4. \[Classic Deployment]: [How to: Node.js and Cassandra](/documentation/articles/virtual-machines-linux-classic-cassandra-nodejs/)
5. \[Resource Manager Deployment]: [How to: IPython Notebook](/documentation/articles/virtual-machines-linux-jupyter-notebook/)
6. \[Classic Deployment]: [Geeking out: Running ASP.NET 5 on Linux using Docker Containers](http://blogs.msdn.com/b/webdev/archive/2015/01/14/running-asp-net-5-applications-in-linux-containers-with-docker.aspx)


### [Debian](https://vmdepot.msopentech.com/List/Index?sort=Featured&search=Debian)

Debian is an important distribution for the Linux and open-source world based on dpkg and apt-get package management. The MSOpenTech VM Depot has several images to use.

### CentOS

The CentOS Linux distribution is a stable, predictable, manageable and reproduceable platform derived from the sources of Red Hat Enterprise Linux (RHEL).

1. [MSOpenTech VM Depot](https://vmdepot.msopentech.com/List/Index?sort=Featured&search=centos)
3. [How to: Prepare a Custom CentOS-Based VM for Azure](/documentation/articles/virtual-machines-linux-create-upload-centos/)
4. \[Classic Deployment]: [Blog: How to Deploy a CentOS VM Image from OpenLogic](https://azure.microsoft.com/blog/2013/01/11/deploying-openlogic-centos-images-on-windows-azure-virtual-machines/)
6. \[Classic Deployment]: [How to: Install Apache Qpid Proton-C for AMQP and Service Bus](/documentation/articles/service-bus-amqp-apache/)

### SUSE Linux Enterprise Server and openSUSE

9. [MSOpenTech VM Depot](https://vmdepot.msopentech.com/List/Index?sort=Featured&search=OpenSUSE)
11. \[Classic Deployment]: [How to: Install and Run MySQL](/documentation/articles/virtual-machines-linux-classic-mysql-on-opensuse/)
12. [How To: Prep a Custom SLES or openSUSE VM](/documentation/articles/virtual-machines-linux-suse-create-upload-vhd/)  
13. [[SUSE forum] How to: Move to a New Patch Server](https://forums.suse.com/showthread.php?5622-New-Update-Infrastructure)

### CoreOS

CoreOS is a small, optimized distro for pure compute scale with a high degree of control for customization.

11. \[Classic Deployment]: [How to: Use CoreOS on Azure](/documentation/articles/virtual-machines-linux-classic-coreos-howto/)
12. \[Classic Deployment]: [How to: Get Started with Fleet and Docker on CoreOS on Azure](/documentation/articles/virtual-machines-linux-classic-coreos-fleet-get-started/)


#### Oracle Linux
  2. [Prepare an Oracle Linux Virtual Machine for Azure](/documentation/articles/virtual-machines-linux-oracle-create-upload-vhd/)

### FreeBSD

12. [MSOpenTech VM Depot](https://vmdepot.msopentech.com/List/Index?sort=Date&search=FreeBSD)
13. \[Classic Deployment]: [Blog: Running FreeBSD in Azure](https://azure.microsoft.com/blog/2014/05/22/running-freebsd-in-azure/)
14. \[Classic Deployment]: [Blog: Easy Deploy FreeBSD](http://msopentech.com/blog/2014/10/24/easy-deploy-freebsd-microsoft-azure-vm-depot/)
15. [Blog: Deploying a Customized FreeBSD Image](http://msopentech.com/blog/2014/05/14/deploy-customize-freebsd-virtual-machine-image-microsoft-azure/)
17. [How to: Install the Azure Linux Agent](/documentation/articles/virtual-machines-linux-agent-user-guide/)

## The basics

1. [The basics: Azure Command-Line Interface (Azure CLI)](/documentation/articles/xplat-cli-install/)
5. [The basics: Selecting Linux Usernames](/documentation/articles/virtual-machines-linux-usernames/)
6. \[Classic Deployment]: [The basics: Log on to a Linux VM Using the Azure classic portal](/documentation/articles/virtual-machines-linux-classic-log-on/)
7. [The basics: SSH](/documentation/articles/virtual-machines-linux-ssh-from-linux/)
8. \[Classic Deployment]: [The basics: How to Reset a Password or SSH Properties for Linux](/documentation/articles/virtual-machines-linux-classic-reset-access/)
9. [The basics: Using Root](/documentation/articles/virtual-machines-linux-use-root-privileges/)
10. \[Classic Deployment]: [The basics: Attaching a Data Disk to a Linux VM](/documentation/articles/virtual-machines-linux-classic-attach-disk/)
11. \[Classic Deployment]: [The basics: Detaching a Data Disk from a Linux VM](/documentation/articles/virtual-machines-linux-classic-detach-disk/)
12. [Blogging the basics: Optimizing Storage, Disks, and Performance with Linux and Azure](http://blogs.msdn.com/b/igorpag/archive/2014/10/23/azure-storage-secrets-and-linux-i-o-optimizations.aspx)
13. [The basics: RAID](/documentation/articles/virtual-machines-linux-configure-raid/)
14. \[Classic Deployment]: [The basics: Capturing a Linux VM to Make a Template](/documentation/articles/virtual-machines-linux-classic-capture-image/)
15. [The basics: The Azure Linux Agent](/documentation/articles/virtual-machines-linux-agent-user-guide/)
16. [The basics: Azure VM Extensions and Features](/documentation/articles/virtual-machines-linux-extensions-features/)
17. \[Classic Deployment]: [The basics: Injecting Custom Data into a VM to use with Cloud-init](/documentation/articles/virtual-machines-linux-classic-inject-custom-data/)
18. \[Classic Deployment]: [Blogging the basics: Building Highly Available Linux on Azure in 12 Steps](http://blogs.technet.com/b/keithmayer/archive/2014/10/03/quick-start-guide-building-highly-available-linux-servers-in-the-cloud-on-microsoft-azure.aspx)
19. \[Classic Deployment]: [Blogging the basics: Automate Provisioning Linux on Azure with Azure CLI, node.js, jhawk](http://blogs.technet.com/b/keithmayer/archive/2014/11/24/step-by-step-automated-provisioning-for-linux-in-the-cloud-with-microsoft-azure-xplat-cli-json-and-node-js-part-1.aspx)
20. [The basics: The Azure Docker VM Extension](/documentation/articles/virtual-machines-linux-dockerextension/)
23. \[Classic Deployment]: [Azure Service Management REST API](https://msdn.microsoft.com/zh-cn/library/azure/ee460799.aspx) reference
24. \[Classic Deployment]: [GlusterFS on Azure](http://dastouri.azurewebsites.net/gluster-on-azure-part-1/)

## Community images and repositories
3. [MSOpenTech VM Depot](https://vmdepot.msopentech.com/List/Index) &mdash; for community provided virtual machine images.
4. [GitHub](https://github.com/Azure/) &mdash; for the Azure CLI, and many other tools and projects.
5. [Docker Hub Registry](https://registry.hub.docker.com/) &mdash; the registry for Docker container images.

## Languages and platforms
### [Azure Java dev center](/develop/java/)

1. [Images](https://vmdepot.msopentech.com/List/Index?sort=Featured&search=java)
2. [How to: Use Service Bus from Java with AMQP 1.0](/documentation/articles/service-bus-amqp-java/)
3. [How to: Set up Tomcat7 on Linux Using the Azure classic portal](/documentation/articles/virtual-machines-linux-classic-setup-tomcat/)
4. [Video: Azure Java SDK for Service Management](http://channel9.msdn.com/Shows/Cloud+Cover/Episode-157-The-Java-SDK-for-Azure-Management-with-Brady-Gaster)
5. [Blog: Getting Started with Azure Management Libraries for Java](https://azure.microsoft.com/blog/2014/09/15/getting-started-with-the-azure-java-management-libraries/)
5. [GitHub repo: Azure Toolkit for Eclipse with Java](https://github.com/MSOpenTech/WindowsAzureToolkitForEclipseWithJava)
6. [Reference: Azure Toolkit for Eclipse with Java](/documentation/articles/azure-toolkit-for-eclipse/)
7. [GitHub repo: MS Open Tech Tools plugin for IntelliJ IDEA and Android Studio](https://github.com/MSOpenTech/msopentech-tools-for-intellij)
7. [Blog: MSOpenTech Contributes to the OpenJDK](http://msopentech.com/blog/2014/10/21/ms-open-techs-first-contribution-openjdk/)


### JVM languages

1. [Scala: Running Play Framework Applications in Azure Cloud Services](http://msopentech.com/blog/2014/09/25/tutorial-running-play-framework-applications-microsoft-azure-cloud-services-2/)

### SDK types, installations, upgrades
4. [Azure Service Management SDK: Java](http://azure.github.io/azure-sdk-for-java/)
5. [Azure Service Management SDK: Go](https://github.com/MSOpenTech/azure-sdk-for-go)
5. [Azure Service Management SDK: Ruby](https://github.com/MSOpenTech/azure-sdk-for-ruby)
    - [How to: Install Ruby on Rails](/documentation/articles/virtual-machines-linux-classic-ruby-rails-web-app/)
6. [Azure Service Management SDK: Python](https://github.com/Azure/azure-sdk-for-python)
    - [How to: Django Hello World Web Application (Mac-Linux)](/documentation/articles/virtual-machines-linux-python-django-web-app/)
7. [Azure Service Management SDK: Node.js](https://github.com/MSOpenTech/azure-sdk-for-node)
8. [Azure Service Management SDK: PHP](https://github.com/MSOpenTech/azure-sdk-for-php)
    - [How to: Install the LAMP Stack on an Azure VM](/documentation/articles/virtual-machines-linux-install-lamp-stack/)
    - [Video: Install a LAMP Stack on an Azure VM](http://channel9.msdn.com/Shows/Azure-Friday/LAMP-stack-on-Azure-VMs-with-Guy-Bowerman)
9. [Azure Service Management SDK: .NET](https://github.com/Azure/azure-sdk-for-net)
10. [Blog: Mono, ASP.NET 5, Linux, and Docker](http://blogs.msdn.com/b/webdev/archive/2015/01/14/running-asp-net-5-applications-in-linux-containers-with-docker.aspx)

## Samples and scripts

Look for this section to fill up quickly. If you have suggestions, send us a PR or leave them in comments, below.

2. [Patrick Chanezon's Azure Linux GitHub repository](https://github.com/chanezon/azure-linux)

## Data

This section contains information about several different storage approaches and technologies, including NoSQL, Relational, and Big Data.

### NoSQL

1. [Blog: 8 Open-source NoSql Databases for Azure](http://openness.microsoft.com/blog/2014/11/03/open-source-nosql-databases-microsoft-azure/)
2. Couchdb
    - [Slideshare (MSOpenTech): Experiences with CouchDb on Azure](http://www.slideshare.net/brianbenz/experiences-using-couchdb-inside-microsofts-azure-team)
    - [Blog: Running CouchDB-as-a-Service with node.js, CORS, and Grunt](http://msopentech.com/blog/2013/12/19/tutorial-building-multi-tier-windows-azure-web-application-use-cloudants-couchdb-service-node-js-cors-grunt-2/)
3. MongoDB
    - [How to: Create a Node.js Application on Azure with MongoDB using the MongoLab Add-On](/documentation/articles/web-sites-dotnet-store-data-mongodb-vm/)
4. Cassandra
    - [How to: Running Cassandra with Linux on Azure and Accessing it from Node.js](/documentation/articles/virtual-machines-linux-classic-cassandra-nodejs/)
5. Redis
    - [Blog: Redis on Windows in the Azure Redis Cache Service](http://msopentech.com/blog/2014/05/12/redis-on-windows/)
    - [Blog: Announcing ASP.NET Session State Provider for Redis Preview Release](http://blogs.msdn.com/b/webdev/archive/2014/05/12/announcing-asp-net-session-state-provider-for-redis-preview-release.aspx)

### Big Data
2. Hadoop/Cloudera  
	- [Blog: Installing Hadoop on Azure Linux VMs](http://blogs.msdn.com/b/benjguin/archive/2013/04/05/how-to-install-hadoop-on-windows-azure-linux-virtual-machines.aspx)
3. [Azure HDInsight](/documentation/services/hdinsight/) -- a fully managed Hadoop service on Azure.

### Relational database
2. MySQL
    - [How to: Install and Run MySQL](/documentation/articles/virtual-machines-linux-classic-mysql-on-opensuse/)
    - [How to: Optimize Performance of MySQL on Azure](/documentation/articles/virtual-machines-linux-classic-optimize-mysql/)
    - [How to: MySQL Clusters](/documentation/articles/virtual-machines-linux-classic-mysql-cluster/)
    - [How to: Create a MySQL Database using the Marketplace](/documentation/articles/store-php-create-mysql-database/)
    - [How to: Django and MySQL on Azure Websites with Python and Visual Studio](/documentation/articles/web-sites-python-ptvs-django-mysql/)
    - [MySQL High Availability Architecture in Azure](http://download.microsoft.com/download/6/1/C/61C0E37C-F252-4B33-9557-42B90BA3E472/MySQL_HADR_solution_in_Azure.pdf)
7. MariaDB
    - [How to: Create a Multi-Master cluster of MariaDbs](/documentation/articles/virtual-machines-linux-classic-mariadb-mysql-cluster/)
8. [Installing Postgres with corosync, pg_bouncer using ILB](https://github.com/chgeuer/postgres-azure)


## Auth and encryption

Authentication and encryption are critical topics in software development, and there are many, many topics on the web that describe how to learn and use proper security techniques for both. We describe some of the basic usage to get up and running quickly with Linux and opensource workloads, as well pointing to tools to use to reset or remove remote security features on Azure. These are basic procedures, and we will be adding more complex scenarios soon.

7. [The basics: SSH](/documentation/articles/virtual-machines-linux-ssh-from-linux/)
8. [The basics: How to Reset a Password or SSH Properties for Linux](/documentation/articles/virtual-machines-linux-classic-reset-access/)
9. [The basics: Using Root](/documentation/articles/virtual-machines-linux-use-root-privileges/)

## Linux high performance computing (HPC)

Run HPC workloads on Linux VM clusters built with open-source tools or with Microsoft HPC Pack.

4.	[Tutorial: Get started with Linux compute nodes in an HPC Pack cluster in Azure](/documentation/articles/virtual-machines-linux-classic-hpcpack-cluster/)
5.	[Tutorial: Run NAMD with Microsoft HPC Pack on Linux compute nodes in Azure](/documentation/articles/virtual-machines-linux-classic-hpcpack-cluster-namd/)
6.	[Tutorial: Set up a Linux RDMA cluster to run MPI applications](/documentation/articles/virtual-machines-linux-classic-rdma-cluster/)


## Devops, management, and optimization

This section starts with a blog entry containing a series of videos on [Video: Azure Virtual Machines : Using Chef, Puppet and Docker for managing Linux VMs](https://azure.microsoft.com/blog/2014/12/15/azure-virtual-machines-using-chef-puppet-and-docker-for-managing-linux-vms/). However, the world of devops, management, and optimization is quite expansive and changing very quickly, so you should consider the list below a starting point.

1. Docker
	- [Docker VM Extension for Linux on Azure](/documentation/articles/virtual-machines-linux-dockerextension/)
	- [Using the Docker VM Extension from the Azure Command-line Interface (Azure CLI)](/documentation/articles/virtual-machines-linux-classic-cli-use-docker/)
	- [Using the Docker VM Extension from the Azure portal](/documentation/articles/virtual-machines-docker-with-portal/)
	- [Getting Started Quickly with Docker in the Azure gallery](/documentation/articles/virtual-machines-docker-ubuntu-quickstart/)
	- [How to use docker-machine on Azure](/documentation/articles/virtual-machines-linux-classic-docker-machine/)
	- [How to use docker with swarm on Azure](/documentation/articles/virtual-machines-linux-docker-swarm/)
	- [Get Started with Docker and Compose on Azure](/documentation/articles/virtual-machines-linux-docker-compose-quickstart/)

2. [Fleet with CoreOS](/documentation/articles/virtual-machines-linux-classic-coreos-howto/)
3. Deis
	- [GitHub repo: Installing Deis on a CoreOS cluster on Azure](https://github.com/chanezon/azure-linux/tree/master/coreos/deis)
4. Kubernetes
	- [Complete guide to automated Kubernetes cluster deployment with CoreOS and Weave](https://github.com/GoogleCloudPlatform/kubernetes/blob/master/docs/getting-started-guides/coreos/azure/README.md#kubernetes-on-azure-with-coreos-and-weave)
	- [Kubernetes Visualizer](https://azure.microsoft.com/blog/2014/08/28/hackathon-with-kubernetes-on-azure/)
5. Jenkins and Hudson
	- [Blog: Jenkins Slave Plug-in for Azure](http://msopentech.com/blog/2014/09/23/announcing-jenkins-slave-plugin-azure/)
	- [GitHub repo: Jenkins Storage Plug-in for Azure](https://github.com/jenkinsci/windows-azure-storage-plugin)
	- [Third Party: Hudson Slave Plug-in for Azure](http://wiki.hudson-ci.org/display/HUDSON/Azure+Slave+Plugin)
	- [Third Party: Hudson Storage Plug-in for Azure](https://github.com/hudson3-plugins/windows-azure-storage-plugin)
10. Chef
	- [Chef and Virtual Machines](/documentation/articles/virtual-machines-windows-chef-automation/)
13. Powershell DSC for Linux
    - [Blog: How to do Powershell DSC for Linux](http://blogs.technet.com/b/privatecloud/archive/2014/05/19/powershell-dsc-for-linux-step-by-step.aspx)
    - [GitHub: Docker Client DSC](https://github.com/anweiss/DockerClientDSC)
13. [Ubuntu Juju](https://juju.ubuntu.com/docs/config-azure.html)
14. [Packer plugin for Azure](https://github.com/msopentech/packer-azure)

## Support, troubleshooting, and "it just doesn't work"

1. Microsoft support documentation
	- [Support: Support for Linux Images on Azure](http://support2.microsoft.com/kb/2941892)

<!--Anchors-->
[Distros]: #distros
[The Basics]: #basics
[Community Images and Repositories]: #images
[Languages and Platforms]: #langsandplats
[Samples and Scripts]: #samples
[Auth and Encryption]: #security
[Devops, Management, and Optimization]: #devops
[Support, Troubleshooting, and "It Just Doesn't Work"]: #supportdebug

<!--Link references--In actual articles, you only need a single period before the slash. -->
[How to use docker-machine on Azure]: /documentation/articles/virtual-machines-linux-classic-docker-machine/
[How to use docker with swarm on Azure]: /documentation/articles/virtual-machines-linux-docker-swarm/
