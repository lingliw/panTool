<properties
	pageTitle="Troubleshoot: web site unavailable due to HTTP 502/503"
	description="This article helps you troubleshoot HTTP 502/503 errors in your web site hosted in Azure Websites."
	services="app-service\web"
	documentationCenter=""
	authors="cephalin"
	manager="wpickett"
	editor=""
	tags="top-support-issue"/>

<tags
	ms.service="app-service-web"
	ms.date="10/23/2015"
	wacn.date=""/>

# Troubleshoot: web site unavailable due to HTTP 502/503

This article helps you troubleshoot HTTP 502/503 errors in your web site hosted in [Azure Websites](/documentation/services/web-sites/).

If you need more help at any point in this article, you can contact the Azure experts on [the MSDN Azure and the Stack Overflow forums](/support/forums/). Alternatively, you can also file an Azure support incident. Go to the [Azure Support site](/support/contact/) and click on **Get Support**.

## Symptom

When you browse to the web site, it returns a HTTP “502 Bad Gateway” or a HTTP “503 Service Unavailable”.

## Cause

This problem is often caused by application level issues, such as:

-	requests taking a long time
-	application using high memory/CPU
-	application crashing due to an exception.

## Troubleshooting steps

Troubleshooting can be divided into three distinct tasks, in sequential order:

1.	[Observe and monitor application behavior](#observe)
2.	[Collect data](#collect)
3.	[Mitigate the issue](#mitigate)

[Azure Websites](/home/features/web-site/) gives you various options at each step.

<a name="observe"></a>
### 1. Observe and monitor application behavior

####	Monitor your web site

This option enables you to find out if your application is having any issues. In your web site's blade, click the **Requests and errors** tile. The **Metric** blade will show you all the metrics you can add.

Some of the metrics that you might want to monitor for your web site are

-	Average memory working set
-	Average response time
-	CPU time
-	Memory working set
-	Requests

![](./media/app-service-web-troubleshoot-HTTP-502-503/1-monitor-metrics.png)

For more information, see:

-	[Monitor web sites in Azure Websites](/documentation/articles/web-sites-monitor)
-	[Receive alert notifications](/documentation/articles/insights-receive-alert-notifications)

<a name="collect"></a>
### 2. Collect data

####	Use the Azure Websites Support Portal

web sites provides you with the ability to troubleshoot issues related to your web site by looking at HTTP logs, event logs, process dumps, and more. You can access all this information using our Support portal at **http://&lt;your app name>.scm.chinacloudsites.cn/Support**

The Azure Websites Support portal provides you with three separate tabs to support the three steps of a common troubleshooting scenario:

1.	Observe current behavior
2.	Analyze by collecting diagnostics information and running the built-in analyzers
3.	Mitigate

If the issue is happening right now, click **Analyze** > **Diagnostics** > **Diagnose Now** to create a diagnostic session for you, which will collect HTTP logs, event viewer logs, memory dumps, PHP error logs and PHP process report.

Once the data is collected, it will also run an analysis on the data and provide you with an HTML report.

In case you want to download the data, by default, it would be stored in the D:\home\data\DaaS folder.

For more information on the Azure Websites Support portal, see [New Updates to Support Site Extension for Azure Websites](/blog/new-updates-to-support-site-extension-for-azure-websites).

####	Use the Kudu Debug Console

web sites comes with a debug console that you can use for debugging, exploring, uploading files, as well as JSON endpoints for getting information about your environment. This is called the _Kudu Console_ or the _SCM Dashboard_ for your web site.

You can access this dashboard by going to the link **https://&lt;Your app name>.scm.chinacloudsites.cn/**.

Some of the things that Kudu provides are:

-	environment settings for your application
-	log stream
-	diagnostic dump
-	debug console in which you can run Powershell cmdlets and basic DOS commands.


Another useful feature of Kudu is that, in case your application is throwing first-chance exceptions, you can use Kudu and the SysInternals tool Procdump to create memory dumps. These memory dumps are snapshots of the process and can often help you troubleshoot more complicated issues with your web site.

For more information on features available in Kudu, see
[Azure Websites online tools you should know about](/blog/windows-azure-websites-online-tools-you-should-know-about/).

<a name="mitigate"></a>
### 3. Mitigate the issue

####	Scale the web site

In Azure Websites, for increased performance and throughput,  you can adjust the scale at which you are running your application. Scaling up a web site involves two related actions: changing your App Service plan to a higher pricing tier, and configuring certain settings after you have switched to the higher pricing tier.

For more information on scaling, see [Scale a web site in Azure Websites](/documentation/articles/web-sites-scale).

Additionally, you can choose to run your application on more than one instance . This not only provides you with more processing capability, but also gives you some amount of fault tolerance. If the process goes down on one instance, the other instance will still continue serving requests.

You can set the scaling to be Manual or Automatic.

####	Use AutoHeal

AutoHeal recycles the worker process for your app based on settings you choose (like configuration changes, requests, memory-based limits, or the time needed to execute a request). Most of the time, recycle the process is the fastest way to recover from a problem. Though you can always restart the web site from directly within the Azure Management Portal, AutoHeal will do it automatically for you. All you need to do is add some triggers in the root web.config for your web site. Note that these settings would work in the same way even if your application is not a .Net one.

For more information, see [Auto-Healing Azure Web Sites](/blog/auto-healing-windows-azure-web-sites/).


####	Restart the web site

This is often the simplest way to recover from one-time issues. On the [Azure Management Portal](https://manage.windowsazure.cn), on your web site's blade, you have the options to stop or restart your app.

 ![](./media/app-service-web-troubleshoot-HTTP-502-503/2-restart.png)

You can also manage your web site using Azure Powershell. For more information, see
[Using Azure PowerShell with Azure Resource Manager](/documentation/articles/powershell-azure-resource-manager).
