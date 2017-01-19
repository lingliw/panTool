<!-- need to be verified -->

<properties
    pageTitle="Create an Azure VM using PowerShell | Azure"
    description="Use Azure PowerShell and Azure Resource Manager to easily create a new VM running Windows Server."
    services="virtual-machines-windows"
    documentationcenter=""
    author="davidmu1"
    manager="timlt"
    editor=""
    tags="azure-resource-manager" />
<tags
    ms.assetid="14fe9ca9-e228-4d3b-a5d8-3101e9478f6e"
    ms.service="virtual-machines-windows"
    ms.workload="na"
    ms.tgt_pltfrm="na"
    ms.devlang="na"
    ms.topic="get-started-article"
    ms.date="10/21/2016"
    wacn.date=""
    ms.author="davidmu" />

# Create a Windows VM using Resource Manager and PowerShell
This article shows you how to quickly create an Azure Virtual Machine running Windows Server and the resources it needs using [Resource Manager](/documentation/articles/resource-group-overview/) and PowerShell. 

All the steps in this article are required to create a virtual machine and it should take about 30 minutes to do the steps. Replace example parameter values in the commands with names that make sense for your environment.

## Step 1: Install Azure PowerShell
See [How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure/) for information about installing the latest version of Azure PowerShell, selecting your subscription, and signing in to your account.

## Step 2: Create a resource group
All resources must be contained in a resource group, so lets create that first.  

1. Get a list of available locations where resources can be created.

        Get-AzureRmLocation | sort Location | Select Location

2. Set the location for the resources. This command sets the location to **chinaeast**.

        $location = "chinaeast"

3. Create a resource group. This command creates the resource group named **myResourceGroup** in the location that you set.

        $myResourceGroup = "myResourceGroup"
        New-AzureRmResourceGroup -Name $myResourceGroup -Location $location

## Step 3: Create a storage account
A [storage account](/documentation/articles/storage-introduction/) is needed to store the virtual hard disk that is used by the virtual machine that you create. Storage account names must be between 3 and 24 characters in length and may contain numbers and lowercase letters only.

1. Test the storage account name for uniqueness. This command tests the name **myStorageAccount**.

        $myStorageAccountName = "mystorageaccount"
        Get-AzureRmStorageAccountNameAvailability $myStorageAccountName

    If this command returns **True**, your proposed name is unique within Azure. 
2. Now, create the storage account.

        $myStorageAccount = New-AzureRmStorageAccount -ResourceGroupName $myResourceGroup `
            -Name $myStorageAccountName -SkuName "Standard_LRS" -Kind "Storage" -Location $location

## Step 4: Create a virtual network
All virtual machines are part of a [virtual network](/documentation/articles/virtual-networks-overview/).

1. Create a subnet for the virtual network. This command creates a subnet named **mySubnet** with an address prefix of 10.0.0.0/24.

        $mySubnet = New-AzureRmVirtualNetworkSubnetConfig -Name "mySubnet" -AddressPrefix 10.0.0.0/24

2. Now, create the virtual network. This command creates a virtual network named **myVnet** using the subnet that you created and an address prefix of **10.0.0.0/16**.

        $myVnet = New-AzureRmVirtualNetwork -Name "myVnet" -ResourceGroupName $myResourceGroup `
            -Location $location -AddressPrefix 10.0.0.0/16 -Subnet $mySubnet

## Step 5: Create a public IP address and network interface
To enable communication with the virtual machine in the virtual network, you need a [public IP address](/documentation/articles/virtual-network-ip-addresses-overview-arm/) and a network interface.

1. Create the public IP address. This command creates a public IP address named **myPublicIp** with an allocation method of **Dynamic**.

        $myPublicIp = New-AzureRmPublicIpAddress -Name "myPublicIp" -ResourceGroupName $myResourceGroup `
            -Location $location -AllocationMethod Dynamic

2. Create the network interface. This command creates a network interface named **myNIC**.

        $myNIC = New-AzureRmNetworkInterface -Name "myNIC" -ResourceGroupName $myResourceGroup `
            -Location $location -SubnetId $myVnet.Subnets[0].Id -PublicIpAddressId $myPublicIp.Id

## Step 6: Create a virtual machine
Now that you have all the pieces in place, it's time to create the virtual machine.

1. Run this command to set the administrator account name and password for the virtual machine.

        $cred = Get-Credential -Message "Type the name and password of the local administrator account."

    The password must be at 12-123 characters long and have at least one lower case character, one upper case character, one number, and one special character. 
2. Create the configuration object for the virtual machine. This command creates a configuration object named **myVmConfig** that defines the name of the VM and the size of the VM.

        $myVm = New-AzureRmVMConfig -VMName "myVM" -VMSize "Standard_DS1_v2"

    See [Sizes for virtual machines in Azure](/documentation/articles/virtual-machines-windows-sizes/) for a list of available sizes for a virtual machine.
3. Configure operating system settings for the VM. This command sets the computer name, operating system type, and account credentials for the VM.

        $myVM = Set-AzureRmVMOperatingSystem -VM $myVM -Windows -ComputerName "myVM" -Credential $cred `
            -ProvisionVMAgent -EnableAutoUpdate

4. Define the image to use to provision the VM. This command defines the Windows Server image to use for the VM. 

        $myVM = Set-AzureRmVMSourceImage -VM $myVM -PublisherName "MicrosoftWindowsServer" `
            -Offer "WindowsServer" -Skus "2012-R2-Datacenter" -Version "latest"

    For more information about selecting images to use, see [Navigate and select Windows virtual machine images in Azure with PowerShell or the CLI](/documentation/articles/virtual-machines-windows-cli-ps-findimage/).
5. Add the network interface that you created to the configuration.

        $myVM = Add-AzureRmVMNetworkInterface -VM $myVM -Id $myNIC.Id

6. Define the name and location of the VM hard disk. The virtual hard disk file is stored in a container. This command creates the disk in a container named **vhds/WindowsVMosDisk.vhd** in the storage account that you created.

        $blobPath = "vhds/myOsDisk1.vhd"
        $osDiskUri = $myStorageAccount.PrimaryEndpoints.Blob.ToString() + $blobPath

7. Add the operating system disk information to the VM configuration. Replace The value of **$diskName** with a name for the operating system disk. Create the variable and add the disk information to the configuration.

        $vm = Set-AzureRmVMOSDisk -VM $myVM -Name "myOsDisk1" -VhdUri $osDiskUri -CreateOption fromImage

8. Finally, create the virtual machine.

        New-AzureRmVM -ResourceGroupName $myResourceGroup -Location $location -VM $myVM

## Next Steps
* If there were issues with the deployment, a next step would be to look at [Troubleshooting resource group deployments with Azure portal preview](/documentation/articles/resource-manager-troubleshoot-deployments-portal/)
* Learn how to manage the virtual machine that you created by reviewing [Manage virtual machines using Azure Resource Manager and PowerShell](/documentation/articles/virtual-machines-windows-ps-manage/).
* Take advantage of using a template to create a virtual machine by using the information in [Create a Windows virtual machine with a Resource Manager template](/documentation/articles/virtual-machines-windows-ps-template/)

