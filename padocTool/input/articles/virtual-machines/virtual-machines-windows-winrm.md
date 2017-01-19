<properties
    pageTitle="Setting up WinRM access for Virtual Machines in Azure Resource Manager | Azure"
    description="How to setup WinRM access for use with an Azure Resource Manager virtual machine"
    services="virtual-machines-windows"
    documentationcenter=""
    author="singhkays"
    manager="timlt"
    editor=""
    tags="azure-resource-manager" />
<tags
    ms.assetid="9718e85b-d360-4621-90b8-0b0b84a21208"
    ms.service="virtual-machines-windows"
    ms.workload="infrastructure-services"
    ms.tgt_pltfrm="vm-windows"
    ms.devlang="na"
    ms.topic="article"
    ms.date="06/16/2016"
    wacn.date=""
    ms.author="singhkay" />

# Setting up WinRM access for Virtual Machines in Azure Resource Manager
## WinRM in Azure Service Management vs Azure Resource Manager

[AZURE.INCLUDE [learn-about-deployment-models](../../includes/learn-about-deployment-models-rm-include.md)]

* For an overview of the Azure Resource Manager, please see this [article](/documentation/articles/resource-group-overview/)
* For differences between Azure Service Management and Azure Resource Manager, please see this [article](/documentation/articles/resource-manager-deployment-model/)

The key difference in setting up WinRM configuration between the two stacks is how the certificate gets installed on the VM. In the Azure Resource Manager stack, the certificates are modeled as resources managed by the Key Vault Resource Provider. Therefore, the user needs to provide their own certificate and upload it to a Key Vault before using it in a VM.

Here are the steps you need to take to set up a VM with WinRM connectivity

1. Create a Key Vault
2. Create a self-signed certificate
3. Upload your self-signed certificate to Key Vault
4. Get the URL for your self-signed certificate in the Key Vault
5. Reference your self-signed certificates URL while creating a VM

## Step 1: Create a Key Vault
You can use the below command to create the Key Vault

    New-AzureRmKeyVault -VaultName "<vault-name>" -ResourceGroupName "<rg-name>" -Location "<vault-location>" -EnabledForDeployment -EnabledForTemplateDeployment

## Step 2: Create a self-signed certificate
You can create a self-signed certificate using this PowerShell script

    $certificateName = "somename"

    $thumbprint = (New-SelfSignedCertificate -DnsName $certificateName -CertStoreLocation Cert:\CurrentUser\My -KeySpec KeyExchange).Thumbprint

    $cert = (Get-ChildItem -Path cert:\CurrentUser\My\$thumbprint)

    $password = Read-Host -Prompt "Please enter the certificate password." -AsSecureString

    Export-PfxCertificate -Cert $cert -FilePath ".\$certificateName.pfx" -Password $password

## Step 3: Upload your self-signed certificate to the Key Vault
Before uploading the certificate to the Key Vault created in step 1, it needs to converted into a format the Microsoft.Compute resource provider will understand. The below PowerShell script will allow you do that

    $fileName = "<Path to the .pfx file>"
    $fileContentBytes = Get-Content $fileName -Encoding Byte
    $fileContentEncoded = [System.Convert]::ToBase64String($fileContentBytes)

    $jsonObject = @"
    {
      "data": "$filecontentencoded",
      "dataType" :"pfx",
      "password": "<password>"
    }
    "@

    $jsonObjectBytes = [System.Text.Encoding]::UTF8.GetBytes($jsonObject)
    $jsonEncoded = [System.Convert]::ToBase64String($jsonObjectBytes)

    $secret = ConvertTo-SecureString -String $jsonEncoded -AsPlainText -Force
    Set-AzureKeyVaultSecret -VaultName "<vault name>" -Name "<secret name>" -SecretValue $secret

## Step 4: Get the URL for your self-signed certificate in the Key Vault
The Microsoft.Compute resource provider needs a URL to the secret inside the Key Vault while provisioning the VM. This enables the Microsoft.Compute resource provider to download the secret and create the equivalent certificate on the VM.

> [AZURE.NOTE]
> The URL of the secret needs to include the version as well. An example URL looks like below
> https://contosovault.vault.chinacloudapi.cn:443/secrets/contososecret/01h9db0df2cd4300a20ence585a6s7ve
> 
> 

#### Templates
You can get the link to the URL in the template using the below code

    "certificateUrl": "[reference(resourceId(resourceGroup().name, 'Microsoft.KeyVault/vaults/secrets', '<vault-name>', '<secret-name>'), '2015-06-01').secretUriWithVersion]"

#### PowerShell
You can get this URL using the below PowerShell command

    $secretURL = (Get-AzureKeyVaultSecret -VaultName "<vault name>" -Name "<secret name>").Id

## Step 5: Reference your self-signed certificates URL while creating a VM
#### Azure Resource Manager Templates
While creating a VM through templates, the certificate gets referenced in the secrets section and the winRM section as below:

    "osProfile": {
          ...
          "secrets": [
            {
              "sourceVault": {
                "id": "<resource id of the Key Vault containing the secret>"
              },
              "vaultCertificates": [
                {
                  "certificateUrl": "<URL for the certificate you got in Step 4>",
                  "certificateStore": "<Name of the certificate store on the VM>"
                }
              ]
            }
          ],
          "windowsConfiguration": {
            ...
            "winRM": {
              "listeners": [
                {
                  "protocol": "http"
                },
                {
                  "protocol": "https",
                  "certificateUrl": "<URL for the certificate you got in Step 4>"
                }
              ]
            },
            ...
          }
        },

A sample template for the above can be found here at [201-vm-winrm-keyvault-windows](https://github.com/Azure/azure-quickstart-templates/tree/master/201-vm-winrm-keyvault-windows)

Source code for this template can be found on [GitHub](https://github.com/Azure/azure-quickstart-templates/tree/master/201-vm-winrm-keyvault-windows)

>[AZURE.NOTE] Templates you downloaded from the GitHub Repo "azure-quickstart-templates" must be modified in order to fit in the Azure China Cloud Environment. For example, replace some endpoints -- "blob.core.chinacloudapi.cn" by "blob.core.chinacloudapi.cn", "chinacloudapp.cn" by "chinacloudapp.cn"; change some unsupported VM images; and, changes some unsupported VM sizes.

#### PowerShell
    $vm = New-AzureRmVMConfig -VMName "<VM name>" -VMSize "<VM Size>"
    $credential = Get-Credential
    $secretURL = (Get-AzureKeyVaultSecret -VaultName "<vault name>" -Name "<secret name>").Id
    $vm = Set-AzureRmVMOperatingSystem -VM $vm -Windows -ComputerName "<Computer Name>" -Credential $credential -WinRMHttp -WinRMHttps -WinRMCertificateUrl $secretURL
    $sourceVaultId = (Get-AzureRmKeyVault -ResourceGroupName "<Resource Group name>" -VaultName "<Vault Name>").ResourceId
    $CertificateStore = "My"
    $vm = Add-AzureRmVMSecret -VM $vm -SourceVaultId $sourceVaultId -CertificateStore $CertificateStore -CertificateUrl $secretURL

## Step 6: Connecting to the VM
Before you can connect to the VM you'll need to make sure your machine is configured for WinRM remote management. Start PowerShell as an administrator and execute the below command to make sure you're set up.

    Enable-PSRemoting -Force

> [AZURE.NOTE]
> You might need to make sure the WinRM service is running if the above does not work. You can do that using `Get-Service WinRM`
> 
> 

Once the setup is done, you can connect to the VM using the below command

    Enter-PSSession -ConnectionUri https://<public-ip-dns-of-the-vm>:5986 -Credential $cred -SessionOption (New-PSSessionOption -SkipCACheck -SkipCNCheck -SkipRevocationCheck) -Authentication Negotiate