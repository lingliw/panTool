> [AZURE.NOTE]
> In order to use the China Cloud Environment, the following Azure PowerShell commands need to add **"-Environment AzureChinaCloud"** parameter.
> 
	Add-AzureAccount
	Get-AzurePublishSettingsFile
	Import-AzurePublishSettingsFile
	New-AzureProfile
	New-AzureStorageContext
	Set-AzureSubscription
	Show-AzurePortal
For example, `Add-AzureAccount -Credential $Cred -ErrorAction Stop` should become `Add-AzureAccount -Credential $Cred -ErrorAction Stop -Environment AzureChinaCloud`
> 
