<properties 
	pageTitle="How to Scale a media service" 
	description="Learn how to scale Media Services by specifying the number of On-Demand Streaming Reserved Units and Encoding Reserved Units that you would like your account to be provisioned with." 
	services="media-services" 
	documentationCenter="" 
	authors="juliako" 
	manager="dwrede" 
	editor=""/>

<tags
	ms.service="media-services"
	ms.date="09/07/2015"
	wacn.date=""/>


#How to Scale a Media Service  

##Overview

You can scale **Media Services** by specifying the number of **Streaming Reserved Units** and **Encoding Reserved Units** that you would like your account to be provisioned with. 

You can also scale your Media Services account by adding storage accounts to it. Each storage account is limited to 500 TB. To expand your storage beyond the default limitations, you can choose to attach multiple storage accounts to a single Media Services account.

This topic links to relevant topics.

##<a id="streaming_endpoins"></a>Streaming Reserved Units

For more information, see [Scaling streaming units](/documentation/articles/media-services-manage-origins#scale_streaming_endpoints).

##<a id="encoding_reserved_units"></a>Encoding Reserved Units

For information about scaling encoding units, see the following **Portal** and **.NET** topics.

[AZURE.INCLUDE [media-services-selector-scale-encoding-units](../includes/media-services-selector-scale-encoding-units.md)]

Note that the reserved units are the same for Encoding and Indexing tasks.

##<a id="storage"></a>Scale Storage

For more information, see [Managing Media Services Assets across Multiple Storage Accounts](https://msdn.microsoft.com/zh-cn/library/azure/dn271889.aspx) and [Working with Azure Storage](https://msdn.microsoft.com/zh-cn/library/azure/dn767951.aspx).



<!-- deleted by customization
 
##Media Services learning paths

You can view AMS learning paths here:

- [AMS Live Streaming Workflow](http://azure.microsoft.com/documentation/learning-paths/media-services-streaming-live/)
- [AMS on Demand Streaming Workflow](http://azure.microsoft.com/documentation/learning-paths/media-services-streaming-on-demand/)
-->

