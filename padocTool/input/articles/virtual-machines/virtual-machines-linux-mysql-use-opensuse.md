<!-- rename to virtual-machines-linux-classic-mysql-on-opensuse -->

<properties
	pageTitle="Install MySQL on a OpenSUSE Linux VM in Azure"
	description="Learn to install MySQL on a virtual machine in Azure."
	services="virtual-machines"
	documentationCenter=""
	authors="cynthn"
	manager="timlt"
	editor=""
	tags="azure-service-management"/>

<tags
	ms.service="virtual-machines"
	ms.date="01/21/2016"
	wacn.date=""/>

# Install MySQL on a virtual machine running OpenSUSE Linux in Azure

[MySQL][MySQL] is a popular, open-source SQL database. This tutorial shows you how to create a virtual machine running OpenSUSE Linux, then install MySQL.

> [AZURE.IMPORTANT] Azure has two different deployment models for creating and working with resources:  [Resource Manager and classic](/documentation/articles/resource-manager-deployment-model/).  This article covers using the classic deployment model. Azure recommends that most new deployments use the Resource Manager model.


<br>


## Create a virtual machine running OpenSUSE Linux

[AZURE.INCLUDE [create-and-configure-opensuse-vm-in-portal](../../includes/create-and-configure-opensuse-vm-in-portal.md)]

## Install and run MySQL on the virtual machine

[AZURE.INCLUDE [install-and-run-mysql-on-opensuse-vm](../../includes/install-and-run-mysql-on-opensuse-vm.md)]

## Next steps
For details about MySQL, see the [MySQL Documentation][MySQLDocs].

[MySQLDocs]: http://dev.mysql.com/doc/index-topic.html
[MySQL]: http://www.mysql.com

