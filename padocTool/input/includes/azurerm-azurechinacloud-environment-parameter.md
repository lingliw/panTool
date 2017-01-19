> [AZURE.NOTE]
> In order to use the China Cloud Environment, the following Azure PowerShell commands need to add **"-Environment"** parameter.
> 
>	`Add-AzureRmAccount` <br />
>	`Login-AzureRmAccount` <br />
>	
>For example, `Login-AzureRmAccount` should become `$china = Get-AzureRmEnvironment -Name AzureChinaCloud; Login-AzureRmAccount -Environment $china` if you are using Azure PowerShell 1.0.0 or 1.0.1, or `Login-AzureRmAccount -EnvironmentName AzureChinaCloud` if you are using Azure PowerShell 1.0.2 or greater.
> 