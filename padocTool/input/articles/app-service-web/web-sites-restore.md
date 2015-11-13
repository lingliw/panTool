<properties 
	pageTitle="Restore a web app in Azure Websites" 
	description="Learn how to restore your web app from a backup." 
	services="app-service" 
	documentationCenter="" 
	authors="cephalin" 
	manager="wpickett" 
	editor="jimbe"/>

<tags
	ms.service="app-service"
	ms.date="09/16/2015"
	wacn.date=""/>

# Restore a web app in Azure Websites

This article shows you how to restore a web app that you have previously backed up by using the [Azure Websites](/documentation/services/web-sites/) Backup feature. For more information, see [Azure Websites Backups](/documentation/articles/web-sites-backup). 
<!-- deleted by customization

[AZURE.INCLUDE [app-service-web-to-api-and-mobile](../includes/app-service-web-to-api-and-mobile.md)]
-->

The Web Apps Restore feature lets you restore your web app on-demand to a previous state, or create a new web app based on one of your original web app's backups. Creating a new web app that runs in parallel to the latest version can be useful for A/B testing.

The Web Apps Restore feature, available on the **Backups** blade in the [Azure <!-- deleted by customization preview portal --><!-- keep by customization: begin -->Management Portal<!-- keep by customization: end -->](http://manage.windowsazure.cn), is available only in Standard and Premium modes. For information about scaling your app using Standard or Premium mode, see [Scale a web app in Azure Websites](/documentation/articles/web-sites-scale). 
<!-- deleted by customization
Note that the Premium mode allows a greater number of daily backups to be performed over the Standard mode.
-->
<!-- keep by customization: begin -->
##In this article
- [To Restore an Azure  Website from a previously made backup](#PreviousBackup)
- [To Restore an Azure  Website directly from a storage account](#StorageAccount)
- [Choose Your  Website Restore Settings and Start the Restore Operation](#RestoreSettings)
- [View the Operation Logs](#OperationLogs)
<!-- keep by customization: end -->

<a name="PreviousBackup"></a>
## To Restore a web app from a previously made backup
<!-- deleted by customization

1. On the **Settings** blade of your web app in the Azure Management Portal, click the **Backups** option to display the **Backups** blade. Scroll in this blade and select one of the backup item based on the **BACKUP TIME** and the **STATUS** from the backup list.
	
	![Choose backup source][ChooseBackupSource]
	
2. Select **Restore Now** at the top of the **Backups** blade. 

	![Choose restore now][ChooseRestoreNow]

3. In the **Restore** blade, to restore the existing web app, verify all the displayed details and then click **OK**. 
	
You can also restore your web app to a new web app by selecting the **WEB APP** part from the **Restore** blade and selecting the **Create a new web app** part.
	
-->
<!-- keep by customization: begin -->
1. On the **Backups** tab, click **Restore Now** in the command bar at the bottom of the portal page. The **Restore Now** dialog box appears.
	
	![Choose backup source][ChooseBackupSource]
	
2. Under **Choose backup source**, select **Previous Backup for this  Website**.
3. Select the date of the backup that you want to restore, and then click the right arrow to continue.
4. Follow the steps in the [Choose Your  Website Restore Settings](#RestoreSettings) section later in this article.
<!-- keep by customization: end -->
<a name="StorageAccount"></a>
## Download or delete a backup from a storage account
<!-- deleted by customization
	
1. From the main **Browse** blade of the Azure Management Portal, select **Storage Accounts**.
	
	A list of your existing storage accounts will be displayed. 
	
2. Select the storage account that contains the backup that you want to download or delete.
	
	The **STORAGE** blade will be displayed.

3. Select the **Containers** part in the **STORAGE** blade to display the **Containers** blade.
	
	A list of containers will be displayed. This list will also show the URL and the date of when this container was last modified.
	
	![View Containers][ViewContainers]

4. In the list, select the container and display the blade that shows a list of file names, along with the size of each file.
	
5. By selecting a file, you can either choose to **Download** or **Delete** the file. Note that there are two primary file types, .zip files and .xml files. 

-->
<!-- keep by customization: begin -->
1. On the **Backups** tab, click **Restore Now** in the command bar at the bottom of the portal page. The **Restore Now** dialog box appears.
	
	![Choose backup source][ChooseBackupSource]
	
2. Under **Choose backup source**, select **Storage Account File**. Here you can directly specify the URL for the storage account file, or click the folder icon to navigate to blob storage and specify the backup file. This example chooses the folder icon.
	
	![Storage Account File][StorageAccountFile]
	
3. Click the folder icon to open the **Browse Cloud Storage** dialog box.
	
	![Browse Cloud Storage][BrowseCloudStorage]
	

4. Expand the name of the storage account that you want to use, and then select ** Websitebackups**, which contains your backups.
5. Select the zip file containing the backup that you want to restore, and then click **Open**.
6. The Storage account file has been selected and shows in the storage account box. Click the right arrow to continue.
	
	![Storage Account File Selected][StorageAccountFileSelected]
	
7. Continue with the section that follows, [Choose Your  Website Restore Settings and Start the Restore Operation](#RestoreSettings).
<!-- keep by customization: end -->
<!-- keep by customization: begin -->
<a name="RestoreSettings"></a>
##Choose Your  Website Restore Settings and Start the Restore Operation
1. Under **Choose your  Website restore settings**, **Restore To**, select either **Current  Website** or **New  Website instance**.
	
	![Choose your  Website restore settings][ChooseRestoreSettings]
	
	If you select **Current  Website**, your existing  Website will be overwritten by the backup that you selected (destructive restore). All changes you have made to the  Website since the time of the chosen backup will be permanently removed, and the restore operation cannot be undone. During the restore operation, your current  Website will be temporarily unavailable, and you will be warned to this effect.
	
	If you select **New  Website instance**, a new  Website will be created in the same region with the name that you specify. (By default, the new name is **restored-***old WebsiteName*.) 
	
	The site that you restore will contain the same content and configuration that were made in the portal for the original site. It will also include any databases that you choose to include in the next step.
2. If you want to restore a database along with your  Website, under **Included Databases**, select the name of the database server that you want to restore the database to by using the dropdown under **Restore To**. You can also choose to create a new database server to restore to, or choose **Don't Restore** to not restore the database, which is the default. 
	
	After you have chosen the server name, specify the name of the target database for the restore in the **Database Name** box.
	
	If your restore includes one or more databases, you can select **Automatically adjust connection strings** to update your connection strings stored in the backup to point to your new database, or database server, as appropriate. You should verify that all functionality related to databases works as expected after the restore completes.
	
	![Choose database server host][ChooseDBServer]
	
	> [AZURE.NOTE] You cannot restore a SQL database with the same name to the same SQL Server. You must choose either a different database name or a different SQL Server host to restore the database to. 
	
	> [AZURE.NOTE] You can restore a MySQL database with the same name to the same server, but be aware that this will clear out the existing content stored in the MySQL database.	
	
3. If you choose to restore an existing database, you will need to provide a user name and password. If you choose to restore to a new database, you will need to provide a new database name:
	
	![Restore to a new SQL database][RestoreToNewSQLDB]
	
	Click the right arrow to continue.	
4. If you chose to create a new database, you will need to provide credentials and other initial configuration information for the database in the next dialog. The example here shows a new SQL database. (The options for a new MySQL database are somewhat different.)
	
	![New SQL database settings][NewSQLDBConfig]
	
5. Click the check mark to start the restore operation. When it completes, the new  Website instance (if that is the restore option you chose) will be visible in the list of  Websites in the portal.
	
	![Restored Contoso  Website][RestoredContoso Website]
<!-- keep by customization: end -->
<a name="OperationLogs"></a>
## View the Audit Logs
<!-- deleted by customization
	
1. To see details about the success or failure of the web app restore operation, select the **Audit Log** part of the main **Browse** blade. 
	
	The **Audio log** blade displays all of your operations, along with level, status, resource, and time details.
	
2. Scroll the blade to find operations related to your web app.
3. To view additional details about an operation, select the operation in the list.
	
The details blade will display the available information related to the operation.
	
-->
<!-- keep by customization: begin -->
1. To see details about the success or failure of the  Website restore operation, go to the  Website's Dashboard tab. In the **Quick Glance** section, under **Management Services**, click **Operation Logs**.
	
	![Dashboard - Operation Logs Link][DashboardOperationLogsLink]
	
2. You are taken to the Management Services portal **Operation Logs** page, where you can see the log for your restore operation in the list of operation logs:
	
	![Management Services Operation Logs page][ManagementServicesOperationLogsList]
	
3. To view details about the operation, select the operation in the list, and then click the **Details** button in the command bar.
	
	![Details Button][DetailsButton]
	
	When you do so, the **Operations Details** window opens and shows you the copiable contents of the log file:
	
	![Operation Details][OperationDetails]
<!-- keep by customization: end -->
<!-- deleted by customization
>[AZURE.NOTE] If you want to get started with Azure Websites before signing up for an Azure account, go to [Try Azure Websites](http://go.microsoft.com/fwlink/?LinkId=523751), where you can immediately create a short-lived starter web app in Azure Websites. No credit cards required; no commitments.
	
## What's changed
* For a guide to the change from Websites to Azure Websites see: [Azure Websites and Its Impact on Existing Azure Services](/documentation/services/web-sites/)
* For a guide to the change of the Management Portal to the new portal see: [Reference for navigating the preview portal](https://manage.windowsazure.cn/)
-->

<!-- IMAGES -->
<!-- keep by customization: begin -->
[RestoredContoso Website]: ./media/web-sites-restore/09RestoredContosoWebsite.png
<!-- keep by customization: end -->
[ChooseBackupSource]: ./media/web-sites-restore/01ChooseBackupSource.png
[ChooseRestoreNow]: ./media/web-sites-restore/02ChooseRestoreNow.png
[ViewContainers]: ./media/web-sites-restore/03ViewContainers.png
[StorageAccountFile]: ./media/web-sites-restore/02StorageAccountFile.png
[BrowseCloudStorage]: ./media/web-sites-restore/03BrowseCloudStorage.png
[StorageAccountFileSelected]: ./media/web-sites-restore/04StorageAccountFileSelected.png
[ChooseRestoreSettings]: ./media/web-sites-restore/05ChooseRestoreSettings.png
[ChooseDBServer]: ./media/web-sites-restore/06ChooseDBServer.png
[RestoreToNewSQLDB]: ./media/web-sites-restore/07RestoreToNewSQLDB.png
[NewSQLDBConfig]: ./media/web-sites-restore/08NewSQLDBConfig.png
[RestoredContosoWebSite]: ./media/web-sites-restore/09RestoredContosoWebSite.png
[DashboardOperationLogsLink]: ./media/web-sites-restore/10DashboardOperationLogsLink.png
[ManagementServicesOperationLogsList]: ./media/web-sites-restore/11ManagementServicesOperationLogsList.png
[DetailsButton]: ./media/web-sites-restore/12DetailsButton.png
[OperationDetails]: ./media/web-sites-restore/13OperationDetails.png
 