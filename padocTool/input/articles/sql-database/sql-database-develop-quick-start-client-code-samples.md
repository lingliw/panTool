<properties 
	pageTitle="Client quick start code samples to SQL Database | Windows Azure" 
	description="Provides code samples and drivers for Node.js on Linux, Python on Mac OS, Java and Windows, Enterprise Library, and many more all for Azure SQL Database clients."
	services="sql-database" 
	documentationCenter="" 
	authors="MightyPen" 
	manager="jeffreyg" 
	editor=""/>


<tags 
	ms.service="sql-database" 
	ms.date="08/04/2015" 
	wacn.date=""/>


# Client quick-start code samples to SQL Database


This topic provides links to quick-start code samples you can use to connect to Azure SQL Database:


- Short samples connect and query.
- Retry samples connect and query, but automatically retry if an encountered error is classified as a [*transient fault*](/documentation/articles/sql-database-develop-error-messages#bkmk_connection_errors) (such as a connection timeout).


The samples cover:


- A variety of programming languages.
- Windows, Linux, and Mac OS as the operating systems that your client program can run on.
- Links for downloads to any necessary connection drivers.
- Short quick start code samples.
- Longer samples that contain transient fault handling in the form of automated retry logic.
- Code samples that convert relational result sets into an object  oriented format.


> [AZURE.NOTE] Code samples for more languages are being prepared, and links to them will be added to this topic.


## Clients on Linux


This section provides links to code sample topics for client programs that run on Linux.


| Language | Short sample | Retry sample | Relational to object |
| :-- | :-- | :-- | :-- |
| Node.js | [Tedious](/documentation/articles/sql-database-develop-nodejs-simple-linux) | . | . |
| Python | [FreeTDS, pymssql](/documentation/articles/sql-database-develop-python-simple-unbutu-linux) | . | . |
| Ruby | [FreeTDS, TinyTDS](/documentation/articles/sql-database-develop-ruby-simple-linux) | . | . |


## Clients on Mac OS


This section provides links to code sample topics for client programs that run on Mac OS.


| Language | Short sample | Retry sample | Relational to object |
| :-- | :-- | :-- | :-- |
| Python | [pymssql](/documentation/articles/sql-database-develop-python-simple-mac-osx) | . | . |
| Ruby | [Homebrew<br/>FreeTDS, TinyTDS](/documentation/articles/sql-database-develop-ruby-simple-mac-osx) | . | . |


## Clients on Windows


This section provides links to code sample topics for client programs that run on Windows.


| Language | Short sample | Retry sample | Relational to object |
| :-- | :-- | :-- | :-- |
| C# | [ADO.NET](/documentation/articles/sql-database-develop-dotnet-simple) | [ADO.NET custom](/documentation/articles/sql-database-develop-csharp-retry-windows)<br/><br/>[Enterprise Library](/documentation/articles/sql-database-develop-entlib-csharp-retry-windows) | (Entity Framework) |
| C++ | [ODBC driver](http://msdn.microsoft.com/zh-cn/library/azure/hh974312.aspx) | . | . |
| Java | [Java. JDBC, JDK. Insert, Transaction, Select.](/documentation/articles/sql-database-develop-java-simple-windows)<br/><br/>[Java. Eclipse](/documentation/articles/sql-data-java-how-to-use-sql-database)<br/><br/>[Java. JDBC](http://msdn.microsoft.com/zh-cn/library/azure/gg715284.aspx) | . | . |
| Node.js | [msnodesql](/documentation/articles/sql-database-develop-nodejs-simple-windows) | . | . |
| PHP | [ODBC](/documentation/articles/sql-database-develop-php-simple-windows) | [ODBC custom](/documentation/articles/sql-database-develop-php-retry-windows) | . |
| Python | [pymssql](/documentation/articles/sql-database-develop-python-simple-windows) | . | . |


## See also


- [Downloads for SDKs and tools, for numerous languages and platforms](http://azure.microsoft.com/ZH-CN/downloads/#cmd-line-tools)
- [Connection Libraries for SQL Database and SQL Server](/documentation/articles/sql-database-libraries)
- [List of numeric codes for transient errors](/documentation/articles/sql-database-develop-error-messages#bkmk_connection_errors)<br/>&nbsp;
- [Azure SQL Database Development: How-to Topics](https://msdn.microsoft.com/zh-CN/library/azure/ee621787.aspx)
- [Connecting to SQL Database: Links, Best Practices and Design Guidelines](/documentation/articles/sql-database-connect-central-recommendations)
- [Create your first Azure SQL Database](/documentation/articles/sql-database-get-started)


