<properties 
   pageTitle="Specifying a DNS Settings in a Virtual Network Configuration File | Windows Azure"
   description="How to change DNS server settings in a virtual network using a virtual network configuration file"
   services="virtual-network"
   documentationCenter="na"
   authors="joaoma"
   manager="jdial"
   editor="tysonn" />
<tags
	ms.service="virtual-network"
	ms.date="08/25/2015"
	wacn.date=""/>

# Specifying DNS settings in a virtual network configuration file

A network configuration file has two elements that you can use to specify Domain Name System (DNS) settings: **DnsServers** and **DnsServerRef**. You can add a list of DNS servers by specifying their IP addresses and reference names to the **DnsServers** element. You can then use a **DnsServerRef** element to specify which DNS server entries from the DnsServers element are used for different network sites within your virtual network.

>[AZURE.IMPORTANT] For information about how to configure the network configuration file, see [Configure a Virtual Network Using a Network Configuration File](/documentation/articles/virtual-networks-using-network-configuration-file). For information about each element contained in the network configuration file, see [Azure Virtual Network Configuration Schema](https://msdn.microsoft.com/zh-cn/library/azure/jj157100.aspx).

The network configuration file may contain the following elements. The title of each element is linked to a page that provides additional information about the element value settings.

[Dns Element](https://msdn.microsoft.com/zh-cn/library/azure/jj157100)

    <Dns>
      <DnsServers>
        <DnsServer name="ID1" IPAddress="IPAddress1" />
        <DnsServer name="ID2" IPAddress="IPAddress2" />
        <DnsServer name="ID3" IPAddress="IPAddress3" />
      </DnsServers>
    </Dns>

>[AZURE.WARNING] The **name** attribute in the **DnsServer** element is used only as a reference for the **DnsServerRef** element. It does not represent the host name for the DNS server. Each **DnsServer** attribute value must be unique across the entire Windows Azure subscription

[Virtual Network Sites Element](https://msdn.microsoft.com/zh-cn/library/azure/jj157100)

	<DnsServersRef>
	  <DnsServerRef name="ID1" />
	  <DnsServerRef name="ID2" />
	  <DnsServerRef name="ID3" />
	</DnsServersRef>

>[AZURE.NOTE] In order to specify this setting for the Virtual Network Sites element, it must be previously defined in the DNS element. The DnsServerRef *name* in the Virtual Network Sites element must refer to a name value specified in the DNS element for DnsServer *name*.

## Next steps

[Configure a virtual network using Network configuration files](/documentation/articles/virtual-networks-using-network-configuration-file)

[Azure Virtual Network Configuration Schema](https://msdn.microsoft.com/zh-cn/library/azure/jj157100)

[Azure Service Configuration Schema](https://msdn.microsoft.com/zh-cn/library/azure/ee758710)
