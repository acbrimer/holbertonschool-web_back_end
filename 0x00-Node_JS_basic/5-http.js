const http = require('http');
const fs = require('fs');

const port = 1245;

const database = process.argv[2];
console.log('Database: ', database);

const parseCsv = (csv) => {
  /**
   * parseCsv - converts CSV to an array of JSON objects
   */

  // split all non-empty lines to array of arrays
  const rows = csv
    .split('\n')
    .filter((r) => r.trim() !== '')
    .map((r) => r.split(','));
  // remove columns from first row
  const columns = rows.shift();
  // zip cols/rows to array of objects
  return rows.map((r) => Object.fromEntries(columns.map((k, i) => [k, r[i]])));
};

function countStudents(path) {
  console.log('Count students: ', path);
  try {
    // read file to csv string
    const csv = fs.readFileSync(path).toString();
    // parse to array of objects
    const data = parseCsv(csv);
    // log total students
    const lines = [`Number of students: ${data.length}`];

    // filter and log students for CS, SWE fields
    ['CS', 'SWE'].forEach((field) => {
      const students = data.filter((r) => r.field && r.field === field);
      const countMsg = `Number of students in ${field}: ${
        students.length
      }. List: ${students.map((r) => r.firstname).join(', ')}`;
      lines.push(countMsg);
    });
    return lines.join('\n');
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

// create a server object:
const app = http
  .createServer((req, res) => {
    if (req.url.startsWith('/students')) {
      try {
        const countMessage = countStudents(database);
        res.write(countMessage);
        res.end();
      } catch (err) {
        res.statusCode = 404;
        res.write('Cannot load the database');
        res.end();
      }
    } else {
      res.write('Hello Holberton School!');
      res.end();
    }
  })
  .listen(port);

module.exports = app;
