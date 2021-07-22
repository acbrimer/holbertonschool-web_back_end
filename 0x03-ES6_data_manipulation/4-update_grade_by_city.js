export default function updateStudentGradeByCity(students, city, newGrades) {
  const newGradesObj = newGrades.reduce((acc, c) => ({ ...acc, [c.id]: c.grade }), {});
  return students.filter((f) => f.location === city).map((s) => (
    {
      id: s.id,
      firstName: s.firstName,
      grade: newGradesObj[s.id] ? newGradesObj[s.id] : 'N/A',
    }
  ));
}
