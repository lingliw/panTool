<properties 
	pageTitle="Back up a web app in Azure Websites" 
	description="Learn how to create backups of your web apps in Azure Websites." 
	services="app-service" 
	documentationCenter="" 
	authors="cephalin" 
	manager="wpickett" 
	editor="jimbe"/>

<tags
	ms.service="app-service"
	ms.date="09/16/2015"
	wacn.date=""/>

# Back up a web app in Azure Websites


The Backup and Restore feature in [Azure Websites](/documentation/services/web-sites/) lets you easily create web app backups manually or automatically. You can restore your web app to a previous state, or create a new web app based on one of your original app's backups. 

For information on restoring an Azure web app from backup, see [Restore a web app](/documentation/articles/web-sites-restore).
<!-- deleted by customization

[AZURE.INCLUDE [app-service-web-to-api-and-mobile](../includes/app-service-web-to-api-and-mobile.md)] 
-->
<!-- keep by customization: begin -->
##In this article

- [Automatic and Easy Backup (Video)](#video)
- [What Gets Backed Up](#whatsbackedup)
- [Requirements and Restrictions](#requirements)
- [To Create a Manual Backup](#manualbackup)
- [To Configure Automated Backups](#automatedbackups)
- [How Backups Are Stored](#aboutbackups)
- [Notes](#notes)
- [Next Steps](#nextsteps)
	- [More about storage accounts](#moreaboutstorage)
<!-- keep by customization: end -->

<a name="whatsbackedup"></a>
## What gets backed up 
Web Apps can back up the following information:

* Web app configuration
* Web app file content
* Any SQL Server or MySQL databases connected to your app (you can choose which ones to include in the backup)

This information is backed up to the Azure storage account and container that you specify. 

> [AZURE.NOTE] Each backup is a complete offline copy of your app, not an incremental update.

<a name="requirements"></a>
## Requirements and restrictions

* The Backup and Restore feature requires the site to be in Standard mode. For more information about scaling your webapp to use Standard mode, see [Scale a web app in Azure Websites](/documentation/articles/web-sites-scale). <!-- deleted by customization Note that Premium mode allows a greater number of daily backups to be performed over the Standard mode. -->

<!-- deleted by customization
* The Backup and Restore feature requires an Azure storage account and container that must belong to the same subscription as the web app that you are going to back up. If you do not yet have a storage account, you can create one by clicking the **Storage Account** in the **Backups** blade of the [Azure preview portal](http://manage.windowsazure.cn), and then choosing the **Storage Account** and the **Container** from the **Destination** blade. For more information on Azure storage accounts, see the [links](#moreaboutstorage) at the end of this article.

-->
<!-- keep by customization: begin -->
* The Backup and Restore feature requires an Azure storage account and container that must belong to the same subscription as the web app that you are going to back up. If you do not yet have a storage account, you can create one by clicking the **Storage** button (grid icon) in the left pane of the Azure Management Portal, and then choosing **New** in the command bar at the bottom. For more information on Azure storage accounts, see the [links](#moreaboutstorage) at the end of this article.
<!-- keep by customization: end -->
* The Backup and Restore feature supports up to 10GB of website and database content. An error will be indicated in the Operation Logs if the backup feature cannot proceed because the payload exceeds this limit. 

<a name="manualbackup"></a>
## Create a manual backup
<!-- deleted by customization

1. In the Azure Management Portal, choose your web app from the Web Apps blade. This will display the details of your web app in a new blade.
2. Select **Settings** option. The **Settings** blade will be displayed allowing you to modify your web app.
	
	![Backups page][ChooseBackupsPage]

3. Choose the **Backups** option in the **Settings** blade. The **Backups** blade will be displayed.
	
4. From the **Backups** blade, choose your backup destination by selecting a **Storage Account** and **Container**. The storage account must belong to the same subscription as the web app that you are going to back up.
	
	![Choose storage account][ChooseStorageAccount]
	
5. In the **Included databases** option in the **Backups** blade, select the databases that are connected to your web app (SQL Server or MySQL) that you want to back up. 

	> [AZURE.NOTE] 	For a database to appear in this list, its connection string must exist in the **Connection strings** section of the **Web app settings** blade in the portal.
	
6. In the **Backups** blade, select the **Backup destination**. You must choose an existing storage account and container.
7. In the command bar, click **Backup Now**.
	
	![BackUpNow button][BackUpNow]
	
	You will see a progress message during the backup process.
	

You can make a manual backup at any time.  

-->
<!-- keep by customization: begin -->
1. In the Azure Management Portal for your website, choose the **Backups** tab.
	
	![Backups page][ChooseBackupsPage]
	
2. Select the storage account to which you want to back up your website. The storage account must belong to the same subscription as the website that you are going to back up.
	
	![Choose storage account][ChooseStorageAccount]
	
3. In the **Included Databases** option, select the databases that are connected to your website (SQL Server or MySQL) that you want to back up. 
	
	![Choose databases to include][IncludedDatabases]

	> [AZURE.NOTE] 	For a database to appear in this list, its connection string must exist in the **Connection Strings** section of the Configure tab in the portal.
	
4. In the command bar, click **Backup Now**.
	
	![BackUpNow button][BackUpNow]
	
	You will see a progress message during the backup process:
	
	![Backup progress message][BackupProgress]
	
You can make a manual backup at any time. During Preview, no more than 2 manual backups can be made in a 24-hour period (subject to change).  
<!-- keep by customization: end -->
<a name="automatedbackups"></a>
## Configure automated backups
<!-- deleted by customization

1. On the **Backups** blade, set **Scheduled Backup** to ON.
	
	![Enable automated backups][SetAutomatedBackupOn]
	
2. Select the storage account to which you want to back up your web app. The storage account must belong to the same subscription as the web app that you are going to back up.
	
	![Choose storage account][ChooseStorageAccount]
	
3. In the **Frequency** box, specify how often you want automated backups to be made. 
	The number of days must be between 1 and 90, inclusive (from once a day to once every 90 days).
	
4. Use the **Begin** option to specify a date and time when you want the automated backups to begin. 
	
	> [AZURE.NOTE] Azure stores backup times in UTC format, but displays them in accordance with the system time on the computer that you are using to display the portal.
	
5. In the **Included Databases** section, select the databases that are connected to your web app (SQL Server or MySQL) that you want to back up. For a database to appear in the list, its connection string must exist in the **Connection strings** section of the **Web app settings** blade in the portal.
	
	> [AZURE.NOTE] If you choose to include one or more databases in the backup and have specified a Frequency of less than 7 days, you will be warned that frequent backups can increase your database costs.
	
6. Additionally, set the **Retention (Days)** value to the number of days you wish to retain the backup.
7. In the command bar, click the **Save** button to save your configuration changes (or choose **Discard** if you decide not to save them).
	
	![Save button][SaveIcon]

-->
<!-- keep by customization: begin -->
1. On the Backups page, set **Automated Backup** to ON.
	
	![Enable automated backups][SetAutomatedBackupOn]
	
2. Select the storage account to which you want to back up your website. The storage account must belong to the same subscription as the website that you are going to back up.
	
	![Choose storage account][ChooseStorageAccount]
	
3. In the **Frequency** box, specify how often you want automated backups to be made. (During Preview, the number of days is the only time unit available.)
	
	![Choose backup frequency][Frequency]
	
	The number of days must be between 1 and 90, inclusive (from once a day to once every 90 days).
	
4. Use the **Start Date** option to specify a date and time when you want the automated backups to begin. 
	
	![Choose start date][StartDate]
	
	Times are available in half-hour increments.
	
	![Choose start time][StartTime]
	
	> [AZURE.NOTE] Azure stores backup times in UTC format, but displays them in accordance with the system time on the computer that you are using to display the portal.
	
5. In the **Included Databases** section, select the databases that are connected to your website (SQL Server or MySQL) that you want to back up. For a database to appear in the list, its connection string must exist in the **Connection Strings** section of the Configure tab in the portal.
	
	![Choose databases to include][IncludedDatabases]
	
	> [AZURE.NOTE] If you choose to include one or more databases in the backup and have specified a Frequency of less than 7 days, you will be warned that frequent backups can increase your database costs.
	
6. In the command bar, click the **Save** button to save your configuration changes (or choose **Discard** if you decide not to save them).
	
	![Save button][SaveIcon]
<!-- keep by customization: end -->
<a name="notes"></a>
## Notes

* Make sure that you set up the connection strings for each of your databases properly on the **Web app settings** blade within **Settings** of the web app so that the Backup and Restore feature can include your databases.
* Although you can back up more than one web app to the same storage account, for ease of maintenance, consider creating a separate storage account for each web app.
<!-- deleted by customization

>[AZURE.NOTE] If you want to get started with Azure Websites before signing up for an Azure account, go to [Try Azure Websites](http://go.microsoft.com/fwlink/?LinkId=523751), where you can immediately create a short-lived starter web app in Azure Websites. No credit cards required; no commitments.
-->

<a name="partialbackups"></a>
## Backup just part of your web app

Sometimes you don't want to backup everything on your web app. Here are a few examples:

-	You [set up weekly backups](/documentation/articles/web-sites-backup#configure-automated-backups) of your web app that contains static content that never changes, such as old blog posts or images.
-	Your web app has over 10GB of content (that's the max amount you can backup at a time).
-	You don't want to back up the log files.

Partial backups will let you choose exactly which files you want to back up.

### Exclude files from your backup

To exclude files and folders from your backups, create a `_backup.filter` file in the wwwroot folder of your web app and specify the list of files and folders you want to exclude in there. An easy way to access this is through the [Kudu Console](https://github.com/projectkudu/kudu/wiki/Kudu-console). 

Suppose you have a web app that contains log files and static images from past years that are never going to change. You already have a full backup of the web app that includes the old images. Now you want to backup the web app every day, but you don't want to pay for storing log files or the static image files that never change.

![Logs Folder][LogsFolder]
![Images Folder][ImagesFolder]
	
The below steps show how you would exclude these files from the backup.

1. Go to `http://{yourapp}.scm.chinacloudsites.cn/DebugConsole` and identify the folders that you want to exclude from your backups. In this example, you would want to exclude the following files and folders shown in that UI:

		D:\home\site\wwwroot\Logs
		D:\home\LogFiles
		D:\home\site\wwwroot\Images\2013
		D:\home\site\wwwroot\Images\2014
		D:\home\site\wwwroot\Images\brand.png

	[AZURE.NOTE] The last line illustrates that you can exclude individuals files as well as folders.

2. Create a file called `_backup.filter` and put the list above in the file, but remove `D:\home`. List one directory or file per line. So the content of the file should be:

    \site\wwwroot\Logs
    \LogFiles
    \site\wwwroot\Images\2013
    \site\wwwroot\Images\2014
    \site\wwwroot\Images\brand.png

3. Upload this file to the `D:\home\site\wwwroot\` directory of your site using [ftp](/documentation/articles/web-sites-deploy#ftp) or any other method. If you wish, you can create the file directly in `http://{yourapp}.scm.chinacloudsites.cn/DebugConsole` and insert the content there.

4. Run backups the same way you would normally do it, [manually](#create-a-manual-backup) or [automatically](#configure-automated-backups).

Now, any files and folders that are specified in `_backup.filter` will be excluded from the backup. In this example, the log files and the 2013 and 2014 image files will no longer be backed up, as well as brand.png.

>[AZURE.NOTE] You restore partial backups of your site the same way you would [restore a regular backup](/documentation/articles/web-sites-restore). The restore process will do the right thing.
>
>When a full backup is restored, all content on the site is replaced with whatever is in the backup. If a file is on the site but not in the backup it gets deleted. But when a partial backup is restored, any content that is located in one of the blacklisted directories, or any blacklisted file, is left as is.

<a name="aboutbackups"></a>

## How backups are stored

After you have made one or more backups for your web app, the backups will be visible on the **Containers** blade of your storage account, as well as your web app. In the storage account, each backup consists of a .zip file that contains the backup data and an .xml file that contains a manifest of the .zip file contents. You can unzip and browse these files if you want to access your backups without actually performing a web app restore.

The database backup for the web app is stored in the root of the .zip file. For a SQL database, this is a BACPAC file (no file extension) and can be imported. To create a new SQL database based on the BACPAC export, see [Import a BACPAC File to Create a New User Database](http://technet.microsoft.com/zh-cn/library/hh710052.aspx).

> [AZURE.WARNING] Altering any of the files in your **websitebackups** container can cause the backup to become invalid and therefore non-restorable.

<a name="bestpractices"></a>
##Best Practices

In the event of a failure or natural disaster, you want to make sure sure you're prepared beforehand by having an existing backup and restore strategy.

Your backup strategy should be similar to the following:

-	Take at least one full backup of your web app.
-	Take partial backups of your web app after you have a full backup.

Your restore strategy should be similar to the following:
 
-	Create a [staging slot](/documentation/articles/web-sites-staged-publishing) for your web app.
-	Restore the full backup of the web app on the staging slot.
-	Restore the latest partial backup on top of the full backup restore, also on the staging slot.
-	Test the restore to see that the staging app works properly.
-	[Swap](/documentation/articles/web-sites-staged-publishing#Swap) the staged web app into the production slot.

>[AZURE.NOTE] Always test your restore process. For more information, see [Very Good Thing](http://axcient.com/blog/one-thing-can-derail-disaster-recovery-plan/). For example, certain blogging platforms, such as [Ghost](https://ghost.org/), have explicit caveats on how they behave during a backup. By testing your restore process, you can catch these caveats when you're not yet struck by a failure or disaster.

<a name="nextsteps"></a>
## Next Steps
For information on restoring web app from backup, see [Restore a web app in Azure Websites](/documentation/articles/web-sites-restore).

To get started with Azure, see [Windows Azure Trial](/pricing/1rmb-trial/).


<a name="moreaboutstorage"></a>
### More about storage accounts

[What is a Storage Account?](/documentation/articles/storage-whatis-account)

[How to: Create a storage account](/documentation/articles/storage-create-storage-account)

[How To Monitor a Storage Account](/documentation/articles/storage-monitor-storage-account)

[Understanding Azure Storage Billing](http://blogs.msdn.com/b/windowsazurestorage/archive/2010/07/09/understanding-windows-azure-storage-billing-bandwidth-transactions-and-capacity.aspx)
<!-- deleted by customization

## What's changed
* For a guide to the change from Websites to Azure Websites see: [Azure Websites and Its Impact on Existing Azure Services](/documentation/services/web-sites/)
* For a guide to the change of the Management Portal to the new portal see: [Reference for navigating the preview portal](https://manage.windowsazure.cn/)
-->

<!-- IMAGES -->
[ChooseBackupsPage]: ./media/web-sites-backup/01ChooseBackupsPage.png
[ChooseStorageAccount]: ./media/web-sites-backup/02ChooseStorageAccount.png
[IncludedDatabases]: ./media/web-sites-backup/03IncludedDatabases.png
[BackUpNow]: ./media/web-sites-backup/04BackUpNow.png
[BackupProgress]: ./media/web-sites-backup/05BackupProgress.png
[SetAutomatedBackupOn]: ./media/web-sites-backup/06SetAutomatedBackupOn.png
[Frequency]: ./media/web-sites-backup/07Frequency.png
[StartDate]: ./media/web-sites-backup/08StartDate.png
[StartTime]: ./media/web-sites-backup/09StartTime.png
[SaveIcon]: ./media/web-sites-backup/10SaveIcon.png
[ImagesFolder]: ./media/web-sites-backup/11Images.png
[LogsFolder]: ./media/web-sites-backup/12Logs.png
[GhostUpgradeWarning]: ./media/web-sites-backup/13GhostUpgradeWarning.png
 