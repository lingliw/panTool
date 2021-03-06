<properties
   pageTitle="Reliable Actors Events"
   description="Introduction to Events for Service Fabric Reliable Actors."
   services="service-fabric"
   documentationCenter=".net"
   authors="jessebenson"
   manager="timlt"
   editor=""/>

<tags
   ms.service="service-fabric"
   ms.date="08/05/2015"
   wacn.date=""/>


# Actor Events
Actor events provide a way to send best effort notifications from the Actor to the clients. Actor events are designed for Actor-Client communication and should NOT be used for Actor-to-Actor communication.

Following code snippets shows how to use actor events in your application.

Define an interface that describes the events published by the actor. This interface must be derived from the `IActorEvents` interface. The arguments of the methods must be [data contract serializable](/documentation/articles/service-fabric-reliable-actors-notes-on-actor-type-serialization). The methods must return void as event notifications are one-way and best effort.

```csharp
public interface IGameEvents : IActorEvents
{
    void GameScoreUpdated(Guid gameId, string currentScore);
}
```

Declare the events published by the actor in the actor interface.

```csharp
public interface IGameActor : IActor, IActorEventPublisher<IGameEvents>
{
    Task UpdateGameStatus(GameStatus status);

    [Readonly]
    Task<string> GetGameScore();
}
```

On the client side, implement the event handler.

```csharp
class GameEventsHandler : IGameEvents
{
    public void GameScoreUpdated(Guid gameId, string currentScore)
    {
        Console.WriteLine(@"Updates: Game: {0}, Score: {1}", gameId, currentScore);
    }
}
```

On the client, create a proxy to the actor that publishes the event and subscribe to its events.

```csharp
var proxy = ActorProxy.Create<IGameActor>(
                    new ActorId(Guid.Parse(arg)), ApplicationName);
proxy.SubscribeAsync(new GameEventsHandler()).Wait();
```

In the event of failovers the actor may failover to a different process or node. The actor proxy manages the active subscriptions and automatically re-subscribes them. You can control the re-subscription interval through the `ActorProxyEventExtensions.SubscribeAsync<TEvent>` API. To unsubscribe use the `ActorProxyEventExtensions.UnsubscribeAsync<TEvent>` API.

On the actor, simply publish the events as they happen. If there are subscribers subscribed to the event, the Actors runtime will send them the notification.

```csharp
var ev = GetEvent<IGameEvents>();
ev.GameScoreUpdated(Id.GetGuidId(), State.Status.Score);
```
