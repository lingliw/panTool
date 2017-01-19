<properties 
	pageTitle="How to encode an asset using Media Encoder Standard" 
	description="This topic shows how to use .NET to encode an asset using Media Encoder Strandard." 
	services="media-services" 
	documentationCenter="" 
	authors="juliako,anilmur" 
	manager="dwrede" 
	editor=""/>

<tags
	ms.service="media-services"
	ms.date="12/02/2015"
	wacn.date=""/>


#How to encode an asset using Media Encoder Standard

Encoding jobs are one of the most common processing operations in Media Services. You create encoding jobs to convert media files from one encoding to another. When you encode, you can use the Media Services built-in Media Encoder. You can also use an encoder provided by a Media Services partner; third party encoders are available through the Azure Marketplace. 

This topic shows how to use .NET to encode your assets with Media Encoder Standard (MES). Media Encoder Standard is configured using one of the encoder presets described [here](https://msdn.microsoft.com/zh-cn/library/azure/mt269960.aspx).

It is recommended to always encode your mezzanine files into an adaptive bitrate MP4 set and then convert the set to the desired format using the [Dynamic Packaging](/documentation/articles/media-services-dynamic-packaging-overview). To take advantage of dynamic packaging, you must first get at least one On-demand streaming unit for the streaming endpoint from which you plan to delivery your content. For more information, see [How to Scale Media Services](/documentation/articles/media-services-manage-origins#scale_streaming_endpoints).

If your output asset is storage encrypted, you must configure asset delivery policy. For more information see [Configuring asset delivery policy](/documentation/articles/media-services-dotnet-configure-asset-delivery-policy).

###MES Formats

[Formats and codecs](/documentation/articles/media-services-media-encoder-standard-formats)

###MES Presets

Media Encoder Standard is configured using one of the encoder presets described [here](https://msdn.microsoft.com/zh-cn/library/azure/mt269960.aspx).

###MES Input and output metadata

The encoders input metadata is described [here](http://msdn.microsoft.com/zh-cn/library/azure/dn783120.aspx).

The encoders output metadata is described [here](http://msdn.microsoft.com/zh-cn/library/azure/dn783217.aspx).


##Example

The following code example uses Media Services .NET SDK to perform the following tasks:

- Create an encoding job.
- Get a reference to the Media Encoder Standard encoder.
- Specify to use the "H264 Multiple Bitrate 720p" preset. You can see all the presets [here](https://msdn.microsoft.com/zh-cn/library/azure/mt269960.aspx). You can also examine the schema to which these presets must comply [here](https://msdn.microsoft.com/zh-cn/library/mt269962.aspx) topic.
- Add a single encoding task to the job. 
- Specify the input asset to be encoded.
- Create an output asset that will contain the encoded asset.
- Add an event handler to check the job progress.
- Submit the job.
		
		static public IAsset EncodeToAdaptiveBitrateMP4Set(IAsset asset)
		{
		    // Declare a new job.
		    IJob job = _context.Jobs.Create("Media Encoder Standard Job");
		    // Get a media processor reference, and pass to it the name of the 
		    // processor to use for the specific task.
		    IMediaProcessor processor = GetLatestMediaProcessorByName("Media Encoder Standard");
		

		    // Create a task with the encoding details, using a string preset.
		    // In this case "H264 Multiple Bitrate 720p" preset is used.
		    ITask task = job.Tasks.AddNew("My encoding task",
		        processor,
		        "H264 Multiple Bitrate 720p",
		        TaskOptions.None);
		
		    // Specify the input asset to be encoded.
		    task.InputAssets.Add(asset);
		    // Add an output asset to contain the results of the job. 
		    // This output is specified as AssetCreationOptions.None, which 
		    // means the output asset is not encrypted. 
		    task.OutputAssets.AddNew("Output asset",
		        AssetCreationOptions.None);
		
		    job.StateChanged += new EventHandler<JobStateChangedEventArgs>(JobStateChanged);
		    job.Submit();
		    job.GetExecutionProgressTask(CancellationToken.None).Wait();
		
		    return job.OutputMediaAssets[0];
		}
		
		private static void JobStateChanged(object sender, JobStateChangedEventArgs e)
		{
		    Console.WriteLine("Job state changed event:");
		    Console.WriteLine("  Previous state: " + e.PreviousState);
		    Console.WriteLine("  Current state: " + e.CurrentState);
		    switch (e.CurrentState)
		    {
		        case JobState.Finished:
		            Console.WriteLine();
		            Console.WriteLine("Job is finished. Please wait while local tasks or downloads complete...");
		            break;
		        case JobState.Canceling:
		        case JobState.Queued:
		        case JobState.Scheduled:
		        case JobState.Processing:
		            Console.WriteLine("Please wait...\n");
		            break;
		        case JobState.Canceled:
		        case JobState.Error:
		
		            // Cast sender as a job.
		            IJob job = (IJob)sender;
		
		            // Display or log error details as needed.
		            break;
		        default:
		            break;
		    }
		}
		
		
		private static IMediaProcessor GetLatestMediaProcessorByName(string mediaProcessorName)
		{
		    var processor = _context.MediaProcessors.Where(p => p.Name == mediaProcessorName).
		    ToList().OrderBy(p => new Version(p.Version)).LastOrDefault();
		
		    if (processor == null)
		        throw new ArgumentException(string.Format("Unknown media processor", mediaProcessorName));
		
		    return processor;
		}


Use the [User Voice](http://go.microsoft.com/fwlink/?linkid=698785&clcid=0x409) forum to provide feedback and make suggestions on how to improve Azure Media Services. You can also go directly to one of the following categories: 

- [Azure Media Player](https://feedback.azure.com/forums/169396-media-services/category/109320-azure-media-player)
- [Client SDK Libraries](https://feedback.azure.com/forums/169396-media-services/category/144435-client-sdks)
- [Encoding and Processing](https://feedback.azure.com/forums/169396-media-services/category/144411-encoding-and-processing)
- [Live Streaming](https://feedback.azure.com/forums/169396-media-services/category/144414-live-streaming)
- [Azure Management Portal](https://feedback.azure.com/forums/169396-media-services/category/144432-portal)
- [REST API and Platform](https://feedback.azure.com/forums/169396-media-services/category/144423-rest-api-and-platform)
- [VoD Streaming](https://feedback.azure.com/forums/169396-media-services/category/144429-vod-streaming)

##See Also 

[How to generate thumbnail using Media Encoder Standard with .NET](/documentation/articles/media-services-dotnet-generate-thumbnail-with-mes)
[Media Services Encoding Overview](/documentation/articles/media-services-encode-asset)