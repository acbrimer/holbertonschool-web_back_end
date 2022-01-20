// 2-redis_op_async
import redis, { createClient } from 'redis';
import { promisify } from 'util';

class RedisStore {
  /**
   * RedisStore - creates redis client and functions to CRUD data
   */
  constructor() {
    this.client = createClient();
    // set handler functions for error/ready callbacks
    this.client.on('error', this.handleClientError);
    this.client.on('ready', this.handleClientReady);
    // create async get/set against client using promisify
    this.setAsync = promisify(this.client.set).bind(this.client);
    this.getAsync = promisify(this.client.get).bind(this.client);
    // bind functions that use `this.client` class prop
    this.setNewSchool = this.setNewSchool.bind(this);
    this.displaySchoolValue = this.displaySchoolValue.bind(this);
  }

  // handler functions
  handleClientError = (err) =>
    console.log('Redis client not connected to the server: ', err);

  handleClientReady = () => console.log('Redis client connected to the server');

  // CRUD functions
  setNewSchool = async (schoolName, value) => {
    await this.setAsync(schoolName, value);
    console.log('Reply: OK');
  };

  displaySchoolValue = async (schoolName) => {
    const value = await this.getAsync(schoolName);
    console.log(value);
  };
}

const main = async () => {
  const store = new RedisStore();
  await store.displaySchoolValue('Holberton');
  await store.setNewSchool('HolbertonSanFrancisco', '100');
  await store.displaySchoolValue('HolbertonSanFrancisco');
};

main();
