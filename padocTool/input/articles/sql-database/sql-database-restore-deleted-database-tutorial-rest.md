<properties 
   pageTitle="Restore a deleted Azure SQL database with REST API" 
   description="Microsoft Azure SQL Database, restore deleted database, recover deleted database, REST API" 
   services="sql-database" 
   documentationCenter="" 
   authors="elfisher" 
   manager="jeffreyg" 
   editor="v-romcal"/>

<tags
   ms.service="sql-database"
   ms.date="07/24/2015"
   wacn.date=""/>

# Restore a deleted Azure SQL database with REST API

> [AZURE.SELECTOR]
- [Restore deleted database - portal](/documentation/articles/sql-database-restore-deleted-database-tutorial-management-portal)
- [Restore deleted database - PowerShell](/documentation/articles/sql-database-restore-deleted-database-tutorial-powershell) 

## Overview

This guide shows you how to restore a deleted Azure SQL database with REST API. Links to more detailed operations are provided.

Restoring a deleted Azure SQL database creates a new database. The service automatically selects the service tier based on the backup used at the restore point. Make sure you have available quota on the logical server to create another database. If you'd like to request an increased quota, contact [Azure Support](/support/contact/).

## Restrictions and Security

See [Restore a deleted Azure SQL database in the Azure portal](/documentation/articles/sql-database-restore-deleted-database-tutorial-management-portal/).

## How to: Restore a deleted Azure SQL database using REST API

1.	List all of your restorable deleted databases by using the [List Restorable Dropped Databases](https://msdn.microsoft.com/zh-cn/library/azure/dn509562.aspx) operation.
	
2.	Get the details for the deleted database you want to restore by using the [Get Restorable Dropped Database](http://msdn.microsoft.com/zh-cn/library/azure/dn509574.aspx) operation.

3.	Begin your restore by using the [Create Database Restore Request](http://msdn.microsoft.com/zh-cn/library/azure/dn509571.aspx) operation.
	
4.	Track the status of your restore by using the [Database Operation Status](http://msdn.microsoft.com/zh-cn/library/azure/dn720371.aspx) operation.

## Next steps

For more information, see the following:

[Azure SQL Database Business Continuity](http://msdn.microsoft.com/zh-cn/library/azure/hh852669.aspx)

[Azure SQL Database Backup and Restore](http://msdn.microsoft.com/zh-cn/library/azure/jj650016.aspx)

[Service Management REST API Reference](http://msdn.microsoft.com/zh-cn/library/azure/ee460799.aspx)