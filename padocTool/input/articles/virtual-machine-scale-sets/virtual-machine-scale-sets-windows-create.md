<properties
	pageTitle="Create a Virtual Machine Scale Set using PowerShell | Azure"
	description="Create a Virtual Machine Scale Set using PowerShell"
	services="virtual-machine-scale-sets"
    documentationCenter=""
	authors="davidmu1"
	manager="timlt"
	editor=""
	tags="azure-resource-manager"/>

<tags
	ms.service="virtual-machine-scale-sets"
	ms.workload="na"
	ms.tgt_pltfrm="na"
	ms.devlang="na"
	ms.topic="get-started-article"
	ms.date="10/10/2016"
	wacn.date=""
	ms.author="davidmu"/>

# Create a Windows virtual machine scale set using Azure PowerShell

These steps follow a fill-in-the-blanks approach for creating an Azure virtual machine scale set. See [Virtual Machine Scale Sets Overview](/documentation/articles/virtual-machine-scale-sets-overview/) to learn more about scale sets.

It should take about 30 minutes to do the steps in this article.

## Step 1: Install Azure PowerShell

See [How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure/) for information about installing the latest version of Azure PowerShell, selecting your subscription, and signing in to your account.

## Step 2: Create resources

Create the resources that are needed for your new scale set.

### Resource group

A virtual machine scale set must be contained in a resource group.

1. Get a list of available locations and the services that are supported:

        Get-AzureLocation | Sort Name | Select Name, AvailableServices

    You should see something like this example:

        Name                AvailableServices
        ----                -----------------
        Australia East      {Compute, Storage, PersistentVMRole, HighMemory}
        Australia Southeast {Compute, Storage, PersistentVMRole, HighMemory}
        Brazil South        {Compute, Storage, PersistentVMRole, HighMemory}
        Central India       {Compute, Storage, PersistentVMRole, HighMemory}
        China North          {Compute, Storage, PersistentVMRole, HighMemory}
        China East           {Compute, Storage, PersistentVMRole, HighMemory}
        China East             {Compute, Storage, PersistentVMRole, HighMemory}
        China East 2           {Compute, Storage, PersistentVMRole, HighMemory}
        China East          {Compute, Storage, PersistentVMRole, HighMemory}
        China East          {Compute, Storage, PersistentVMRole, HighMemory}
        China North    {Compute, Storage, PersistentVMRole, HighMemory}
        China North        {Compute, Storage, PersistentVMRole, HighMemory}
        China East    {Compute, Storage, PersistentVMRole, HighMemory}
        South India         {Compute, Storage, PersistentVMRole, HighMemory}
        China North      {Compute, Storage, PersistentVMRole, HighMemory}
        West Europe         {Compute, Storage, PersistentVMRole, HighMemory}
        West India          {Compute, Storage, PersistentVMRole, HighMemory}
        China North             {Compute, Storage, PersistentVMRole, HighMemory}

2. Pick a location that works best for you, replace the value of **$locName** with that location name, and then create the variable:

        $locName = "location name from the list, such as China North"

3. Replace the value of **$rgName** with the name that you want to use for the new resource group and then create the variable: 

        $rgName = "resource group name"
        
4. Create the resource group:
    
        New-AzureRmResourceGroup -Name $rgName -Location $locName

    You should see something like this example:

        ResourceGroupName : myrg1
        Location          : chinaeast
        ProvisioningState : Succeeded
        Tags              :
        ResourceId        : /subscriptions/########-####-####-####-############/resourceGroups/myrg1

### Storage account

A storage account is used by a virtual machine to store the operating system disk and diagnostic data used for scaling. When possible, it is best practice to have a storage account for each virtual machine created in a scale set. If not possible, plan for no more than 20 VMs per storage account. The example in this article shows three storage accounts being created for three virtual machines.

1. Replace the value of **$saName** with a name for the storage account. Test the name for uniqueness. 

        $saName = "storage account name"
        Get-AzureRmStorageAccountNameAvailability $saName

    If the answer is **True**, your proposed name is unique.

3. Replace the value of **$saType** with the type of the storage account and then create the variable:  

        $saType = "storage account type"
        
    Possible values are: Standard_LRS, Standard_GRS, Standard_RAGRS, or Premium_LRS.
        
4. Create the account:
    
        New-AzureRmStorageAccount -Name $saName -ResourceGroupName $rgName -Type $saType -Location $locName

    You should see something like this example:

        ResourceGroupName   : myrg1
        StorageAccountName  : myst1
        Id                  : /subscriptions/########-####-####-####-############/resourceGroups/myrg1/providers/Microsoft
	                          .Storage/storageAccounts/myst1
        Location            : chinaeast
        AccountType         : StandardLRS
        CreationTime        : 3/15/2016 4:51:52 PM
        CustomDomain        :
        LastGeoFailoverTime :
        PrimaryEndpoints    : Microsoft.Azure.Management.Storage.Models.Endpoints
        PrimaryLocation     : chinaeast
        ProvisioningState   : Succeeded
        SecondaryEndpoints  :
        SecondaryLocation   :
        StatusOfPrimary     : Available
        StatusOfSecondary   :
        Tags                : {}
        Context             : Microsoft.WindowsAzure.Commands.Common.Storage.AzureStorageContext

5. Repeat steps 1 through 4 to create three storage accounts, for example myst1, myst2, and myst3.

### Virtual network

A virtual network is required for the virtual machines in the scale set.

1. Replace the value of **$subnetName** with the name that you want to use for the subnet in the virtual network and then create the variable: 

        $subnetName = "subnet name"
        
2. Create the subnet configuration:
    
        $subnet = New-AzureRmVirtualNetworkSubnetConfig -Name $subnetName -AddressPrefix 10.0.0.0/24
        
    The address prefix may be different in your virtual network.

3. Replace the value of **$netName** with the name that you want to use for the virtual network and then create the variable: 

        $netName = "virtual network name"
        
4. Create the virtual network:
    
        $vnet = New-AzureRmVirtualNetwork -Name $netName -ResourceGroupName $rgName -Location $locName -AddressPrefix 10.0.0.0/16 -Subnet $subnet

### Public IP address

Before a network interface can be created, you need to create a public IP address.

1. Replace the value of **$domName** with the domain name label that you want to use with your public IP address and then create the variable:  

        $domName = "domain name label"
        
    The label can contain only letters, numbers, and hyphens, and the last character must be a letter or number.
    
2. Test whether the name is unique:
    
        Test-AzureRmDnsAvailability -DomainQualifiedName $domName -Location $locName

    If the answer is **True**, your proposed name is unique.

3. Replace the value of **$pipName** with the name that you want to use for the public IP address and then create the variable. 

        $pipName = "public ip address name"
        
4. Create the public IP address:
    
        $pip = New-AzureRmPublicIpAddress -Name $pipName -ResourceGroupName $rgName -Location $locName -AllocationMethod Dynamic -DomainNameLabel $domName

### Network interface

Now that you have the public IP address, you can create the network interface.

1. Replace the value of **$nicName** with the name that you want to use for the network interface and then create the variable: 

        $nicName = "network interface name"
        
2. Create the network interface:
    
        $nic = New-AzureRmNetworkInterface -Name $nicName -ResourceGroupName $rgName -Location $locName -SubnetId $vnet.Subnets[0].Id -PublicIpAddressId $pip.Id

### Configuration of the scale set

You have all the resources that you need for the scale set configuration, so let's create it.  

1. Replace the value of **$ipName** with the name that you want to use for the IP configuration and then create the variable: 

        $ipName = "IP configuration name"
        
2. Create the IP configuration:

        $ipConfig = New-AzureRmVmssIpConfig -Name $ipName -LoadBalancerBackendAddressPoolsId $null -SubnetId $vnet.Subnets[0].Id

2. Replace the value of **$vmssConfig** with the name that you want to use for the scale set configuration and then create the variable:   

        $vmssConfig = "Scale set configuration name"
        
3. Create the configuration for the scale set:

        $vmss = New-AzureRmVmssConfig -Location $locName -SkuCapacity 3 -SkuName "Standard_A0" -UpgradePolicyMode "manual"
        
    This example shows a scale set being created with three virtual machines. See [Virtual Machine Scale Sets Overview](/documentation/articles/virtual-machine-scale-sets-overview/) for more about the capacity of scale sets. This step also includes setting the size (referred to as SkuName) of the virtual machines in the set. To find a size that meets your needs, look at [Sizes for virtual machines](/documentation/articles/virtual-machines-windows-sizes/).
    
4. Add the network interface configuration to the scale set configuration:
        
        Add-AzureRmVmssNetworkInterfaceConfiguration -VirtualMachineScaleSet $vmss -Name $vmssConfig -Primary $true -IPConfiguration $ipConfig
        
    You should see something like this example:

        Sku                   : Microsoft.Azure.Management.Compute.Models.Sku
        UpgradePolicy         : Microsoft.Azure.Management.Compute.Models.UpgradePolicy
        VirtualMachineProfile : Microsoft.Azure.Management.Compute.Models.VirtualMachineScaleSetVMProfile
        ProvisioningState     :
        OverProvision         :
        Id                    :
        Name                  :
        Type                  :
        Location              : China North
        Tags                  :

#### Operating system profile

1. Replace the value of **$computerName** with the computer name prefix that you want to use and then create the variable: 

        $computerName = "computer name prefix"
        
2. Replace the value of **$adminName** the name of the administrator account on the virtual machines and then create the variable:

        $adminName = "administrator account name"
        
3. Replace the value of **$adminPassword** with the account password and then create the variable:

        $adminPassword = "password for administrator accounts"
        
4. Create the operating system profile:

        Set-AzureRmVmssOsProfile -VirtualMachineScaleSet $vmss -ComputerNamePrefix $computerName -AdminUsername $adminName -AdminPassword $adminPassword

#### Storage profile

1. Replace the value of **$storageProfile** with the name that you want to use for the storage profile and then create the variable:  

        $storageProfile = "storage profile name"
        
2. Create the variables that define the image to use:  
      
        $imagePublisher = "MicrosoftWindowsServer"
        $imageOffer = "WindowsServer"
        $imageSku = "2012-R2-Datacenter"
        
    To find the information about other images to use, look at [Navigate and select Azure virtual machine images with Windows PowerShell and the Azure CLI](/documentation/articles/virtual-machines-windows-cli-ps-findimage/).
        
3. Replace the value of **$vhdContainers** with a list that contains the paths where the virtual hard disks are stored, such as "https://mystorage.blob.core.chinacloudapi.cn/vhds", and then create the variable:
       
        $vhdContainers = @("https://myst1.blob.core.chinacloudapi.cn/vhds","https://myst2.blob.core.chinacloudapi.cn/vhds","https://myst3.blob.core.chinacloudapi.cn/vhds")
        
4. Create the storage profile:

        Set-AzureRmVmssStorageProfile -VirtualMachineScaleSet $vmss -ImageReferencePublisher $imagePublisher -ImageReferenceOffer $imageOffer -ImageReferenceSku $imageSku -ImageReferenceVersion "latest" -Name $storageProfile -VhdContainer $vhdContainers -OsDiskCreateOption "FromImage" -OsDiskCaching "None"  

### Virtual machine scale set

Finally, you can create the scale set.

1. Replace the value of **$vmssName** with the name of the virtual machine scale set and then create the variable:

        $vmssName = "scale set name"
        
2. Create the scale set:

        New-AzureRmVmss -ResourceGroupName $rgName -Name $vmssName -VirtualMachineScaleSet $vmss

    You should see something like this example that shows a successful deployment:

        Sku                   : Microsoft.Azure.Management.Compute.Models.Sku
        UpgradePolicy         : Microsoft.Azure.Management.Compute.Models.UpgradePolicy
        VirtualMachineProfile : Microsoft.Azure.Management.Compute.Models.VirtualMachineScaleSetVMProfile
        ProvisioningState     : Updating
        OverProvision         :
        Id                    : /subscriptions/########-####-####-####-############/resourceGroups/myrg1/providers/Microso
                                ft.Compute/virtualMachineScaleSets/myvmss1
        Name                  : myvmss1
        Type                  : Microsoft.Compute/virtualMachineScaleSets
        Location              : chinaeast
        Tags                  :

## Step 3: Explore resources

Use these resources to explore the virtual machine scale set that you created:

- Azure portal Preview - A limited amount of information is available using the portal.
- Azure PowerShell - Use this command to get information:

        Get-AzureRmVmss -ResourceGroupName "resource group name" -VMScaleSetName "scale set name"
        
        Or 
        
        Get-AzureRmVmssVM -ResourceGroupName "resource group name" -VMScaleSetName "scale set name"
        

## Next steps

- Manage the scale set that you just created using the information in [Manage virtual machines in a Virtual Machine Scale Set](/documentation/articles/virtual-machine-scale-sets-windows-manage/)
- Consider setting up automatic scaling of your scale set by using information in [Automatic scaling and virtual machine scale sets](/documentation/articles/virtual-machine-scale-sets-autoscale-overview/)
- Learn more about vertical scaling by reviewing [Vertical autoscale with Virtual Machine Scale sets](/documentation/articles/virtual-machine-scale-sets-vertical-scale-reprovision/)
