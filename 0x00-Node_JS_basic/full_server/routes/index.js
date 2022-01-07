const express = require('express');
const AppController = require('../controllers/AppController');
const StudentsController = require('../controllers/StudentsController');

const router = express.Router();

router.use('/students/:major', StudentsController.getAllStudentsByMajor);
router.use('/students', StudentsController.getAllStudents);
router.use('/', AppController.getHomepage);

module.exports = router;
