<properties
    pageTitle="Create a Linux VM using the Azure CLI | Azure"
    description="Create a Linux VM on Azure by using the Azure CLI for NodeJs."
    services="virtual-machines-linux"
    documentationcenter=""
    author="vlivech"
    manager="timlt"
    editor="" />
<tags
    ms.assetid="facb1115-2b4e-4ef3-9905-330e42beb686"
    ms.service="virtual-machines-linux"
    ms.devlang="NA"
    ms.topic="hero-article"
    ms.tgt_pltfrm="vm-linux"
    ms.workload="infrastructure"
    ms.date="10/27/2016"
    wacn.date=""
    ms.author="v-livech" />

# Create a Linux VM using the Azure CLI
This article shows how to quickly deploy a Linux virtual machine (VM) on Azure by using the `azure vm quick-create` command in the Azure command-line interface (CLI). The `quick-create` command deploys a VM inside a basic, secure infrastructure that you can use to prototype or test a concept rapidly. 

> [AZURE.NOTE] 
To create a VM using the Azure CLI 2.0 (Preview), see [Create a VM with the Azure CLI](/documentation/articles/virtual-machines-linux-quick-create-cli/).

The article requires:

* an Azure account ([get a trial](/pricing/1rmb-trial/)).
* the [Azure CLI](/documentation/articles/xplat-cli-install/) logged in with `azure login -e AzureChinaCloud`.
* the Azure CLI *must be in* Azure Resource Manager mode `azure config mode arm`.

You can also quickly deploy a Linux VM by using the [Azure portal preview](/documentation/articles/virtual-machines-linux-quick-create-portal/).

## Quick commands
The following example shows how to deploy a CoreOS VM and attach your Secure Shell (SSH) key (your arguments might be different):

    azure vm quick-create -M ~/.ssh/id_rsa.pub -Q CoreOS

## Detailed walkthrough
The following walkthrough has an UbuntuLTS VM being deployed, step by step, with explanations of what each step is doing.

## VM quick-create aliases
A quick way to choose a distribution is to use the Azure CLI aliases mapped to the most common OS distributions. The following table lists the aliases (as of Azure CLI version 0.10). All deployments that use `quick-create` default to VMs that are backed by solid-state drive (SSD) storage, which offers faster provisioning and high-performance disk access. (These aliases represent a tiny portion of the available distributions on Azure. Find more images in the Azure Marketplace by [searching for an image in PowerShell](/documentation/articles/virtual-machines-linux-cli-ps-findimage/), [on the web](https://azure.microsoft.com/marketplace/virtual-machines/), or [upload your own custom image](/documentation/articles/virtual-machines-linux-create-upload-generic/).)

| Alias | Publisher | Offer | SKU | Version |
|:--- |:--- |:--- |:--- |:--- |
| CentOS |OpenLogic |CentOS |7.2 |latest |
| CoreOS |CoreOS |CoreOS |Stable |latest |
| Debian |credativ |Debian |8 |latest |
| openSUSE |SUSE |openSUSE |13.2 |latest |
| UbuntuLTS |Canonical |Ubuntu Server |14.04.3-LTS |latest |

The following sections use the `UbuntuLTS` alias for the **ImageURN** option (`-Q`) to deploy an Ubuntu 14.04.3 LTS Server.

The previous `quick-create` example only called out the `-M` flag to identify the SSH public key to upload while disabling SSH passwords, so you are prompted for the following arguments:

* resource group name (any string is typically fine for your first Azure resource group)
* VM name
* location (`chinanorth` or `westeurope` are good defaults)
* linux (to let Azure know which OS you want)
* username

The following example specifies all the values so that no further prompting is required. So long as you have an `~/.ssh/id_rsa.pub` as a ssh-rsa format public key file, it works as is:

    azure vm quick-create \
      --resource-group myResourceGroup \
      --name myVM \
      --location chinanorth \
      --os-type Linux \
      --admin-username myAdminUser \
      --ssh-public-file ~/.ssh/id_rsa.pub \
      --image-urn UbuntuLTS

The output should look like the following output block:

    info:    Executing command vm quick-create
    + Listing virtual machine sizes available in the location "chinanorth"
    + Looking up the VM "myVM"
    info:    Verifying the public key SSH file: /Users/ahmet/.ssh/id_rsa.pub
    info:    Using the VM Size "Standard_DS1"
    info:    The [OS, Data] Disk or image configuration requires storage account
    + Looking up the storage account cli16330708391032639673
    + Looking up the NIC "examp-china-1633070839-nic"
    info:    An nic with given name "examp-china-1633070839-nic" not found, creating a new one
    + Looking up the virtual network "examp-china-1633070839-vnet"
    info:    Preparing to create new virtual network and subnet
    / Creating a new virtual network "examp-china-1633070839-vnet" [address prefix: "10.0.0.0/16"] with subnet "examp-china-1633070839-snet" [address prefix: "10.+.1.0/24"]
    + Looking up the virtual network "examp-china-1633070839-vnet"
    + Looking up the subnet "examp-china-1633070839-snet" under the virtual network "examp-china-1633070839-vnet"
    info:    Found public ip parameters, trying to setup PublicIP profile
    + Looking up the public ip "examp-china-1633070839-pip"
    info:    PublicIP with given name "examp-china-1633070839-pip" not found, creating a new one
    + Creating public ip "examp-china-1633070839-pip"
    + Looking up the public ip "examp-china-1633070839-pip"
    + Creating NIC "examp-china-1633070839-nic"
    + Looking up the NIC "examp-china-1633070839-nic"
    + Looking up the storage account clisto1710997031examplev
    + Creating VM "myVM"
    + Looking up the VM "myVM"
    + Looking up the NIC "examp-china-1633070839-nic"
    + Looking up the public ip "examp-china-1633070839-pip"
    data:    Id                              :/subscriptions/2<--snip-->d/resourceGroups/exampleResourceGroup/providers/Microsoft.Compute/virtualMachines/exampleVMName
    data:    ProvisioningState               :Succeeded
    data:    Name                            :exampleVMName
    data:    Location                        :chinanorth
    data:    Type                            :Microsoft.Compute/virtualMachines
    data:
    data:    Hardware Profile:
    data:      Size                          :Standard_DS1
    data:
    data:    Storage Profile:
    data:      Image reference:
    data:        Publisher                   :Canonical
    data:        Offer                       :UbuntuServer
    data:        Sku                         :14.04.3-LTS
    data:        Version                     :latest
    data:
    data:      OS Disk:
    data:        OSType                      :Linux
    data:        Name                        :clic7fadb847357e9cf-os-1473374894359
    data:        Caching                     :ReadWrite
    data:        CreateOption                :FromImage
    data:        Vhd:
    data:          Uri                       :https://cli16330708391032639673.blob.core.chinacloudapi.cn/vhds/clic7fadb847357e9cf-os-1473374894359.vhd
    data:
    data:    OS Profile:
    data:      Computer Name                 :myVM
    data:      User Name                     :myAdminUser
    data:      Linux Configuration:
    data:        Disable Password Auth       :true
    data:
    data:    Network Profile:
    data:      Network Interfaces:
    data:        Network Interface #1:
    data:          Primary                   :true
    data:          MAC Address               :00-0D-3A-33-42-FB
    data:          Provisioning State        :Succeeded
    data:          Name                      :examp-china-1633070839-nic
    data:          Location                  :chinanorth
    data:            Public IP address       :138.91.247.29
    data:            FQDN                    :examp-china-1633070839-pip.chinanorth.chinacloudapp.cn
    data:
    data:    Diagnostics Profile:
    data:      BootDiagnostics Enabled       :true
    data:      BootDiagnostics StorageUri    :https://clisto1710997031examplev.blob.core.chinacloudapi.cn/
    data:
    data:      Diagnostics Instance View:
    info:    vm quick-create command OK

## Log in to the new VM
Log in to your VM by using the public IP address listed in the output. You can also use the fully qualified domain name (FQDN) that's listed:

    ssh -i ~/.ssh/id_rsa.pub ahmet@138.91.247.29

The login process should look something like the following output block:

    Warning: Permanently added '138.91.247.29' (ECDSA) to the list of known hosts.
    Welcome to Ubuntu 14.04.3 LTS (GNU/Linux 3.19.0-65-generic x86_64)

     * Documentation:  https://help.ubuntu.com/

      System information as of Thu Sep  8 22:50:57 UTC 2016

      System load: 0.63              Memory usage: 2%   Processes:       81
      Usage of /:  39.6% of 1.94GB   Swap usage:   0%   Users logged in: 0

      Graph this data and manage this system at:
        https://landscape.canonical.com/

      Get cloud support with Ubuntu Advantage Cloud Guest:
        http://www.ubuntu.com/business/services/cloud

    0 packages can be updated.
    0 updates are security updates.



    The programs included with the Ubuntu system are free software;
    the exact distribution terms for each program are described in the
    individual files in /usr/share/doc/*/copyright.

    Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
    applicable law.

    myAdminUser@myVM:~$

## Next steps
The `azure vm quick-create` command is the way to quickly deploy a VM so you can log in to a bash shell and get working. However, using `vm quick-create` does not give you extensive control nor does it enable you to create a more complex environment.  To deploy a Linux VM that's customized for your infrastructure, you can follow any of these articles:

* [Use an Azure Resource Manager template to create a specific deployment](/documentation/articles/virtual-machines-linux-cli-deploy-templates/)
* [Create your own custom environment for a Linux VM using Azure CLI commands directly](/documentation/articles/virtual-machines-linux-create-cli-complete/)
* [Create an SSH Secured Linux VM on Azure using templates](/documentation/articles/virtual-machines-linux-create-ssh-secured-vm-from-template/)
