<properties
	pageTitle="Assigning administrator roles in Azure AD"
	description="Explains what admin roles are available with Azure AD and how to assign them."
	services="active-directory"
	documentationCenter=""
	authors="curtand"
	manager="stevenpo"
	editor=""/>

<tags 
	ms.service="active-directory" 
	ms.date="09/21/2015"
	wacn.date=""/>

# Assigning administrator roles in Azure AD

Depending on the size of your company, you may want to designate several administrators who serve different functions. These administrators will have access to various features in the Azure portal and, depending on their role, will be able to create or edit users, assign administrative roles to others, reset user passwords, manage user licenses, and manage domains, among other things.

It's  important to understand that a user who is assigned an admin role will have the same permissions across all of the cloud services that your organization has subscribed to, regardless of whether you assign the role in the Office 365 portal, or in the Azure portal, or by using the Azure AD module for Windows PowerShell. 

The following administrator roles are available:

- **Billing administrator**: Makes purchases, manages subscriptions, manages support tickets, and monitors service health.
- **Global administrator**: Has access to all administrative features. The person who signs up for the Azure account becomes a global administrator. Only global administrators can assign other administrator roles. There can be more than one global administrator at your company.
- **Password administrator**: Resets passwords, manages service requests, and monitors service health. Password administrators can reset passwords only for users and other password administrators.
- **Service administrator**: Manages service requests and monitors service health.
    > [AZURE.NOTE]
    > To assign the service administrator role to a user, the global administrator must first assign administrative permissions to the user in the service, such as Exchange Online, and then assign the service administrator role to the user in the Azure Management Portal. 
- **User administrator**: Resets passwords, monitors service health, and manages user accounts, user groups, and service requests. Some limitations apply to the permissions of a user management administrator. For example, they cannot delete a global administrator or create other administrators. Also, they cannot reset passwords for billing, global, and service administrators.

## Administrator permissions

### Billing administrator

Can do | Cannot do
------------- | -------------
View company and user information<br>Manage Office support tickets<br>Perform billing and purchasing operations for Office products | Reset user passwords<br>Create and manage user views<br>Create, edit, and delete users and groups, and manage user licenses<br>Manage domains<br>Manage company information<br>Delegate administrative roles to others<br>Use directory synchronization

### Global administrator

Can do | Cannot do
------------ | -------------
View company and user information<br>Manage Office support tickets<br>Perform billing and purchasing operations for Office products <br>Reset user passwords<br> Create and manage user views<br>Create, edit, and delete users and groups, and manage user licenses<br> Manage domains <br>Manage company information<br>Delegate administrative roles to others<br>Use directory synchronization | N/A

### Password administrator

Can do | Cannot do
------------- | -------------
View company and user information<br>Manage Office support tickets<br>Reset user passwords | Perform billing and purchasing operations for Office products<br>Create and manage user views<br>Create, edit, and delete users and groups, and manage user licenses<br>Manage domains<br>Manage company information<br>Delegate administrative roles to others<br>Use directory synchronization

### Service administrator

Can do | Cannot do
------------- | -------------
View company and user information<br>Manage Office support tickets | Reset user passwords<br>Perform billing and purchasing operations for Office products<br>Create and manage user views<br>Create, edit, and delete users and groups, and manage user licenses<br>Manage domains<br>Manage company information<br>Delegate administrative roles to others<br>Use directory synchronization

### User administrator

Can do | Cannot do
------------- | -------------
View company and user information<br>Manage Office support ticketsReset user passwords, with limitations.<br> He or she cannot reset passwords for billing, global, and service administrators.<br>Create and manage user views<br>Create, edit, and delete users and groups, and manage user licenses, with limitations.<br> He or she cannot delete a global administrator or create other administrators. | Perform billing and purchasing operations for Office products<br>Manage domains<br>Manage company information<br>Delegate administrative roles to others<br>Use directory synchronization

## Details about the global administrator role

The global administrator has access to all administrative features. By default, the person who signs up for an Azure subscription is assigned  the global administrator role for the directory. Only global administrators can assign other administrator roles. 

## Assign or remove administrator roles 


1. In the Management Portal, click **Active Directory**, and then click on the name of your organization’s directory.
2. On the **Users** page, click the display name of the user you want to edit.
3. Select the **Organizational Role** drop-down menu, and then select the administrator role that you want to assign to this user, or select **User** if you want to remove an existing administrator role. 
4. In the **Alternate Email Address** box, type an email address. This email address is used for important notifications, including password self-reset, so the user must be able to access the email account whether or not the user can access Azure.
5. Select **Allow** or **Block** to specify whether to allow the user to sign in and access services. 
6. Specify a location from the **Usage Location** drop-down list.
7. When you have finished, click **Save**.

## What's next

- [Manage users](/documentation/articles/active-directory-manage-users)
- [Manage passwords](/documentation/articles/active-directory-manage-passwords)
- [Manage groups](/documentation/articles/active-directory-manage-groups)


