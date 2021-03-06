const fs = require('fs');

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

function readDatabase(path) {
  return new Promise((resolve, reject) => {
    try {
      // read file to csv string
      const csv = fs.readFileSync(path).toString();
      // parse to array of objects
      const data = parseCsv(csv);
      // return object with list of students for each field
      const students = {
        CS: data
          .filter((r) => r.field && r.field === 'CS')
          .map((r) => r.firstname),
        SWE: data
          .filter((r) => r.field && r.field === 'SWE')
          .map((r) => r.firstname),
      };
      resolve(students);
    } catch (err) {
      reject(new Error('Cannot load the database'));
    }
  });
}

module.exports = { readDatabase };
