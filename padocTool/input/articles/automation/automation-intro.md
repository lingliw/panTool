<properties
	pageTitle="What is Azure Automation | Windows Azure"
	description="Learn what value Azure Automation provides and get answers to common questions so that you can get started in creating, using runbooks."
	services="automation"
	documentationCenter=""
	authors="bwren"
	manager="stevenka"
	editor=""/>

<tags
	ms.service="automation"
	ms.date="11/05/2015"
	wacn.date=""/>

# Azure Automation overview


Windows Azure Automation provides a way for users to automate the manual, long-running, error-prone, and frequently repeated tasks that are commonly performed in a cloud and enterprise environment. It saves time and increases the reliability of regular administrative tasks and even schedules them to be automatically performed at regular intervals. You can automate processes using runbooks or automate configuration management using Desired State Configuration. This article provides brief overview of Azure Automation and answers some common questions. You can refer to other articles in this library for more detailed information on the different topics.


## Automating processes with runbooks

A runbook is a set of tasks that perform some automated process in Azure Automation. It may be a simple process such as starting a virtual machine and creating a log entry, or you may have a complex runbook that combines other smaller runbooks to perform a complex process across multiple resources or even multiple clouds and on premise environments.  

For example, you might have an existing manual process for truncating a SQL database if it’s approaching maximum size that includes multiple steps such as connecting to the server, connecting to the database, get the current size of database, check if threshold has exceeded and then truncate it and notify user. Instead of manually performing each of these steps, you could create a runbook that would perform all of these tasks as a single process. You would start the runbook, provide the required information such as the SQL server name, database name, and recipient e-mail and then sit back while the process completes. 


## What can runbooks automate?

Runbooks in Azure Automation are based on Windows PowerShell Workflow, so they do anything that PowerShell can do. If an application or service has an API, then a runbook can work with it. If you have a PowerShell module for the application, then you can load that module into Azure Automation and include those cmdlets in your runbook. Azure Automation runbooks run in the Azure cloud and can access any cloud resources or external resources that can be accessed from the cloud. 


## Getting runbooks from the community

The [Runbook Gallery](http://msdn.microsoft.com/zh-cn/library/azure/dn781422.aspx) contains runbooks from Microsoft and the community that you can either use unchanged in your environment or customize them for your own purposes. They are also useful to as references to learn how to create your own runbooks. You can even contribute your own runbooks to the gallery that you think other users may find useful. 


## Creating Runbooks with Azure Automation 

You can [create your own runbooks](/documentation/articles/automation-creating-importing-runbook) from scratch or modify runbooks from the [Runbook Gallery](http://msdn.microsoft.com/zh-cn/library/azure/dn781422.aspx) for your own requirements. There is only one runbook type in WindowsAzure.cn. You can use a PowerShell Workflow runbook that you edit offline or with the [textual editor](http://msdn.microsoft.com/zh-cn/library/azure/dn879137.aspx) in the Azure Management Portal.

## Getting modules and configurations 

You can get [PowerShell modules](/documentation/articles/automation-runbook-gallery#modules-in-powershell-gallery) containing cmdlets that you can use in your runbooks from the [PowerShell Gallery](http://www.powershellgallery.com/). You can download and import them manually. You cannot install the modules directly from the Azure Management Portal, but you can download them install them as you would any other module. 


## Example practical applications of Azure Automation 

Following are just a few examples of the kinds of scenarios that you can automate with Azure Automation. 

* Create and copy virtual machines in different Azure subscriptions. 
* Schedule file copies from a local machine to an Azure Blob Storage container. 
* Automate security functions such as deny requests from a client when a denial of service attack is detected. 
* Ensure machines continually align with configured security policy.
* Manage continuous deployment of application code across cloud and on premises infrastructure. 
* Build an Active Directory forest in Azure for your lab environment. 
* Truncate a table in a SQL database if DB is approaching maximum size. 
* Remotely update environment settings for an Azure website. 


## How does Azure Automation relate to other automation tools?

[Service Management Automation (SMA)](http://technet.microsoft.com/zh-cn/library/dn469260.aspx) is intended to automate management tasks in the private cloud. It is installed locally in your data center as a component of [Windows Azure Pack](https://www.microsoft.com/server-cloud/). SMA and Azure Automation use the same runbook format based on Windows PowerShell Workflow.

## Where can I get more information? 

A variety of resources are available for you to learn more about Azure Automation and creating your own runbooks. 

## Can I provide feedback? 

**Please give us feedback!** If you are looking for an Azure Automation runbook solution or an integration module, post a Script Request on Script Center. If you have feedback or feature requests for Azure Automation, post them on [User Voice](/product-feedback). Thanks! 


