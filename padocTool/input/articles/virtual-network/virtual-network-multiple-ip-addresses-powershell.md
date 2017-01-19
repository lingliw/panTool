<properties
   pageTitle="Multiple IP addresses for virtual machines - PowerShell | Azure"
   description="Learn how to assign multiple IP addresses to a virtual machine using Azure PowerShell."
   services="virtual-network"
   documentationCenter="na"
   authors="jimdial"
   manager="carmonm"
   editor=""
   tags="azure-resource-manager"
/>
<tags
   ms.service="virtual-network"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="infrastructure-services"
   ms.date="10/05/2016"
   wacn.date=""
   ms.author="jdial;annahar" />


# Assign multiple IP addresses to virtual machines

An Azure Virtual Machine (VM) can have one or more network interfaces (NIC) attached to it. Each NIC can have one or more public or private IP addresses assigned to it. If you're not familiar with IP addresses in Azure, read the [IP addresses in Azure](/documentation/articles/virtual-network-ip-addresses-overview-arm/) article to learn more about them. This article explains how to use Azure PowerShell to assign multiple IP addresses to a NIC in the Azure Resource Manager deployment model.

Assigning multiple IP addresses to a NIC enables the VM to:

- Host multiple websites or services with different IP addresses and SSL certificates on a single server.
- Serve as a network virtual appliance, such as a firewall or load balancer.

>[AZURE.WARNING] This feature is currently in preview release and may not have the same level of availability and reliability as features that are in general availability release. The feature is not supported, may have constrained capabilities, and may not be available in all Azure locations.

To register for the preview, send an email to [Multiple IPs](mailto:MultipleIPsPreview@microsoft.com?subject=Request%20to%20enable%20subscription%20%3csubscription%20id%3e) with your subscription ID and intended use.
## Scenario

In this article, you will associate three IP configurations to a network interface.
The following example configurations will be created and assigned to a NIC that will have three private IP addresses and one public IP address assigned to it:

- IPConfig-1: A dynamic private IP address (default) and a public IP address from the public IP address resource named PIP1.
- IPConfig-2: A static private IP address and no public IP address.
- IPConfig-3: A dynamic private IP address and no public IP address.

    ![Alt image text](./media/virtual-network-multiple-ip-addresses-powershell/OneNIC-3IP.png)

This scenario assumes you have a resource group called *RG1* within which there is a VNet called *VNet1* and a subnet called *Subnet1*. Further, it assumes you have a VM called *VM1*, a network interface called *VM1-NIC1* associated to it and a public IP address called *PIP1*.

[This article](/documentation/articles/virtual-machines-windows-ps-create/) walks through how to create the resources mentioned above in case you have not created them before.

## <a name = "create"></a>Create a VM with multiple IP addresses

1. Open a PowerShell command prompt and complete the remaining steps in this section within a single PowerShell session. If you don't already have PowerShell installed and configured, complete the steps in the [How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure/) article.

2. Change the "values" of the following $Variables to the Azure [location](https://azure.microsoft.com/regions) your virtual network is in, the name of your [resource group](/documentation/articles/resource-group-overview/#resource-groups), the VNet within the resource group, the subnet you want to connect the NIC to and the name of the NIC.

        $Location = "chinaeast"
        $RgName   = "RG1"
        $VNetName   = "VNet1"
        $SubnetName = "Subnet1"
        $NicName     = "VM1-NIC1"
        $PIP = "PIP"

	If you don't know the name of an existing Azure location or resource group, type the following commands:

		Get-AzureRmLocation 	 | Format-Table Location
		Get-AzureRmResourceGroup | Format-Table ResourceGroupName

    <a name="subnet"></a>The NIC must be connected to a subnet within an existing Azure Virtual Network (VNet). The three components: NIC, subnet, and VNet, must all exist in the same region and [subscription](/documentation/articles/azure-glossary-cloud-terminology/#subscription).  If you're not familiar with VNets, read the [Virtual network overview](/documentation/articles/virtual-networks-overview/) article to learn more about them or read the [Create a VNet](/documentation/articles/virtual-networks-create-vnet-arm-ps/) article to learn how to create one.

	If you don't know the name of an existing VNet, enter the following command and replace *VNet1* in the previous variable with the name of a VNet:

		Get-AzureRmVirtualNetwork | Format-Table Name

	If the list returned is empty, you need to create a VNet. To learn how, read the [Create a virtual network](/documentation/articles/virtual-networks-create-vnet-arm-ps/) article.

	Type the following commands to get the name of the existing subnets within the VNet and replace *Subnet1* above with the name of a subnet:

		$VNet = Get-AzureRmVirtualNetwork -Name $VNetName -ResourceGroupName $RgName
		$VNet.Subnets | Format-Table Name, AddressPrefix

4. Enter the following command to retrieve the subnet and assign it to a variable.

		$Subnet = $VNet.Subnets | Where-Object { $_.Name -eq $SubnetName }

5. <a name="ipconfigs"></a>Define the IP configurations you want to assign to the NIC. Each configuration can have one static or dynamic private IP address and one associated public IP address resource with a static or dynamic address.

	Add or remove any number of the configurations that follow depending on how many IP addresses you want to associate to the NIC and the settings you want to configure.

	**IPConfig-1**

	Change the value *PIP1* to the name of an existing public IP address resource that exists in the location you're creating the NIC in and that isn't currently associated with another NIC. Change *RG1* to the name of the resource group the public IP address resource exists in. Change *IPConfig-1* to the name you want to give to the first IP configuration. Enter the following commands:

		$PIP1 = Get-AzureRmPublicIPAddress -Name "PIP1" -ResourceGroupName $RgName

		$IpConfigName1 = "IPConfig-1"
		$IPConfig1     = New-AzureRmNetworkInterfaceIpConfig -Name $IPConfigName1 -Subnet $Subnet -PublicIpAddress $PIP1 -Primary

	Note the *-Primary* switch. When you assign multiple IP configurations to a NIC, one configuration must be assigned as the *Primary*. If you don't know the name of an existing public IP address resource, enter the following command:

		Get-AzureRMPublicIPAddress |Format-Table Name, Location, IPAddress, IpConfiguration

	If the **IPConfiguration** column has no value in the output returned, the public IP address resource is not associated with an existing NIC and can be used. If the list is blank, or there are no available public IP address resources, you can create one using the **New-AzureRmPublicIPAddress** command.

	>[AZURE.NOTE] Public IP addresses have a nominal fee. To learn more about IP address pricing, read the [IP address pricing](/pricing/details/reserved-ip-addresses/) page.

	**IPConfig-2**

	Change *IPConfig-2* to the name you want to give to the second IP configuration and change *10.0.0.5* to an unused valid IP address for the subnet you're assigning the NIC to. Enter the following commands:

		$IPConfigName2 = "IPConfig-2"
		$IPAddress = 10.0.0.5

		$IPConfig2 = New-AzureRmNetworkInterfaceIpConfig -Name $IPConfigName2 -Subnet $Subnet -PrivateIpAddress $IPAddress

	Enter the following command, if you don't know the IP address range assigned to the subnet:

		$VNet.Subnets | Format-Table Name, AddressPrefix

	**IPConfig-3**

	Change *IPConfig-3* to the name you want to give to the third IP configuration and enter the following commands:

		$IPConfigName3 = "IPConfig-3"
		$IPConfig3 = New-AzureRmNetworkInterfaceIpConfig -Name $IPConfigName3 -Subnet $Subnet

	>[AZURE.NOTE] You can assign up to 250 private IP address to a NIC. There is a limit to the number of public IP addresses that can be used within a subscription. To learn more, read the [Azure limits](/documentation/articles/azure-subscription-service-limits/#networking-limits---azure-resource-manager) article.

6. Create the NIC using the IP configurations defined in the previous step.

		$nic = New-AzureRmNetworkInterface -Name $NicName -ResourceGroupName $RgName -Location $Location -IpConfiguration $IpConfig1,$IpConfig2,$IpConfig3

7. Attach the NIC when creating a VM by following the steps in the [Create a VM](/documentation/articles/virtual-machines-windows-ps-create/) article. Though the article creates a VM running Windows Server, the steps are the same for a Linux VM, other than selecting a different operating system. Complete steps 1-3 of the article. Skip steps 4 and 5 and then complete step 6 in the Create a VM article.

	>[AZURE.WARNING] Step 6 in the Create a VM article will fail if you changed the variable named $nic to something else in step 6 of this article, or haven't completed the previous steps of this article.

8. View the private IP addresses that Azure DHCP assigned to the NIC and the public IP address resource assigned to the NIC by entering the following command:

		$nic.IpConfigurations | Format-Table Name, PrivateIPAddress, PublicIPAddress, Primary

9. <a name="os"></a>Manually add all the secondary private IP addresses (IP addresses with *False* in the **Primary** column from the output in the previous step) to the TCP/IP configuration in the operating system. The private IP address assigned to *IPConfig-1* in step 5 is automatically assigned to the operating system via Azure DHCP, because it's the *Primary* configuration.


**Windows**

1. From a command prompt, type *ipconfig /all*.  You only see the *Primary* private IP address (through DHCP).
2. Next type *ncpa.cpl* in the command prompt window. This will open a new window.
3. Open the properties for **Local Area Connection**.
4. Double click on Internet Protocol version 4 (IPv4)
5. Select **Use the following IP address** and enter the following values:
	- **IP address**: Enter the *Primary* private IP address
	- **Subnet mask**: Set based on your subnet. For example, if the subnet is a /24 subnet then the subnet mask is 255.255.255.0.
	- **Default gateway**: The first IP address in the subnet. If your subnet is 10.0.0.0/24, then the gateway IP address is 10.0.0.1.
	- Click **Use the following DNS server addresses** and enter the following values:
		- **Preferred DNS server:** Enter 168.63.129.16 if you are not using your own DNS server.  If you are, enter the IP address for your DNS server.
	- Click the **Advanced** button and add additional IP addresses. Add each of the secondary private IP addresses listed in step 8 to the NIC with the same subnet specified for the primary IP address.
	- Click **OK** to close out the TCP/IP settings and then **OK** again to close the adapter settings. This will then reestablish your RDP connection.

6. From a command prompt, type *ipconfig /all*. All IP addresses you added are shown and DHCP is turned off.


**Linux (Ubuntu)**

1. Open a terminal window.
2. Make sure you are the root user. If you are not, you can do this by using the following command:

			sudo -i
3. Update the configuration file of the network interface (assuming 'eth0').
	- Keep the existing line item for dhcp. This will configure the primary IP address as it used to be earlier.
	- Add a configuration for an additional static IP address with the following commands:

				cd /etc/network/interfaces.d/
				ls

		You should see a .cfg file.
4. Open the file: vi *filename*.

	You should see the following lines at the end of the file:

			auto eth0
			iface eth0 inet dhcp
5. Add the following lines after the lines that exist in this file:

			iface eth0 inet static
			address <your private IP address here>
6. Save the file by using the following command:

			:wq
7.  Reset the network interface with the following command:

			sudo ifdown eth0 && sudo ifup eth0

	>[AZURE.IMPORTANT] Run both ifdown and ifup in the same line if using a remote connection.
8. Verify the IP address is added to the network interface with the following command:

			ip addr list eth0

	You should see the IP address you added as part of the list.

**Linux (Redhat, CentOS, and others)**

1. Open a terminal window.
2. Make sure you are the root user. If you are not, you can do this by using the following command:

			sudo -i
3. Enter your password and follow instructions as prompted. Once you are the root user, navigate to the network scripts folder with the following command:

			cd /etc/sysconfig/network-scripts
4. List the related ifcfg files using the following command:

			ls ifcfg-*

	You should see *ifcfg-eth0* as one of the files.
5. Copy the *ifcfg-eth0* file and name it *ifcfg-eth0:0* with the following command:

			cp ifcfg-eth0 ifcfg-eth0:0
6. Edit the *ifcfg-eth0:0* file with the following command:

			vi ifcfg-eth1
7. Change the device to the appropriate name in the file; *eth0:0* in this case, with the following command:

			DEVICE=eth0:0
8. Change the *IPADDR = YourPrivateIPAddress* line to reflect the IP address.
9. Save the file with the following command:

			:wq
10. Restart the network services and make sure the changes are successful by running the following commands:

			/etc/init.d/network restart
			Ipconfig

	You should see the IP address you added, *eth0:0*, in the list returned.

## <a name="add"></a>Add IP addresses to an existing VM

Complete the following steps to add additional IP addresses to an existing NIC:

1. Open a PowerShell command prompt and complete the remaining steps in this section within a single PowerShell session. If you don't already have PowerShell installed and configured, complete the steps in the [How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure/) article.

2. Change the "values" of the following $Variables to the name of the NIC you want to add IP addresses to and the resource group and location the NIC exists in:

		$NicName     = "RG1-VM1-NIC1"
		$RgName   = "RG1"
		$NicLocation = "chinaeast"

	If you don't know the name of the NIC you want to change, enter the following commands, then change the values of the previous variables:

		Get-AzureRmNetworkInterface | Format-Table Name, ResourceGroupName, Location

3. Create a variable and set it to the existing NIC by typing the following command:

		$nic = Get-AzureRmNetworkInterface -Name $NicName -ResourceGroupName $RgName

4. Retrieve the subnet ID the NIC is connected to by completing [step 3](#subnet) of the Create a VM with multiple IP addresses section of this article.

5. Create the IP configurations you want to add to the network by following the instructions in [step 5](#ipconfigs) of the Create a VM with multiple IP addresses section of this article.

6. Change *$IPConfigName4* to the name of the IP configuration you created in the previous step. To add the configuration, enter the following command:

		Add-AzureRmNetworkInterfaceIpConfig -Name $IPConfigName4 -NetworkInterface $nic -Subnet $Subnet1

7. To set the NIC with the IP configuration, enter the following command:

		Set-AzureRmNetworkInterface -NetworkInterface $nic

8. Add the IP addresses you added to the NIC to the VM operating system by following the instructions in [step 9](#os) of the Create a VM with multiple IP addresses section of this article.
