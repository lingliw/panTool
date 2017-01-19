App Service Mobile Apps uses [Notification Hubs] to send pushes, so you will be configuring a notification hub for your mobile app.

1. In [Azure Portal], go to **App Services**, then click your app backend. Under **Settings**, click **Push**.
2. Click **Connect** to add a notification hub resource to the app. You can either create a hub or connect to an existing one.
   
    ![](./media/app-service-mobile-create-notification-hub/configure-hub-flow.png)

Now you have connected a notification hub to your Mobile App backend. Later you will configure this notification hub to connect to a platform notification system (PNS) to push to devices.

[Azure Portal]: https://portal.azure.cn/
[Notification Hubs]: /documentation/articles/notification-hubs-push-notification-overview/