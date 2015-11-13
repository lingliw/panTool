<properties
   pageTitle="Finalize your recovered Azure SQL Database"
   description="Point in Time Restore, Microsoft Azure SQL Database, restore database, recover database, Azure Management Portal, Azure portal"
   services="sql-database"
   documentationCenter=""
   authors="elfisher"
   manager="jeffreyg"
   editor=""/>

<tags
   ms.service="sql-database"
   ms.date="07/30/2015"
   wacn.date=""/>

# Finalize your recovered Azure SQL Database

## Overview

This article provides a checklist of tasks that you need to go through before putting a newly recovered Azure SQL Database back into production. This checklist applies to databases recovered from Geo-Replication failover, Deleted Database Restore, Point-in-Time Restore, or Geo-Restore.

## Update Connection Strings

Verify connection strings of your application are pointing to the newly recovered database. Update your connection strings if one of the below situations applies:

  + The recovered database uses a different name from the source database name
  + The recovered database is on a different server from the source server

For more information about changing connection strings, see [Guidelines for Connecting to Azure SQL Database Programmatically](https://msdn.microsoft.com/zh-CN/library/azure/ee336282.aspx) and [Connections to Azure SQL Database: Central Recommendations ](/documentation/articles/sql-database-connect-central-recommendations).
 
## Modify Firewall Rules
Verify the firewall rules at server-level and database-level, and make sure connections from your client computers or Azure to the server and the newly recovered database are enabled. For more information, see [Azure SQL Database Firewall](https://msdn.microsoft.com/zh-CN/library/azure/ee621782.aspx) and [How to: Configure Firewall Settings (Azure SQL Database)](https://msdn.microsoft.com/zh-CN/library/azure/jj553530.aspx).

## Verify Server Logins and Database Users

Verify if all the logins used by your application exist on the server which is hosting your recovered database. Re-create the missing logins and grant them appropriate permissions on the recovered database. For more information, see [Managing Databases and Logins in Azure SQL Database](https://msdn.microsoft.com/zh-CN/library/azure/ee336235.aspx).

Verify if each database users in the recovered database is associated with a valid server login. Use ALTER USER statement to map user to valid server login. For more information, see [ALTER USER](http://technet.microsoft.com/zh-CN/library/ms176060(v=sql.120).aspx). 


## Setup Telemetry Alerts

Verify if your existing alert rule settings are map to your recovered database. Update the setting if one of below situations applies:

  + The recovered database uses a different name from the source database name
  + The recovered database is on a different server from the source server

For more information about database alert rules, see [How to: Receive Alert Notifications and Manage Alert Rules in Azure](https://msdn.microsoft.com/zh-CN/library/azure/dn306638.aspx).


## Enable Auditing

If auditing is required to access your database, you need to enable Auditing after the database recovery. A good indicator of auditing is required is that client applications use secure connection strings in a pattern of *.database.secure.chinacloudapi.cn. For more information, see [Get started with SQL database auditing](/documentation/articles/sql-database-auditing-get-started). 
