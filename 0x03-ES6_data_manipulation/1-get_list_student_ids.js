export default function getListStudentIds(students) {
  return Array.isArray(students) ? students.map((s) => s.id) : [];
}
