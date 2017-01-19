<!-- not suitable for Mooncake -->

If you use an Azure subscription where you are not the administrator/owner, such as a company owned subscription, you must verify the following before using the steps in this document:

* Your Azure login must have at least **Contributor** access to the Azure resource group that you use when creating HDInsight (and other Azure resources.)
* Someone with at least **Contributor** access to the Azure subscription must have previously registered the provider for the resource you are using. Provider registration happens when a user with Contributor access to the subscription creates a resource for the first time on the subscription. It can also be accomplished without creating a resource by [registering a provider using REST](https://msdn.microsoft.com/zh-cn/library/azure/dn790548.aspx).

For more information on working with access management, see the following documents:

* [Get started with access management in the Azure portal](/documentation/articles/role-based-access-control-what-is/)
* [Use role assignments to manage access to your Azure subscription resources](/documentation/articles/role-based-access-control-configure/)

