<properties
	pageTitle="Scale sets CLI quick create | Azure"
	description="Deploy scale sets using CLI quick create."
	keywords="virtual machine scale sets" 
	services="virtual-machine-scale-sets"
	documentationCenter=""
	authors="gatneil"
	manager="madhana"
	editor="tysonn"
	tags="azure-resource-manager" />

<tags
	ms.service="virtual-machine-linux"
	ms.workload="infrastructure-services"
	ms.tgt_pltfrm="vm-linux"
	ms.devlang="na"
	ms.topic="article"
	ms.date="03/31/2016"
	wacn.date=""
	ms.author="gatneil"/>

# Quickly create a scale set using the Azure CLI

If you haven't already, you can get an [Azure subscription trial](/pricing/1rmb-trial/) and the [Azure CLI](/documentation/articles/xplat-cli-install/) [connected to your Azure account](/documentation/articles/xplat-cli-connect/). Once you do, you can run the following commands to quick-create a scale set:


    # make sure we are in Resource Manager mode (/documentation/articles/resource-manager-deployment-model/)
    azure config mode arm

    # quick-create a scale set
    #
    # generic syntax:
    # azure vmss quick-create -n SCALE-SET-NAME -g RESOURCE-GROUP-NAME -l LOCATION -u USERNAME -p PASSWORD -C INSTANCE-COUNT -Q IMAGE-URN
    #
    # example:
    azure vmss quick-create -n negatvmss -g negatvmssrg -l chinanorth -u negat -p P4ssw0rd -C 5 -Q Canonical:UbuntuServer:14.04.3-LTS:latest

If you want to customize the location or image-urn, please look into the commands `azure location list` and `azure vm image {list-publishers|list-offers|list-skus|list|show}`.

Once this command has returned, the scale set will have been created. This scale set will have a load balancer with NAT rules mapping port 50,000+i on the load balancer to port 22 on VM i. Thus, once we figure out the FQDN of the load balancer, we will be able to connect via ssh to our VMs:

    # (if you decide to run this as a script, please invoke using bash)

    # list load balancers in the resource group we created
    #
    # generic syntax:
    # azure network lb list -g RESOURCE-GROUP-NAME
    #
    # example with some quick-and-dirty grep-fu to store the result in a variable:
    line=$(azure network lb list -g negatvmssrg | grep negatvmssrg)
    split_line=( $line )
    lb_name=${split_line[1]}

    # now that we have the name of the load balancer, we can show the details to find which Public IP (PIP) is associated to it
    #
    # generic syntax:
    # azure network lb show -g RESOURCE-GROUP-NAME -n LOAD-BALANCER-NAME
    #
    # example with some quick-and-dirty grep-fu to store the result in a variable:
    line=$(azure network lb show -g negatvmssrg -n $lb_name | grep loadBalancerFrontEnd)
    split_line=( $line )
    pip_name=${split_line[4]}

    # now that we have the name of the public IP address, we can show the details to find the FQDN
    #
    # generic syntax:
    # azure network public-ip show -g RESOURCE-GROUP-NAME -n PIP-NAME
    #
    # example with some quick-and-dirty grep-fu to store the result in a variable:
    line=$(azure network public-ip show -g negatvmssrg -n $pip_name | grep FQDN)
    split_line=( $line )
    FQDN=${split_line[3]}

    # now that we have the FQDN, we can use ssh on port 50,000+i to connect to VM i (where i is 0-indexed)
    #
    # example to connct via ssh into VM "0":
    ssh -p 50000 negat@$FQDN

## Next steps

For example Resource Manager templates using scale sets, search for "vmss" in the [Azure Quickstart Templates github repo](https://github.com/Azure/azure-quickstart-templates).

For general information, check out the [main landing page for scale sets](/home/features/virtual-machine-scale-sets/).

