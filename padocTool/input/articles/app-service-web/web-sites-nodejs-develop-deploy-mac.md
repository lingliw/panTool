<properties
	pageTitle="Create a Node.js web app in Azure Websites | Windows Azure"
	description="Learn how to deploy a Node.js application to a web app in Azure Websites."
	services="app-service\web"
	documentationCenter="nodejs"
	authors="MikeWasson"
	manager="wpickett"
	editor=""/>

<tags
	ms.service="app-service-web"
	ms.date="10/13/2015"
	wacn.date=""/>

# Create a Node.js web app in Azure Websites

> [AZURE.SELECTOR]
- [.Net](/documentation/articles/web-sites-dotnet-get-started)
- [Node.js](/documentation/articles/web-sites-nodejs-develop-deploy-mac)
- [Java](/documentation/articles/web-sites-java-get-started)
- [PHP - Git](/documentation/articles/web-sites-php-mysql-deploy-use-git)
- [PHP - FTP](/documentation/articles/web-sites-php-mysql-deploy-use-ftp)
- [Python](/documentation/articles/web-sites-python-ptvs-django-mysql)

This tutorial shows how to create a simple [Node.js](http://nodejs.org) application and deploy it to a [web app](/documentation/articles/app-service-web-overview) in [Azure Websites](/documentation/articles/app-service-value-prop-what-is) by using [Git](http://git-scm.com). The instructions in this tutorial can be followed on any operating system that is capable of running Node.js.

You'll learn:

* How to create a web app in Azure Websites by using the Azure preview portal.
* How to deploy a Node.js application to the web app by pushing to the web app's Git repository.

The completed application writes a short "hello world" string to the browser.

![A browser displaying the 'Hello World' message.][helloworld-completed]

For tutorials and sample code with more complex Node.js applications, or for other topics about how to use Node.js in Azure, see the [Node.js Developer Center](/develop/nodejs/).

> [AZURE.NOTE]
> To complete this tutorial, you need a Windows Azure account. If you don't have an account, you can <!-- deleted by customization [activate your MSDN subscriber benefits](/pricing/member-offers/msdn-benefits-details/?WT.mc_id=A261C142F) or -->[sign up for a trial](/pricing/1rmb-trial/?WT.mc_id=A261C142F).
<!-- deleted by customization
>
> If you want to get started with Azure Websites before you sign up for an Azure account, go to [Try Azure Websites](http://go.microsoft.com/fwlink/?LinkId=523751). There, you can immediately create a short-lived starter web app in Azure Websites—no credit card required, and no commitments.
-->

## Create a web app and enable Git publishing

Follow these steps to create a web app in Azure Websites and enable Git publishing. 
<!-- deleted by customization

[Git](http://git-scm.com/%20target="_blank) is a distributed version control system that you can use to deploy your Azure Website. You'll store the code you write for your web app in a local Git repository, and you'll deploy your code to Azure by pushing to a remote repository. This method of deployment is a feature of Azure Websites web apps.  

1. Sign in to the [Azure preview portal](https://manage.windowsazure.cn).

2. Click the **+ NEW** icon on the top left of the portal.

3. Click **Web + Mobile**, and then click **Web app**.

    ![][portal-quick-create]

4. Enter a name for the web app in the **Web app** box.

	This name must be unique in the chinacloudsites.cn domain because the URL of the web app will be {name}.chinacloudsites.cn. If the name you enter isn't unique, a red exclamation mark appears in the text box.

5. Select a **Resource Group** or create a new one.

	For more information about resource groups, see [Using the Azure Preview Portal to manage your Azure resources](/documentation/articles/resource-group-portal).

5. Select an **App Service plan/Location** or create a new one.

	For more information about App Service plans, see [App Service plans overview](/documentation/articles/azure-web-sites-web-hosting-plans-in-depth-overview)

6. Click **Create**.
   
	![][portal-quick-create2]

	In a short time, typically less than a minute, Azure finishes creating the new web app.

7. Click **Web apps > {your new web app}**.

	![](./media/web-sites-nodejs-develop-deploy-mac/gotowebapp.png)

8. In the **Web app** blade, click the **Deployment** part.

	![][deployment-part]

9. In the **Continuous Deployment** blade, click **Choose Source**

14. Click **Local Git Repository**, and then click **OK**.

	![][setup-git-publishing]

11. Set up deployment credentials if you haven't already done so.

	a. In the Web app blade, click **Settings > Deployment credentials**.

	![][deployment-credentials]
 
	b. Create a user name and password. 
	
	![](./media/web-sites-nodejs-develop-deploy-mac/setdeploycreds.png)

11. In the Web app blade, click **Settings**, and then click **Properties**.
 
	To publish, you'll push to a remote Git repository. The URL for the repository is listed under **GIT URL**. You'll use this URL later in the tutorial.

	![][git-url]

-->
<!-- keep by customization: begin -->
> If you want to get started with Azure Websites before signing up for an account, go to <a href="https://trywebsites.chinacloudsites.cn/?language=nodejs">https://trywebsites.chinacloudsites.cn</a>, where you can immediately create a short-lived ASP.NET starter site in Azure Websites for free. No credit card required, no commitments.

1. Login to the [Azure Management Portal].

2. Click the **+ NEW** icon on the bottom left of the portal

    ![The Azure Management Portal with the +NEW link highlighted.][portal-new-website]

3. Click **WEBSITE**, then **QUICK CREATE**. Enter a value for **URL** and select the datacenter for your website in the **REGION** dropdown. Click the checkmark at the bottom of the dialog.

    ![The Quick Create dialog][portal-quick-create]

4. Once the website status changes to **Running**, click on the name of the website to access the **Dashboard**

	![Open web site dashboard][go-to-dashboard]

6. At the bottom right of the Quickstart page, select **Set up a deployment from source control**.

	![Set up Git publishing][setup-git-publishing]

6. When asked "Where is your source code?" select **Local Git repository**, and then click the arrow.

	![where is your source code][where-is-code]

7. To enable Git publishing, you must provide a user name and password. If you have previously enabled publishing for an Azure Website, you will not be prompted for the user name or password. Instead, a Git repository will be created using the user name and password you previously specified. Make a note of the user name and password, as they will be used for Git publishing to all Azure Websites you create.

	![The dialog prompting for user name and password.][portal-git-username-password]

8. Once the Git repository is ready, you will be presented with instructions on the Git commands to use in order to setup a local repository and then push the files to Azure.

	![Git deployment instructions returned after creating a repository for the website.][git-instructions]
<!-- keep by customization: end -->
## Build and test your application locally

In this section, you'll create a **server.js** file that contains a slightly modified version of the 'Hello World' example from [nodejs.org]. The code adds process.env.PORT as the port to listen on when running in an Azure web app.

1. Create a directory named *helloworld*.

2. Use a text editor to create a new file named **server.js** in the *helloworld* directory.

2. Copy the following code into the **server.js** file, and then save the file:

        var http = require('http')
        var port = process.env.PORT || 1337;
        http.createServer(function(req, res) {
          res.writeHead(200, { 'Content-Type': 'text/plain' });
          res.end('Hello World\n');
        }).listen(port);

3. Open the command line, and use the following command to start the web app locally.

        node server.js

4. Open your web browser and navigate to http://localhost:1337. 

	A webpage that displays "Hello World" appears, as shown in the following screenshot.

    ![A browser displaying the 'Hello World' message.][helloworld-localhost]

## Publish your application

1. Install Git if you haven't already done so.

	For installation instructions for your platform, see the [Git download page](http://git-scm.com/download).

1. From the command line, change directories to the **helloworld** directory and enter the following command to initialize a local Git repository.

		git init


2. Use the following commands to add files to the repository:

		git add .
		git commit -m "initial commit"

3. Add a Git remote for pushing updates to the web app that you created previously, by using the following command:

		git remote add azure [URL for remote repository]

4. Push your changes to Azure by using the following command:

		git push azure master

	You are prompted for the password that you created earlier. The output is similar to the following example.

		Counting objects: 3, done.
		Delta compression using up to 8 threads.
		Compressing objects: 100% (2/2), done.
		Writing objects: 100% (3/3), 374 bytes, done.
		Total 3 (delta 0), reused 0 (delta 0)
		remote: New deployment received.
		remote: Updating branch 'master'.
		remote: Preparing deployment for commit id '5ebbe250c9'.
		remote: Preparing files for deployment.
		remote: Deploying Web.config to enable Node.js activation.
		remote: Deployment successful.
		To https://user@testsite.scm.chinacloudsites.cn/testsite.git
		 * [new branch]      master -> master

5. To view your app, click the **Browse** button on the **Web App** part in the Azure Management Portal.
<!-- deleted by customization

	![Browse button](./media/web-sites-nodejs-develop-deploy-mac/browsebutton.png)

	![Hello world in Azure](./media/web-sites-nodejs-develop-deploy-mac/helloworldazure.png)
-->

## Publish changes to your application

1. Open the **server.js** file in a text editor, and change 'Hello World\n' to 'Hello Azure\n'. 

2. Save the file.

2. From the command line, change directories to the **helloworld** directory and run the following commands:

		git add .
		git commit -m "changing to hello azure"
		git push azure master

	You are prompted for your password again.

3. Refresh the browser window that you navigated to the web app's URL.

	![A web page displaying 'Hello Azure'][helloworld-completed]
<!-- deleted by customization

## Roll back a deployment

From the **Web app** blade you can click **Settings > Continuous Deployment** to see the deployment history in the **Deployments** blade. If you need to roll back to an earlier deployment, you can select it and then click **Redeploy** in the **Deployment Details** blade.

-->
<!-- keep by customization: begin -->
4. You can revert to the previous deployment by selecting it in **Deployments**.
<!-- keep by customization: end -->
## Next steps

You've deployed a Node.js application to a web app in Azure Websites. To learn more about how Azure Websites web apps run Node.js applications, see [Azure Websites: Node.js](http://blogs.msdn.com/b/silverlining/archive/2012/06/14/windows-azure-websites-node-js.aspx) and [Specifying a Node.js version in an Azure application](/documentation/articles/nodejs-specify-node-version-azure-apps).

Node.js provides a rich ecosystem of modules that can be used by your applications. To learn how Web Apps works with modules, see [Using Node.js modules with Azure applications](/documentation/articles/nodejs-use-node-modules-azure-apps).

If you encounter problems with your application after it has been deployed to Azure, see [How to debug a Node.js application in Azure Websites](/documentation/articles/web-sites-nodejs-debug) for information on diagnosing the problem.

This article uses the Azure Management Portal to create a web app. You can also use the [Azure Command-Line Interface](/documentation/articles/xplat-cli-install) or [Azure PowerShell](/documentation/articles/install-configure-powershell) to perform the same operations.

For more information about how to develop Node.js applications on Azure, see the [Node.js Developer Center](/develop/nodejs/).

<!-- keep by customization: begin -->
[Azure Management Portal]: http://manage.windowsazure.cn
[Azure Command-Line Tools for Mac and Linux]: /documentation/articles/xplat-cli
[Azure PowerShell]: /documentation/articles/install-configure-powershell
[portal-new- Website]: ./media/web-sites-nodejs-develop-deploy-mac/plus-new.png
[portal-git-username-password]: ./media/web-sites-nodejs-develop-deploy-mac/git-deployment-credentials.png
[git-instructions]: ./media/web-sites-nodejs-develop-deploy-mac/git-instructions.png
[git-deployments-first]: ./media/web-sites-nodejs-develop-deploy-mac/git_deployments_first.png
[git-deployments-second]: ./media/web-sites-nodejs-develop-deploy-mac/git_deployments_second.png
[where-is-code]: ./media/web-sites-nodejs-develop-deploy-mac/where_is_code.png
<!-- keep by customization: end -->
[helloworld-completed]: ./media/web-sites-nodejs-develop-deploy-mac/helloazure.png
[helloworld-localhost]: ./media/web-sites-nodejs-develop-deploy-mac/helloworldlocal.png
[portal-quick-create]: ./media/web-sites-nodejs-develop-deploy-mac/create-quick-website.png
[portal-quick-create2]: ./media/web-sites-nodejs-develop-deploy-mac/create-quick-website2.png
[setup-git-publishing]: ./media/web-sites-nodejs-develop-deploy-mac/setup_git_publishing.png
[go-to-dashboard]: ./media/web-sites-nodejs-develop-deploy-mac/go_to_dashboard.png
[deployment-part]: ./media/web-sites-nodejs-develop-deploy-mac/deployment-part.png
[deployment-credentials]: ./media/web-sites-nodejs-develop-deploy-mac/deployment-credentials.png
[git-url]: ./media/web-sites-nodejs-develop-deploy-mac/git-url.png
