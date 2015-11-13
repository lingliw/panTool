<properties title="How to create a PHP  Website in Azure  Websites" pageTitle="How to create a PHP  Website in Azure  Websites" metaKeywords="PHP Azure  Websites" description="Learn how to create a PHP  Website in Azure  Websites" documentationCenter="PHP" services=" Websites" editor="mollybos" manager="bjsmith" authors="" />

#How to create a PHP  Website in Azure  Websites

This article will show you how to create a PHP  Website in [Azure  Websites][waws] by using the [Azure Management Portal], the [Azure Command Line Tools for Mac and Linux][xplat-tools], or the [Azure PowerShell cmdlets][powershell-cmdlets].

In general, creating a PHP  Website is no different that creating *any*  Website in Azure  Websites. By default, PHP is enabled for all  Websites. For information about configuring PHP (or providing your own customized PHP runtime), see [How to configure PHP in Azure  Websites][configure-php].

Each option described below shows you how to create a website in a shared hosting environment at no cost, but with some limitations on CPU usage and bandwidth usage. For more information, see [Azure Web Sites Pricing][websites-pricing]. For information about how to upgrade and scale your website, see [How to scale Web Sites][scale-websites].

> [AZURE.NOTE]
> If you want to get started with Azure Websites before signing up for an account, go to <a href="https://trywebsites.chinacloudsites.cn/?language=php">https://trywebsites.chinacloudsites.cn</a>, where you can immediately create a short-lived ASP.NET starter site in Azure Websites for free. No credit card required, no commitments.

##Table of Contents
* [Create a  Website using the Azure Management Portal](#portal)
* [Create a  Website using the Azure Command Line Tools for Mac and Linux](#XplatTools)
* [Create a  Website using the Azure PowerShell cmdlets](#PowerShell)

<h2><a name="portal"></a>Create a PHP  Website using the Azure Management Portal</h2>

When you create a  Website in the Azure Management Portal, you have two options: **Quick Create** and **Create with Database**. The instructions below will cover the **Quick Create** option. For information about the other two options, see [Create a PHP-MySQL Azure  Website and deploy using Git] and [ Website-mysql-git].

To create a PHP  Website using the Azure Management Portal, do the following:

1. Login to the [Azure Management Portal].
1. Click **New** at the bottom of the page, then click **Compute**, ** Website**, and **Quick Create**. Provide a **URL** for your  Website and select the **Region** for your  Website. Finally, click **Create  Website**.

![Select Quick Create  Website](./media/web-sites-php-create-web-sites/select-quickcreate-Website.png)

<h2><a name="XplatTools"></a>Create a PHP  Website using the Azure Command Line Tools for Mac and Linux</h2>

To create a PHP  Website using the Azure Command Line Tools for Mac and Linux do the following:

1. Install the Azure Command Line Tools by following the instructions here: [How to install the Azure Command Line Tools for Mac and Linux](/documentation/articles/xplat-cli#Download).

1. Download and import your publish settings file by following the instructions here: [How to download and import publish settings](/documentation/articles/xplat-cli#Account).

1. Run the following command from a command prompt:

		azure site create MySiteName

The URL for the newly created  Website will be  `http://MySiteName.chinacloudsites.cn`.  
 
Note that you can execute the `azure site create` command with any of the following options:

* `--location [location name]`. This option allows you to specify the location of the data center in which your  Website is created (e.g. "China East"). If you omit this option, you will be promted to choose a location.
* `--hostname [custom host name]`. This option allows you to specify a custom hostname for your  Website.
* `--git`. This option allows you to use git to publish to your  Website by creating git repositories in both your local application directory and in your  Website's data center. Note that if your local folder is already a git repository, the command will add a new remote to the existing repository, pointing to the repository in your  Website's data center.

For information about additional options, see [How to create and manage an Azure  Website](/documentation/articles/xplat-cli# Websites).

<h2><a name="PowerShell"></a>Create a PHP  Website using the Azure PowerShell cmdlets</h2>

To create a PHP  Website using the Azure PowerShell cmdlets, do the following:

1. Install the Azure PowerShell cmdlets by following the instructions here: [Get started with Azure PowerShell](/documentation/articles/install-configure-powershell#GetStarted).

1. Download and import your publish settings file by following the instructions here: [How to: Import publish settings](/documentation/articles/install-configure-powershell#ImportPubSettings).

1. Open a PowerShell command prompt and execute the following command:

		New-Azure Website MySiteName

The URL for the newly created  Website will be  `http://MySiteName.chinacloudsites.cn`.  
 
Note that you can execute the `New-Azure Website` command with any of the following options:

* `-Location [location name]`. This option allows you to specify the location of the data center in which your  Website is created (e.g. "China East"). If you omit this option, you will be promted to choose a location.
* `-Hostname [custom host name]`. This option allows you to specify a custom hostname for your  Website.
* `-Git`. This option allows you to use git to publish to your  Website by creating git repositories in both your local application directory and in your  Website's data center. Note that if your local folder is already a git repository, the command will add a new remote to the existing repository, pointing to the repository in your  Website's data center.

For information about additional options, see [How to: Create and manage an Azure  Website](/develop/php/how-to-guides/powershell-cmdlets/# Website).

<h2><a name="NextSteps"></a>Next steps</h2>

Now that you have created a PHP  Website in Azure  Websites, you can manage, configure, monitor, deploy to, and scale your site. For more information, see the following links:

* [How to configure  Websites](/documentation/articles/web-sites-configure//)
* [How to configure PHP in Azure  Websites][configure-php]
* [How to manage  Websites](/documentation/articles/web-sites-manage)
* [How to monitor  Websites](/documentation/articles/web-sites-monitor)
* [How to scale  Websites](/documentation/articles/web-sites-scale)
* [Publishing with Git](/documentation/articles/web-sites-publish-source-control//)

For end-to-end tutorials, visit the [PHP Developer Center - Tutorials](/develop/php//) page.

[waws]: /zh-cn/documentation/services/web-sites
[Azure Management Portal]: http://manage.windowsazure.cn/
[xplat-tools]: /documentation/articles/xplat-cli
[powershell-cmdlets]: /documentation/articles/install-configure-powershell
[configure-php]: /documentation/articles/web-sites-php-configure
[Website-mysql-git]: /documentation/articles/web-sites-php-mysql-deploy-use-git
[Websites-pricing]: /zh-cn/pricing/overview/
[scale-Websites]: /documentation/articles/web-sites-scale
