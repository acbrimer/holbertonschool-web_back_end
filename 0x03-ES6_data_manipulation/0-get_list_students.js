export default function getListStudents() {
  return [['Guillaume', 1, 'San Francisco'],
    ['James', 2, 'Columbia'],
    ['Serena', 5, 'San Francisco']].map((r) => ({ id: r[1], firstName: r[0], location: r[2] }));
}
