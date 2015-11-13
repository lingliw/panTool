<properties 
    pageTitle="Import a BACPAC to an Azure SQL Database using PowerShell" 
    description="Import a BACPAC to an Azure SQL Database using PowerShell" 
    services="sql-database" 
    documentationCenter="" 
    authors="stevestein" 
    manager="jeffreyg" 
    editor=""/>

<tags
    ms.service="sql-database"
    ms.date="09/05/2015"
    wacn.date=""/>

# Import a BACPAC to a SQL Database using PowerShell

**Single database**

> [AZURE.SELECTOR]
- [Azure Preview Portal](/documentation/articles/sql-database-import)
- [PowerShell](/documentation/articles/sql-database-import-powershell)


This article shows you how to create a SQL database by importing a BACPAC with PowerShell.

A BACPAC is a .bacpac file that contains a database schema and data. For details, see Backup Package (.bacpac) in [Data-tier Applications](https://msdn.microsoft.com/library/ee210546.aspx).

The database is created from a BACPAC imported from an Azure storage blob container. If you don't have a .bacpac file in Azure storage you can create one by following the steps in [Create and export a BACPAC of an Azure SQL Database](/documentation/articles/sql-database-backup).

> [AZURE.NOTE] Azure SQL Database automatically creates and maintains backups for every user database that you can restore. For details, see [Business Continuity Overview](/documentation/articles/sql-database-business-continuity).


To import a SQL database you need the following:

- An Azure subscription. If you need an Azure subscription simply click **FREE TRIAL** at the top of this page, and then come back to finish this article.
- A .bacpac file (BACPAC) of the database you want to restore. The BACPAC needs to be in an [Azure Storage account (classic)](/documentation/articles/storage-create-storage-account) blob container.
- Azure PowerShell. You can download and install the Azure PowerShell modules by running the [Microsoft Web Platform Installer](http://go.microsoft.com/fwlink/p/?linkid=320376&clcid=0x409). For detailed information, see [How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure).



## Configure your credentials and select your subscription

First you must establish access to your Azure account so start PowerShell and then run the following cmdlet. In the login screen enter the same email and password that you use to sign in to the Azure portal.

	Add-AzureAccount

After successfully signing in you will see some information on screen that includes the Id you signed in with and the Azure subscriptions you have access to.


### Select your Azure subscription

To select the subscription you need your subscription Id. You can copy the subscription Id from the information displayed from the previous step, or if you have multiple subscriptions and need more details you can run the **Get-AzureSubscription** cmdlet and copy the desired subscription information from the resultset. Once you have your subscription Id run the following cmdlet:

	Select-AzureSubscription -SubscriptionId 4cac86b0-1e56-bbbb-aaaa-000000000000

After successfully running **Select-AzureSubscription** you are returned to the PowerShell prompt. If you have more than one subscription you can run **Get-AzureSubscription** and verify the subscription you selected shows **IsCurrent : True**.


## Setup the variables for your environment

There are a few variables where you need to replace the example values with the specific values for your database and your storage account.

The server name needs to be a server that currently exists in the subscription selected in the previous step and is the server you want the database to be created in.

The database name is the name you want for the new database.

    $ServerName = "servername"
    $DatabaseName = "databasename"


The following variables are from the storage account where your BACPAC is located. In the [Azure Preview Portal](https://portal.azure.com) browse to your storage account to get these values. You can find the primary access key by clicking **All settings** and then **Keys** from your storage account's blade.

The blob name is the name of an existing .bacpac file that you want to create the database from. You need to include the .bacpac extension.

    $StorageName = "storageaccountname"
    $ContainerName = "blobcontainername"
    $BlobName = "filename.bacpac"
    $StorageKey = "primaryaccesskey"

## Create a pointer to your server and storage account

Running the **Get-Credential** cmdlet opens a window asking for your username and password. Enter the admin login and password for the SQL server you want to create the database in($ServerName from above), and not the username and password for your Azure account.

    $credential = Get-Credential
    $SqlCtx = New-AzureSqlDatabaseServerContext -ServerName $ServerName -Credential $credential

    $StorageCtx = New-AzureStorageContext -StorageAccountName $StorageName -StorageAccountKey $StorageKey
    $Container = Get-AzureStorageContainer -Name $ContainerName -Context $StorageCtx


## Import the database

This command submits an import database request to the service. Depending on the size of your database the import operation may take some time to complete.

    $exportRequest = Start-AzureSqlDatabaseExport -SqlConnectionContext $SqlCtx -StorageContainer $Container -DatabaseName $DatabaseName -BlobName $BlobName
    

## Monitor the progress of the operation

After running **Start-AzureSqlDatabaseImport** you can check the status of the request. 

Checking status immediately after the request will usually return a status of **Pending**, or **Running** and will provide current percent complete so you can run this multiple times until you see **Status : Completed** in the output. 

Running this command will prompt you for a password. Enter the admin login and password for your SQL server.


    Get-AzureSqlDatabaseImportExportStatus -RequestId $ImportRequest.RequestGuid -ServerName $ServerName -Username $credential.UserName
 


## SQL Database PowerShell restore script


    Add-AzureAccount
    Select-AzureSubscription -SubscriptionId "4cac86b0-1e56-bbbb-aaaa-000000000000"
    
    $ServerName = "servername"
    $DatabaseName = "nameofnewdatabase"

    $StorageName = "storageaccountname"
    $ContainerName = "blobcontainername"
    $BlobName = "filename.bacpac"
    $StorageKey = "primaryaccesskey"
    
    $credential = Get-Credential
    $SqlCtx = New-AzureSqlDatabaseServerContext -ServerName $ServerName -Credential $credential
    
    $StorageCtx = New-AzureStorageContext -StorageAccountName $StorageName -StorageAccountKey $StorageKey
    $Container = Get-AzureStorageContainer -Name $ContainerName -Context $StorageCtx
    
    $ImportRequest = Start-AzureSqlDatabaseExport -SqlConnectionContext $SqlCtx -StorageContainer $Container -DatabaseName $DatabaseName -BlobName $BlobName
    
    Get-AzureSqlDatabaseImportExportStatus -RequestId $ImportRequest.RequestGuid -ServerName $ServerName -Username $credential.UserName
    

## Next steps

- [Connect with SQL Server Management Studio (SSMS)](/documentation/articles/sql-database-connect-to-database)




## Additional resources

- [Business Continuity Overview](/documentation/articles/sql-database-business-continuity)
- [Disaster Recovery Drills](/documentation/articles/sql-database-disaster-recovery-drills)
- [SQL Database documentation](https://azure.microsoft.com/documentation/services/sql-database/)
