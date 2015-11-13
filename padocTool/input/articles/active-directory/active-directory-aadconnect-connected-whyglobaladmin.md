<properties 
	pageTitle="Why we require an Azure AD global administrator account for setting up Azure AD Connect" 
	description="Custom settings description of why we require a global admin account." 
	services="active-directory" 
	documentationCenter="" 
	authors="billmath" 
	manager="stevenpo" 
	editor="curtand"/>

<tags 
	ms.service="active-directory" 
	ms.date="08/24/2015" 
	wacn.date=""/>

# Why we require an Azure AD global administrator account for setting up Azure AD Connect

The following table shows the reasons an Azure AD global administrator account is required for setting up Azure AD Connect.

Under the following conditions  | Description 
------------- | ------------- |
For Express Settings and DirSync Upgrade | We enable sync (if required) in your Azure AD directory and create the Azure AD account that will be used for the on-going sync operations (the Azure AD Connector account). 
For custom settings | We enable sync in your Azure AD directory and create the Azure AD account that will be used for on-going sync operations (the Azure AD Connector account).  For the Single Sign-on with the AD FS option, we read and configure federation properties in Azure AD.



**Additional Resources**


* [More on Azure AD Connect accounts and permissions](/documentation/articles/active-directory-aadconnect-account-summary)
* [Custom installation of Azure AD Connect](/documentation/articles/active-directory-aadconnect-get-started-custom)
* [Azure AD Connect on MSDN](https://msdn.microsoft.com/zh-cn/library/azure/dn832695.aspx) 