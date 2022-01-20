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
    // bind functions that use `this.client` class prop
    this.setNewSchool = this.setNewSchool.bind(this);
    this.displaySchoolValue = this.displaySchoolValue.bind(this);
  }

  // handler functions
  handleClientError = (err) =>
    console.log('Redis client not connected to the server: ', err);

  handleClientReady = () => console.log('Redis client connected to the server');

  // CRUD functions
  setNewSchool = (schoolName, value) =>
    this.client.set(schoolName, value, redis.print);

  displaySchoolValue = (schoolName) =>
    this.client.get(schoolName, (err, data) => console.log(data));
}

const main = () => {
  const store = new RedisStore();
  store.displaySchoolValue('Holberton');
  store.setNewSchool('HolbertonSanFrancisco', '100');
  store.displaySchoolValue('HolbertonSanFrancisco');
};

main();
