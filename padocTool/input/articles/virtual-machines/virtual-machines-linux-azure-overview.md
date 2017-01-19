<properties
    pageTitle="Azure and Linux | Azure"
    description="Describes Azure Compute, Storage, and Networking services with Linux virtual machines."
    services="virtual-machines-linux"
    documentationcenter="virtual-machines-linux"
    author="vlivech"
    manager="timlt"
    editor="" />
<tags
    ms.assetid="7965a80f-ea24-4cc2-bc43-60b574101902"
    ms.service="virtual-machines-linux"
    ms.devlang="NA"
    ms.topic="article"
    ms.tgt_pltfrm="vm-linux"
    ms.workload="infrastructure"
    ms.date="09/14/2016"
    wacn.date=""
    ms.author="v-livech" />

# Azure and Linux
Azure is a growing collection of integrated public cloud services including analytics, Virtual Machines, databases, mobile, networking, storage, and web -- ideal for hosting your solutions.  Azure provides a scalable computing platform that allows you to only pay for what you use, when you want it - without having to invest in on-premises hardware.  Azure is ready when you are to scale your solutions up and out to whatever scale you require to service the needs of your clients.

## Availability
In order for your deployment to qualify for our 99.95 VM Service Level Agreement, you need to deploy two or more VMs running your workload inside of an availability set. This will ensure your VMs are distributed across multiple fault domains in our data centers as well as deployed onto hosts with different maintenance windows. The full [Azure SLA](/support/sla/virtual-machines/) explains the guaranteed availability of Azure as a whole.

## Azure Virtual Machines & Instances
Azure supports running a number of popular Linux distributions provided and maintained by a number of partners.  You will find distributions such as Red Hat Enterprise, CentOS, Debian, Ubuntu, CoreOS, RancherOS, FreeBSD, and more in the Azure Marketplace. We actively work with various Linux communities to add even more flavors to the [Azure endorsed Linux Distros](/documentation/articles/virtual-machines-linux-endorsed-distros/) list.

If your preferred Linux distro of choice is not currently present in the gallery, you can "Bring your own Linux" VM by [creating and uploading a Linux VHD in Azure](/documentation/articles/virtual-machines-linux-create-upload-generic/).

Azure virtual machines allow you to deploy a wide range of computing solutions in an agile way. You can deploy virtually any workload and any language on nearly any operating system - Windows, Linux, or a custom created one from any one of our growing list of partners. Still don't see what you are looking for?  Don't worry - you can also bring your own images from on-premises.

## VM Sizes
When you deploy a VM in Azure, you are going to select a VM size within one of our series of sizes that is suitable to your workload. The size also affects the processing power, memory, and storage capacity of the virtual machine. You are billed based on the amount of time the VM is running and consuming its allocated resources. A complete list of [sizes of Virtual Machines](/documentation/articles/virtual-machines-linux-sizes/).

Here are some basic guidelines for selecting a VM size from one of our series (A, D, DS, G and GS).

* A-series VMs are our value priced entry-level VMs for light workloads and Dev/Test scenarios. They are widely available in all regions and can connect and use all standard resources available to virtual machines.
* D-series VMs are designed to run applications that demand higher compute power and temporary disk performance. D-series VMs provide faster processors, a higher memory-to-core ratio, and a solid-state drive (SSD) for the temporary disk.
* Dv2-series, is the latest version of our D-series, features a more powerful CPU. The Dv2-series CPU is about 35% faster than the D-series CPU. It is based on the latest generation 2.4 GHz Intel Xeon® E5-2673 v3 (Haskell) processor, and with the Intel Turbo Boost Technology 2.0, can go up to 3.2 GHz. The Dv2-series has the same memory and disk configurations as the D-series.

Note: DS-series VMs have access to Premium Storage - our SSD backed high-performance, low-latency storage for I/O intensive workloads. Premium Storage is available in certain regions. For details, see:

- [Premium Storage: High-performance storage for Azure virtual machine workloads](/documentation/articles/storage-premium-storage/)

## Automation
To achieve a proper DevOps culture, all infrastructure must be code.  When all the infrastructure lives in code it can easily be recreated (Phoenix Servers).  Azure works with all the major automation tooling like Ansible, Chef, SaltStack, and Puppet.  Azure also has its own tooling for automation:

* [Azure Templates](/documentation/articles/virtual-machines-linux-create-ssh-secured-vm-from-template/)
* [Azure VMAccess](/documentation/articles/virtual-machines-linux-using-vmaccess-extension/)

Azure is rolling out support for [cloud-init](http://cloud-init.io/) across most Linux Distros that support it.  Currently Canonical's Ubuntu VMs are deployed with cloud-init enabled by default.  RedHats RHEL, CentOS, and Fedora support cloud-init, however the Azure images maintained by RedHat do not have cloud-init installed.  To use cloud-init on a RedHat family OS, you must create a custom image with cloud-init installed.

* [Using cloud-init on Azure Linux VMs](/documentation/articles/virtual-machines-linux-using-cloud-init/)

## Quotas
Each Azure Subscription has default quota limits in place that could impact the deployment of a large number of VMs for your project. The current limit on a per subscription basis is 20 VMs per region.  Quota limits can be raised by filing a support ticket requesting a limit increase.  For more details on quota limits:

* [Azure Subscription Service Limits](/documentation/articles/azure-subscription-service-limits/)

## Partners
Microsoft works closely with our partners to ensure the images available are updated and optimized for an Azure runtime.  For more information on our partners check their marketplace pages below.

Linux on Azure - [Endorsed Distributions](/documentation/articles/virtual-machines-linux-endorsed-distros/)

Canonical - [Azure Marketplace - Ubuntu Server 16.04 LTS](https://portal.azure.cn/#create/Canonical.UbuntuServer1604LTS)

Debian - [Azure Marketplace - Debian 8 "Jessie"](https://portal.azure.cn/#create/credativ.Debian8)

FreeBSD - [Azure Marketplace - FreeBSD 10.3](https://portal.azure.cn/#create/Microsoft.FreeBSD103)

CoreOS - [Azure Marketplace - CoreOS (Stable)](https://portal.azure.cn/#create/CoreOS.CoreOSStable)

## Getting Setup on Azure
To begin using Azure you need an Azure account, the Azure CLI installed, and a pair of SSH public and private keys.

## Sign up for an account
The first step in using the Azure Cloud is to sign up for an Azure account.  Go to the [Azure Account Signup](/pricing/1rmb-trial/) page to get started.

## Install the CLI
With your new Azure account, you can get started immediately using the Azure portal preview, which is a web-based admin panel.  To manage the Azure Cloud via the command-line, you install the `azure-cli`.  Install the [Azure CLI ](/documentation/articles/xplat-cli-install/)on your Mac or Linux workstation.

## Create an SSH key pair
Now you have an Azure account, the Azure web portal, and the Azure CLI.  The next step is to create an SSH key pair that is used to SSH into Linux without using a password.  [Create SSH keys on Linux and Mac](/documentation/articles/virtual-machines-linux-mac-create-ssh-keys/) to enable password-less logins and better security.

## Getting Started with Linux on Azure
With your Azure account setup, the Azure CLI installed and SSH keys created you are now ready to start building out an infrastructure in the Azure Cloud.  The first task is to create a couple of VMs.

## Create a VM using the CLI
Creating a Linux VM using the CLI is a quick way to deploy a VM without leaving the terminal you are working in.  Everything you can specify on the web portal is available via a command-line flag or switch.  

* [Create a Linux VM using the CLI](/documentation/articles/virtual-machines-linux-quick-create-cli/)

## Create a VM in the portal
Creating a Linux VM in the Azure web portal is a way to easily point and click through the various options to get to a deployment.  Instead of using command-line flags or switches, you are able to view a nice web layout of various options and settings.  Everything available via the command-line interface is also available in the portal.

* [Create a Linux VM using the Portal](/documentation/articles/virtual-machines-linux-quick-create-portal/)

## Login using SSH without a password
The VM is now running on Azure and you are ready to log in.  Using passwords to log in via SSH is insecure and time consuming.  Using SSH keys is the most secure way and also the quickest way to login.  When you create you Linux VM via the portal or the CLI, you have two authentication choices.  If you choose a password for SSH, Azure configures the VM to allow logins via passwords.  If you chose to use an SSH public key, Azure configures the VM to only allow logins via SSH keys and disables password logins. To secure your Linux VM by only allowing SSH key logins, use the SSH public key option during the VM creation in the portal or CLI.

* [Disable SSH passwords on your Linux VM by configuring SSHD](/documentation/articles/virtual-machines-linux-mac-disable-ssh-password-usage/)

## Related Azure components
## Storage
* [Introduction to Azure Storage](/documentation/articles/storage-introduction/)
* [Add a disk to a Linux VM using the azure-cli](/documentation/articles/virtual-machines-linux-add-disk/)
* [How to attach a data disk to a Linux VM in the Azure portal preview](/documentation/articles/virtual-machines-linux-attach-disk-portal/)

## Networking
* [Virtual Network Overview](/documentation/articles/virtual-networks-overview/)
* [IP addresses in Azure](/documentation/articles/virtual-network-ip-addresses-overview-arm/)
* [Opening ports to a Linux VM in Azure](/documentation/articles/virtual-machines-linux-nsg-quickstart/)
* [Create a Fully Qualified Domain Name in the Azure portal preview](/documentation/articles/virtual-machines-linux-portal-create-fqdn/)


## Next steps
You now have an overview of Linux on Azure.  The next step is to dive in and create a few VMs!

* [Create a Linux VM on Azure using the Portal](/documentation/articles/virtual-machines-linux-quick-create-portal/)
* [Create a Linux VM on Azure by using the CLI](/documentation/articles/virtual-machines-linux-quick-create-cli/)
