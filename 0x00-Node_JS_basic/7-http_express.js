const fs = require('fs');
const express = require('express');

const app = express();
const port = 1245;

const database = process.argv[2];

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
    return 'Cannot load the database';
  }
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.send(`This is the list of our students\n${countStudents(database)}`);
});

app.listen(port);

module.exports = app;
