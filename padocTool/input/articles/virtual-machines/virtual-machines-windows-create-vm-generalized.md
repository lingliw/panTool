<properties
    pageTitle="Create VM from a generalized VHD | Azure"
    description="Learn how to create a Windows virtual machine from a generalized VHD image using Azure PowerShell, in the Resource Manager deployment model."
    services="virtual-machines-windows"
    documentationcenter=""
    author="cynthn"
    manager="timlt"
    editor=""
    tags="azure-resource-manager" />
<tags
    ms.assetid="b4808871-9ef1-49ea-a617-9154d417abb0"
    ms.service="virtual-machines-windows"
    ms.workload="infrastructure-services"
    ms.tgt_pltfrm="vm-windows"
    ms.devlang="na"
    ms.topic="article"
    ms.date="10/10/2016"
    wacn.date=""
    ms.author="cynthn" />

# Create a VM from a generalized VHD image
A generalized VHD image has had all of your personal account information removed using [Sysprep](/documentation/articles/virtual-machines-windows-generalize-vhd/). You can create a generalized VHD by running Sysprep on an on-premises VM, then [uploading the VHD to Azure](/documentation/articles/virtual-machines-windows-upload-image/), or by running Sysprep on an existing Azure VM and then [copying the VHD](/documentation/articles/virtual-machines-windows-vhd-copy/).

If you want to create a VM from a specialized VHD, see [Create a VM from a specialized VHD](/documentation/articles/virtual-machines-windows-create-vm-specialized/).

The quickest way to create a VM from a generalized VHD is to use a [quick start template](https://github.com/Azure/azure-quickstart-templates/tree/master/101-vm-from-user-image). 

## Prerequisites
If you are going to use a VHD uploaded from an on-premises VM, like one created using Hyper-V, you should make sure you followed the directions in [Prepare a Windows VHD to upload to Azure](/documentation/articles/virtual-machines-windows-prepare-for-upload-vhd-image/). 

Both uploaded VHDs and existing Azure VM VHDs need to be generalized before you can create a VM using this method. For more information, see [Generalize a Windows virtual machine using Sysprep](/documentation/articles/virtual-machines-windows-generalize-vhd/). 

## Set the URI of the VHD
The URI for the VHD to use is in the format: https://**mystorageaccount**.blob.core.chinacloudapi.cn/**mycontainer**/**MyVhdName**.vhd. In this example the VHD named **myVHD** is in the storage account **mystorageaccount** in the container **mycontainer**.

    $imageURI = "https://mystorageaccount.blob.core.chinacloudapi.cn/mycontainer/myVhd.vhd"

## Create a virtual network
Create the vNet and subnet of the [virtual network](/documentation/articles/virtual-networks-overview/).

1. Create the subnet. The following sample creates a subnet named **mySubnet** in the resource group **myResourceGroup** with the address prefix of **10.0.0.0/24**.  

        $rgName = "myResourceGroup"
        $subnetName = "mySubnet"
        $singleSubnet = New-AzureRmVirtualNetworkSubnetConfig -Name $subnetName -AddressPrefix 10.0.0.0/24

2. Create the virtual network. The following sample creates a virtual network named **myVnet** in the **China North** location with the address prefix of **10.0.0.0/16**.  

        $location = "China North"
        $vnetName = "myVnet"
        $vnet = New-AzureRmVirtualNetwork -Name $vnetName -ResourceGroupName $rgName -Location $location `
            -AddressPrefix 10.0.0.0/16 -Subnet $singleSubnet

## Create a public IP address and network interface
To enable communication with the virtual machine in the virtual network, you need a [public IP address](/documentation/articles/virtual-network-ip-addresses-overview-arm/) and a network interface.

1. Create a public IP address. This example creates a public IP address named **myPip**. 

        $ipName = "myPip"
        $pip = New-AzureRmPublicIpAddress -Name $ipName -ResourceGroupName $rgName -Location $location `
            -AllocationMethod Dynamic

2. Create the NIC. This example creates a NIC named **myNic**. 

        $nicName = "myNic"
        $nic = New-AzureRmNetworkInterface -Name $nicName -ResourceGroupName $rgName -Location $location `
            -SubnetId $vnet.Subnets[0].Id -PublicIpAddressId $pip.Id

## Create the network security group and an RDP rule
To be able to log in to your VM using RDP, you need to have a security rule that allows RDP access on port 3389. 

This example creates an NSG named **myNsg** that contains a rule called **myRdpRule** that allows RDP traffic over port 3389. For more information about NSGs, see [Opening ports to a VM in Azure using PowerShell](/documentation/articles/virtual-machines-windows-nsg-quickstart-powershell/).

    $nsgName = "myNsg"

    $rdpRule = New-AzureRmNetworkSecurityRuleConfig -Name myRdpRule -Description "Allow RDP" `
        -Access Allow -Protocol Tcp -Direction Inbound -Priority 110 `
        -SourceAddressPrefix Internet -SourcePortRange * `
        -DestinationAddressPrefix * -DestinationPortRange 3389

    $nsg = New-AzureRmNetworkSecurityGroup -ResourceGroupName $rgName -Location $location `
        -Name $nsgName -SecurityRules $rdpRule

## Create a variable for the virtual network
Create a variable for the completed virtual network. 

    $vnet = Get-AzureRmVirtualNetwork -ResourceGroupName $rgName -Name $vnetName

## Create the VM
The following PowerShell script shows how to set up the virtual machine configurations and use the uploaded VM image as the source for the new installation.

</br>

        # Enter a new user name and password to use as the local administrator account 
        # for remotely accessing the VM.
        $cred = Get-Credential

        # Name of the storage account where the VHD is located. This example sets the 
        # storage account name as "myStorageAccount"
        $storageAccName = "myStorageAccount"

        # Name of the virtual machine. This example sets the VM name as "myVM".
        $vmName = "myVM"

        # Size of the virtual machine. This example creates "Standard_D2_v2" sized VM. 
        # See the VM sizes documentation for more information: 
        # /documentation/articles/virtual-machines-windows-sizes/
        $vmSize = "Standard_D2_v2"

        # Computer name for the VM. This examples sets the computer name as "myComputer".
        $computerName = "myComputer"

        # Name of the disk that holds the OS. This example sets the 
        # OS disk name as "myOsDisk"
        $osDiskName = "myOsDisk"

        # Assign a SKU name. This example sets the SKU name as "Standard_LRS"
        # Valid values for -SkuName are: Standard_LRS - locally redundant storage, Standard_ZRS - zone redundant
        # storage, Standard_GRS - geo redundant storage, Standard_RAGRS - read access geo redundant storage,
        # Premium_LRS - premium locally redundant storage. 
        $skuName = "Standard_LRS"

        # Get the storage account where the uploaded image is stored
        $storageAcc = Get-AzureRmStorageAccount -ResourceGroupName $rgName -AccountName $storageAccName

        # Set the VM name and size
        $vmConfig = New-AzureRmVMConfig -VMName $vmName -VMSize $vmSize

        #Set the Windows operating system configuration and add the NIC
        $vm = Set-AzureRmVMOperatingSystem -VM $vmConfig -Windows -ComputerName $computerName `
            -Credential $cred -ProvisionVMAgent -EnableAutoUpdate
        $vm = Add-AzureRmVMNetworkInterface -VM $vm -Id $nic.Id

        # Create the OS disk URI
        $osDiskUri = '{0}vhds/{1}-{2}.vhd' `
            -f $storageAcc.PrimaryEndpoints.Blob.ToString(), $vmName.ToLower(), $osDiskName

        # Configure the OS disk to be created from the existing VHD image (-CreateOption fromImage).
        $vm = Set-AzureRmVMOSDisk -VM $vm -Name $osDiskName -VhdUri $osDiskUri `
            -CreateOption fromImage -SourceImageUri $imageURI -Windows

        # Create the new VM
        New-AzureRmVM -ResourceGroupName $rgName -Location $location -VM $vm

## Verify that the VM was created
When complete, you should see the newly created VM in the [Azure portal preview](https://portal.azure.cn) under **Browse** > **Virtual machines**, or by using the following PowerShell commands:

        $vmList = Get-AzureRmVM -ResourceGroupName $rgName
        $vmList.Name

## Next steps
To manage your new virtual machine with Azure PowerShell, see [Manage virtual machines using Azure Resource Manager and PowerShell](/documentation/articles/virtual-machines-windows-ps-manage/).

