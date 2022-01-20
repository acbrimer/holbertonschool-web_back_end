// 1-redis_op
import redis, { createClient } from 'redis';

class RedisStore {
  /**
   * RedisStore - creates redis client and functions to CRUD data
   */
  constructor() {
    this.client = createClient();
    // set handler functions for error/ready callbacks
    this.client.on('error', this.handleClientError);
    this.client.on('ready', this.handleClientReady);
    // bind functions that reference other stuff in class (funcs that use `this.`)
    this.setObject = this.setObject.bind(this);
    this.displayObject = this.displayObject.bind(this);
  }

  // handler functions
  handleClientError = (err) =>
    console.log('Redis client not connected to the server: ', err);

  handleClientReady = () => console.log('Redis client connected to the server');

  // CRUD functions
  setObject(key, obj = {}) {
    Object.entries(obj).forEach((field, value) =>
      this.client.hset(key, field, value, redis.print)
    );
  }

  displayObject(key) {
    this.client.hgetall(key, (err, data) => console.log(data));
  }
}

const main = () => {
  const store = new RedisStore();

  store.setObject('HolbertonSchools', {
    Portland: '50',
    Seattle: '80',
    ['New York']: '20',
    Bogota: '20',
    Cali: '40',
    Paris: '2',
  });
  store.displayObject('HolbertonSchools');
};

main();
