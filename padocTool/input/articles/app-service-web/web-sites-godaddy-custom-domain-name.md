<!-- not suitable for mooncake -->

<properties
	pageTitle="Configure a custom domain name in Azure Websites (GoDaddy)"
	description="Learn how to use a domain name from GoDaddy with Azure Web Apps"
	services="app-service\web"
	documentationCenter=""
	authors="erikre"
	manager="wpickett"
	editor=""/>

<tags
	ms.service="app-service-web"
	ms.date="09/16/2015"
	wacn.date=""/>

#Configure a custom domain name for an Azure Website (GoDaddy)

[AZURE.INCLUDE [web-selector](../includes/websites-custom-domain-selector.md)]

[AZURE.INCLUDE [intro](../includes/custom-dns-web-site-intro.md)]

[AZURE.INCLUDE [websites-cloud-services-css-guided-walkthrough](../includes/websites-cloud-services-css-guided-walkthrough.md)]

This article provides instructions on using a custom domain name purchased from [Go Daddy](https://godaddy.com) with Azure  Websites.

[WACOM.INCLUDE [introfooter](../includes/custom-dns-web-site-intro-notes.md)]

In this article:

-   [Understanding DNS records](#understanding-records)
-   [Add a DNS record for your custom domain](#bkmk_configurecname)
-   [Enable the domain on your web site](#enabledomain)

<a name="understanding-records"></a>
##Understanding DNS records

[WACOM.INCLUDE [understandingdns](../includes/custom-dns-web-site-understanding-dns-raw.md)]



<a name="bkmk_configurecname"></a>
## Add a DNS record for your custom domain

To associate your custom domain with an Azure Website, you must add a new entry in the DNS table for your custom domain by using tools provided by GoDaddy. Use the following steps to locate the DNS tools for GoDaddy.com

1. Log on to your account with GoDaddy.com, and select **My Account** and then **Manage my domains**. Finally, select the drop-down menu for the domain name that you wish to use with your Azure web app and select **Manage DNS**.

	![custom domain page for GoDaddy](./media/web-sites-godaddy-custom-domain-name/godaddy-customdomain.png)

2. From the **Domain details** page, scroll to the **DNS Zone File** tab. This is the section used for adding and modifying DNS records for your domain name. 

	![DNS Zone File tab](./media/web-sites-godaddy-custom-domain-name/godaddy-zonetab.png)

	Select **Add Record** to add an existing record.

	To **edit** an existing record, select the pen & paper icon beside the record.

	> [AZURE.NOTE] Before adding new records, note that GoDaddy has already created DNS records for popular sub-domains (called **Host** in editor,) such as **email**, **files**, **mail**, and others. If the name you wish to use already exists, modify the existing record instead of creating a new one.

4. When adding a record, you must first select the record type.

	![select record type](./media/web-sites-godaddy-custom-domain-name/godaddy-selectrecordtype.png)

	Next, you must provide the **Host** (the custom domain or sub-domain) and what it **Points to**.

	![add zone record](./media/web-sites-godaddy-custom-domain-name/godaddy-addzonerecord.png)

	* When adding an **A (host) record** - you must set the **Host** field to either **@** (this represents root domain name, such as **contoso.com**,) * (a wildcard for matching multiple sub-domains,) or the sub-domain you wish to use (for example, **www**.) You must set the **Points to** field to the IP address of your Azure web app.
	
		> [AZURE.NOTE] When using A (host) records, you must also add a CNAME record with the following configuration:
		> 
		> * A **Host** value of **awverify** that **Points to** a value of **awverify.&lt;yourwebsitename&gt;.chinacloudsites.cn**.
		> 
		> This CNAME record is used by Azure to validate that you own the domain described by the A record

	* When adding a **CNAME (alias) record** - you must set the **Host** field to the sub-domain you wish to use. For example, **www**. You must set the **Points to** field to the **.chinacloudsites.cn** domain name of your Azure Website. For example, **contoso.azurwebsites.net**.


5. When you have finished adding or modifying records, click **Finish** to save changes.

<a name="enabledomain"></a>
## Enable the domain name on your web app

[WACOM.INCLUDE [modes](../includes/custom-dns-web-site-enable-on-web-site.md)]

