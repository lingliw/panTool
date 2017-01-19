

Ever since its launch, the Custom Script extension has been used widely to configure workloads on both Windows and Linux VMs. With the introduction of Azure Resource Manager templates, users can now create a single template that not only provisions the VM but also configures the workloads on it.

## About Azure Resource Manager templates
Azure Resource Manager templates allow you to declaratively specify the Azure IaaS infrastructure in JSON language by defining the dependencies between resources. For a detailed overview of Azure Resource Manager templates, see the following articles:

* [Resource Group Overview](/documentation/articles/resource-group-overview/)
* [Deploying Templates with Azure PowerShell](/documentation/articles/virtual-machines-windows-ps-manage/)

### Prerequisites
1. Download the Azure command-line tools for your operating system from [here](/downloads/).
2. If the scripts will be run on an existing VM, make sure VM Agent is enabled on the VM, if not follow [the Linux](/documentation/articles/virtual-machines-linux-classic-manage-extensions/) or [Windows](/documentation/articles/virtual-machines-windows-classic-manage-extensions/) guidance to install one.
3. Upload the scripts that you want to run on the VM to Azure Storage. The scripts can come from a single or multiple storage containers.
4. Alternatively the scripts can also be uploaded to a GitHub account.
5. The script should be authored in such a way that the entry script which is launched by the extension in turn launches other scripts.

## Using the Custom Script extension
For deploying with templates we use the same version of Custom Script extension that's available for Azure Service Management APIs. The extension supports the same parameters and scenarios like uploading files to Azure Storage account or GitHub location. The key difference while using with templates is the exact version of the extension should be specified, as opposed to specifying the version in majorversion.* format.

