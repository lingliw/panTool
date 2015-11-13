<properties 
	pageTitle="Use Active Directory for authentication in Azure Websites" 
	description="Learn the different authentication and authorization options for line-of-business applications that are deployed to Azure Websites" 
	services="app-service" 
	documentationCenter="" 
	authors="cephalin" 
	manager="wpickett" 
	editor="jimbe"/>

<tags
	ms.service="app-service"
	ms.date="09/29/2015"
	wacn.date=""/>

# Use Active Directory for authentication in Azure Websites #

[Azure Websites](/documentation/services/web-sites/) enables enterprise line-of-business application scenarios by supporting single sign-on (SSO) of users whether they access the application from your on-premises environment or the public internet. It can be integrated with [Azure Active Directory](/home/features/identity/) (AAD) or an on-premises secure token service (STS), such as Active Directory Federation Services (AD FS), to authenticate your internal Active Directory (AD) users and authorize them properly.

## Zero-friction authentication and authorization ##

With a few clicks of a button, you can enable authentication and authorization for your web app. The checkbox style configuration in every Azure web app provides basic access control for your line-of-business web app. It does so by enforcing HTTPS and authentication to an Azure AD tenant of your choice before granting users access to your web app content. For more information, see [Web Apps Authentication / Authorization](http://azure.microsoft.com/blog/2014/11/13/azure-websites-authentication-authorization/).

>[AZURE.NOTE] This feature is currently in preview.

## Manually implement authentication and authorization ##

In many scenarios, you want to customize the authentication and authorization behavior of the application, such as a login and logout page, custom authorization logic, mult-tenant application behavior, and so on. In these cases, it may be better to configure authentication and authorization manually for greater flexibility of its features. Below are two main options  

-	[Azure AD](/documentation/articles/web-sites-dotnet-lob-application-azure-ad) - You can implement authentication and authorization for your web app with Azure AD. Using Azure AD as the identity provider has the following characteristics:
	-	Supports popular authentication protocols, such as [OAuth 2.0](http://oauth.net/2/), [OpenID Connect](http://openid.net/connect/), and [SAML 2.0](http://en.wikipedia.org/wiki/SAML_2.0). For the complete list of supported protocols, see [Azure Active Directory Authentication Protocols](http://msdn.microsoft.com/zh-cn/library/azure/dn151124.aspx).
	-	Can use an Azure-only identity provider without any on-premises infrastructure.
	-	Can also configure directory sync with an on-premises AD (managed on-premises).
	-	Azure AD with directory sync from your on-premises AD domain enables a smooth SSO experience to your web app when AD users access from the intranet and the internet. From the intranet, AD users can automatically access the web app through Integrated Authentication. From the internet, AD users can log into the web app using their Windows credentials.
	-	Provides SSO to [all applications supported by Azure AD](/home/features/identity/), including Azure, Office 365, Dynamics CRM Online, Microsoft Intune, and thousands of non-Microsoft cloud applications. 
	-	Azure AD delegates management of [relying party](http://en.wikipedia.org/wiki/Relying_party) applications to non-administrator roles, while application access to sensitive directory data must still be configured by global administrators.
	-	Sends a general-purpose set of claim types for all relying party applications. For the list of claim types, see [Supported Token and Claim Types](http://msdn.microsoft.com/zh-cn/library/azure/dn195587.aspx). Claims are not customizable.
	-	[Azure AD Graph API](http://msdn.microsoft.com/zh-cn/library/azure/hh974476.aspx) enables application access to directory data in Azure AD.
-	[On-premises secure token service (STS), such as AD FS](/documentation/articles/web-sites-dotnet-lob-application-adfs) - You can implement authentication and authorization for your web app with an on-premises STS like AD FS. Using on-premises AD FS has the following characteristics:
	-	AD FS topology must be deployed on-premises, with cost and management overhead.
	-	Best when company policy demands that AD data be stored on-premises.
	-	Only AD FS administrators can configure [relying party trusts and claim rules](http://technet.microsoft.com/zh-cn/library/dd807108.aspx).
	-	Can manage [claims](http://technet.microsoft.com/zh-cn/library/ee913571.aspx) on a per-application basis.
	-	Must have a separate solution for accessing on-premises AD data through the corporate firewall.
<!-- deleted by customization

>[AZURE.NOTE] If you want to get started with Azure Websites before signing up for an Azure account, go to [Try Azure Websites](http://go.microsoft.com/fwlink/?LinkId=523751), where you can immediately create a short-lived starter web app in Azure Websites. No credit cards required; no commitments.

## What's changed
* For a guide to the change from Websites to Azure Websites see: [Azure Websites and Its Impact on Existing Azure Services](/documentation/services/web-sites/)
* For a guide to the change of the Management Portal to the new portal see: [Reference for navigating the preview portal](https://manage.windowsazure.cn/)
-->
 
