| Resource | Free | Shared (Preview) | Basic | Standard | Premium (Preview)</th> |
| --- | --- | --- | --- | --- | --- |
| [Web, mobile, or API apps](/home/features/app-service/) per [App Service plan](/documentation/articles/azure-web-sites-web-hosting-plans-in-depth-overview/)<sup>1</sup> |10 |100 |Unlimited<sup>2</sup> |Unlimited<sup>2</sup> |Unlimited<sup>2</sup> |
| [App Service plan](/documentation/articles/azure-web-sites-web-hosting-plans-in-depth-overview/) |1 per region |10 per resource group |100 per resource group |100 per resource group |100 per resource group |
| Compute instance type |Shared |Shared |Dedicated<sup>3</sup> |Dedicated<sup>3</sup> |Dedicated<sup>3</sup></p> |
| [Scale-Out](/documentation/articles/web-sites-scale/) (max instances) |1 shared |1 shared |3 dedicated<sup>3</sup> |10 dedicated<sup>3</sup> |20 dedicated<sup>3</sup> |
| Storage<sup>5</sup> |1 GB<sup>5</sup> |1 GB<sup>5</sup> |10 GB<sup>5</sup> |50 GB<sup>5</sup> |500 GB<sup>4,5</sup></p> |
| CPU time (short)<sup>6</sup> |3 minutes |3 minutes |Unlimited, pay at standard [rates](/pricing/details/app-service/)</a> |Unlimited, pay at standard rates |Unlimited, pay at standard rates |
| CPU time (day)<sup>6</sup> |60 minutes |240 minutes |Unlimited, pay at standard [rates](/pricing/details/app-service/)</a> |Unlimited, pay at standard rates |Unlimited, pay at standard rates |
| Memory (1 hour) |1024 MB per App Service plan |1024 MB per app |N/A |N/A |N/A |
| Bandwidth |165 MB |Unlimited, [data transfer rates](/pricing/details/data-transfer/) apply |Unlimited, data transfer rates apply |Unlimited, data transfer rates apply |Unlimited, data transfer rates apply |
| Application architecture |32-bit |32-bit |32-bit/64-bit |32-bit/64-bit |32-bit/64-bit |
| Web Sockets per instance<sup>7</sup> |5 |35 |350 |Unlimited |Unlimited |
| Concurrent [debugger connections](/documentation/articles/web-sites-dotnet-troubleshoot-visual-studio/) per application |1 |1 |1 |5 |5 |
| [chinacloudsites.cn subdomain with FTP/S and SSL](/documentation/articles/web-sites-configure-ssl-certificate/) |X |X |X |X |X |
| [Custom domain](/documentation/articles/web-sites-custom-domain-name/) support | |X |X |X |X |
| Custom domain [SSL support](/documentation/articles/web-sites-configure-ssl-certificate/) | | |Unlimited |Unlimited, 5 SNI SSL and 1 IP SSL connections included |Unlimited, 5 SNI SSL and 1 IP SSL connections included |
| Integrated Load Balancer | |X |X |X |X |
| [Always On](/documentation/articles/web-sites-configure/) | | |X |X |X |
| [Scheduled Backups](/documentation/articles/web-sites-backup/) | | | |Once per day |50 times per day |
| [Auto Scale](/documentation/articles/web-sites-scale/) | | |X |X |X |
| [WebJobs](/documentation/articles/web-sites-create-web-jobs/)<sup>9</sup> |X |X |X |X |X |
| [Azure Scheduler](/home/features/scheduler/) support | |X |X |X |X |
| [Endpoint monitoring](/documentation/articles/web-sites-monitor/) | | |X |X |X |
| [Staging Slots (Preview)](/documentation/articles/web-sites-staged-publishing/) | | | |5 |20 |
| Custom domains per app</a> | |500 |500 |500 |500 |
| SLA | |<p> |99.9% |99.95%<sup>10</sup> |99.95%<sup>10</sup> |

<sup>1</sup>Apps and storage quotas are per App Service plan unless noted otherwise.  
<sup>2</sup>The actual number of apps that you can host on these machines depends on the activity of the apps, the size of the machine instances, and the corresponding resource utilization.  
<sup>3</sup>Dedicated instances can be of different sizes. See [App Service Pricing](/pricing/details/app-service/) for more details.
<sup>5</sup>The storage limit is the total content size across all apps in the
same App Service plan.
<sup>6</sup>These resources are constrained by physical resources on the dedicated instances (the instance size and the number of instances).  
<sup>7</sup>If you scale an app in the Basic tier to two instances, you have 350 concurrent connections for each of the two instances.  
<sup>9</sup>Run custom executables and/or scripts on demand, on a schedule, or continuously as a background task within your App Service instance. Always On is required for continuous WebJobs execution. Azure Scheduler Free or Standard is required for scheduled WebJobs. There is no predefined limit on the number of WebJobs that can run in an App Service instance, but there are practical limits that depend on what the application code is trying to do.   
<sup>10</sup>SLA of 99.95% provided for deployments that use multiple instances with Azure Traffic Manager configured for failover.  

