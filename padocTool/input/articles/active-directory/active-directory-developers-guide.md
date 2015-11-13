<properties
   pageTitle="Azure Active Directory developer's guide | Windows Azure"
   description="This article provides a comprehensive guide to developer-oriented resources for Azure Active Directory."
   services="active-directory"
   documentationCenter="dev-center-name"
   authors="msmbaldwin"
   manager="mbaldwin"
   editor=""/>

<tags
   ms.service="active-directory"
   ms.date="09/02/2015"
   wacn.date=""/>


# Azure Active Directory Developer's Guide

## Overview
As an identity management as a service (IDMaaS) platform, Azure Active Directory provides developers an effective way to integrate identity management into their applications. The following articles provide overviews on implementation and key features of Azure Active Directory. We suggest that you read them in order, or jump to [Getting started](#getting-started) if you're ready to dig in.


1. [The benefits of Azure Active Directory integration](active-directory-how-to-integrate): Discover why integration with Azure Active Directory offers the best solution for secure sign-in and authorization.

2. [Active Directory authentication scenarios](active-directory-authentication-scenarios): Take advantage of simplified authentication in Azure Active Directory to provide sign-on to your application.

3. [Integrating applications with Azure Active Directory](active-directory-integrating-applications): Learn how to add, update, and remove applications from Azure Active Directory, and about the branding guidelines for integrated apps.

4. [Azure Active Directory Graph API](active-directory-graph-api): Use the Azure Active Directory Graph API to programmatically access Azure Active Directory through REST API endpoints.

5. [Azure Active Directory authentication libraries](active-directory-authentication-libraries): Easily authenticate users to obtain access tokens by using the Azure authentication libraries.

## Getting Started

These tutorials are tailored for multiple platforms and can help you quickly start developing with Azure Active Directory. As a prerequisite, you must [get an Azure Active Directory tenant](active-directory-howto-tenant).

### Mobile and PC application quick-start guides

|[![iOS](./media/active-directory-developers-guide/ios.png)](active-directory-devquickstarts-ios)|[![Android](./media/active-directory-developers-guide/android.png)](active-directory-devquickstarts-android)|[![.NET](./media/active-directory-developers-guide/net.png)](active-directory-devquickstarts-dotnet)| [![Windows Phone](./media/active-directory-developers-guide/windows.png)](active-directory-devquickstarts-windowsphone)|[![Windows Store](./media/active-directory-developers-guide/windows.png)](active-directory-devquickstarts-windowsstore)|[![Xamarin](./media/active-directory-developers-guide/xamarin.png)](active-directory-devquickstarts-xamarin)|[![Cordova](./media/active-directory-developers-guide/cordova.png)](active-directory-devquickstarts-cordova)
|:--:|:--:|:--:|:--:|:--:|:--:|:--:
|[iOS](active-directory-devquickstarts-ios.md)|[Android](active-directory-devquickstarts-android)|[.NET](active-directory-devquickstarts-dotnet.md)|[Windows Phone](active-directory-devquickstarts-windowsphone)|[Windows Store](active-directory-devquickstarts-windowsstore)|[Xamarin](active-directory-devquickstarts-xamarin)|[Cordova](active-directory-devquickstarts-cordova)

### Web application quick-start guides

|[![.NET](./media/active-directory-developers-guide/net.png)](active-directory-devquickstarts-webapp-dotnet)|[![Javascript](./media/active-directory-developers-guide/javascript.png)](active-directory-devquickstarts-angular)|[![Node.js](./media/active-directory-developers-guide/nodejs.png)](active-directory-devquickstarts-openidconnect-nodejs)
|:--:|:--:|:--:|
|[.NET](active-directory-devquickstarts-webapp-dotnet.md)|[Javascript](active-directory-devquickstarts-angular)|[Node.js](active-directory-devquickstarts-openidconnect-nodejs)

### Web API quick-start guides

|[![.NET](./media/active-directory-developers-guide/net.png)](active-directory-devquickstarts-webapi-dotnet)|[![Node.js](./media/active-directory-developers-guide/nodejs.png)](active-directory-devquickstarts-webapi-nodejs)
|:--:|:--:|
|[.NET](active-directory-devquickstarts-webapi-dotnet.md)|[Node.js](active-directory-devquickstarts-webapi-nodejs)

### Querying the directory quickstart guide

| [![.NET](./media/active-directory-developers-guide/graph.png)](active-directory-graph-api-quickstart)|
|:--:|
|[Graph API](active-directory-graph-api-quickstart)|


## How Tos

These articles describe how to perform specific tasks using Azure Active Directory (AD).

- [Get an Azure Active Directory tenant](active-directory-howto-tenant)
- [List your application in the Azure Active Directory application gallery](active-directory-app-gallery-listing)
- [Understand the Azure Active Directory application manifest](active-directory-application-manifest)
- [Create an app with Office 365 APIs](https://msdn.microsoft.com/office/office365/howto/getting-started-Office-365-APIs)
- [Submit web apps for Office 365 to the Seller Dashboard](https://msdn.microsoft.com/office/office365/howto/submit-web-apps-seller-dashboard)

## Reference

These articles provide foundation reference for REST and authentication library APIs, protocols, errors, code samples, and endpoints.  

####  Support
- **[Where to get support](http://stackoverflow.com/questions/tagged/azure-active-directory)**: Find Azure AD solutions on Stack Overflow by searching for the tags [azure-active-directory](http://stackoverflow.com/questions/tagged/azure-active-directory) and [adal](http://stackoverflow.com/questions/tagged/adal).

#### Code

- **[Azure AD open source libraries](http://github.com/AzureAD)**: The easiest way to find a library’s source is using our [library list](https://msdn.microsoft.com/zh-cn/library/azure/dn151135.aspx).

- **[Azure AD samples](http://github.com/AzureADSamples)**: The easiest way to navigate the list of samples is using the [Code Samples Index](active-directory-code-samples).


#### Graph API

- **[Graph API Reference](https://msdn.microsoft.com/zh-cn/library/azure/hh974476.aspx)**: REST reference for the Azure Active Directory Graph API. [View the new interactive Graph API reference experience](https://msdn.microsoft.com/zh-cn/library/Azure/Ad/Graph/api/api-catalog).

- **[Graph API Permission Scopes](https://msdn.microsoft.com/zh-cn/library/Azure/Ad/Graph/api/graph-api-permission-scopes)**: The OAuth 2.0 permission scopes that are used to control the access an app has to directory data in a tenant.


#### Authentication Protocols

- **[SAML 2.0 Protocol Reference](https://msdn.microsoft.com/zh-cn/library/azure/dn195591.aspx)**: The SAML 2.0 protocol enables applications to provide a single sign-on experience to their users.


- **[OAuth 2.0 Protocol Reference](https://msdn.microsoft.com/zh-cn/library/azure/dn645545.aspx)**: The OAuth 2.0 protocol enables you to authorize access to web applications and web APIs in your Azure AD tenant.


- **[OpenID Connect 1.0 Protocol Reference](https://msdn.microsoft.com/zh-cn/library/azure/dn645541.aspx)**: The OpenID Connect 1.0 protocol extends OAuth 2.0 for use as an authentication protocol.


- **[WS-Federation 1.2 Protocol Reference](https://msdn.microsoft.com/zh-cn/library/azure/dn903702.aspx)**: The WS-Federation 1.2 protocol, as specified in the Web Services Federation Version 1.2 Specification.

- **[Supported Security Tokens and Claims](active-directory-token-and-claims)**: A guide of understanding and evaluating the claims in the SAML 2.0 and JSON Web Tokens (JWT) tokens.

## Social

- **[Active Directory Team Blog](http://blogs.technet.com/b/ad/)**: Keep abreast of the latest developments in the world of Azure AD.

- **[Azure AD Graph Blog](http://blogs.msdn.com/b/aadgraphteam)**: Azure AD information specific to the Graph API.

- **[Cloud Identity](http://www.cloudidentity.net)**: Thoughts on Identity Management as a Service, from a Principle Azure Active Directory PM.  

