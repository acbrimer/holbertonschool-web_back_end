// 5-publisher
import { createClient } from 'redis';

class RedisPublisher {
  /**
   * RedisPublisher - connects to redis and publishes to a channel
   */
  constructor(channel = 'holberton school channel') {
    this.client = createClient();
    this.channel = channel;
    this.client.on('error', this.handleClientError);
    this.client.on('ready', this.handleClientReady);

    // bind functions that reference other stuff in class (funcs that use `this.`)
    this.handleClientReady = this.handleClientReady.bind(this);
    this.publishMessage = this.publishMessage.bind(this);
  }

  // handler functions
  handleClientError = (err) =>
    console.log('Redis client not connected to the server: ', err);

  handleClientReady = () => console.log('Redis client connected to the server');

  // handler for messages from subscribed channel (`this.channel`)
  publishMessage(message, time) {
    setTimeout(() => {
      console.log(`About to send ${message}`);
      this.client.publish(this.channel, message);
    }, time);
  }
}

const main = () => {
  const pub = new RedisPublisher('holberton school channel');
  pub.publishMessage('Holberton Student #1 starts course', 100);
  pub.publishMessage('Holberton Student #2 starts course', 200);
  pub.publishMessage('KILL_SERVER', 300);
  pub.publishMessage('Holberton Student #3 starts course', 400);
};

main();
