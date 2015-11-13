<properties
 pageTitle="What is Azure Scheduler? | Windows Azure"
 description="Azure Scheduler allows you to declaratively describe actions to run in the cloud. It then schedules and runs those actions automatically."
 services="scheduler"
 documentationCenter=".NET"
 authors="krisragh"
 manager="dwrede"
 editor=""/>
<tags
 ms.service="scheduler"
 ms.date="08/04/2015"
 wacn.date=""/>

# What is Scheduler?

Azure Scheduler allows you to declaratively describe actions to run in the cloud. It then schedules and runs those actions automatically. Azure Scheduler does this by using [the Azure portal](/documentation/articles/scheduler-get-started-portal), code, [REST API](https://msdn.microsoft.com/zh-cn/library/dn528946), or PowerShell.

Scheduler creates, maintains, and invokes scheduled work.  Scheduler does not host any workloads or run any code. It only _invokes_ code hosted elsewhere—in Azure, on-premises, or with another provider. It invokes via HTTP, HTTPS, or a storage queue.

Scheduler schedules [jobs](/documentation/articles/scheduler-concepts-terms.md), keeps a history of job execution results that one can review, and deterministically and reliably schedules workloads to be run. Azure WebJobs (part of the Web Apps feature in Azure App Service) and other Azure scheduling capabilities use Scheduler in the background. The [Scheduler REST API](https://msdn.microsoft.com/zh-cn/library/dn528946) helps manage the communication for these actions. As such, Scheduler supports [complex schedules and advanced recurrence](/documentation/articles/scheduler-advanced-complexity) easily.

There are several scenarios that lend themselves to the usage of Scheduler. For example:

+ _Recurring application actions:_ Periodically gathering data from Twitter into a feed.
+ _Daily maintenance:_ Daily pruning of logs, performing backups, and other maintenance tasks. For example, an administrator may choose to back up the database at 1:00 A.M. every day for the next nine months.

Scheduler allows you to create, update, delete, view, and manage jobs and [job collections ](/documentation/articles/scheduler-concepts-terms) programmatically, by using scripts, and in the portal. 

## See Also

 [Scheduler Concepts, Terminology, and Entity Hierarchy](/documentation/articles/scheduler-concepts-terms)

 [Get Started Using Scheduler in the Management Portal](/documentation/articles/scheduler-get-started-portal)

 [Plans and Billing in Azure Scheduler](/documentation/articles/scheduler-plans-billing)

 [How to Build Complex Schedules and Advanced Recurrence with Azure Scheduler](/documentation/articles/scheduler-advanced-complexity)

 [Scheduler REST API Reference](https://msdn.microsoft.com/zh-cn/library/dn528946)   

 [Scheduler PowerShell Cmdlets Reference](/documentation/articles/scheduler-powershell-reference)

 [Scheduler High-Availability and Reliability](/documentation/articles/scheduler-high-availability-reliability)

 [Scheduler Limits, Defaults, and Error Codes](/documentation/articles/scheduler-limits-defaults-errors)

 [Scheduler Outbound Authentication](/documentation/articles/scheduler-outbound-authentication)
 
 