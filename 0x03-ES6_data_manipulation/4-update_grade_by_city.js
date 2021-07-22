export default function updateStudentGradeByCity(students, city, newGrades) {
  const newGradesObj = newGrades.reduce((acc, c) => ({ ...acc, [c.studentId]: c.grade }), {});
  return students.filter((f) => f.location === city).map((s) => (
    {
      id: s.id,
      firstName: s.firstName,
      location: s.location,
      grade: Object.keys(newGradesObj).includes(s.id.toString()) ? newGradesObj[s.id.toString()] : 'N/A',
    }
  ));
}
