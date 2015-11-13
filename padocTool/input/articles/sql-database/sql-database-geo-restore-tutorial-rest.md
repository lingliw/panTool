<properties 
   pageTitle="Recover an Azure SQL database using Geo-Restore with REST API" 
   description="Geo-Restore, Microsoft Azure SQL Database, restore database, recover database, REST API" 
   services="sql-database" 
   documentationCenter="" 
   authors="elfisher" 
   manager="jeffreyg" 
   editor="v-romcal"/>

<tags
   ms.service="sql-database"
   ms.date="07/24/2015"
   wacn.date=""/>

# Recover an Azure SQL database using Geo-Restore with REST API

> [AZURE.SELECTOR]
- [Geo-Restore - portal](/documentation/articles/sql-database-geo-restore-tutorial-management-portal)
- [Geo-Restore - PowerShell](/documentation/articles/sql-database-geo-restore-tutorial-powershell)

## Overview

This guide shows you how to recover an Azure SQL database using REST API. Links to more detailed operations are provided. Geo-Restore is the core disaster recovery protection included for all Basic, Standard, and Premium Azure SQL Databases service tiers.

## Restrictions and Security

See [Recover an Azure SQL Database using Geo-Restore in the Azure portal](/documentation/articles/sql-database-geo-restore-tutorial-management-portal).

## How to: Recover an Azure SQL database using REST API

1.	Get your list of recoverable databases using the [List Recoverable Databases](http://msdn.microsoft.com/zh-cn/library/azure/dn800984.aspx) operation.
	
2.	Get the database you want to recover using the [Get Recoverable Database](http://msdn.microsoft.com/zh-cn/library/azure/dn800985.aspx) operation.
	
3.	Create the recovery request using the [Create Database Recovery Request](http://msdn.microsoft.com/zh-cn/library/azure/dn800986.aspx) operation.
	
4.	Track the status of the recovery using the [Database Operation Status](http://msdn.microsoft.com/zh-cn/library/azure/dn720371.aspx) operation.

## Next steps

For more information, see the following:

[Restore an Azure SQL database using Point in Time Restore in the Azure portal](/documentation/articles/sql-database-point-in-time-restore-tutorial-management-portal)

[Restore a deleted Azure SQL database in the Azure portal](/documentation/articles/sql-database-restore-deleted-database-tutorial-management-portal)

[Azure SQL Database Business Continuity](http://msdn.microsoft.com/zh-cn/library/azure/hh852669.aspx)

[Azure SQL Database Backup and Restore](http://msdn.microsoft.com/zh-cn/library/azure/jj650016.aspx)

[Azure SQL Database Geo-Restore (blog)](http://azure.microsoft.com/blog/2014/09/13/azure-sql-database-geo-restore/)

[Service Management REST API Reference](https://msdn.microsoft.com/zh-cn/library/azure/ee460799.aspx)
