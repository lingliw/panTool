<!-- need to be verified -->

<properties
    pageTitle="Open ports to a VM using PowerShell | Azure"
    description="Learn how to open a port / create an endpoint to your Windows VM using the Azure resource manager deployment mode and Azure PowerShell"
    services="virtual-machines-windows"
    documentationcenter=""
    author="iainfoulds"
    manager="timlt"
    editor="" />
<tags
    ms.assetid="cf45f7d8-451a-48ab-8419-730366d54f1e"
    ms.service="virtual-machines-windows"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="vm-windows"
    ms.workload="infrastructure-services"
    ms.date="10/27/2016"
    wacn.date=""
    ms.author="iainfou" />

# Opening ports and endpoints to a VM in Azure using PowerShell
[AZURE.INCLUDE [virtual-machines-common-nsg-quickstart](../../includes/virtual-machines-common-nsg-quickstart.md)]

## Quick commands
To create a Network Security Group and ACL rules you need [the latest version of Azure PowerShell installed](/documentation/articles/powershell-install-configure/). You can also [perform these steps using the Azure portal preview](/documentation/articles/virtual-machines-windows-nsg-quickstart-portal/).

Log in to your Azure account:

    Login-AzureRmAccount -EnvironmentName AzureChinaCloud

In the following examples, replace example parameter names with your own values. Example parameter names included `myResourceGroup`, `myNetworkSecurityGroup`, and `myVnet`.

Create a rule. The following example creates a rule named `myNetworkSecurityGroupRule` to allow TCP traffic on port 80:

    $httprule = New-AzureRmNetworkSecurityRuleConfig -Name "myNetworkSecurityGroupRule" `
        -Description "Allow HTTP" -Access "Allow" -Protocol "Tcp" -Direction "Inbound" `
        -Priority "100" -SourceAddressPrefix "Internet" -SourcePortRange * `
        -DestinationAddressPrefix * -DestinationPortRange 80

Next, create your Network Security group and assign the HTTP rule you just created as follows. The following example creates a Network Security Group named `myNetworkSecurityGroup`:

    $nsg = New-AzureRmNetworkSecurityGroup -ResourceGroupName "myResourceGroup" `
        -Location "ChinaNorth" -Name "myNetworkSecurityGroup" -SecurityRules $httprule

Now let's assign your Network Security Group to a subnet. The following example assigns an existing virtual network named `myVnet` to the variable `$vnet`:

    $vnet = Get-AzureRmVirtualNetwork -ResourceGroupName "myResourceGroup" `
        -Name "myVnet"

Associate your Network Security Group with your subnet. The following example associates the subnet named `mySubnet` with your Network Security Group:

    $subnetPrefix = $vnet.Subnets|?{$_.Name -eq 'mySubnet'}

    Set-AzureRmVirtualNetworkSubnetConfig -VirtualNetwork $vnet -Name "mySubnet" `
        -AddressPrefix $subnetPrefix.AddressPrefix `
        -NetworkSecurityGroup $nsg

Finally, update your virtual network in order for your changes to take effect:

    Set-AzureRmVirtualNetwork -VirtualNetwork $vnet

## More information on Network Security Groups
The quick commands here allow you to get up and running with traffic flowing to your VM. Network Security Groups provide many great features and granularity for controlling access to your resources. You can read more about [creating a Network Security Group and ACL rules here](/documentation/articles/virtual-networks-create-nsg-arm-ps/).

You can define Network Security Groups and ACL rules as part of Azure Resource Manager templates. Read more about [creating Network Security Groups with templates](/documentation/articles/virtual-networks-create-nsg-arm-template/).

If you need to use port-forwarding to map a unique external port to an internal port on your VM, use a load balancer and Network Address Translation (NAT) rules. For example, you may want to expose TCP port 8080 externally and have traffic directed to TCP port 80 on a VM. You can learn about [creating an Internet-facing load balancer](/documentation/articles/load-balancer-get-started-internet-arm-ps/).

## Next steps
In this example, you created a simple rule to allow HTTP traffic. You can find information on creating more detailed environments in the following articles:

* [Azure Resource Manager overview](/documentation/articles/resource-group-overview/)
* [What is a Network Security Group (NSG)?](/documentation/articles/virtual-networks-nsg/)
* [Azure Resource Manager Overview for Load Balancers](/documentation/articles/load-balancer-arm/)

