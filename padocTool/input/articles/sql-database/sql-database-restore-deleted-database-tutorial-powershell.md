<properties 
   pageTitle="Restore a deleted Azure SQL database in Azure PowerShell" 
   description="Microsoft Azure SQL Database, restore deleted database, recover deleted database, Azure PowerShell" 
   services="sql-database" 
   documentationCenter="" 
   authors="elfisher" 
   manager="jeffreyg" 
   editor="v-romcal"/>

<tags
   ms.service="sql-database"
   ms.date="07/24/2015"
   wacn.date=""/>

# Restore a deleted Azure SQL database in Azure PowerShell

> [AZURE.SELECTOR]
- [Restore deleted database - portal](/documentation/articles/sql-database-restore-deleted-database-tutorial-management-portal)
- [Restore deleted database - REST API](/documentation/articles/sql-database-restore-deleted-database-tutorial-rest)

## Overview

This tutorial shows you how to restore a deleted Azure SQL database in [Azure PowerShell](/documentation/articles/install-configure-powershell). You can restore a database that was deleted during its retention period to the point at which it was deleted. The retention period is determined by the service tier of the database.

Restoring a deleted Azure SQL database creates a new database. The service automatically selects the service tier based on the backup used at the restore point. Make sure you have available quota on the logical server to create another database. If you'd like to request an increased quota, contact [Azure Support](/support/contact/).

## Restrictions and Security

See [Restore a deleted Azure SQL database in the Azure portal](/documentation/articles/sql-database-restore-deleted-database-tutorial-management-portal).

## How to: Restore a deleted Azure SQL database in Azure PowerShell

<!--<iframe src="http://channel9.msdn.com/Blogs/Windows-Azure/Restore-a-Deleted-SQL-Database-With-Microsoft-Azure-PowerShell/player" width="960" height="540" allowFullScreen frameBorder="0"></iframe>-->

You must use certificate based authentication to run the following cmdlets. For more information, see the *Use the certificate method* section in [How to install and configure Azure PowerShell](/documentation/articles/powershell-install-configure#use-the-certificate-method).

1. Get the list of recoverable databases by using the [Get-AzureSqlDatabase](http://msdn.microsoft.com/zh-cn/library/azure/dn546735.aspx) cmdlet.
	* Use the **RestorableDropped** switch and specify the **ServerName** of the server from which the database was deleted.
	* Running the following command stores the results in a variable called **$RecoverableDBs**.
	
	`PS C:\>$RecoverableDBs = Get-AzureSqlDatabase -ServerName "myserver" –RestorableDropped`

2. Choose the deleted database you want to restore from the list of deleted databases.

	* Type the deleted database number from the **$RecoverableDBs** list.  

	`PS C:\>$Database = $RecoverableDBs[<deleted database number>]`

	* For more information about how to get a restorable dropped database object, see [Get-AzureSqlDatabase](http://msdn.microsoft.com/zh-cn/library/dn546735.aspx).

3. Begin the restore by using the [Start-AzureSqlDatabaseRestore](http://msdn.microsoft.com/zh-cn/library/azure/dn720218.aspx) cmdlet. Specify the following parameters:	
	* **SourceRestorableDroppedDatabase**
	* **TargetDatabaseName** of the database you are restoring to.

	Store what is returned to a variable called **$RestoreRequest**. This variable contains the restore request ID which is used for monitoring the status of a restore.
	
	`PS C:\>$RestoreRequest = Start-AzureSqlDatabaseRestore -SourceRestorableDroppedDatabase $Database –TargetDatabaseName “myrestoredDB”`

A restore may take some time to complete. To monitor the status of the restore, use the [Get-AzureSqlDatabaseOperation](http://msdn.microsoft.com/zh-cn/library/azure/dn546738.aspx) cmdlet and specify the following parameters:

* **ServerName** of the database you are restoring to.
* **OperationGuid** which is the Restore Request ID that was stored in the **$RestoreRequest** variable in Step 3.

	`PS C:\>Get-AzureSqlDatabaseOperation –ServerName "myserver" –OperationGuid $RestoreRequest.RequestID`

The **State** and **PercentComplete** fields show the status of the restore.

## Next steps

For more information, see the following:

[Azure SQL Database Business Continuity](http://msdn.microsoft.com/zh-cn/library/azure/hh852669.aspx)

[Azure SQL Database Backup and Restore](http://msdn.microsoft.com/zh-cn/library/azure/jj650016.aspx)

[Azure PowerShell](http://msdn.microsoft.com/zh-cn/library/azure/jj156055.aspx)