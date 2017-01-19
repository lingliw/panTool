<properties
	pageTitle="Create non-interactive authentication .NET HDInsight applciations | Azure"
	description="Learn how to create non-interactive authentication .NET HDInsight applications."
	editor="cgronlun"
	manager="paulettm"
	services="hdinsight"
	documentationCenter=""
	tags="azure-portal"
	authors="mumian"/>

<tags
	ms.service="hdinsight"
	ms.date="03/23/2016"
	wacn.date=""/>

# Create non-interactive authentication .NET HDInsight applications

You can execute your .NET Azure HDInsight application either under application's own identity (non-interactive) or under the identity of the signed-in user of the application (interactive). For a sample of the interactive application, see [Submit Hive/Pig/Sqoop jobs using HDInsight .NET SDK](/documentation/articles/hdinsight-submit-hadoop-jobs-programmatically#submit-hivepigsqoop-jobs-using-hdinsight-net-sdk). This article shows you how to create non-interactive authentication .NET application to connect to Azure HDInsight and submit a Hive job.

From your .NET application, you will need:

- your Azure subscription tenant ID
- the Azure Directory application client ID
- the Azure Directory application secret key.  

The main process includes the following steps:

2. Create an Azure Directory application.
2. Assign roles to the AD application.
3. Develop your client application.


##Prerequisites

- HDInsight cluster. You can create one using the instructions found in the [getting started tutorial](/documentation/articles/hdinsight-hadoop-tutorial-get-started-windows-v1#create-cluster). 




## Create Azure Directory application 
When you create an Active Directory application, it actually creates both the application and a service principal. You can execute the application under the application's identity.

Currently, you must use the Azure classic portal to create a new Active Directory application. This ability will be added to the Azure portal in a later release. You can also perform these steps through Azure PowerShell or Azure CLI. For more information about using PowerShell or CLI with the service principal, see [Authenticate service principal with Azure Resource Manager](/documentation/articles/resource-group-authenticate-service-principal).

**To create an Azure Directory application**

1.	Sign in to the [Azure classic portal]( https://manage.windowsazure.cn/).
2.	Select **Active Directory** from the left pane.

    ![Azure classic portal active directory](.\media\hdinsight-create-non-interactive-authentication-dotnet-application\active-directory.png)
    
3.	Select the directory that you want to use for creating the new application. It shall be the existing one.
4.	Click **Applications** from the top to list the existing applications.
5.	Click **Add** from the bottom to add a new application.
6.	Enter **Name**, select **Web application and/or Web API**, and then click **Next**.

    ![new azure active directory application](.\media\hdinsight-create-non-interactive-authentication-dotnet-application\hdinsight-add-ad-application.png)

7.	Enter **Sign-on URL** and **App ID URI**. For **SIGN-ON URL**, provide the URI to a web-site that describes your application. The existence of the web-site is not validated. For APP ID URI, provide the URI that identifies your application. And then click **Complete**.
It takes a few moments to create the application.  Once the application is created, the portal shows you the Quick Glace page of the new application. Don't close the portal. 

    ![new azure active directory application properties](.\media\hdinsight-create-non-interactive-authentication-dotnet-application\hdinsight-add-ad-application-properties.png)

**To get the application client ID and the secret key**

1.	From the newly created AD application page, click **Configure** from the top menu.
2.	Make a copy of **Client ID**. You will need it in your .NET application.
3.	Under **Keys**, click **Select duration** dropdown, and select either **1 year** or **2 years**. The key value will not be displayed until you save the configuration.
4.	Click **Save** on the bottom of the page. When the secret key appears, make a copy of the key. You will need it in your .NET application.

##Assign AD application to role

You must assign the application to a [role](/documentation/articles/role-based-access-built-in-roles) to grant it permissions for performing actions. You can set the scope at the level of the subscription, resource group, or resource. The permissions are inherited to lower levels of scope (for example, adding an application to the Reader role for a resource group means it can read the resource group and any resources it contains). In this tutorial, you will set the scope at the resource group level.  Because the Azure classic portal doesn't support resource groups, this part has to be performed from the Azure portal. 

**To add the Owner role to the AD application**

1.	Sign in to the [Azure portal](https://portal.azure.cn).
2.	Click **Subscriptions** from the left pane.
3.	Click the subscription that contains the HDInsight cluster where you will run your Hive query later in this tutorial. If there are too many subscriptions, you can use the filter.
4.	Click **Setting** from the subscription blade, and then click "Users".
5.	Click **Add** from the **Users** blade.
6.	Follow the instruction to add the **Owner** role to the AD application you created in the last procedure. When you complete it successfully, you shall see the application listed in the Users blade with the Owner role.


##Develop HDInsight client application

Create a C# .net console application following the instructions found in [Submit Hadoop jobs in HDInsight](/documentation/articles/hdinsight-submit-hadoop-jobs-programmatically#submit-hivepigsqoop-jobs-using-hdinsight-net-sdk). Then replace the GetTokenCloudCredentials method with the following:

    public static TokenCloudCredentials GetTokenCloudCredentials(string tenantId, string clientId, SecureString secretKey)
    {
        var authFactory = new AuthenticationFactory();

        var account = new AzureAccount { Type = AzureAccount.AccountType.ServicePrincipal, Id = clientId };

        var env = AzureEnvironment.PublicEnvironments[EnvironmentName.AzureCloud];

        var accessToken =
            authFactory.Authenticate(account, env, tenantId, secretKey, ShowDialog.Never)
                .AccessToken;

        return new TokenCloudCredentials(accessToken);
    }

To retrieve the Tenant ID through PowerShell:

    Get-AzureRmSubscription

Or, Azure CLI:

    azure account show --json

      
## See also

- [Submit Hadoop jobs in HDInsight](/documentation/articles/hdinsight-submit-hadoop-jobs-programmatically)
- [Create Active Directory application and service principal using portal](/documentation/articles/resource-group-create-service-principal-portal)
- [Authenticate service principal with Azure Resource Manager](/documentation/articles/resource-group-authenticate-service-principal)
- [Azure Role-Based Access Control](/documentation/articles/role-based-access-control-configure)