<!-- deleted in Global -->

4. Navigate to your API app's gateway blade.

	![Click gateway](./media/app-service-api-gateway-config-auth/gateway.png)

7. In the **Gateway** blade, click **Settings**, and then click **Identity**.

	![Click Settings](./media/app-service-api-gateway-config-auth/clicksettingsingateway.png)

	![Click Identity](./media/app-service-api-gateway-config-auth/clickidentity.png)

	From the **Identity** blade you can navigate to different blades for configuring authentication using Azure Active Directory and several other providers.

	![Identity blade](./media/app-service-api-gateway-config-auth/identityblade.png)
  
3. Choose the identity provider you want to use, and follow the steps in the corresponding article to configure your API app with that provider. These articles were written for mobile apps, but the procedures are the same for API apps. Some of the procedures require you to use the [Azure Management Portal]. 

 - [Microsoft Account](/documentation/articles/app-service-mobile-how-to-configure-microsoft-authentication)
 - [Facebook login](/documentation/articles/app-service-mobile-how-to-configure-facebook-authentication)
 - [Twitter login](/documentation/articles/app-service-mobile-how-to-configure-twitter-authentication)
 - [Google login](/documentation/articles/app-service-mobile-how-to-configure-google-authentication)
 - [Azure Active Directory](/documentation/articles/app-service-mobile-how-to-configure-active-directory-authentication)

As an example, the following screen shots show what you should see in the [Azure Management Portal] pages and [Azure preview portal] blades after you have set up Azure Active Directory authentication.

In the Azure preview portal, The **Azure Active Directory** blade has a **Client ID** from the application you created in the Azure Active Directory tab of the Azure Management Portal, and **Allowed Tenants** has your Azure Active Directory tenant (for example, "contoso.partner.onmschina.cn").

![Azure Active Directory blade](./media/app-service-api-gateway-config-auth/tdinaadblade.png)

In the Azure Management Portal, the **Configure** tab for the application you created in the **Azure Active Directory** tab has the **Sign-on URL**, **App ID URI**, and **Reply URL** from the **Azure Active Directory** blade in the Azure preview portal.

![](./media/app-service-api-gateway-config-auth/oldportal1.png)

![](./media/app-service-api-gateway-config-auth/oldportal2.png)

![](./media/app-service-api-gateway-config-auth/oldportal3.png)

![](./media/app-service-api-gateway-config-auth/oldportal4.png)

(The Reply URL in the image shows the same URL twice, once with `http:` and once with `https:`.)
