<properties 
	pageTitle="Developing WordPress on Azure Web App" 
	description="Learn the Best Practices for Developing and Scaling WordPress on Azure." 
	keywords="app service, azure app service, scale wordpress, scalable wordpress, wordpress"
	services="app-service" 
	documentationCenter="" 
	authors="sunbuild" 
	manager="wpickett" 
	editor=""/>

<tags
	ms.service="app-service"
	ms.date="12/08/2015"
	wacn.date=""/>

# Developing WordPress on Azure

## WordPress and Azure App Service

* [What is WordPress?](https://wordpress.org/)
* [How to setup enterprise-class WordPress web app](web-sites-php-enterprise-wordpress.md)
* [Deploy a WordPress web app backed with MySQL replication cluster](/documentation/templates/wordpress-mysql-replication/)
* [Build your own Master-Master MySQL Cluster using Percona Cluster](/documentation/templates/mysql-ha-pxc/) and [learn more on how to manage the cluster](https://github.com/fanjeffrey/axiom.articles/tree/master/pxc)
* [Deploy WordPress backed by MySQL replication cluster with master-slave configuration](/documentation/templates/mysql-replication/)
  
## Chapter 2 : Troubleshooting WordPress Application

* [How to troubleshoot your WordPress app](https://sunithamk.wordpress.com/2014/09/04/wordpress-troubleshooting-techniques-on-azure-websites/)
* [Gather usage  telemetry using Azure Application Insights  service](https://azure.microsoft.com/blog/usage-analytics-for-wordpress-with-azure-app-insights/)
* [Run Zend Zray profiler against your web app to diagnose issues and performance](https://sunithamk.wordpress.com/2015/08/04/profiling-php-application-on-azure-web-apps/)
* [Use Kudu Support portal to diagnose and mitigate issues in real time](https://sunithamk.wordpress.com/2015/11/04/diagnose-and-mitigate-issues-with-azure-web-apps-support-portal/)
* [Use various auto-heal rules to automate resolving real time incidents](http://microsoftazurewebsitescheatsheet.info/#auto-heal)
* [How to backup your web app](/documentation/articles/web-sites-backup) and [How to restore your web app](/documentation/articles/web-sites-restore)

## Chapter 3: Performance

* [How to speed up WordPress web app](https://sunithamk.wordpress.com/2014/08/01/10-ways-to-speed-up-your-wordpress-site-on-azure-websites/)
* [How to enabled redis cache](/documentation/articles/cache-dotnet-how-to-use-azure-redis-cache) using [redis cache plugin](https://wordpress.org/plugins/wp-redis/)
* [How to enable memcached object cache for WordPress](/documentation/articles/web-sites-connect-to-redis-using-memcache-protocol) using [memcached plugin](https://wordpress.org/plugins/memcached/)
* [Enable wincache with W3 total cache plugin](https://wordpress.org/plugins/w3-total-cache/)
* [How to use supercache plugin to speed up WordPress app](http://ruslany.net/2008/12/speed-up-wordpress-on-iis-70/)
* [How to server caching using IIS output caching](http://blogs.msdn.com/b/brian_swan/archive/2011/06/08/performance-tuning-php-apps-on-windows-iis-with-output-caching.aspx)
* [How to enabled browser caching for static content](http://www.iis.net/configreference/system.webserver/staticcontent)
