<properties 
	pageTitle="How to uninstall elastic database job tool" 
	description="How to uninstall elastic database job tool" 
	services="sql-database" 
	documentationCenter="" 
	manager="jeffreyg" 
	authors="sidneyh" 
	editor=""/>

<tags 
	ms.service="sql-database" 
	ms.date="08/09/2015" 
	wacn.date=""/>

#Uninstall Elastic Database jobs components
**Elastic Database jobs** components can be uninstalled using either the Portal or PowerShell.

##Uninstall Elastic Database jobs components using the Azure portal

1. Open the [Azure portal](https://manage.windowsazure.cn).
2. Navigate to the subscription that contains **Elastic Database jobs** components, namely the subscription in which Elastic Database jobs components were installed.
3. Click **Browse** and click **Resource groups**.
4. Select the resource group named "__ElasticDatabaseJob".
5. Delete the resource group.

##Uninstall  Elastic Database jobs components using PowerShell

1.	Launch a Microsoft Azure PowerShell command window and navigate to the tools sub-directory under the Microsoft.Azure.SqlDatabase.Jobs.x.x.xxxx.x folder: Type cd tools

		PS C:\*Microsoft.Azure.SqlDatabase.Jobs.x.x.xxxx.x*>cd tools

2.	Execute the .\UninstallElasticDatabaseJobs.ps1 PowerShell script.

		PS C:\*Microsoft.Azure.SqlDatabase.Jobs.x.x.xxxx.x*\tools>Unblock-File .\UninstallElasticDatabaseJobs.ps1
		PS C:\*Microsoft.Azure.SqlDatabase.Jobs.x.x.xxxx.x*\tools>.\UninstallElasticDatabaseJobs.ps1

Or simply, execute the following script, assuming default values where used on installation of the components:

		$ResourceGroupName = "__ElasticDatabaseJob"
		Switch-AzureMode AzureResourceManager
		
		$resourceGroup = Get-AzureResourceGroup -Name $ResourceGroupName
		if(!$resourceGroup)
		{
		    Write-Host "The Azure Resource Group: $ResourceGroupName has already been deleted.  Elastic database job components are uninstalled."
		    return
		}
		
		Write-Host "Removing the Azure Resource Group: $ResourceGroupName.  This may take a few minutes.”
		Remove-AzureResourceGroup -Name $ResourceGroupName -Force
		Write-Host "Completed removing the Azure Resource Group: $ResourceGroupName.  Elastic database job compoennts are now uninstalled."

## Next steps

To re-install Elastic Database jobs, see [Installing the Elastic Database job service](/documentation/articles/sql-database-elastic-jobs-service-installation)

For an overview of Elastic Database jobs, see [Elastic Database jobs overview](/documentation/articles/sql-database-elastic-jobs-overview).

<!--Image references-->
[1]: ./media/sql-database-elastic-job-uninstall/
 
