# Content Adaptation Standard and Guidance

This article introduces how to adapt Global technical contents to Azure China Environment.

## Terms replacement

### Domain and endpoint replacement

The following is a list of Domains or endpoints that needs to be replaced in Azure China.

|Service Type |Global |Azure China |
|--------|--------|---------|
|Azure - regular |`*.windows.net` |`*.chinacloudapi.cn` |
|Azure - Compute |`*.cloudapp.net` |`*.chinacloudapp.cn` |
|Azure - Service Fabric Cluster |`*.cloudapp.azure.com` |`*.chinaeast.chinacloudapp.cn` |
|Azure - Storage |`*.blob.core.windows.net`<br/>`*.queue.core.windows.net`<br/>`*.table.core.windows.net`<br/>`*.file.core.windows.net` |`*.blob.core.chinacloudapi.cn`<br/>`*.queue.core.chinacloudapi.cn`<br/>`*.table.core.chinacloudapi.cn`<br/>`*.file.core.chinacloudapi.cn` |
|Azure - Service Management |`https://management.core.windows.net` |`https://management.core.chinacloudapi.cn` |
|Azure - Resource Manager (ARM) |`https://management.azure.com` |`https://management.chinacloudapi.cn` |
|SQL Database |`*.database.windows.net` |`*.database.chinacloudapi.cn` |
|Azure Portal |`https://manage.windowsazure.com`<br/>`https://portal.azure.com` |`https://manage.windowsazure.cn`<br/>`https://portal.azure.cn` |
|Azure SQL Database Management API |`https://management.database.windows.net` |`https://management.database.chinacloudapi.cn` |
|Service Bus |`*.servicebus.windows.net` |`*.servicebus.chinacloudapi.cn` |
|ACS |`*.accesscontrol.windows.net` |`*.accesscontrol.chinacloudapi.cn` |
|HDInsight |`*.azurehdinsight.net` |`*.azurehdinsight.cn` |
|AAD |`*.onmicrosoft.com` |`*.partner.onmschina.cn` |
|AAD Login |`https://login.windows.net`<br/>`https://login.microsoftonline.com` |`https://login.chinacloudapi.cn` |
|AAD Graph API |`https://graph.windows.net` |`https://graph.chinacloudapi.cn` |
|Azure Cognitive Service |`https://api.projectoxford.ai/face/v1.0` |`https://api.cognitive.azure.cn/face/v1.0` |
|Azure Media Services API Server URI |`https://media.windows.net/api/` | China East: `https://wamsshaclus001rest-hs.chinacloudapp.cn/API/`<br/> China North: `https://wamsbjbclus001rest-hs.chinacloudapp.cn/API/` |
||||

There are exception for these damain and endpoint replacements. For Example, in HDInsight, There are articles (like [this one]("https://www.azure.cn/documentation/articles/hdinsight-hadoop-script-actions")) that contain links to Global Azure Storage blobs. Those are sample data or sample script for HDInsight. Replacing those blob endpoints will cause HTTP 404 error while trying to download. Such a link should not be replaced. The following is a list of endpoints that **should not** be replaced.

- hdiconfigactions.blob.core.windows.net
- hditutorialdata.blob.core.windows.net
- sidneyhcontent.blob.core.windows.net
- smf.cloudapp.net
- amsplayer.azurewebsites.net
- aestoken.azurewebsites.net
- sltoken.azurewebsites.net
- dashplayer.azurewebsites.net
- dsahandler.blob.core.windows.net
- dastouri.azurewebsites.net
- auxmktplceprod.blob.core.windows.net
- blitline.blob.core.windows.net
- zumo.blob.core.windows.net
- azuresdkscu.blob.core.windows.net

### Link replacement

1. Relative paths of articles should be replaced with the relative addresses on the site. For Example, "**./virtual-machines-command-line-tools.md**" should be replaced by "**/documentation/articles/virtual-machines-command-line-tools/**".

1. For azure docs links with domain, remove the damain and change it to "**/documentation/articles/.../**". For example "**[https://docs.microsoft.com/azure/storage/storage-create-storage-account#create-a-storage-account](https://docs.microsoft.com/azure/storage/storage-create-storage-account#create-a-storage-account)**" should be replaced with "**/documentation/articles/storage-create-storage-account#create-a-storage-account/**"

1. MSDN or TechNet documents should be replaced by the Chinese version. The basic rule is to replace "**en-us**" with "**zh-cn**" or add "**zh-cn**" between "**.com**" and "**library**" if there is no "**en-us**". For Example, "**[https://msdn.microsoft.com/library/ee460799.aspx](https://msdn.microsoft.com/library/ee460799.aspx)**" should be replaced by "**[https://msdn.microsoft.com/zh-cn/library/ee460799.aspx](https://msdn.microsoft.com/zh-cn/library/ee460799.aspx)**", and "**[https://technet.microsoft.com/library/dn282285.aspx](https://technet.microsoft.com/library/dn282285.aspx)**" should be replaced by "**[https://technet.microsoft.com/zh-cn/library/dn282285.aspx](https://technet.microsoft.com/zh-cn/library/dn282285.aspx)**".

1. Some wikipedia links can be replaced with the Chinese version. For Example, "**[http://en.wikipedia.org/wiki/Adaptive_bitrate_streaming](http://en.wikipedia.org/wiki/Adaptive_bitrate_streaming)**" should be replaced by "**[http://zh.wikipedia.org/wiki/自适性串流](http://zh.wikipedia.org/wiki/自适性串流)**".

1. Some MSDN links are redirected to Azure articles in global site. Those links should be replaced with a relative url on A.CN if exists.

    There are msdn links redirecting to Global Azure articles. For example, **[http://msdn.microsoft.com/zh-cn/library/azure/gg551722.aspx](http://msdn.microsoft.com/library/azure/gg551722.aspx)** is redirecting to **[https://docs.microsoft.com/azure/cloud-services/cloud-services-certs-create](https://docs.microsoft.com/azure/cloud-services/cloud-services-certs-create)**; hence, it should be replaced with "**/documentation/articles/cloud-services-certs-create/**", and check if "**https://www.azure.cn/documentation/articles/cloud-services-certs-create/**" is accessable.
    Furthermore, There are **go.microsoft.com** and **aka.ms** forwarding links redirecting to Global Azure articles. For example, **[http://go.microsoft.com/fwlink/?LinkId=296649](http://go.microsoft.com/fwlink/?LinkId=296649)** is redirecting to **[https://docs.microsoft.com/azure/virtual-network/virtual-networks-overview](https://docs.microsoft.com/azure/virtual-network/virtual-networks-overview)**, so it should be replaced with "**/documentation/articles/virtual-networks-overview/**". And, **[http://aka.ms/runbookauthor/azure/runbookoutput](http://aka.ms/runbookauthor/azure/runbookoutput)** is redirecting to **[https://docs.microsoft.com/azure/automation/automation-runbook-output-and-messages](https://docs.microsoft.com/azure/automation/automation-runbook-output-and-messages)**, so it should be replaced with "**/documentation/articles/automation-runbook-output-and-messages/**". **DO NOT** forget to check the links after replacement.

### Other terminologies

1. **Azure Region**. All Azure Region should be replaced by either "**China North**" or "**China East**".

    There are 28 regions in Global Azure, while there are only 2 in Azure China. Be careful if there are more than 2 regions involved within one article. For example, in [Traffic Manager nested Profile](https://docs.microsoft.com/en-ca/azure/traffic-manager/traffic-manager-nested-profiles), the article involved with 3 regions, **West US**, **West Europe**, and **East Asia**. A simple replacement will create ambiguousness. Hence, in the [A.CN artcle](https://www.azure.cn/documentation/articles/traffic-manager-nested-profiles/), **West US** is replaced with **China North**, **West Europe** is replaced with **China East Site 1**, and **East Asia** is replaced with **China East Site 2**. Here, the traffic manager only involved web sites; hence, such a replacement is meaningful. If the article must have more than 3 regions, delete it from Azure China.

1. **Azure portal**. The Ibiza portal should be replaced by "**Azure Portal Preview**", and the classic portal should be replaced with "**Azure Classic Management Portal**".

1. **Microsoft Azure**. "**Microsoft Azure**" Should be replaced by "**Azure**".

1. **Free trial**. "**Free trial**" should be replaced with "**1rmb trial**".

1. **Azure Login**. AzureChinaCloud Environment should be specified.

    - Azure PowerShell - `Add-AzureAccount -EnvironmentName AzureChinaCloud` or `Add-AzureRmAccount -EnvironmentName AzureChinaCloud`
    - Azure CLI - `azure login -e AzureChinaCloud`

For term replacement, a tool has been developed with python. Here is the [GitHub Repo](https://github.com/bbetstcw/CustomizeTool).

## Deleting not suitable contents

For features that are not available in Azure China, The corresponding technical contents should be removed. Refer to [Azure.cn](https://www.azure.cn) for the latest content for the latest services. The following list are some overall differences between Azure China and Global Azure.

- No free trial is available in Azure China. Only 1rmb trial
- Visual Studio subscriber benefits or MSDN subscriber benefits are not available in Azure China.
- [Azure Resource Explorer](https://resources.azure.com) is not available in Azure China.
- To use Azure CLI 2.0 in Azure China, setting up Azure Context is needed.
- Templates from the GitHub Repo "azure-quickstart-templates" must be modified in order to fit in the Azure China Cloud Environment. For example, replace some endpoints -- "blob.core.windows.net" by "blob.core.chinacloudapi.cn", "cloudapp.azure.com" by "chinacloudapp.cn".
- Application Insights in not available in the new portal for Azure China.
- When using `ARMClient.exe login [environment name]` to login, `[environment name]` should be `MOONCAKE`. In other words, the command to log into China Azure is `ARMClient.exe login MOONCAKE`.

Contents below are differences from Global Azure for Each service in Azure China.

## Compute

### Virtual Machines

| features | Differences |
|---|---|
| `azure feature` in Azure CLI | Not available in Azure China |
| A8-A11, G series, Gs series,<br/> H series, and N series VM| Not available in Azure China |
| Azure Container | Not available in Azure China |
| RDMA cluster | Not available in Azure China |
| Operations Management Suite | Not available in Azure China |
| Extensions | [Some of them](#table_of_unavailable_extentions) are not available, and most of them are not manageable in the <br/> new portal except "PowerShell DSC (Desired State Configuration) Extension" |

<a name="table_of_unavailable_extentions"></a>
**Table of unavailable extentions**

| Extensions | | |
|---|---|---|
| MS Enterprise Application | Centos Chef Client | Chef Client |
| Linux Chef Client | Puppet Enterprise Agent | Cloud Link Secure VM Windows Agent |
| McAfee Endpoint Security | Portal Protect Extension | Remote Debug VS14CTP |
| Remote Debug VS2013 | Remote DebugV S2012 | Hpc Vm Drivers |
| Symantec | Acronis Backup | Datadog Windows Agent |
| VM Snapshot Linux | Acronis Backup Linux | Puppet Agent |
| Site 24x7 Apm Insight | BMC CTM Agent Linux | Dynatrace Linux |
| Site 24x7 Linux Server | BMC CTM Agent Windows | Dynatrace Windows |
| Site 24x7 Windows Server | HPE Security Application Defender | Trend Micro DSA Linux |
| Datadog Linux Agent | | |

#### 1. Virtual Machines Windows

| features | Differences |
|---|---|
| ARM mode HPC Windows | Not available in Azure China |
| Hybrid Use Benefit and "bring your own license (BYOL)" | Not publically available in Azure China |
| Symantec | Not available in Azure China |
| Always On availability group | Cannot be configured through the new portal in Azure China |
| Marketplace Images: <ul><li>Oracle Windows</li><li>DynamicsNAV</li><li>MicrosoftSharePointServer</li><li>WindowsServerEssentials</li><li>HPC Pack 2016 cluster</li></ul>| Not available in Azure China |

#### 2. Virtual Machines Linux

| features | Differences |
|---|---|
| Docker Extension | Available but cannot be installed properly in Azure China |
| HPC Linux | Not available in Azure China |
| Linux Sap | Not available in Azure China |
| Marketplace Images: <ul><li>Redhat</li><li>RancherOS</li><li>Bitnami</li><li>Mesosphere</li><li>Docker</li><li>Jenkins</li><li>MariaDB Enterprise cluster</li><li>Oracle Linux</li></ul>| Not available in Azure China |

### Virtual Machine Scale Sets

| features | Differences |
|---|---|
| Vertical scaling | Not suitable for Azure China |

### Service Fabric

| features | Differences |
|---|---|
| Container related content | Not available in Azure China |
| Service Fabric for linux | Not available in Azure China |

### Batch

| features | Differences |
|---|---|
|"Log Analytics" related content | Not available in Azure China |

### Cloud Services

| features | Differences |
|---|---|
| Continuous delivery using VSO | Not available in Azure China |
| Diagnostics using Application Insights | Not available in Azure China |
| Preview portal related features | Not available in Azure China |

## Networking

### Virtual Network

| features | Differences |
|---|---|
| Azure DNS | Not available in Azure China |
| Accelerated networking | Not available in Azure China |
|"Log Analytics" related content | Not available in Azure China |

### Load Balancer

| features | Differences |
|---|---|
|"Log Analytics" related content | Not available in Azure China |

### Application Gateway

| features | Differences |
|---|---|
|"Log Analytics" related content | Not available in Azure China |

### VPN Gateway

| features | Differences |
|---|---|
|"Log Analytics" related content | Not available in Azure China |

### Traffic Manager

| features | Differences |
|---|---|
| Regions | Only 2 regions in Azure China, so nested profile can only involve 2 regions |

### Expressroute

| features | Differences |
|---|---|
| Bandwidth upgrade | Not available in Azure China |
| NAT related features | Not available in Azure China |
| NSP/EXP related features | Not available in Azure China |
| Share circuit | Not available in Azure China |
| Asymmetric routing | Not available in Azure China |
| Microsoft peering | Not available in Azure China |
| SKU of UltraPerformance | Not available in Azure China |

## Storage

### Storage

| features | Differences |
|---|---|
| ZRS | Not available in Azure China |
| Storage connection string|<p>Global Azure: `DefaultEndpointsProtocol=https;AccountName=storagesample;AccountKey=<account-key>`</P><P>Azure China: `DefaultEndpointsProtocol=https;AccountName=storagesample;AccountKey=<account-key>;EndpointSuffix=core.chinacloudapi.cn`</P> |
| disk encryption | Not available in Azure China |
| Import/export service For classic mode | Not available in Azure China |


### Backup

| features | Differences |
|---|---|
| Ibiza portal related content | Not available in Azure China |

### Site Recovery

| features | Differences |
|---|---|
| Site Recovery for VMware | Not available in Azure China |
| Ibiza portal related content | Not available in Azure China |
| Mobility Service | Not available in Azure China |

## Web + Mobile

### App Service

| features | Differences |
|---|---|
| App Service Environment | Not available in Azure China |
| Authentication with Google, Facebook, or Twitter | Not available in Azure China |
| Logic App | Not available in Azure China |
| App Service Linux | Not available in Azure China |
| Marketplace Templates like "Web App + SQL",<br/> "Web App + MySQL", and "Wordpress Web App" | Not available in Azure China |
| "Try App Service" | Not available in Azure China |
| Hybrid connection | Not available in Azure China |
| BizTalk Services | Not available in Azure China |
| Source controls | <ul><li>Source controls other than Git or Mercurial are not available in Azure China. <br/> (For example, TFS (not using Git), OneDrive, and Dropbox)</li><li>When Setting up deployment for source control, only local git repository and <br/> external repository are available for Azure China. More details on source control <br/> and continuous deployment, please read [continuous deployment differences](#continuous-deployment-differences).</li></ul>|

<a name="continuous-deployment-differences"></a>
**Continuous deployment differences**:

- Deployment credentials cannot be set up through the new portal. Hence, if seeing deployment credentials setup, replace it with a classic portal solution.
- Since only local git repository and external repository are available for Azure China, continuous deployment can only be set in KUDU with Webhook. For more details, see [Continuous Deployment to Azure App Service](https://www.azure.cn/documentation/articles/app-service-continuous-deployment/)
- In Azure China, deployment cannot be viewed or rolled back in the new portal yet. But, it can be done through the classic portal.

#### 1. App Service Web

| features | Differences |
|---|---|
| Azure Toolkit for Eclipse | Not available in Azure China |
| Azure Toolkit for IntelliJ | Not available in Azure China |
| "Buy domain" and "GoDaddy" | Not available in Azure China |
| "Azure DNS" and "purchase  SSL" | Not available in Azure China |
| New Relic | Not available in Azure China (It's possible to configure through KUDU) |
| SendGrid | Not available in Azure China (It's possible to configure through KUDU) |
| ClearDB | Not available in Azure China |
| Migration from IIS | Not available in Azure China |
| WebMatrix | Need to use publish setting profile |

#### 2. App Service API

| features | Differences |
|---|---|
| API Management | Not available in Azure China |

#### <a name="app-service-mobile"></a> 3. App Service Mobile

| features | Differences |
|---|---|
| GCM(Google Cloud Messaging) | Not available in Azure China |

### Mobile services

*Will migrate to App service mobile.*  See the info of [App service mobile](#app-service-mobile).

### Media Services

| features | Differences |
|---|---|
| Steps for connecting to Media Services service endpoint | See details [below](#steps-for-connecting-to-media-mervices-service-endpoint) |
| Code for creating CloudMediaContext | See details [below](#code-for-creating-cloudmediacontext) |
| premium workflow | Not available in Azure China |
| Axinon integration | Not available in Azure China |
| Ibiza portal related content | Not available in Azure China |

#### <a name="steps-for-connecting-to-media-mervices-service-endpoint"></a> 1. Steps for connecting to Media Services service endpoint is different in Azure China

- **Connecting to Media Services in Global Azure**:

    1. Getting an access token 
    2. Connecting to the Media Services URI(https://media.windows.net)
    3. Post your subsequent API calls to the new URL.

- **Connecting to Media Services in Azure China**:

    Directly post API calls to Media Services URI(ShangHai: https://wamsshaclus001rest-hs.chinacloudapp.cn/API/ ; Beijing: https://wamsbjbclus001rest-hs.chinacloudapp.cn/API/)

    **Example**:

    *Global Azure article(media-services-rest-connect-programmatically.md)*

    The following steps describe the most common workflow when using the Media Services REST API to connect to Media Services:

    1. Getting an access token 
    2. Connecting to the Media Services URI 

        >[AZURE.NOTE] After successfully connecting to https://media.windows.net, you will receive a 301 redirect specifying another Media Services URI. You must make subsequent calls to the new URI.
        You may also receive a HTTP/1.1 200 response that contains the ODATA API metadata description.

    3. Post your subsequent API calls to the new URL. 

        For example, if after trying to connect, you got the following:

            HTTP/1.1 301 Moved Permanently
            Location: https://wamsshaclus001rest-hs.windows.net/api/

        You should post your subsequent API calls to https://wamsbayclus001rest-hs.windows.net/api/.

    *Azure China article(media-services-rest-connect-programmatically.md)*

    The following steps describe the most common workflow when using the Media Services REST API to connect to Media Services:

    1. Getting an access token 
    2. Connecting to the Media Services URI 

        >[AZURE.NOTE] ShangHai DC URI: https://wamsshaclus001rest-hs.chinacloudapp.cn/API/; Beijing DC URI: https://wamsbjbclus001rest-hs.chinacloudapp.cn/API/

    3. Post your API calls to the target URL. 



#### <a name="code-for-creating-cloudmediacontext"></a> 2. Code difference when creating CloudMediaContext

- For Global Azure

        // Read values from the App.config file.
            private static readonly string _mediaServicesAccountName =
                ConfigurationManager.AppSettings["MediaServicesAccountName"];
            private static readonly string _mediaServicesAccountKey =
                ConfigurationManager.AppSettings["MediaServicesAccountKey"];

            // Field for service context.
            private static CloudMediaContext _context = null;
            private static MediaServicesCredentials _cachedCredentials = null;

            static void Main(string[] args)
            {
                try
                {
                    // Create and cache the Media Services credentials in a static class variable.
                    _cachedCredentials = new MediaServicesCredentials(
                                    _mediaServicesAccountName,
                                    _mediaServicesAccountKey);
                    // Used the chached credentials to create CloudMediaContext.
                    _context = new CloudMediaContext(_cachedCredentials);
                    ...

- For Azure China

        // Read values from the App.config file.
            private static readonly string _mediaServicesAccountName =
                ConfigurationManager.AppSettings["MediaServicesAccountName"];
            private static readonly string _mediaServicesAccountKey =
                ConfigurationManager.AppSettings["MediaServicesAccountKey"];

            private static readonly String _defaultScope = "urn:WindowsAzureMediaServices";

        // Azure China uses a different API server and a different ACS Base Address from the Global.
        private static readonly String _chinaApiServerUrl = "https://wamsshaclus001rest-hs.chinacloudapp.cn/API/";
        private static readonly String _chinaAcsBaseAddressUrl = "https://wamsprodglobal001acs.accesscontrol.chinacloudapi.cn";

            // Field for service context.
            private static CloudMediaContext _context = null;
        private static MediaServicesCredentials _cachedCredentials = null;
        private static Uri _apiServer = null;

            static void Main(string[] args)
            {
                try
                {
                    // Create and cache the Media Services credentials in a static class variable.
                    _cachedCredentials = new MediaServicesCredentials(
                                    _mediaServicesAccountName,
                                    _mediaServicesAccountKey,
                    _defaultScope,
                    _chinaAcsBaseAddressUrl);

            // Create the API server Uri
            _apiServer = new Uri(_chinaApiServerUrl);

                    // Used the chached credentials to create CloudMediaContext.
                    _context = new CloudMediaContext(_apiServer, _cachedCredentials);

### Notification-hubs
| features | Differences |
|---|---|
| Google Android, GCM(Google could message) | Not available in Azure China |

## Databases

### SQL Database

| features | Differences |
|---|---|
| Long term retention | Not available in Azure China |
| Long term retention | Not available in Azure China |
| Elastic Job | Not available in Azure China |
| In-memory table | Not available in Azure China |

### SQL Data Warehouse

| features | Differences |
|---|---|
| Auditing/threat-detection | Not available in Azure China |
| Integration with Azure Data Factory/machine learning/PBI | Not available in Azure China |
| Partner data integration | Not available in Azure China |

### Documentdb

| features | Differences |
|---|---|
| "quick start" | Not available in the new portal of Azure China for both Nosql(Documentdb) and MongoDB |
| "Resource Health" | Not available in the new portal of Azure China for both Nosql(Documentdb) and MongoDB |
| "New Support Request" | Not available in the new portal of Azure China for both Nosql(Documentdb) and MongoDB |

### Redis Cache

| features | Differences |
|---|---|
| "Diagnose and solve problems" | Not available in the new portal of Azure China |
| "Resource health" | Not available in the new portal of Azure China |

## Intelligence + Analytics

### HDInsight

| features | Differences |
|---|---|
| ARM HDInsight cluster | Not available in Azure China |
| Linux HDInsight | Not available in Azure China |
| Azure CLI | HDInsight cluster is not manageable by 0.10.x but 0.9.x |
| Microsoft Azure HDInsight Management Library | Since ARM HDInsight is not available, "Microsoft.Azure.Management.HDInsight" dotnet package <br/> is not suitable for Azure China. Instead, "Microsoft.WindowsAzure.Management.HDInsight" can be <br/> used. However, "Microsoft.Azure.Management.HDInsight.Job" is good for Azure China, because it's for hadoop job only.
| The new Portal | Since ARM HDInsight is not available, HDInsight cluster is not manageable by the new portal |
| Apache Kafka | Not available in Azure China |
| Spark | Not available in Azure China |
| Ambari | Not available in Azure China , because it's for Linux cluster only |
| HDInsight application | Not available in Azure China , because it's for Linux cluster only |
| Domain-joined HDInsight clusters | Not available in Azure China |
| R Server on HDInsight | Not available in Azure China |

### Stream Analytics

| features | Differences |
|---|---|
| Data lake output | Not available in Azure China |
| Documentdb output | Not available in Azure China |
| Store data from Stream analytic in Redis Cache | Not available in Azure China |
| Machine Learning integration in Stream Analytics | Not available in Azure China |
| Using Power BI as output of Stream analytics | Not available in Azure China |
| Scale with Machine Learning functions | Not available in Azure China |
| Set up alerts | Not available in Azure China |
| Twitter setiment analysis | Not available in Azure China |

## Internet of Things

### IoT hub

| features | Differences |
|---|---|
| Certified devices | Not available in Azure China |

### IoT suite

| features | Differences |
|---|---|
| Bing Maps API | Not available in Azure China |
| Predictive Maintenance | Not available in Azure China |
| Logic apps | Not available in Azure China |

### Event hubs

| features | Differences |
|---|---|
| Archive features | Not available in Azure China |
| Preview portal related features | Not available in Azure China |

## Enterprise Integration

### Service bus

| features | Differences |
|---|---|
| Premium messaging | Not available in Azure China |
| Creating namespace through preview portal | Not available in Azure China |

## Security + Identity

### Key-Vault

| features | Differences |
|---|---|
| HSM(hardware security module) | Not available in Azure China |
| key-vault logging | Not available in Azure China |

### Active Directory

| features | Differences |
|---|---|
| Device writeback | Not available in Azure China |
| Connect health | Not available in Azure China |
| Groups | Not available in Azure China |
| Access management | Not available in Azure China |
| Application proxy | Not available in Azure China |
| Azure adjoin | Not available in Azure China |
| B2B | Not available in Azure China |
| B2C | Not available in Azure China |
| Domain services | Not available in Azure China |
| Cloud app discovery | Not available in Azure China |
| Conditional access | Not available in Azure China |
| Hybrid identity | Not available in Azure China |
| Identity protection | Not available in Azure China |
| Privileged identity | Not available in Azure China |
| Reporting | Not available in Azure China |
| Saas | Not available in Azure China |
| Windows enterprise state roaming | Not available in Azure China |
| Ibiza portal related content. | Not available in Azure China |
|Basic and premium version | Not available in Azure China |

### MFA

| features | Differences |
|---|---|
| MFA on-premises | Not available in Azure China, only MFA on cloud are available in Azure China|

## Monitoring + Management

### Automation

| features | Differences |
|---|---|
| ARM Automation | Not available in Azure China, so Automation is not manageable in the new portal|
| DSC configuration | Not available in Azure China |
| Graphical Runbook and PowerShell Runbook | Not available in Azure China |
| Hybrid Runbook | Not available in Azure China |
| Migration from Orchestrator to Azure Automation | Not available in Azure China |
| Azure Automation webhooks | Not available in Azure China |

### Scheduler

| features | Differences |
|---|---|
| Scheduler Outbound Authentication | <ul><li>Global Azure - "audience":"https://management.core.windows.net/"</li><li>Azure China - "audience":"https://management.core.chinacloudapi.cn/"</li></ul> See [the sample below](#example) |

#### <a name="example"></a> 2. Example

Sample REST Request for Basic Authentication

- Global Azure

        PUT https://management.azure.com/subscriptions/1d908808-e491-4fe5-b97e-29886e18efd4/resourceGroups/CS-SoutheastAsia-scheduler/providers/Microsoft.Scheduler/jobcollections/southeastasiajc/jobs/httpjob?api-version=2016-01-01 HTTP/1.1
        User-Agent: Fiddler
        Host: management.azure.com
        Authorization: Bearer sometoken
        Content-Length: 562
        Content-Type: application/json; charset=utf-8

        {
        "properties": {
            "startTime": "2015-05-14T14:10:00Z",
            "action": {
            "request": {
                "uri": "https://mywebserviceendpoint.com",
                "method": "GET",
                "headers": {
                "x-ms-version": "2013-03-01"
                },
                "authentication": {
                "type": "basic",
                "username": "user",
                "password": "password"
                }
            },
            "type": "http"
            },
            "recurrence": {
            "frequency": "minute",
            "endTime": "2016-04-10T08:00:00Z",
            "interval": 1
            },
            "state": "enabled",
        }
        }


- Azure China

        PUT https://management.chinacloudapi.cn/subscriptions/1fe0abdf-581e-4dfe-9ec7-e5cb8e7b205e/resourceGroups/CS-SoutheastAsia-scheduler/providers/Microsoft.Scheduler/jobcollections/southeastasiajc/jobs/httpjob?api-version=2016-01-01 HTTP/1.1
        User-Agent: Fiddler
        Host: management.chinacloudapi.cn
        Authorization: Bearer sometoken
        Content-Type: application/json; charset=utf-8

        {
          "properties": {
            "startTime": "2015-05-14T14:10:00Z",
            "action": {
              "request": {
                "uri": "https://mywebserviceendpoint.com",
                "method": "GET",
            "headers": {
                  "x-ms-version": "2013-03-01"
                },
            "authentication": {
                  "type": "clientcertificate",
                  "password": "password",
                  "pfx": "pfx key"
                }
              },
              "type": "http"
            },
            "recurrence": {
              "frequency": "minute",
              "endTime": "2016-04-10T08:00:00Z",
              "interval": 1
            },
            "state": "enabled",
          }
        }

### Azure Resource Manager
| features | Differences |
|---|---|
| resource providers or resource types | some resource providers or resource types are not available in Azure China |

**Resource Providers not available in Azure China**

| Resource Providers | | |
|---|---|---|
| Microsoft.Automation | Microsoft.BingMaps | Microsoft.BizTalkServices |
| Microsoft.ContainerService | Microsoft.Logic | Microsoft.MobileEngagement |
| Microsoft.OperationalInsights | Microsoft.ResourceHealth | Microsoft.Search |
| Microsoft.Security | microsoft.visualstudio | SuccessBricks.ClearDB |
| Microsoft.ADHybridHealthService | microsoft.support | |

**Resource Types not available in Azure China**

| Resource Types | | |
|---|---|---|
| Microsoft.HDInsight/clusters |

### Azure portal

| features | Differences |
|---|---|
| Monitoring Metrics | Not available in Azure China |
| Monitoring Diagnostics logs | Not available in Azure China |
| Monitoring Alerts | Not available in Azure China |
| Monitoring Application Insights | Not available in Azure China |
| Monitoring features except Active Log | Not available in Azure China |

## Some detailed customizations

For some important articles, contents may not be suitable for Azure China. However, if a substitute solution exits, those articles still can be customized.

For example, in App Service of Azure China Environment. Continuous deployment is not possible to be set through the Portal. However, it can be done for public Repo in GitHub with KUDU and Webhook. Since, the continuous deployment functionality is quite important for App Service, and it's related with Agile Development which is also very important for App Service. Customizing the article other than simply deleting it would be a good idea. [This A.CN article](https://www.azure.cn/documentation/articles/app-service-continuous-deployment/) is for this scenario, and the [A.COM article](https://docs.microsoft.com/en-us/azure/app-service-web/app-service-continuous-deployment) is the orinal article.

However, if the features involved become available in Azure China, those customizations will not be needed any more. That is what happened for Redis Cache. Before the Ibiza portal is available in Azure China, Redis Cache could only be manageable with Azure PowerShell or Azure CLI. So, all portal solutions were replaced by command line solutions. After Redis Cache is available in the preview portal, all those customizations should be rolled back.