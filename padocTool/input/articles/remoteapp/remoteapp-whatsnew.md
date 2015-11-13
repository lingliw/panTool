
<properties 
    pageTitle="What's new in Azure RemoteApp?"
    description="Learn about changes and improvements made to Azure RemoteApp" 
    services="remoteapp" 
    documentationCenter="" 
    authors="lizap" 
    manager="mbaldwin" />

<tags 
    ms.service="remoteapp" 
    ms.date="08/12/2015" 
    wacn.date="" />



# What's new in RemoteApp?

One of the advantages of RemoteApp is that we are always working to improve it. Every time we do, we'll announce those changes here.

## July 2015

July set the stage for changes coming in August, so there's not a lot to talk about now, mostly doc updates. Here are the most recent changes:

- Added a **Support** tab to the portal so you can more easily access support resources, like the forums.
- Reworked the troubleshooting information for creating a hybrid collection. Check out [the latest and greatest](/documentation/articles/remoteapp-hybridtrouble) for troubleshooting tips like, how to identify the correct ports to configure for your VNET.
- Documented how [user data](/documentation/articles/remoteapp-upd) is created and saved in Azure RemoteApp.
- Documented how to [lock down apps](/documentation/articles/remoteapp-secure).
- Published the [Azure RemoteApp cmdlets](https://msdn.microsoft.com/library/mt428031.aspx).
- And finally, we started a conversation with some Azure RemoteApp users about terminology. Look for changes to the way we refer to the different collection options.

## June 2015

So many changes! The team has been very busy in June:

- Redesigned the Azure RemoteApp [landing page](https://www.remoteapp.windowsazure.cn/) - check it out! 
- Updated the software in all the images available as part of your subscription.
- Made improvements to hybrid collections, including forced tunneling support and checking IP subnet size before trying to create the collection.
- Discovered that the * wildcard doesn't work for webcams. Instead, you need to specify the instance ID or GUID. We'll be updating the redirection information to reflect that.
- Made it so you can add custom antivirus software to your image when you create a template image from the Azure gallery.

We've got more changes rolling out in July, so we'll be back with another update soon.

## May 2015

There have been a number of additions (and months) since we first created this topic, so this list cheats a bit and is from the beginning of March through May. Check out these new features:

- Automate everything - Azure RemoteApp now has [cmdlets in the Azure PowerShell module](/documentation/articles/remoteapp-tutorial-arawithpowershell). 
- [Create an Azure RemoteApp image from an Azure virtual machine](/documentation/articles/remoteapp-image-on-azurevm). Makes uploading your custom image to Azure much quicker.
- Use an Azure VNET instead of a RemoteApp VNET to connect your corporate network resources to Azure. We've updated the [hybrid collection instructions](/documentation/articles/remoteapp-create-hybrid-deployment) to walk you through creating an Azure VNET (it's Step 1).
- Speaking of VNETs, check out [the new guidance](/documentation/articles/remoteapp-vnetsizing) around VNET size limits and limitations.
- And speaking of limits - just what are the [service limits and defaults](/documentation/articles/remoteapp-servicelimits)?

Want to learn more about Azure RemoteApp? The RemoteApp team was out in force at Ignite a few weeks ago. Check out Eric's video, [The Fundamentals of Windows Azure RemoteApp Management and Administration](http://channel9.msdn.com/Events/Ignite/2015/BRK3868).

Need to see Azure RemoteApp in the real world? Check out the [Run any app on any device anywhere](/documentation/articles/remoteapp-anyapp) tutorial - it shows you how to share Access with your users, including sharing the database files. We also have a tutorial on [making Office 365](/documentation/articles/remoteapp-tutorial-o365anywhere) run the same on any device.

Thanks for sticking with us - back next month with more updates. 