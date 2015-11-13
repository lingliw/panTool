<properties 
	pageTitle="Azure Active Directory Editions" 
	description="A topic that explains choices for free and paid editions of Azure Active Directory." 
	services="active-directory" 
	documentationCenter="" 
	authors="Justinha" 
	manager="TerryLan" 
	editor="LisaToft"/>

<tags 
	ms.service="active-directory" 
	ms.date="08/14/2015"
	wacn.date="" />

# Azure Active Directory Editions

Azure Active Directory is a service that provides comprehensive identity and access management capabilities in the cloud. It combines directory services, advanced identity governance, application access management and a rich standards-based platform for developers. For more information, see this video.

Built on top of a large set of free capabilities in Windows Azure Active Directory, Azure Active Directory Premium and Basic editions provide a set of more advanced features to empower enterprises with more demanding identity and access management needs. When you subscribe to Azure, you get your choice of the following free and paid editions of Azure Active Directory:

- **Free** - The Free edition of Azure Active Directory is part of every Azure subscription. There is nothing to license and nothing to install. With it, you can manage user accounts, synchronize with on-premises directories, get single sign-on across Azure, Office 365, and thousands of popular SaaS applications like Salesforce, Workday, Concur, DocuSign, Google Apps, Box, ServiceNow, Dropbox, and more.
- **Basic** - Azure Active Directory Basic edition provides application access and self-service identity management requirements for task workers with cloud-first needs. With the Basic edition of Azure Active Directory, you get all the capabilities that Azure Active Directory Free has to offer, plus group-based access management, self-service password reset for cloud applications, Azure Active Directory application proxy (to publish on-premises web applications using Azure Active Directory), customizable environment for launching enterprise and consumer cloud applications, and an enterprise-level SLA of 99.9 percent uptime.
    An administrator who is licensed for the Azure Active Directory Basic edition can also activate an Azure Active Directory Premium trial.
- **Premium** - With the Premium edition of Azure Active Directory, you get all of the capabilities that the Azure Active Directory Free and Basic editions have to offer, plus additional feature-rich enterprise-level identity management capabilities explained below.

<!--To sign up and start using Active Directory Premium today, see [Getting started with Azure Active Directory Premium](active-directory-get-started-premium.md).-->

> [AZURE.NOTE]
Azure Active Directory Premium and Basic editions are available for customers in China using the worldwide instance of Azure Active Directory. Azure Active Directory Premium and Basic editions are not currently supported in the Windows Azure service operated by 21Vianet in China. For more information, contact us at the [Azure Active Directory Forum](http://feedback.azure.com/forums/169401-azure-active-directory).

## Features in Azure Active Directory Basic

Active Directory Basic edition is a paid offering of Azure Active Directory and includes the following features:

- **Company branding** - To make the end user experience even better, you can add your company logo and color schemes to your organization’s Sign In and Access Panel pages. Once you’ve added your logo, you also have the option to add localized versions of the logo for different languages and locales. 
    For more information, see [Add company branding to your Sign In and Access Panel pages](active-directory-add-company-branding).
- **Group-based application access** - Use groups to provision users and assign user access in bulk to thousands of SaaS applications. These groups can either be created solely in the cloud or you can leverage existing groups that have been synced in from your on-premises Active Directory. 
    For more information, see [Assign access for a group to a SaaS application in Azure AD](active-directory-accessmanagement-group-saasapps).
- **Self-service password reset** - Azure has always allowed directory administrators to reset passwords. With Azure Active Directory Basic, you can now reduce helpdesk calls when your users forget a password by giving all users in your directory the capability to reset their password, using the same sign in experience they have for Office 365.
    For more information, see [Password Management in Azure AD](https://msdn.microsoft.com/zh-cn/library/azure/dn510386.aspx).
- **Enterprise SLA of 99.9%** - We guarantee at least 99.9% availability of the Azure Active Directory Basic service.
- [**Azure Active Directory Application Proxy**](https://msdn.microsoft.com/zh-cn/library/azure/dn768214.aspx) - Give your employees secure access to on-premises applications like SharePoint and Exchange/OWA from the cloud using Azure Active Directory.

## Features in Azure Active Directory Premium

Active Directory Premium edition is a paid offering of Azure Active Directory and includes all of the features of the Free and Basic editions plus the following features:

- **Self-service group management** - Azure Active Directory Premium simplifies day-to-day administration of groups by enabling users to create groups, request access to other groups, delegate group ownership so others can approve requests and maintain their group’s memberships.

    For more information, see [Self-service group management for users in Azure AD](https://msdn.microsoft.com/library/azure/dn641267.aspx).

- **Advanced security reports and alerts** – Monitor and protect access to your cloud applications by viewing detailed logs showing more advanced anomalies and inconsistent access pattern reports. Advanced reports are machine learning-based and can help you gain new insights to improve access security and respond to potential threats.

    For more information, see [View your access and usage reports](active-directory-view-access-usage-reports.md).

- **Multi-Factor Authentication** - Multi-Factor Authentication is now included with Premium and can help you to secure access to on-premises applications (VPN, RADIUS, etc.), Azure, Microsoft Online Services like Office 365 and Dynamics CRM Online, and thousands of Non-MS Cloud services preintegrated with Azure Active Directory. Simply enable Multi-Factor Authentication for Azure Active Directory identities, and users will be prompted to set up additional verification the next time they sign in.

    For more information, see [Adding Multi-Factor Authentication to Azure Active Directory](https://msdn.microsoft.com/library/azure/dn249466.aspx).

- **Microsoft Identity Manager (MIM)** - Premium comes with the option to grant rights to use a MIM server (and CALs) in your on-premises network to support any combination of Hybrid Identity solutions. This is a great option if you have a variation of on-premises directories and databases that you want to sync directly to Azure Active Directory. There is no limit on the number of FIM servers you can use, however, MIM CALs are granted based on the allocation of an Azure Active Directory premium user license.

    For more information, see [Deploy MIM 2010 R2](https://www.microsoft.com/server-cloud/products/forefront-identity-manager/features.aspx).

- **Enterprise SLA of 99.9%** - We guarantee at least 99.9% availability of the Azure Active Directory Premium service.

    For more information, see [Active Directory Premium SLA](http://azure.microsoft.com/support/legal/sla/).

- **Password reset with write-back** - Self-service password reset can be written back to on-premises directories.

- [Azure Active Directory Connect Health](https://msdn.microsoft.com/library/azure/dn906722.aspx): monitor the health of your on premises Active Directory infrastructure and get usage analytics.



## Comparing editions: Capabilities common to all editions

- Directory as a service
    For the free edition, there is a 500K object limit. But the 500k object limit does not apply for Office 365, Windows Intune or any other Microsoft online service that relies on Azure Active Directory for directory services. The Basic and Premium editions have no object limit.
- User and group management using UI or Windows PowerShell cmdlets
- Device registration
- Access Panel portal for single sign-in (SSO) based user access to SaaS and custom applications
    With Azure Active Directory Free and Azure Active Directory Basic, end users who have been assigned access to each SaaS app, can see up to 10 apps in their Access Panel and get single sign-in access to them (assuming they have first been configured with SSO by the admin). Admins can configure SSO and assign user access to as many SaaS apps as they want with Free, but end users will see only 10 apps in their Access Panel at a time. Azure Active Directory Premium has no application limit.
- User-based application access management and provisioning
- Self-service password change for cloud users
- Directory synchronization tool – For syncing between on-premises Active Directory and Azure Active Directory
- Standard security reports

### basic features

- High availability SLA uptime (99.9%)
- Group-based application access management and provisioning
- Customization of company logo and colors to the Sign In and Access Panel pages
- Self-service password reset for cloud users
- Application Proxy: Secure Remote Access and SSO to on-premises web applications

## What's next

<!--- [Getting started with Azure Active Directory Premium](active-directory-get-started-premium.md)-->
- [Add company branding to your Sign In and Access Panel pages](active-directory-add-company-branding)
- [View your access and usage reports](active-directory-view-access-usage-reports)

