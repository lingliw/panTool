<properties 
	pageTitle="Playback your content" 
	description="This topic lists existing players that you can use to playback your content." 
	services="media-services" 
	documentationCenter="" 
	authors="Juliako" 
	manager="dwrede" 
	editor=""/>

<tags
	ms.service="media-services"
	ms.date="09/07/2015"
	wacn.date=""/>


#Playing your content with existing players

Azure Media Services supports many popular streaming formats, such as Smooth Streaming, HTTP Live Streaming, and MPEG-Dash. This topic points you to existing players that you can use to test your streams.  

>[AZURE.NOTE]To play dynamically packaged or dynamically encrypted content, make sure to get at least one streaming unit for the streaming endpoint from which you plan to deliver your content. For information about scaling streaming units, see: [How to scale streaming units](/documentation/articles/media-services-manage-origins#scale_streaming_endpoints).

###Azure Management Portal Media Services content Player

The **Azure Management Portal** provides a content player that you can use to test your video.

Click on the desired video (make sure it was [published](/documentation/articles/media-services-manage-content#publish)) and click the **Play** button at the bottom of the portal. 
 
Some considerations apply:

- The **MEDIA SERVICES CONTENT PLAYER** plays from the default streaming endpoint. If you want to play from a non-default streaming endpoint, use another player. For example, [Azure Media Services Player](http://amsplayer.azurewebsites.net/azuremediaplayer.html).
 

![AMSPlayer][AMSPlayer]

###Azure Media Services Player

Use [Azure Media Services Player](http://amsplayer.azurewebsites.net/azuremediaplayer.html) to playback your content (clear or protected) in any of the following formats:

- Smooth Streaming
- MPEG DASH
- HLS
- Progressive MP4


###Flash Player

####AES-encrypted with Token 

[http://aestoken.azurewebsites.net]("http://aestoken.azurewebsites.net)

###Silverlight Players

####Monitoring

[http://smf.cloudapp.net/healthmonitor](http://smf.cloudapp.net/healthmonitor)

####PlayReady with Token

[http://sltoken.azurewebsites.net](http://sltoken.azurewebsites.net)

### DASH Players

[http://dashplayer.azurewebsites.net](http://dashplayer.azurewebsites.net)

[http://dashif.org](http://dashif.org)

###Other

To test HLS URLs you can also use:

- **Safari** on an iOS device or
- **3ivx HLS Player** on Windows.

##Developing video players

For information about how to develop your own players, see [Developing video players](/documentation/articles/media-services-develop-video-players)

<!-- deleted by customization

##Media Services learning paths

You can view AMS learning paths here:

- [AMS Live Streaming Workflow](http://azure.microsoft.com/documentation/learning-paths/media-services-streaming-live/)
- [AMS on Demand Streaming Workflow](http://azure.microsoft.com/documentation/learning-paths/media-services-streaming-on-demand/)
-->
 
[AMSPlayer]: ./media/media-services-playback-content-with-existing-players/media-services-portal-player.png 