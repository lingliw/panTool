<properties
	pageTitle="What's new in SQL Database V12"
	description="Describes the latest features that have been added to Azure SQL Database."
	services="sql-database"
	documentationCenter=""
	authors="MightyPen"
	manager="jeffreyg"
	editor=""/>

<tags
	ms.service="sql-database"  
	ms.date="04/28/2015"
	wacn.date=""/>


# What's new in SQL Database V12




Azure SQL Database version V12 ([at preview in some regions](sql-database-preview-whats-new#V12AzureSqlDbPreviewGaTable)) now provides nearly complete compatibility with the Microsoft SQL Server engine. The recent enhancements help to streamline SQL Server application migrations to SQL Database, and they help your system robustly process heavier database workloads.


[Sign up](https://manage.windowsazure.cn) for SQL Database to then [get started](sql-database-get-started) with this new generation on Windows Azure. You first need a subscription to Windows Azure. You can sign up for a [Azure trial](/pricing/1rmb-trial) and review [pricing](/home/features/sql-database/#price) information.


Your path to planning and upgrading your earlier version databases to V12 starts at [Plan and prepare to upgrade to SQL Database V12](sql-database-preview-plan-prepare-upgrade).


## Highlights


- **Azure portal** is [available](http://manage.windowsazure.cn/) to create SQL Database databases and servers at version V12, or optionally at the earlier version. In the Azure portal you specify your SQL Database database and then proceed to specify a SQL Database server to host it.


- **Choose a version** of SQL Database server when you use the Azure preview portal to create a new database. The default is V12, but you can choose the earlier version of the SQL Database server.


- **Security** enjoys the new feature of [users in contained databases](sql-database-preview-whats-new#UsersInContainedDatabases). Two other features are [row-level security](sql-database-preview-whats-new#RowLevelSecurity) and [dynamic data masking](sql-database-preview-whats-new#DynamicDataMasking), although these are still at preview and are not yet at GA.


- **Easier management** of large databases to support heavier workloads with parallel queries (Premium only), [table partitioning](http://msdn.microsoft.com/zh-cn/library/ms187802.aspx), [online indexing](http://msdn.microsoft.com/zh-cn/library/ms188388.aspx), worry-free large index rebuilds with 2GB size limit removed, and more options on the [ALTER DATABASE](http://msdn.microsoft.com/zh-cn/library/bb522682.aspx) command.


- **Support for key programmability functions** to drive more robust application design with [CLR integration](http://msdn.microsoft.com/zh-cn/library/ms189524.aspx), Transact-SQL [window functions](http://msdn.microsoft.com/zh-cn/library/ms189461.aspx), [XML indexes](http://msdn.microsoft.com/zh-cn/library/bb934097.aspx), and [change tracking](http://msdn.microsoft.com/zh-cn/library/bb933875.aspx) for data.


- **Breakthrough performance** with support for in-memory [columnstore index](http://msdn.microsoft.com/zh-cn/library/gg492153.aspx) queries (Premium tier only) for data mart and smaller analytic workloads.


- **Monitoring and troubleshooting** are improved with visibility into over 100 new table views in an expanded set of Database Management Views ([DMVs](http://msdn.microsoft.com/zh-cn/library/ms188754.aspx))


- **New S3 performance level in the Standard tier:** offers more [pricing](sql-database-upgrade-new-service-tiers) flexibility between Standard and Premium. S3 will deliver more DTUs (database throughput units) and all the features available in the Standard tier.


## V12 enhancements


### Expanded database management


| Feature | Description |
| :--- | :--- |
| . | ***December 2014:*** |
| <a name="UsersInContainedDatabases" id="UsersInContainedDatabases"></a>Users in contained databases | You can now create users in your contained database without having a corresponding login in the master database. This makes it much simpler to move your database to another server. The connection code in your client applications is the same whether you use contained database users or not.<br/><br/>Use of this feature is an excellent way to benefit from higher guaranteed service level agreements.<br/><br/>We generally encourage you to consider using this feature. However, you might have specific scenarios that make the traditional *login+user* pair the better choice for you at this time.<br/><br/>For more information, see:<br/>- [Azure SQL Database Security Guidelines and Limitations](http://msdn.microsoft.com/zh-cn/library/azure/ff394108.aspx)<br/>- [Managing Databases and Logins in Azure SQL Database](http://msdn.microsoft.com/zh-cn/library/azure/ee336235.aspx)<br/>- [Contained Databases](http://msdn.microsoft.com/zh-cn/library/azure/ff929071.aspx) |
| Table partitioning | Previous limitations on [table partitioning](http://msdn.microsoft.com/zh-cn/library/ms190787.aspx) are eliminated. |
| Larger transactions | With V12 you are no longer limited to a maximum of 2 GB of data modifications in a single transaction. <br/><br/> One benefit is that rebuilding a large index is no longer limited by 2 GB transaction size limit. For general information, see [Azure SQL Database Resource Limits](http://msdn.microsoft.com/zh-cn/library/azure/dn338081.aspx). |
| Online index build and rebuild | Before V12, Azure SQL Database generally supported the (ONLINE=ON) clause of the [ALTER INDEX](http://msdn.microsoft.com/zh-cn/library/ms188388.aspx) command, but this was not supported for indexes on a BLOB type column. Now V12 does support (ONLINE=ON) even for indexes on BLOB columns.<br/><br/> The ONLINE feature enables queries to benefit from an index even while the index is being rebuilt. |
| CHECKPOINT support | With V12 you can issue the Transact-SQL [CHECKPOINT](http://msdn.microsoft.com/zh-cn/library/ms188748.aspx) command for your database. |
| ALTER TABLE enhancement | Allows many alter column actions to be performed while the table remains available. For more information, see [ALTER TABLE (Transact-SQL)](http://msdn.microsoft.com/zh-cn/library/ms190273.aspx) |
| TRUNCATE TABLE enhancement | Allows truncation of specific partitions. For more information, see [TRUNCATE TABLE (Transact-SQL)](http://msdn.microsoft.com/zh-cn/library/ms177570.aspx). |
| More options on ALTER DATABASE | V12 supports more of the options that are available on the [ALTER DATABASE](http://msdn.microsoft.com/zh-cn/library/ms174269.aspx) command. <br/><br/> For more information, see [Azure SQL Database Transact-SQL Reference](http://msdn.microsoft.com/zh-cn/library/azure/ee336281.aspx). |
| More DBCC commands | Several more [DBCC](http://msdn.microsoft.com/zh-cn/library/ms188796.aspx) commands are now available in V12. For details see [Azure SQL Database Transact-SQL Reference](http://msdn.microsoft.com/zh-cn/library/azure/ee336281.aspx). |


### Programming and application support


| Feature | Description |
| :--- | :--- |
| . | ***February 2015:*** |
| <a name="DynamicDataMasking" id="DynamicDataMasking"></a> Dynamic data masking preview | When a rowset is generated from a query, an established data masking policy can replace parts of the data with 'X' characters to overlay and protect sensitive information. After the masking operation completes, the modified rowset is sent to the client.<br/><br/>One example use might be to mask all but the last few digits of a credit card number.<br/><br/>**NOTE:** This feature is at the preview status, and has not yet been announced for general availability for production use.<br/><br/>For detailed information, see [Get started with Azure SQL Database Dynamic Data Masking](sql-database-dynamic-data-masking-get-started). |
| . | ***January 2015:*** |
| <a name="RowLevelSecurity" id="RowLevelSecurity"></a> Row-level security (RLS) preview | **Caution:** The RLS feature is presently at *preview* status only, even in geographic regions where V12 is in general availability (GA) status. Until RLS is in GA status, RLS is not yet appropriate for use in a business critical production database.<br/><br/>The new [CREATE SECURITY POLICY](http://msdn.microsoft.com/zh-cn/library/dn765135.aspx) command in Transact-SQL enables you to implement RLS. RLS causes the database server to add conditions which filter out some data rows before a rowset is returned to the caller.<br/><br/>In the industry, RLS is sometimes also called fine-grained access control.<br/><br/>For a code example and more, see [Row-Level Security Preview](http://msdn.microsoft.com/zh-cn/library/7221fa4e-ca4a-4d5c-9f93-1b8a4af7b9e8.aspx). |
| . | ***December 2014:*** |
| Window functions in Transact-SQL queries | The ANSI window functions are access with the [OVER clause](http://msdn.microsoft.com/zh-cn/library/ms189461.aspx). <br/><br/> Itzik Ben-Gan has an excellent [blog post](http://sqlmag.com/sql-server-2012/how-use-microsoft-sql-server-2012s-window-functions-part-1) that further explains window functions and the OVER clause. |
| .NET CLR integration | The CLR (common language runtime) of the .NET Framework is integrated into V12. <br/><br/> Only SAFE assemblies that are fully compiled to binary code are supported. For details see [CLR Integration Programming Model Restrictions](http://msdn.microsoft.com/zh-cn/library/ms403273.aspx). <br/><br/> You can find information about this feature in the following topics: <br/> * [Introduction to SQL Server CLR Integration](http://msdn.microsoft.com/zh-cn/library/ms254498.aspx) <br/> * [CREATE ASSEMBLY (Transact-SQL)](http://msdn.microsoft.com/zh-cn/library/ms189524.aspx). |
| Change tracking for data | Change tracking for data can now be configured at the database or table level. <br/><br/> For information about change tracking, see [About Change Tracking (SQL Server)](http://msdn.microsoft.com/zh-cn/library/bb933875.aspx). |
| XML indexes | V12 enables you use the Transact-SQL commands [CREATE XML INDEX](http://msdn.microsoft.com/zh-cn/library/bb934097.aspx) and [CREATE SELECTIVE XML INDEX](http://msdn.microsoft.com/zh-cn/library/jj670104.aspx). |
| Table as a heap | V12 enables you to create a table that has no clustered index. <br/><br/> This feature is especially helpful for its support of the Transact-SQL [SELECT...INTO](http://msdn.microsoft.com/zh-cn/library/ms188029.aspx) command which creates a table from a query result. |
| Application roles | For security and permissions control, V12 enables you to issue [GRANT](http://msdn.microsoft.com/zh-cn/library/ms187965.aspx) - [DENY](http://msdn.microsoft.com/zh-cn/library/ms188338.aspx) - [REVOKE](http://msdn.microsoft.com/zh-cn/library/ms187728.aspx) commands against [application roles](http://msdn.microsoft.com/zh-cn/library/ms190998.aspx). |


### Better customer insights


| Feature | Description |
| :--- | :--- |
| . | ***December 2014:*** |
| DMVs (dynamic management views) | Several DMVs are added in V12. For details see [Azure SQL Database Transact-SQL Reference](http://msdn.microsoft.com/zh-cn/library/azure/ee336281.aspx). |
| Change tracking | V12 fully supports change tracking. <br/><br/> For details of this feature see [Enable and Disable Change Tracking (SQL Server)](http://msdn.microsoft.com/zh-cn/library/bb964713.aspx). |
| Columnstore indexes | A columnstore index improves system performance for data warehouses when an indexed column contains repetitions of the same value. The [columnstore index compresses](http://msdn.microsoft.com/zh-cn/library/gg492088.aspx) the duplicate values to reduce the number of physical rows that must be accessed during queries. |


### Performance improvements at the Premium service tier


These performance enhancements apply to the P2 and P3 levels within the Premium service tier.


| Feature | Description |
| :--- | :--- |
| . | ***December 2014:*** |
| Parallel processing for queries | V12 provides a higher degree of parallelism for queries that can benefit from it. |
| Briefer I/O latency | V12 has significantly briefer latency for input/output operations. |
| Increased IOPS | V12 can process a larger quantity of input/output per second (IOPS). |
| Log rate | V12 can log more data changes per second. |


| Feature | Description |  
| :--- | :--- |  
| . | ***August 2015:*** |
| Create server using REST or PowerShell |  When you create a server without specifying a server version, the default version will change from V11 to V12.<br/><br/>This aligns with the [Azure portal](http://manage.windowsazure.cn). |  
| Create database using Transact-SQL, REST, or PowerShell | On V11 servers, when you create a new database without specifying an edition or service objective, the default service objective will be S0 instead of Web-and-Business. This aligns with V12 servers in the Azure preview portal. |  


### Summary of enhancements


V12 elevates our SQL Database close to full feature compatibility with our SQL Server product. V12 focuses on the most popular features, and on programmability support. This makes your development more efficient and more enjoyable.  It is now even easier to move your SQL database applications to the cloud.


And at the Premium tier V12 brings major performance improvements. Some applications will see extreme gains in query speed. Applications with heavy workloads will see reliably robust throughput.


## <a name="V12AzureSqlDbPreviewGaTable"></a>V12 general availability (GA) status per region


> [AZURE.NOTE]
> [Pricing](/home/features/sql-database/#price) during the preview has been at a discount. Pricing returns to the GA level for all regions on Tuesday, March 31, 2015.


For any region that has reached GA, all new subscriptions and their subsequent databases use the V12 service architecture and therefore have access to the latest features. The present article lists the new features brought by V12.


At GA, if you have pre-V12 servers and databases, you can elect to upgrade (or move) your databases to the V12 service architecture. Then you can use the new features for production. V12 databases must be at the basic, standard, or premium [pricing tier](sql-database-upgrade-new-service-tiers).


## How to proceed


You can learn how to upgrade your databases from Azure SQL Database V11 to V12 at [Plan and Prepare to Upgrade to the Latest Azure SQL Database Update Preview](sql-database-preview-plan-prepare-upgrade).


Version numbers like V12 refer to the value returned by the following Transact-SQL statement:<br/>
**SELECT @@version;**


- 11.0.9228.18 *(V11)*
- 12.0.2000.8 *(or a bit higher, V12)*


For the latest pricing details about V12 see [SQL Database Pricing](/home/features/sql-database/#price).


## Cautions for the V12 preview


There are important things to know about limitations during and after an upgrade of your V11 database to V12. You can read the details at this link to a [midpoint](sql-database-preview-plan-prepare-upgrade#limitations) in the *Plan and prepare to upgrade to SQL Database V12* topic.


[V12 general availability (GA) status per region]:#V12AzureSqlDbPreviewGaTable


<!-- EndOfFile -->
