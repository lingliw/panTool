<properties 
	pageTitle="Create and Deploy a PHP-MySQL web app in Azure Websites using WebMatrix" 
	description="A tutorial that demonstrates how to use the free WebMatrix IDE to create and deploy a PHP web app in Azure Websites that stores data in MySQL."
	tags="azure-portal" 
	services="app-service\web" 
	documentationCenter="php" 
	authors="tfitzmac" 
	manager="wpickett" 
	editor="mollybos"/>

<tags 
	ms.service="app-service-web" 
	ms.date="07/07/2015" 
	wacn.date=""/>





# Create and Deploy a PHP-MySQL web app in Azure Websites using WebMatrix

This tutorial shows you how to use WebMatrix to develop and deploy a PHP-MySQL application to [Azure Websites](/documentation/services/web-sites/) Web Apps. WebMatrix is a free web development tool from Microsoft that includes everything you need for website development. WebMatrix supports PHP and includes intellisense for PHP development.

This tutorial assumes you have [MySQL][install-mysql] installed on your computer so that you can test an application locally. However, you can complete the tutorial without having MySQL installed. Instead, you can deploy your application directly to Azure Websites.

Upon completing this guide, you will have a PHP-MySQL website running in Web Apps.
 
You will learn:

* How to create a website in Azure Websites and a MySQL database using the [Azure Management Portal](https://manage.windowsazure.cn/). Because PHP is enabled in Web Apps by default, nothing special is required to run your PHP code.
* How to develop a PHP application using WebMatrix.
* How to publish and re-publish your application to Web Apps using WebMatrix.
 
By following this tutorial, you will build a simple Tasklist web application in PHP. The application will be hosted in Azure Websites. A screenshot of the running application is below:

![Azure PHP Web Site][running-app]

[AZURE.INCLUDE [create-account-and-websites-note](../includes/create-account-and-websites-note.md)]
<!-- deleted by customization
 -->
##Prerequisites

1. [Download][tasklist-mysql-download] the Tasklist application files. The Tasklist application is a simple PHP application that allows you to add, mark complete, and delete items from a task list. Task list items are stored in a MySQL database. The application consists of these files:

	* **additem.php**: Adds an item to the list.
	* **createtable.php**: Creates the MySQL table for the application. This file will only be called once.
	* **deleteitem.php**: Deletes an item.
	* **getitems.php**: Gets all items in the database.
	* **index.php**: Displays tasks and provides a form for adding an item to the list.
	* **markitemcomplete.php**: Changes the status of an item to complete.
	* **taskmodel.php**: Contains functions that add, get, update, and delete items from the database.

1. Create a local MySQL database called `tasklist`. You can do this either from the Database workspace in WebMatrix (after it is installed below in the tutorial) or from the MySQL command prompt with this command:

		mysql> create database tasklist;

	This step is only necessary if you want to test your application locally.

## Create a web app and MySQL database

Follow these steps to create a web app and a MySQL database:
<!-- keep by customization: begin -->
1. Login to the [Management Portal][Azure-portal].
1. Click the **+ New** icon on the bottom left of the portal.

	![Create New Azure  Website][New Website1]

1. Click ** Website**, then **CUSTOM CREATE**.

	![Custom Create a new  Website][New Website2]

	> [AZURE.NOTE]
	> You cannot create a MySQL Database for a website after creating the website. You must create a website and a MySQL database as described in the steps below.

1. Enter a value for **URL**, select **Create a New MySQL Database** from the **DATABASE** dropdown,  and select the data center for your  Website in the **REGION** dropdown. Click the arrow at the bottom of the dialog.

	![Fill in  Website details][New Website3]

5. Enter a value for the **NAME** of your database, select the data center for your database in the **REGION** dropdown, and check the box that indicates you agree with the legal terms. Click the checkmark at the bottom of the dialog.

	![Create new MySQL database][New Website4]

	When the  Website has been created you will see the text **Creating  Website '[SITENAME]' succeeded**.

	Next, you need to get the MySQL connection information.


6. Click the name of the  Website displayed in the list of  Websites to open the  Website's Quick Start page.

	![Open  Website dashboard][New Website5]

7. Click the **CONFIGURE** tab:

	![Configure tab][New Website6]

8. Scroll down to the **connection strings** section. The values for `Database`, `Data Source`, `User Id`, and `Password` are (respectively) the database name, server name, user name, and user password. Make note of the database connection information as it will be needed later.

	![Connection string][ConnectionString]
<!-- keep by customization: end -->
## Create your application in WebMatrix

In the next few steps you will develop the Tasklist application by adding the files you downloaded earlier and making a few modifications. You could, however, add your own existing files or create new files.

1. Launch [Microsoft WebMatrix](http://www.microsoft.com/web/webmatrix/). If you haven't alreayd installed it yet, do it now.
2. If this is the first time you've used WebMatrix 3, you will be prompted to sign into Azure.  Otherwise, you can click on the **Sign In** button, and choose **Add Account**.  Choose to **Sign in** using your Microsoft Account.

	![Add Account](./media/web-sites-php-mysql-use-webmatrix/webmatrix-add-account.png)

3. If you have signed up for an Azure account, you may log in using your Microsoft Account:

	![Sign into Azure](./media/web-sites-php-mysql-use-webmatrix/webmatrix-sign-in.png)

1. On the start screen, click the **New** button, and choose **Template Gallery** to create a new site from the Template Gallery:

	![New site from Template Gallery](./media/web-sites-php-mysql-use-webmatrix/webmatrix-site-from-template.png)

4. From the available templates, choose **PHP**.

	![Site from template][site-from-template]

5. Select the **Empty Site** template. Provide a name for the site and click **NEXT**.

	![Provide name for site][site-from-template-2]

	Your site will be opened on WebMatrix with some default files in place.

	In the next few steps you will develop the Tasklist application by adding the files you downloaded earlier and making a few modifications. You could, however, add your own existing files or create new files.

6. Add your application files by clicking **Add Existing**:

	![WebMatrix - Add existing files][edit_addexisting]

	In the resulting dialog, navigate to the files you downloaded earlier, select all of them, and click Open. When prompted, choose to replace the `index.php` file. 

7. Next, you need to add your local MySQL database connection information to the `taskmodel.php` file. Open the  `taskmodel.php` file by double clicking it, and update the database connection information in the `connect` function. (**Note**: Jump to [Publish Your Application](#Publish) if you do not want to test your application locally and want to instead publish directly to Azure  Websites.)

		// DB connection info
		$host = "localhost";
		$user = "your user name";
		$pwd = "your password";
		$db = "tasklist";

	Save the `taskmodel.php` file.

8. For the application to run, the `items` table needs to be created. Right click the `createtable.php` file and select **Launch in browser**. This will launch `createtable.php` in your browser and execute code that creates the `items` table in the `tasklist` database.

	![WebMatrix - Launch createtable.php in browser][edit_run]

9. Now you can test the application locally. Right click the `index.php` file and select **Launch in browser**. Test the application by adding items, marking them complete, and deleting them.  


## Publish your application

Before publishing your application to Azure  Websites, the database connection information in `taskmodel.php` needs to be updated with the connection information you obtained earlier (in the [Create an Azure  Website and MySQL Database](#Create Website) section).

1. Open the `taskmodel.php` file by double clicking it, and update the database connection information in the `connect` function.

		// DB connection info
		$host = "value of Data Source";
		$user = "value of User Id";
		$pwd = "value of Password";
		$db = "value of Database";
	
	Save the `taskmodel.php` file.

2. Click **Publish** in WebMatrix.

	![WebMatrix - Publish][edit_publish]

3. Click **Choose an existing site from Windows Azure**.

3. Select the Azure Websites web app you created earlier.

	![](./media/web-sites-php-mysql-use-webmatrix/webmatrix-publish-existing-site-choose.png)

3. Keep clicking **Continue** until WebMatrix publishes the site to Azure Websites.

3. Navigate to http://[your web site name].chinacloudsites.cn/createtable.php to create the `items` table.

4. Lastly, navigate to http://[your  Website name].chinacloudsites.cn/index.php to use the application.
	
##Modify and republish your application

You can easily modify your application by editing the local copy of the site you downloaded earlier and republish or you can make the edit directly in the Remote mode. Here, you will make a simple change to the heading in in the `index.php` file and save it directly to the live site.

1. Click on the Remote tab of your site in WebMatrix and select **Open Remote View**. This will open your remote site for editing directly.
	 ![WebMatrix - Open Remote View][OpenRemoteView]
 
2. Open the `index.php` file by double-clicking it.
	![WebMatrix - Open index file][Remote_editIndex]

3. Change **My ToDo List** to **My Task List** in the **title** and **h1** tags and save the file.


4. When saving has completed, click the Run button to see the changes on the live site.
	![WebMatrix - Launch site in Remote][Remote_run]


## Next Steps

* [WebMatrix web site](http://www.microsoft.com/click/services/Redirect2.ashx?CR_CC=200106398)
<!-- deleted by customization
 -->
[install-mysql]: http://dev.mysql.com/doc/refman/5.6/en/installing.html
[running-app]: ./media/web-sites-php-mysql-use-webmatrix/tasklist_app_windows.png
[tasklist-mysql-download]: http://go.microsoft.com/fwlink/?LinkId=252506
[NewWebSite1]: ./media/web-sites-php-mysql-use-webmatrix/NewWebSite1.jpg
[NewWebSite2]: ./media/web-sites-php-mysql-use-webmatrix/NewWebSite2.png
[NewWebSite3]: ./media/web-sites-php-mysql-use-webmatrix/NewWebSite3.png
[NewWebSite4]: ./media/web-sites-php-mysql-use-webmatrix/NewWebSite4.png
[NewWebSite5]: ./media/web-sites-php-mysql-use-webmatrix/NewWebSite5.png
[NewWebSite6]: ./media/web-sites-php-mysql-use-webmatrix/NewWebSite6.png
[ConnectionString]: ./media/web-sites-php-mysql-use-webmatrix/ConnectionString.png
[InstallWebMatrix]: ./media/web-sites-php-mysql-use-webmatrix/InstallWebMatrix.png
[download-site]: ./media/web-sites-php-mysql-use-webmatrix/download-site-1.png
[site-from-template]: ./media/web-sites-php-mysql-use-webmatrix/site-from-template.png
[site-from-template-2]: ./media/web-sites-php-mysql-use-webmatrix/site-from-template-2.png
[edit_addexisting]: ./media/web-sites-php-mysql-use-webmatrix/edit_addexisting.png
[edit_run]: ./media/web-sites-php-mysql-use-webmatrix/edit_run.png
[edit_publish]: ./media/web-sites-php-mysql-use-webmatrix/edit_publish.png
[OpenRemoteView]: ./media/web-sites-php-mysql-use-webmatrix/OpenRemoteView.png
[Remote_editIndex]: ./media/web-sites-php-mysql-use-webmatrix/Remote_editIndex.png
[Remote_run]: ./media/web-sites-php-mysql-use-webmatrix/Remote_run.png













[Azure-portal]: https://manage.windowsazure.cn













