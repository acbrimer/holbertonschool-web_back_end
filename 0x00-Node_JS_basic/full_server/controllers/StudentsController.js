/* eslint-disable no-unused-vars */
const { readDatabase } = require('../utils');

const database = process.argv[2];

class StudentsController {
  static getAllStudents(request, response) {
    readDatabase(database)
      .then((data) => {
        const results = Object.keys(data)
          .map(
            (f) =>
              // eslint-disable-next-line implicit-arrow-linebreak
              `Number of students in ${f}: ${data[f].length}. List: ${data[
                f
                // eslint-disable-next-line comma-dangle
              ].join(', ')}`
          )
          .join('\n');
        const message = `This is the list of our students\n${results}`;
        return response.status(200).send(message);
      })
      .catch((err) => response.status(404).send(err.message));
  }

  static getAllStudentsByMajor(request, response) {
    readDatabase(database)
      .then((data) => {
        const field = request.params.major;
        if (Object.keys(data).includes(field)) {
          return response.status(200).send(`List: ${data[field].join(', ')}`);
        }
        return response.status(500).send('Major parameter must be CS or SWE');
      })
      .catch((err) => response.status(404).send(err.message));
  }
}

module.exports = StudentsController;
