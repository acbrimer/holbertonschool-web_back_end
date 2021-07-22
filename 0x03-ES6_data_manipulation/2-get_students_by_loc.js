export default function getStudentsByLocation(students, city) {
  return students.filter((f) => f.location === city);
}
