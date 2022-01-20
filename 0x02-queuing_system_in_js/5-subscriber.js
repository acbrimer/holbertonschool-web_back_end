// 5-subscriber
import { createClient } from 'redis';

class RedisSubscriber {
  /**
   * RedisSubscriber - connects to redis and subscribes to channel
   */
  constructor(channel = 'holberton school channel') {
    this.client = createClient();
    this.channel = channel;
    this.client.on('error', this.handleClientError);
    // set handler for messages
    this.client.on('message', this.handleClientMessage);

    this.client.on('ready', this.handleClientReady);

    // bind functions that reference other stuff in class (funcs that use `this.`)
    this.handleClientReady = this.handleClientReady.bind(this);
    this.handleClientMessage = this.handleClientMessage.bind(this);
  }

  // handler functions
  handleClientError = (err) =>
    console.log('Redis client not connected to the server: ', err);

  handleClientReady = () => {
    console.log('Redis client connected to the server');
    // subscribe to the channel after ready event
    this.client.subscribe(this.channel);
  };

  // handler for messages from subscribed channel (`this.channel`)
  handleClientMessage = (channel, message) => {
    // unsubscribe and quit on kill message
    if (message === 'KILL_SERVER') {
      this.client.unsubscribe(channel);
      this.client.quit();
    }
    console.log(message);
  };
}

const main = () => {
  new RedisSubscriber('holberton school channel');
};

main();
