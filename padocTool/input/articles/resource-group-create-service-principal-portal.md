<properties
   pageTitle="Create a new Azure Service Principal using the Azure portal"
   description="Describes how to create a new Azure service principal that can be used with the role-based access control in Azure Resource Manager to manage access to resources."
   services="azure-resource-manager"
   documentationCenter="na"
   authors="tfitzmac"
   manager="wpickett"
   editor=""/>

<tags
   ms.service="azure-resource-manager"
   ms.date="09/18/2015"
   wacn.date=""/>

# Create a new Azure Service Principal using the Azure portal

## Overview
A service principal is an automated process, application or service that needs to access other resources. Using Azure Resource Manager, you can grant access
to a service principal and authenticate it so it can perform the permitted management actions on resources that exist in 
the subscription or as a tenant. 

This topic shows you how to create a new service principal using the Azure portal. Currently, you must use the Windows Azure portal to create a new service principal. This ability will be added to the Azure preview portal in a later release.

## Concepts
1. Azure Active Directory (AAD) - an identity and access management service build for the cloud. For more details see: [What is Azure active Directory](/documentation/articles/active-directory-whatis)
2. Service Principal - an instance of an application in a directory.
3. AD Application - a directory record in AAD that identifies an application to AAD. For more details see [Basics of Authentication in Azure AD](https://msdn.microsoft.com/zh-cn/library/azure/874839d9-6de6-43aa-9a5c-613b0c93247e#BKMK_Auth).


## Create Active Directory application
1. Login to your Azure Account through the [classic portal](https://manage.windowsazure.cn/).

2. Select **Active Directory** from the left pane.

     ![select Active Directory][1]

3. Select the directory that you want to use for creating the new application.

     ![choose directory][2]

3. To view the applications in your directory, click on **Applications**.

     ![view applications][11]

4. If you haven't created an application in that directory before you should see something similar to following image. Click on **ADD AN APPLICATION**

     ![add application][6]

     Or, click **Add** in the bottom pane.

     ![add][12]

5. Select the type of application you would like to create. For this tutorial, we will not use an application from the gallery.

     ![new application][10]

6. Fill in name of the application and select the type of application you want to use. Since we intend to use this application's service principal to authenticate with Azure Resource Manager, we will elect to create a **WEB APPLICATION AND/OR WEB API** and click the next button.

     ![name application][9]

7. Fill in the properties for your app. For **SIGN-ON URL**, provide the URI to a web-site that describes your application. The existence of the web-site is not validated. 
For **APP ID URI**, provide the URI that identifies your application. The uniqueness or existence of the endpoint is not validated. Click the **Complete** to create you AAD Application.

     ![application properties][4]

## Create your service principal password
The portal should now have your application selected.

1. Click on the **Configure** tab to configure your application's password.

     ![configure application][3]

2. Scroll down to the **Keys** section and select how long you would like your password to be valid.

     ![keys][7]

3. Select **Save** to create your key.

     ![save][13]

     The saved key is displayed and you can copy it.

     ![saved key][8]

4. You can now use you key to authenticate as a service principal. You will need your **CLIENT ID** in addition to your **KEY** to sign in. Go to **CLIENT ID** and copy it.
  
     ![client id][5]


Your application is now ready and the service principal created on your tenant. When signing in as a service principal be sure to use:

* **CLIENT ID** - as your user name.
* **KEY** - as your password.

## Next Steps

- To learn about specifying security policies, see [Managing and Auditing Access to Resources](/documentation/articles/resource-group-rbac)  
- For the steps to permit a service principal to access resources, see [Authenticating a Service Principal with Azure Resource Manager](/documentation/articles/resource-group-authenticate-service-principal)  
- For an overview of role-based access control, see [Role-based access control in the Windows Azure portal](/documentation/articles/role-based-access-control-configure)
- For guidance on implementing security with Azure Resource Manager, see [Security considerations for Azure Resource Manager](/documentation/articles/best-practices-resource-manager-security)


<!-- Images. -->
[1]: ./media/resource-group-create-service-principal-portal/active-directory.png
[2]: ./media/resource-group-create-service-principal-portal/active-directory-details.png
[3]: ./media/resource-group-create-service-principal-portal/application-configure.png
[4]: ./media/resource-group-create-service-principal-portal/app-properties.png
[5]: ./media/resource-group-create-service-principal-portal/client-id.png
[6]: ./media/resource-group-create-service-principal-portal/create-application.png
[7]: ./media/resource-group-create-service-principal-portal/create-key.png
[8]: ./media/resource-group-create-service-principal-portal/save-key.png
[9]: ./media/resource-group-create-service-principal-portal/tell-us-about-your-application.png
[10]: ./media/resource-group-create-service-principal-portal/what-do-you-want-to-do.png
[11]: ./media/resource-group-create-service-principal-portal/view-applications.png
[12]: ./media/resource-group-create-service-principal-portal/add-icon.png
[13]: ./media/resource-group-create-service-principal-portal/save-icon.png