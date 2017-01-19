Before you can use the Azure CLI with Resource Manager commands and templates to deploy Azure resources and workloads using resource groups, you will need an account with Azure. If you do not have an account, you can get an [Azure trial here](/pricing/1rmb-trial/).

If you haven't already installed the Azure CLI and connected to your subscription, see [Install the Azure CLI](/documentation/articles/xplat-cli-install/) set the mode to `arm` with `azure config mode arm`, and connect to Azure with the `azure login -e AzureChinaCloud` command.

## Basic Azure Resource Manager commands in Azure CLI
This article covers basic commands you will want to use with Azure CLI to manage and interact with your ARM resources (primarily VMs) in your Azure subscription.  For more detailed help with specific command line switches and options, you can use the online command help and options by typing `azure <command> <subcommand> --help` or `azure help <command> <subcommand>`.

> [AZURE.NOTE]
> These examples don't include template-based operations which are generally recommended for VM deployments in Resource Manager. For information, see [Use the Azure CLI with Azure Resource Manager](/documentation/articles/xplat-cli-azure-resource-manager/) and [Deploy and manage virtual machines by using Azure Resource Manager templates and the Azure CLI](/documentation/articles/virtual-machines-linux-cli-deploy-templates/).
> 
> 

| Task | Resource Manager |
| --- | --- | --- |
| Create the most basic VM |`azure vm quick-create [options] <resource-group> <name> <location> <os-type> <image-urn> <admin-username> <admin-password>`<br/><br/>(Obtain the `image-urn` from the `azure vm image list` command. See [this article](/documentation/articles/virtual-machines-linux-cli-ps-findimage/) for examples.) |
| Create a Linux VM |`azure  vm create [options] <resource-group> <name> <location> -y "Linux"` |
| Create a Windows VM |`azure  vm create [options] <resource-group> <name> <location> -y "Windows"` |
| List VMs |`azure  vm list [options]` |
| Get information about a VM |`azure  vm show [options] <resource_group> <name>` |
| Start a VM |`azure vm start [options] <resource_group> <name>` |
| Stop a VM |`azure vm stop [options] <resource_group> <name>` |
| Deallocate a VM |`azure vm deallocate [options] <resource-group> <name>` |
| Restart a VM |`azure vm restart [options] <resource_group> <name>` |
| Delete a VM |`azure vm delete [options] <resource_group> <name>` |
| Capture a VM |`azure vm capture [options] <resource_group> <name>` |
| Create a VM from a user image |`azure  vm create [options] -q <image-name> <resource-group> <name> <location> <os-type>` |
| Create a VM from a specialized disk |`azue  vm create [options] -d <os-disk-vhd> <resource-group> <name> <location> <os-type>` |
| Add a data disk to a VM |`azure  vm disk attach-new [options] <resource-group> <vm-name> <size-in-gb> [vhd-name]` |
| Remove a data disk from a VM |`azure  vm disk detach [options] <resource-group> <vm-name> <lun>` |
| Add a generic extension to a VM |`azure  vm extension set [options] <resource-group> <vm-name> <name> <publisher-name> <version>` |
| Add VM Access extension to a VM |`azure vm reset-access [options] <resource-group> <name>` |
| Remove a VM extension |`azure  vm extension set [options] -u <resource-group> <vm-name> <name> <publisher-name> <version>` |
| Get usage of VM resources |`azure vm list-usage [options] <location>` |
| Get all available VM sizes |`azure vm sizes [options]` |

## Next steps
* For additional examples of the CLI commands going beyond basic VM management, see [Using the Azure CLI with Azure Resource Manager](/documentation/articles/azure-cli-arm-commands/).

