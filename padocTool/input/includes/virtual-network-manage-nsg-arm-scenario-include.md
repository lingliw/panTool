## Sample Scenario
To better illustrate how to manage NSGs, this article uses the scenario below.

![VNet scenario](./media/virtual-networks-create-nsg-scenario-include/figure1.png)

In this scenario you will create an NSG for each subnet in the **TestVNet** virtual network, as described below: 

* **NSG-FrontEnd**. The front end NSG will be applied to the *FrontEnd* subnet, and contain two rules:    
  * **rdp-rule**. This rule will allow RDP traffic to the *FrontEnd* subnet.
  * **web-rule**. This rule will allow HTTP traffic to the *FrontEnd* subnet.
* **NSG-BackEnd**. The back end NSG will be applied to the *BackEnd* subnet, and contain two rules:    
  * **sql-rule**. This rule allows SQL traffic only from the *FrontEnd* subnet.
  * **web-rule**. This rule denies all internet bound traffic from the *BackEnd* subnet.

The combination of these rules create a DMZ-like scenario, where the back end subnet can only receive incoming traffic for SQL traffic from the front end subnet, and has no access to the Internet, while the front end subnet can communicate with the Internet, and receive incoming HTTP requests only.

To deploy the scenario described above, follow [this link](http://github.com/telmosampaio/azure-templates/tree/master/201-IaaS-WebFrontEnd-SQLBackEnd-NSG). Download the template, do some necessary modification, and deploy it with Azure CLI.

>[AZURE.NOTE] Templates you downloaded from the GitHub Repo "azure-quickstart-templates" must be modified in order to fit in the Azure China Cloud Environment. For example, replace some endpoints -- "blob.core.windows.net" by "blob.core.chinacloudapi.cn", "cloudapp.azure.com" by "chinacloudapp.cn"; change some unsupported VM images; and, changes some unsupported VM sizes.

