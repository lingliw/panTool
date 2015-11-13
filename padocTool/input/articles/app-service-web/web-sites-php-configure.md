<properties
	pageTitle="Configure PHP in Azure Websites"
	description="Learn how to configure the default PHP installation or add a custom PHP installation for Web Apps in Azure Websites."
	services="app-service"
	documentationCenter="php"
	authors="tfitzmac"
	manager="wpickett"
	editor=""/>

<tags
	ms.service="app-service"
	ms.date="09/16/2015"
	wacn.date=""/>

#Configure PHP in Azure Websites

<!-- keep by customization: begin -->
##Table of Contents

* [What is Azure  Websites?](#WhatIs)
* [How to: Change the default PHP configuration](#ChangeBuiltInPHP)
* [How to: Enable extensions in the built-in PHP runtime](#EnableExtDefaultPHP)
* [How to: Use a custom PHP runtime](#UseCustomPHP)
* [Next steps](#NextSteps)
<!-- keep by customization: end -->
## Introduction

This guide will show you how to configure the built-in PHP runtime for Web Apps in [Azure Websites](/documentation/services/web-sites/), provide a custom PHP runtime, and enable extensions. To use Azure Websites, sign up for the [trial]. To get the most from this guide, you should first create a PHP web app in Azure Websites.
<!-- deleted by customization

[AZURE.INCLUDE [app-service-web-to-api-and-mobile](../includes/app-service-web-to-api-and-mobile.md)]
-->

## How to: Change the built-in PHP version
By default, PHP 5.4 is installed and immediately available for use when you create an Azure Websites web app. The best way to see the available release revision, its default configuration, and the enabled extensions is to deploy a script that calls the [phpinfo()] function.

PHP 5.5 and PHP 5.6 versions are also available, but not enabled by default. To update the PHP version, follow one of these methods:

### Azure Management Portal
<!-- deleted by customization

1. Browse to your web app in the [Azure Management Portal](https://manage.windowsazure.cn/) and click on the **Settings** button.

	![Web App Settings][settings-button]

2. From the **Settings** blade select **Application Settings** and choose the new PHP version.

    ![Application Settings][application-settings]

3. Click the **Save** button at the top of the **Web app settings** blade.

	![Save configuration settings][save-button]

### Azure PowerShell (Windows)

1. Open Windows PowerShell
2. Type `Set-AzureWebsite -PhpVersion [5.4 | 5.5 | 5.6] -Name <site-name>` then press enter.
3. The PHP version is now set.

	![Setting the PHP version with Azure PowerShell][SETPHPVERPS]
4. You can confirm these settings by typing `Get-AzureWebiste -Name <site-name>` then press enter.

	![Verifying the PHP version with Azure PowerShell][GETPHPVERPS]

### Azure Command-Line Interface (Linux, Mac, Windows)

To use the Azure Command-Line Interface, you must have **Node.js** installed on your computer.

1. Open Terminal.
2. Type `azure site set --php-version [5.4 | 5.5] [site-name]` then press enter.
3. The PHP version is now set.

	![Setting the PHP version with Azure Command-Line Interface][SETPHPVERCLI]
4. You can confirm these settings by typing `azure site show [site-name]` then press enter.

	![Verifying the PHP version with Azure Command-Line Interface][GETPHPVERCLI]

-->
<!-- keep by customization: begin -->
1. Browse to your  Website's dashboard in the Azure Management Portal, click on **Configure**.

	![Configure tab on  Websites dashboard][configure]

1. Click PHP 5.5.

	![Select PHP version][select-php-version]

1. Click **Save** at the bottom of the page.

	![Save configuration settings][save-button]

<!-- keep by customization: end -->
## How to: Change the built-in PHP configurations

For any built-in PHP runtime, you can change any of the configuration options by following the steps below. (For information about php.ini directives, see [List of php.ini directives].)

### Changing PHP_INI_USER, PHP_INI_PERDIR, PHP_INI_ALL configuration settings

1. Add a [.user.ini] file to your root directory.
2. Add configuration settings to the `.user.ini` file using the same syntax you would use in a `php.ini` file. For example, if you wanted to turn the `display_errors` setting on and set `upload_max_filesize` setting to 10M, your `.user.ini` file would contain this text:

		; Example Settings
		display_errors=On
		upload_max_filesize=10M

3. Deploy your web app.
4. Restart the web app. (Restarting is necessary because the frequency with which PHP reads `.user.ini` files is governed by the `user_ini.cache_ttl` setting, which is a system level setting and is 300 seconds (5 minutes) by default. Restarting the web app forces PHP to read the new settings in the `.user.ini` file.)

As an alternative to using a `.user.ini` file, you can use the [ini_set()] function in scripts to set configuration options that are not system-level directives.

### Changing PHP_INI_SYSTEM configuration settings

1. Add an App Setting to your Web App with the key `PHP_INI_SCAN_DIR` and value `d:\home\site\ini`
2. Create an `settings.ini` file using Kudu Console (http://&lt;site-name&gt;.scm.azurewebsite.net) in the `d:\home\site\ini` directory.
3. Add configuration settings to the `settings.ini` file using the same syntax you would use in a php.ini file. For example, if you wanted to point the `curl.cainfo` setting to a `*.crt` file and set 'wincache.maxfilesize' setting to 512K, your `settings.ini` file would contain this text:

		; Example Settings
		curl.cainfo="%ProgramFiles(x86)%\Git\bin\curl-ca-bundle.crt"
		wincache.maxfilesize=512
4. Restart your Web App to load the changes.

## How to: Enable extensions in the default PHP runtime
As noted in the previous section, the best way to see the default PHP version, its default configuration, and the enabled extensions is to deploy a script that calls [phpinfo()]. To enable additional extensions, follow the steps below:

### Configure via ini settings

1. Add a `ext` directory to the `d:\home\site` directory.
2. Put `.dll` extension files in the `ext` directory (for example, `php_mongo.dll` and `php_xdebug.dll`). Make sure that the extensions are compatible with default version of PHP (which is, as of this writing, PHP 5.4) and are VC9 and non-thread-safe (nts) compatible.
3. Add an App Setting to your Web App with the key `PHP_INI_SCAN_DIR` and value `d:\home\site\ini`
4. Create an `ini` file in `d:\home\site\ini` called `extensions.ini`.
5. Add configuration settings to the `extensions.ini` file using the same syntax you would use in a php.ini file. For example, if you wanted to enable the MongoDB and XDebug extensions, your `extensions.ini` file would contain this text:

		; Enable Extensions
		extension=d:\home\site\ext\php_mongo.dll
		zend_extension=d:\home\site\ext\php_xdebug.dll
6. Restart your Web App to load the changes.

### Configure via App Setting

1. Add a `bin` directory to the root directory.
2. Put `.dll` extension files in the `bin` directory (for example, `php_mongo.dll`). Make sure that the extensions are compatible with default version of PHP (which is, as of this writing, PHP 5.4) and are VC9 and non-thread-safe (nts) compatible.
3. Deploy your web app.
<!-- deleted by customization
4. Browse to your web app in the Azure Management Portal and click on the **Settings** button.

	![Web App Settings][settings-button]

5. From the **Settings** blade select **Application Settings** and scroll to the **App settings** section.
6. In the **App settings** section, create a **PHP_EXTENSIONS** key. The value for this key would be a path relative to website root: **bin\your-ext-file**.

	![Enable extension in app settings][php-extensions]

7. Click the **Save** button at the top of the **Web app settings** blade.

	![Save configuration settings][save-button]

-->
<!-- keep by customization: begin -->
1. Navigate to your site's dashboard in the Azure Management Portal, and click on **Configure**.

	![Configure tab on  Websites dashboard][configure]

1. In the **app settings** section, create a key **PHP_EXTENSIONS** and a value **bin\your-ext-file**. To enable multiple extensions, incude a comma-separated list of `.dll` files.

	![Enable extension in app settings][app-settings]

1. Click **Save** at the bottom of the page.

	![Save configuration settings][save-button]
<!-- keep by customization: end -->
Zend extensions are also supported by using a **PHP_ZENDEXTENSIONS** key. To enable multiple extensions, include a comma-separated list of `.dll` files for the app setting value.


## How to: Use a custom PHP runtime
Instead of the default PHP runtime, Azure Websites can use a PHP runtime that you provide to execute PHP scripts. The runtime that you provide can be configured by a `php.ini` file that you also provide. To use a custom PHP runtime with Web Apps, follow the steps below.

1. Obtain a non-thread-safe, VC9 or VC11 compatible version of PHP for Windows. Recent releases of PHP for Windows can be found here: [http://windows.php.net/download/]. Older releases can be found in the archive here: [http://windows.php.net/downloads/releases/archives/].
2. Modify the `php.ini` file for your runtime. Note that any configuration settings that are system-level-only directives will be ignored by Web Apps. (For information about system-level-only directives, see [List of php.ini directives]).
3. Optionally, add extensions to your PHP runtime and enable them in the `php.ini` file.
4. Add a `bin` directory to your root directory, and put the directory that contains your PHP runtime in it (for example, `bin\php`).
5. Deploy your web app.
<!-- deleted by customization
4. Browse to your web app in the Azure Management Portal and click on the **Settings** button.

	![Web App Settings][settings-button]

7. From the **Settings** blade select **Application Settings** and scroll to the **Handler mappings** section. Add `*.php` to the Extension field and add the path to the `php-cgi.exe` executable. If you put your PHP runtime in the `bin` directory in the root of you application, the path will be `D:\home\site\wwwroot\bin\php\php-cgi.exe`.

	![Specify handler in hander mappings][handler-mappings]

8. Click the **Save** button at the top of the **Web app settings** blade.

	![Save configuration settings][save-button]

## Next steps

For more information, see the [PHP Developer Center](/develop/php/).

>[AZURE.NOTE] If you want to get started with Azure Websites before signing up for an Azure account, go to [Try Azure Websites](http://go.microsoft.com/fwlink/?LinkId=523751), where you can immediately create a short-lived starter web app in Azure Websites. No credit cards required; no commitments.

## What's changed
* For a guide to the change from Websites to Azure Websites see: [Azure Websites and Its Impact on Existing Azure Services](/documentation/services/web-sites/)
* For a guide to the change of the Management Portal to the new portal see: [Reference for navigating the preview portal](https://manage.windowsazure.cn/)

-->
<!-- keep by customization: begin -->
1. Navigate to your site's dashboard in the Azure Management Portal, and click on **Configure**.

	![Configure tab on  Websites dashboard][configure]

1. In the **handler mappings** section, add `*.php` to EXTENSION and add the path to the `php-cgi.exe` executable. If your put your PHP runtime in the `bin` directory in the root of you application, the path will be `D:\home\site\wwwroot\bin\php\php-cgi.exe`.

	![Specify handler in hander mappings][handler-mappings]

1. Click **Save** at the bottom of the page.

	![Save configuration settings][save-button]
<!-- keep by customization: end -->
<!-- keep by customization: begin -->
[PHP Developer Center Tutorials]: /develop/php/
[How to Configure  Websites]: /documentation/articles/web-sites-configure
[configure]: ./media/web-sites-php-configure/configure.png
[app-settings]: ./media/web-sites-php-configure/app-settings.png
[handler-mappings]: ./media/web-sites-php-configure/handler-mappings.png
[Configure, monitor, and scale your  Websites in Azure]: /zh-cn/documentation/services/web-sites
[Download the Azure SDK for PHP]: /zh-cn/downloads/?sdk=php
<!-- keep by customization: end -->
[trial]: https://azure.microsoft.com/pricing/1rmb-trial/
[phpinfo()]: http://php.net/manual/en/function.phpinfo.php
[select-php-version]: ./media/web-sites-php-configure/select-php-version.png
[List of php.ini directives]: http://www.php.net/manual/en/ini.list.php
[.user.ini]: http://www.php.net/manual/en/configuration.file.per-user.php
[ini_set()]: http://www.php.net/manual/en/function.ini-set.php
[application-settings]: ./media/web-sites-php-configure/application-settings.png
[settings-button]: ./media/web-sites-php-configure/settings-button.png
[save-button]: ./media/web-sites-php-configure/save-button.png
[php-extensions]: ./media/web-sites-php-configure/php-extensions.png
[handler-mappings]: ./media/web-sites-php-configure/handler-mappings.png
[http://windows.php.net/download/]: http://windows.php.net/download/
[http://windows.php.net/downloads/releases/archives/]: http://windows.php.net/downloads/releases/archives/
[SETPHPVERCLI]: ./media/web-sites-php-configure/ChangePHPVersion-XPlatCLI.png
[GETPHPVERCLI]: ./media/web-sites-php-configure/ShowPHPVersion-XplatCLI.png
[SETPHPVERPS]: ./media/web-sites-php-configure/ChangePHPVersion-PS.png
[GETPHPVERPS]: ./media/web-sites-php-configure/ShowPHPVersion-PS.png
 
