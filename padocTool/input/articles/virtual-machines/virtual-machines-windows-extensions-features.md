<!-- need to be verified -->

<properties
    pageTitle="Virtual machine extensions and features | Azure"
    description="Learn what extensions are available for Azure virtual machines, grouped by what they provide or improve."
    services="virtual-machines-windows"
    documentationcenter=""
    author="neilpeterson"
    manager="timlt"
    editor=""
    tags="azure-service-management,azure-resource-manager" />
<tags
    ms.assetid="999d63ee-890e-432e-9391-25b3fc6cde28"
    ms.service="virtual-machines-windows"
    ms.devlang="na"
    ms.topic="article"
    ms.tgt_pltfrm="vm-windows"
    ms.workload="infrastructure-services"
    ms.date="11/17/2016"
    wacn.date=""
    ms.author="nepeters" />

# About virtual machine extensions and features

Azure Virtual Machine extensions are small applications that provide post deployment configuration and automation task on Azure Virtual Machines. For example, if a Virtual Machine requires software to be installed, anti-virus protection, or Docker configuration, a VM extension can be used to complete these tasks. Azure VM extensions can be run using the Azure CLI, PowerShell, Resource Manage templates, and the Azure portal preview. Extensions can be bundled with a new virtual machine deployment, or run against any existing system.

This document provides an overview of virtual machine extensions, prerequisites for using Azure Virtual Machine extensions, and guidance on how to detect, manage, and remove virtual machine extensions. Because many VM extensions are available, each with a potentially unique configuration, this document provides generalized information. Extensions specific details can be found in each document specific the individual extension. 

## Use cases and samples

There are many different Azure VM extensions available, each with a specific use case. Some example use cases are:

- Apply PowerShell Desired State Configurations to a virtual machine using the DSC extension for Windows. For more information, see [Azure Desired State configuration extension](/documentation/articles/virtual-machines-windows-extensions-dsc-overview/).
- Configure monitoring of virtual machines with using the Microsoft Monitoring Agent VM extension. For more information, see [Connect Azure virtual machines to Log Analytics](/documentation/articles/log-analytics-azure-vm-extension/). 
- Configure monitoring of your Azure infrastructure with the Datadog extension. For more information, see [Datadog blog](https://www.datadoghq.com/blog/introducing-azure-monitoring-with-one-click-datadog-deployment/).
- Configure an Azure virtual machine using Chef. For more information, see [Automating Azure virtual machine deployment with Chef](/documentation/articles/virtual-machines-windows-chef-automation/).

In addition to process specific extensions, a Custom Script extension is available for both Windows and Linux virtual machines. The Custom Script extension for Windows allows any PowerShell script to be run on a virtual machine. This is useful when designing Azure deployments that require configuration beyond what native Azure tooling can provide. For more information, see [Windows VM Custom Script extension](/documentation/articles/virtual-machines-windows-extensions-customscript/).

To work through an example where a VM extension is used in an end to end application deployment, check out [Automating application deployments to Azure Virtual Machines](/documentation/articles/virtual-machines-windows-dotnet-core-1-landing/).

## Prerequisites

Each virtual machine extension may have its own set of prerequisites. For instance, the Docker VM extension has a prerequisite of a supported Linux distribution. Requirements of individual extension are detailed in the extension-specific documentation. 

### Azure VM Agent
The Azure VM Agent manages interaction between an Azure Virtual Machine and the Azure Fabric Controller. The VM agent is responsible for many functional aspects of deploying and managing Azure Virtual Machines, including running VM Extensions. The Azure VM Agent is pre-installed on Azure Gallery Images, and can be installed on supported operating systems. 

For information on supported operating systems and installation instructions, see [Azure Virtual Machine Agent](/documentation/articles/virtual-machines-windows-classic-agents-and-extensions/).

## Discover VM extensions
Many different VM extensions are available for use with Azure Virtual Machines. To see a complete list, run the following command with the Azure PowerShell module.

    Get-AzureVMAvailableExtension | Select ExtensionName, Version

## Running VM extensions

Azure virtual machine extensions can be run on existing virtual machines, which is useful when needing to make configuration changes or recover connectivity on an already deployed VM. VM extensions can also be bundled with Azure Resource Manager template deployments. Using extension with Resource Manager templates enables Azure virtual machines to be deployed and configured without the need for post deployment intervention.

The following methods can be used to run an extension against an existing virtual machine. 

### PowerShell

Several PowerShell commands exist for running individual extensions. To see a list, run the following PowerShell commands:

    get-command Set-AzureRM*Extension* -Module AzureRM.Compute

Which provides output similar to the following:

    CommandType     Name                                               Version    Source
    -----------     ----                                               -------    ------
    Cmdlet          Set-AzureRmVMAccessExtension                       2.2.0      AzureRM.Compute
    Cmdlet          Set-AzureRmVMADDomainExtension                     2.2.0      AzureRM.Compute
    Cmdlet          Set-AzureRmVMAEMExtension                          2.2.0      AzureRM.Compute
    Cmdlet          Set-AzureRmVMBackupExtension                       2.2.0      AzureRM.Compute
    Cmdlet          Set-AzureRmVMBginfoExtension                       2.2.0      AzureRM.Compute
    Cmdlet          Set-AzureRmVMChefExtension                         2.2.0      AzureRM.Compute
    Cmdlet          Set-AzureRmVMCustomScriptExtension                 2.2.0      AzureRM.Compute
    Cmdlet          Set-AzureRmVMDiagnosticsExtension                  2.2.0      AzureRM.Compute
    Cmdlet          Set-AzureRmVMDiskEncryptionExtension               2.2.0      AzureRM.Compute
    Cmdlet          Set-AzureRmVMDscExtension                          2.2.0      AzureRM.Compute
    Cmdlet          Set-AzureRmVMExtension                             2.2.0      AzureRM.Compute
    Cmdlet          Set-AzureRmVMSqlServerExtension                    2.2.0      AzureRM.Compute

The following example uses the custom script extension to download a script from a GitHub repository onto the target virtual machine, and then run the script. For more information on the VM Access Extension, see [Custom Script Extension overview](/documentation/articles/virtual-machines-windows-extensions-customscript/).

    Set-AzureRmVMCustomScriptExtension -ResourceGroupName "myResourceGroup" `
        -VMName "myVM" -Name "myCustomScript" `
        -FileUri "https://raw.githubusercontent.com/neilpeterson/nepeters-azure-templates/master/windows-custom-script-simple/support-scripts/Create-File.ps1" `
        -Run "Create-File.ps1" -Location "China North"

In this example, the VM Access Extension is used to reset the administrative password of a Windows virtual machine. For more information on the VM Access Extension, see [Reset Remote Desktop service in a Windows VM](/documentation/articles/virtual-machines-windows-reset-rdp/).

    $cred=Get-Credential

    Set-AzureRmVMAccessExtension -ResourceGroupName "myResourceGroup" -VMName "myVM" -Name "myVMAccess" `
        -Location ChinaNorth -UserName $cred.GetNetworkCredential().Username `
        -Password $cred.GetNetworkCredential().Password -typeHandlerVersion "2.0"

The `Set-AzureRmVMExtension` command can be used as a catch all or general command for starting any VM extension. For more information, see [Set-AzureRmVMExtension reference](https://msdn.microsoft.com/zh-cn/library/mt603745.aspx).


### Azure portal preview

VM extension can be applied to an existing virtual machine through the Azure portal preview. To do so, select the virtual machine - extensions - and click add. Doing so provides a list of available extensions. Select the one you want, which provides a wizard for configuration. 

The following image depicts the installation of the Microsoft Antimalware extension from the Azure portal preview.

![Antimalware Extension](./media/virtual-machines-windows-extensions-features/anti-virus-extension.png)

### Azure Resource Manager templates

VM extensions can be added to an Azure Resource Manager template and executed with the deployment of the template. Deploying extension with a template is useful for creating fully configured Azure deployments. For example, the following JSON is taken from a Resource Manager template that deploys a set of load balanced virtual machines, an Azure SQL database, and installs a .Net Core application on each VM. The VM extension takes care of the software installation. 

The full Resource Manager template can be found [here](https://github.com/Microsoft/dotnet-core-sample-templates/tree/master/dotnet-core-music-windows). 

>[AZURE.NOTE] Templates you downloaded must be modified in order to fit in the Azure China Cloud Environment. For example, replace some endpoints -- "blob.core.windows.net" by "blob.core.chinacloudapi.cn", "cloudapp.azure.com" by "chinacloudapp.cn", and "database.windows.net" by "database.chinacloudapi.cn"; change some unsupported VM images; and, changes some unsupported VM sizes.

    {
        "apiVersion": "2015-06-15",
        "type": "extensions",
        "name": "config-app",
        "location": "[resourceGroup().location]",
        "dependsOn": [
        "[concat('Microsoft.Compute/virtualMachines/', variables('vmName'),copyindex())]",
        "[variables('musicstoresqlName')]"
        ],
        "tags": {
        "displayName": "config-app"
        },
        "properties": {
        "publisher": "Microsoft.Compute",
        "type": "CustomScriptExtension",
        "typeHandlerVersion": "1.4",
        "autoUpgradeMinorVersion": true,
        "settings": {
            "fileUris": [
            "https://raw.githubusercontent.com/Microsoft/dotnet-core-sample-templates/master/dotnet-core-music-windows/scripts/configure-music-app.ps1"
            ]
        },
        "protectedSettings": {
            "commandToExecute": "[concat('powershell -ExecutionPolicy Unrestricted -File configure-music-app.ps1 -user ',parameters('adminUsername'),' -password ',parameters('adminPassword'),' -sqlserver ',variables('musicstoresqlName'),'.database.chinacloudapi.cn')]"
        }
        }
    }

For more information, see [Authoring Azure Resource Manager templates with Windows VM extensions](/documentation/articles/virtual-machines-windows-extensions-authoring-templates/).

## Troubleshoot VM extensions

Each VM extension may have troubleshooting steps specific to the extensions. For instance, when using the Custom Script Extension, script execution details can be found locally on the virtual machine on which the extension was run. Any extension-specific troubleshooting steps are detailed in extension-specific documentation. 

The following troubleshooting steps apply to all Virtual Machine extensions.

### Viewing extension status

Once a Virtual Machine extension has been run against a virtual machine, use the following PowerShell command to return extension status. Replace example parameter names with your own values. The `Name` parameter takes the name given to the extension at execution time.

    Get-AzureRmVMExtension -ResourceGroupName myResourceGroup -VMName myVM -Name myExtensionName

The output looks similar to the following:

    ResourceGroupName       : myResourceGroup
    VMName                  : myVM
    Name                    : myExtensionName
    Location                : chinanorth
    Etag                    : null
    Publisher               : Microsoft.Azure.Extensions
    ExtensionType           : DockerExtension
    TypeHandlerVersion      : 1.0
    Id                      : /subscriptions/mySubscriptionIS/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachines/myVM/extensions/myExtensionName
    PublicSettings          : 
    ProtectedSettings       :
    ProvisioningState       : Succeeded
    Statuses                :
    SubStatuses             :
    AutoUpgradeMinorVersion : False
    ForceUpdateTag          :

Extension execution status can also be found in the Azure portal preview. To view the status of an extension, select the virtual machine > extensions > select the desired extension.

### Rerunning VM extensions 

There may be cases where a virtual machine extension needs to be rerun. This can be accomplished by removing the extension, and then rerunning the extension with an execution method of your choice. To remove an extension, run the following command with the Azure PowerShell module. Replace example parameter names with your own values.

    Remove-AzureRmVMExtension -ResourceGroupName myResourceGroup -VMName myVM -Name myExtensionName

An extension can also be removed using the Azure portal preview. To do so, select a virtual machine > extensions > the desired extension > uninstall.

## Common VM extensions reference
| Extension Name | Description | More Information |
| --- | --- | --- |
| Custom Script Extension for Windows |Run scripts against an Azure Virtual Machine |[Custom Script Extension for Windows](/documentation/articles/virtual-machines-windows-extensions-customscript/) |
| DSC Extension for Windows |PowerShell DSC (Desired State Configuration) Extension. |[DSC Extension for Windows](/documentation/articles/virtual-machines-windows-extensions-dsc-overview/) |
| Azure Diagnostics Extension |Manage Azure Diagnostics |[Azure Diagnostics Extension](https://azure.microsoft.com/blog/windows-azure-virtual-machine-monitoring-with-wad-extension/) |
| Azure VM Access Extension |Manage users and credentials |[VM Access Extension for Windows](https://azure.microsoft.com/blog/using-vmaccess-extension-to-reset-login-credentials-for-linux-vm/) |
