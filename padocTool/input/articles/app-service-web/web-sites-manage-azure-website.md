<properties 
	pageTitle="Manage a web app in Azure Websites" 
	description="Links to resources for managing a web app in Azure Websites." 
	services="app-service\web" 
	documentationCenter="" 
	authors="erikre" 
	manager="wpickett" 
	editor=""/>

<tags
	ms.service="app-service-web"
	ms.date="07/31/2015"
	wacn.date=""/>

# Manage a web app in Azure Websites

This topic contains links to resources for managing a web app in [Azure Websites](/documentation/services/web-sites/). Management includes all of the tasks that keep your web app running smoothly. 

Over the lifetime of a web app, you will perform different management tasks, as you move from initial deployment to normal operation, maintenance, and updates.

Many web app management tasks can be performed in the Azure Management Portal.

## Before you deploy your web app to production

### Choose a tier

Azure Websites is offered in five tiers: Free, Shared, Basic, Standard, and Premium. For information about the features and pricing for each tier, see [Pricing details](/home/features/app-service/#price). 

- [App Service plans](/documentation/articles/azure-web-sites-web-hosting-plans-in-depth-overview) let you group multiple web apps under the same tier.
- You can always [switch tiers](/documentation/articles/web-sites-scale) after you create your web app.

### Configuration

Use the [Azure <!-- deleted by customization preview portal --><!-- keep by customization: begin -->Management Portal<!-- keep by customization: end -->](https://manage.windowsazure.cn/) to set various configuration options. For details, see [Configure web apps in Azure Websites](/documentation/articles/web-sites-configure). Here is a quick checklist:

- Select **runtime versions** for .NET, PHP, Java, or Python, if needed.
- Enable **WebSockets** if your web app uses the WebSocket protocol. (This includes apps that use [ASP.NET SignalR](http://www.asp.net/signalr) or [socket.io](/documentation/articles/web-sites-nodejs-chat-app-socketio).)
- Are you running continuous web jobs? If so, enable **Always On**.
- Set the **default document**, such as index.html.

In addition to these basic configuration settings, you may want to configure the following:

- **Secure Socket Layer (SSL)** encryption. To use SSL with a custom domain name, you must get an SSL certificate and configure your web app to use it. See [Enable HTTPS for a web app in Azure Websites](/documentation/articles/web-sites-configure-ssl-certificate).
- **Custom domain name.** Your web app automatically has a subdomain under chinacloudsites.cn. You can associate a custom domain name, such as contoso.com. See [Configure a custom domain name in Azure Websites](/documentation/articles/web-sites-custom-domain-name).

Language-specific configuration:

- **PHP**: [Configure PHP in Azure Websites](/documentation/articles/web-sites-php-configure).
- **Python**: [Configuring Python with Azure Websites](/documentation/articles/web-sites-python-configure)


## While your web app is running

While your web app is running, you want to make sure it is available, and that it scales to meet user traffic. You may also need to troubleshoot errors.

### Monitoring

- Through the Azure <!-- deleted by customization preview portal --><!-- keep by customization: begin -->Management Portal<!-- keep by customization: end -->, you can [add performance metrics](/documentation/articles/web-sites-monitor) such as CPU usage and number of client requests.
- For deeper insight, use New Relic to monitor and manage performance. See [.NET web app in Azure Websites with New Relic application performance management](/documentation/articles/store-new-relic-web-sites-dotnet-application-performance-management).
- [Scale your web app](/documentation/articles/web-sites-scale) in response to traffic. Depending on your tier, you can scale the number of VMs and/or the size of the VM instances. In the Standard and Premium tiers, you can also set up autoscaling, so your web app scales automatically, either on a fixed schedule, or in response to load.  
 
### Backups

- Set [automatic backups](/documentation/articles/web-sites-backup) of your web app. Learn more about backups in [this video](http://azure.microsoft.com/documentation/videos/azure-websites-automatic-and-easy-backup/).
- Learn about the options for [database recovery](http://msdn.microsoft.com/zh-cn/library/azure/hh852669.aspx) in Azure SQL Database.

### Troubleshooting

- If something goes wrong, you can [troubleshoot in Visual Studio](/documentation/articles/web-sites-dotnet-troubleshoot-visual-studio#remotedebug), using diagnostic logs and live debugging in the cloud. 
- Outside of Visual Studio, there are various ways to collect diagnostic logs. See [Enable diagnostics logging for web apps in Azure Websites](/documentation/articles/web-sites-enable-diagnostic-log).
- For Node.js applications, see [How to debug a Node.js web app in Azure Websites](/documentation/articles/web-sites-nodejs-debug).

### Restoring Data

- [Restore](/documentation/articles/web-sites-restore) a web app that was previously backed up.


## When you update your web app

If you have not enabled automatic backups, you can create a [manual backup](/documentation/articles/web-sites-backup).

Consider using [staged deployment](/documentation/articles/web-sites-staged-publishing). This option lets you publish updates to a staging deployment that runs side-by-side with your production deployment. 

If you use Visual Studio Online, you can set up continuous deployment from source control:

- [Using Team Foundation Version Control (TFVC)](/documentation/articles/cloud-services-continuous-delivery-use-vso) 
- [Using Git](/documentation/articles/cloud-services-continuous-delivery-use-vso-git)
 
[AZURE.INCLUDE [app-service-web-whats-changed](../includes/app-service-web-whats-changed.md)]

[AZURE.INCLUDE [app-service-web-try-app-service](../includes/app-service-web-try-app-service.md)]
 
<!-- Anchors. -->


[Before you deploy your site to production]: #before-you-deploy-your-site-to-production
[While your website is running]: #while-your-website-is-running
[When you update your website]: #when-you-update-your-website

  
