<properties
   pageTitle="Create a custom probe for an application gateway by using the portal | Azure"
   description="Learn how to create a custom probe for Application Gateway by using the portal"
   services="application-gateway"
   documentationCenter="na"
   authors="georgewallace"
   manager="carmonm"
   editor=""
   tags="azure-resource-manager"
/>
<tags
	ms.service="application-gateway"
	ms.date="08/09/2016"
	wacn.date=""/>

# Create a custom probe for Application Gateway by using the portal

> [AZURE.SELECTOR]
- [Azure portal](/documentation/articles/application-gateway-create-probe-portal/)
- [Azure Resource Manager PowerShell](/documentation/articles/application-gateway-create-probe-ps/)
- [Azure Classic PowerShell](/documentation/articles/application-gateway-create-probe-classic-ps/)

<BR>

Custom probes allows you to have more granular control about health monitoring status for your back end pool of servers. You can change the interval checks, failed request threshold and timeout settings.

This article will guide you to create an application gateway with a custom probe or adding a custom probe to an existing application gateway. 


## Scenario

The following scenario goes through creating a custom health probe in an existing application gateway.
The scenario assumes that you have already followed the steps to [Create an Application Gateway](/documentation/articles/application-gateway-create-gateway-portal/).

## <a name="createprobe"></a>Create the probe

Probes are configured in a two-step process through the portal. The first step is to create the probe, next you add the probe to the backend http settings of the application gateway.

### Step 1

Navigate to http://portal.azure.cn and select an existing application gateway.

![Application Gateway overview][1]

### Step 2

Click **Probes** and click the **Add** button to add a new probe.

![Add Probe blade with information filled out][2]

### Step 3

Fill out the required information for the probe and when complete click **OK**.

- **Name** - This is a friendly name to the probe that is accessible in the portal.
- **Host** - This is the host name that is used for the probe.
- **Path** - The remainder of the full url for the custom probe.
- **Interval (secs)** - How often the probe is run to check for health.
- **Timeout (secs)** - The amount of time the probe waits before timing out.
- **Unhealthy threshold** - Number of failed attempts to be considered unhealthy.

> [AZURE.IMPORTANT] the host name is not the server name. This is the name of the virtual host running on the application server. The probe is sent to http://(host name):(port from httpsetting)/urlPath

![probe configuration settings][3]

## Add probe to the gateway

Now that the probe has been created, it is time to add it to the gateway. Probe settings are set on the backend http settings of the application gateway.

### Step 1

Click the **HTTP settings** of the application gateway, and then click the current backend http settings in the window to bring up the configuration blade.

![https settings window][4]

### Step 2

On the **appGatewayBackEndHttp** settings blade, click **Use custom probe** and choose the probe created in the [Create the probe](#createprobe) section.
When complete, click **OK** and the settings are applied.

![appgatewaybackend settings blade][5]

The default probe checks the default access to the web application. Now that a custom probe has been created, the application gateway uses the custom path defined to monitor health for the backend selected. Based on the criteria that was defined, the application gateway checks the file
specified in the probe. If the call to host:Port/path does not return an Http 200 OK status response, the server is taken out of rotation, after the unhealthy threshold is reached. Probing continues on the unhealthy instance to determine when it becomes healthy again. Once the instance is added back to healthy server pool traffic begins flowing to it again and probing to the instance continues at user specified interval as normal.


## Next steps

To learn how to configure SSL Offloading with Azure Application Gateway see [Configure SSL Offload](/documentation/articles/application-gateway-ssl-portal/)

[1]: ./media/application-gateway-create-probe-portal/figure1.png
[2]: ./media/application-gateway-create-probe-portal/figure2.png
[3]: ./media/application-gateway-create-probe-portal/figure3.png
[4]: ./media/application-gateway-create-probe-portal/figure4.png
[5]: ./media/application-gateway-create-probe-portal/figure5.png