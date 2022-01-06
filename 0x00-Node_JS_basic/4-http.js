const http = require('http');

const port = 1245;

// create a server object:
const app = http
  .createServer((req, res) => {
    res.write('Hello Holberton School!');
    res.end();
  })
  .listen(port);

module.exports = app;
