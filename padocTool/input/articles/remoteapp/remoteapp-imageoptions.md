<properties 
    pageTitle="Create an Azure RemoteApp image"
    description="Learn about the options available for creating images for Azure RemoteApp" 
    services="remoteapp" 
    documentationCenter="" 
    authors="lizap" 
    manager="mbaldwin" />

<tags 
    ms.service="remoteapp" 
    ms.date="08/12/2015" 
    wacn.date="" />



# Create an Azure RemoteApp image

Azure RemoteApp uses images to hold the apps that you share with your users. To create an Azure RemoteApp collection with your choice of applications, whether it is cloud or hybrid, you  start by creating an image with those applications installed. Then, create a collection that uses that image, assign users to the collection, and publish apps to those users. 

You have several options for creating or using images. The basic [requirement](/documentation/articles/remoteapp-imagereqs) for an image is that it run Windows Server 2012 R2 and have the Remote Desktop Session Host (RDSH) role installed. How you get that is where things get interesting.

You have the following options when it comes to images:

- You can import and use an [image based on an Azure virtual machine](/documentation/articles/remoteapp-image-on-azurevm). This is good for line-of-business apps that require custom settings. You can customize the image to work for the app.
- You can [create and upload a custom image](/documentation/articles/remoteapp-create-custom-image). This is good if you already have an image that you use for your on-premises Remote Desktop Services deployment.
- You can use one of the [template images](/documentation/articles/remoteapp-images) included in your RemoteApp subscription. These images are created and maintained by the RemoteApp team and contain some standard applications (like the Office suite) that you can make available to your users. Note that only the Office 365 Pro Plus image can be used in a production setting.

Regardless of where you get your image or how you create it, you'll want to make sure you understand the [app requirements](/documentation/articles/remoteapp-appreqs) to ensure that your app works well in RemoteApp. Then, the next step is to create a [cloud](/documentation/articles/remoteapp-create-cloud-deployment) or [hybrid](/documentation/articles/remoteapp-create-hybrid-deployment) collection.
 