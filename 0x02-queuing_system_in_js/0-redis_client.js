// 0-redis_client
import { createClient } from 'redis';

// create client
const client = createClient();

// create callbacks for error/ready
client.on('error', (err) =>
  console.log('Redis client not connected to the server: ', err)
);

client.on('ready', () => console.log('Redis client connected to the server'));
