<properties
	urlDisplayName="How to connect to an Azure SQL database using SQL Server Management Studio (SSMS)"
	pageTitle="How to connect to an Azure SQL database using SSMS | Microsoft Azure"
	metaKeywords=""
	description="Learn how to connect to an Azure SQL database using SSMS."
	metaCanonical=""
	services="sql-database"
	documentationCenter=""
	title="How to connect to an Azure SQL database using SSMS"
	authors="sidneyh" solutions=""
	manager="jhubbard" editor="" />

<tags
	ms.service="sql-database"
	ms.date="09/14/2015"
	wacn.date="" />

# Connect with SQL Server Management Studio (SSMS)

Use the following steps to connect and query your SQL database using SQL Server Management Studio (SSMS).

## Prerequisites

* SQL Server Management Studio (SSMS) - To download the latest version of SSMS, see [Download SQL Server Management Studio](https://msdn.microsoft.com/zh-cn/library/mt238290.aspx).
* An SQL Database AdventureWorks sample database as described in [Getting Started with Microsoft Azure SQL Database](/documentation/articles/sql-database-get-started).


## Get your fully qualified Azure SQL server name

To connect to your database you need the full name  of the server (***servername**.database.windows.net*) that contains the database you want to connect to.

1. Go to the [Azure preview portal](https://portal.azure.com).
2. Browse to the database you want to connect to.
3. Locate the full server name:

    ![fully qualified server name][6]

    Use the fully qualified server name in step 3 below.



## Connect to your SQL Database

1. Open SSMS.
2. Click **Connect** > **Database Engine...**

    ![Connect > Database Engine][7]

2. In the **Connect to Server** dialog box, in the **Server name** box, type the server name in the format *&lt;servername>*.**database.windows.net**.
3. In the **Authentication** list, select **SQL Server Authentication**.
4. Enter the **Login** and **Password** you specified when you created your SQL Database server, and click **Connect**.

	![Connect to server dialog][2]



### If the connection fails
Make sure that the firewall of the logical server you have created allows connections from your local computer. For more information, see [How to: Configure Firewall Settings on SQL Database](https://msdn.microsoft.com/library/azure/jj553530.aspx).

## Run sample queries

1. In **Object Explorer**, navigate to the **AdventureWorks** database.
2. Right-click the database and then select **New Query**.

	![New query][4]

3. In the query window, copy and paste the following code:

		SELECT
		CustomerId
		,Title
		,FirstName
		,LastName
		,CompanyName
		FROM SalesLT.Customer;

4. Click the **Execute** button.  The following screen shot shows a successful query.

	![Sucess][5]




## Next steps
You can use Transact-SQL statements to create or manage databases. For more information see [CREATE DATABASE (Azure SQL Database)](https://msdn.microsoft.com/zh-cn/library/dn268335.aspx) and [Managing Azure SQL Database using SQL Server Management Studio](/documentation/articles/sql-database-manage-azure-ssms). You can also log events to Azure storage. See [Get started with SQL database auditing](/documentation/articles/sql-database-auditing-get-started) for more information.

<!--Image references-->

[1]:./media/sql-database-connect-to-database/1-download.png
[2]:./media/sql-database-connect-to-database/2-connect.png
[3]:./media/sql-database-connect-to-database/3-connect-to-database.png
[4]:./media/sql-database-connect-to-database/4-run-query.png
[5]:./media/sql-database-connect-to-database/5-success.png
[6]:./media/sql-database-connect-to-database/server-name.png
[7]:./media/sql-database-connect-to-database/connect-dbengine.png
