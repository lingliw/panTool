<!-- not suitable for Mooncake -->

<properties 
	pageTitle="Network Configuration Details for Working with Express Route" 
	description="Network configuration details for running Azure Websites Environments in a Virtual Networks connected to an ExpressRoute Circuit." 
	services="app-service" 
	documentationCenter="" 
	authors="stefsch" 
	manager="nirma" 
	editor=""/>

<tags
	ms.service="app-service"
	ms.date="09/11/2015"
	wacn.date=""/>	

# Network Configuration Details for Azure Websites Environments with ExpressRoute 

## Overview ##
Customers can connect an [Azure ExpressRoute][ExpressRoute] circuit to their virtual network infrastructure, thus extending their on-premises network to Azure.  An Azure Websites Environment can  be created in a subnet of this [virtual network][virtualnetwork] infrastructure.  Apps running on the Azure Websites Environment can then establish secure connections to back-end resources accessible only over the ExpressRoute connection.  

**Note:**  An Azure Websites Environment cannot be created in a "v2" virtual network.  Azure Websites Environments are currently only supported in classic "v1" virtual networks.

[AZURE.INCLUDE [app-service-web-to-api-and-mobile](../includes/app-service-web-to-api-and-mobile.md)] 

## Required Network Connectivity ##
There are network connectivity requirements for Azure Websites Environments that may not be initially met in a virtual network connected to an ExpressRoute.

Azure Websites Environments require all of the following in order to function properly:


-  Outbound network connectivity to Azure Storage worldwide, and connectivity to Sql DB resources located in the same region as the Azure Websites Environment.  This network path cannot travel through internal corporate proxies because doing so will likely change the effective NAT address of the outbound network traffic.  Changing the NAT address of an Azure Websites Environment's outbound network traffic directed at Azure Storage and Sql DB endpoints will cause connectivity failures.
-  The DNS configuration for the virtual network must be capable of resolving endpoints within the following Azure controlled domains:  **.file.core.chinacloudapi.cn*, **.blob.core.chinacloudapi.cn*, **.database.chinacloudapi.cn*.
-  DNS configuration for the virtual network must remain stable whenever Azure Websites Environments are created, as well as during re-configurations and scaling changes to Azure Websites Environments.   
-  If a custom DNS server exists on the other end of a VPN gateway, the DNS server must be reachable and available. 
-  Inbound network access to required ports for Azure Websites Environments must be allowed as described in this [article][requiredports].

The DNS requirement can be met by ensuring a valid DNS configuration for the virtual network.  

The inbound network access requirements can be met by configuring a [network security group][NetworkSecurityGroups] on the Azure Websites Environment's subnet to allow the required access as described in this [article][requiredports].

## Enabling Outbound Network Connectivity for an Azure Websites Environment##
By default, a newly created ExpressRoute circuit advertises a default route that allows outbound Internet connectivity.  With this configuration an Azure Websites Environment will be able to connect to other Azure endpoints.

However a common customer configuration is to define their own default route which forces outbound Internet traffic to instead flow on-premises through a customer's proxy/firewall infrastructure.  This traffic flow invariably breaks Azure Websites Environments because the outbound traffic is either blocked on-premises, or NAT'd to an unrecognizable set of addresses that no longer work with various Azure endpoints.

The solution is to define one (or more) user defined routes (UDRs) on the subnet that contains the Azure Websites Environment.  A UDR defines subnet-specific routes that will be honored instead of the default route.

Background information on user defined routes is available in this [overview][UDROverview].  

Details on creating and configuring user defined routes is available in this [How To Guide][UDRHowTo].

## Example UDR Configuration for an Azure Websites Environment ##

**Pre-requisites**

1. Install the very latest Azure Powershell from the [Azure Downloads page][AzureDownloads] (dated June 2015 or later).  Under "Command-line tools" there is an "Install" link under "Windows Powershell" that will install the latest Powershell cmdlets.

2. It is recommended that a unique subnet is created for exclusive use by an Azure Websites Environment.  This ensures that the UDRs applied to the subnet will only open outbound traffic for the Azure Websites Environment.
3. **Important**:  do not deploy the Azure Websites Environment until **after** the following configuration steps are followed.  This ensures that outbound network connectivity is available before attempting to deploy an Azure Websites Environment.

**Step 1:  Create a named route table**

The following snippet creates a route table called "DirectInternetRouteTable" in the China North Azure region:

    New-AzureRouteTable -Name 'DirectInternetRouteTable' -Location uswest

**Step 2:  Create one or more routes in the route table**

You will need to add one or more routes to the route table in order to enable outbound Internet access.  The example below adds enough routes to cover all possible Azure addresses used in the China North region.

    Get-AzureRouteTable -Name 'DirectInternetRouteTable' | Set-AzureRoute -RouteName 'Direct Internet Range 1' -AddressPrefix 23.0.0.0/8 -NextHopType Internet
    Get-AzureRouteTable -Name 'DirectInternetRouteTable' | Set-AzureRoute -RouteName 'Direct Internet Range 2' -AddressPrefix 40.0.0.0/8 -NextHopType Internet
    Get-AzureRouteTable -Name 'DirectInternetRouteTable' | Set-AzureRoute -RouteName 'Direct Internet Range 3' -AddressPrefix 65.0.0.0/8 -NextHopType Internet
    Get-AzureRouteTable -Name 'DirectInternetRouteTable' | Set-AzureRoute -RouteName 'Direct Internet Range 4' -AddressPrefix 104.0.0.0/8 -NextHopType Internet
    Get-AzureRouteTable -Name 'DirectInternetRouteTable' | Set-AzureRoute -RouteName 'Direct Internet Range 5' -AddressPrefix 137.0.0.0/8 -NextHopType Internet
    Get-AzureRouteTable -Name 'DirectInternetRouteTable' | Set-AzureRoute -RouteName 'Direct Internet Range 6' -AddressPrefix 138.0.0.0/8 -NextHopType Internet
    Get-AzureRouteTable -Name 'DirectInternetRouteTable' | Set-AzureRoute -RouteName 'Direct Internet Range 7' -AddressPrefix 157.0.0.0/8 -NextHopType Internet
    Get-AzureRouteTable -Name 'DirectInternetRouteTable' | Set-AzureRoute -RouteName 'Direct Internet Range 8' -AddressPrefix 168.0.0.0/8 -NextHopType Internet
    Get-AzureRouteTable -Name 'DirectInternetRouteTable' | Set-AzureRoute -RouteName 'Direct Internet Range 9' -AddressPrefix 191.0.0.0/8 -NextHopType Internet


For a comprehensive and updated list of CIDR ranges in use by Azure, you can download an Xml file containing all of the ranges from the [Microsoft Download Center][DownloadCenterAddressRanges] 

**Note:**  at some point an abbreviated CIDR short-hand of 0.0.0.0/0 will be available for use in the *AddressPrefix* parameter.  This short hand equates to "all Internet addresses".  For now developers will need to instead use a broad set of CIDR ranges sufficient to cover all possible Azure address ranges.

**Step 3:  Associate the route table to the subnet containing the Azure Websites Environment**

The last  configuration step is to associate the route table to the subnet where the Azure Websites Environment will be deployed.  The following command associates the "DirectInternetRouteTable" to the "ASESubnet" that will eventually contain an Azure Websites Environment.

    Set-AzureSubnetRouteTable -VirtualNetworkName 'YourVirtualNetworkNameHere' -SubnetName 'ASESubnet' -RouteTableName 'DirectInternetRouteTable'


**Step 4:  Final Steps**

Once the route table is bound to the subnet, it is recommended to first test and confirm the intended effect.  For example, deploy a virtual machine into the subnet and confirm that:


- Outbound traffic to Azure endpoints is not flowing down the ExpressRoute circuit.
- DNS lookups for Azure endpoints are resolving properly. 

Once the above steps are confirmed, you can delete the virtual machine and then proceed with creating an Azure Websites Environment!

## Getting started

To get started with Azure Websites Environments, see [Introduction to Azure Websites Environment][IntroToAppServiceEnvironment]

For more information about the Azure Websites platform, see [Azure Websites][AzureAppService].

<!-- LINKS -->
[virtualnetwork]: http://azure.microsoft.com/services/networking/
[ExpressRoute]: http://azure.microsoft.com/services/expressroute/
[requiredports]: /documentation/articles/app-service-app-service-environment-control-inbound-traffic/
[NetworkSecurityGroups]: /documentation/articles/virtual-networks-nsg/
[UDROverview]: /documentation/articles/virtual-networks-udr-overview/
[UDRHowTo]: /documentation/articles/virtual-networks-udr-how-to/
[HowToCreateAnAppServiceEnvironment]: /documentation/articles/app-service-web-how-to-create-an-app-service-environment/
[AzureDownloads]: /downloads/ 
[DownloadCenterAddressRanges]: http://www.microsoft.com/download/details.aspx?id=41653  
[NetworkSecurityGroups]: /documentation/articles/virtual-networks-nsg/
[AzureAppService]: /documentation/articles/app-service-value-prop-what-is/
[IntroToAppServiceEnvironment]:  /documentation/articles/app-service-app-service-environment-intro/
 

<!-- IMAGES -->
