export default function createIteratorObject(report) {
  if (report && Object.keys(report).length > 0) {
    return Object.keys(report.allEmployees).flatMap((k) => report.allEmployees[k]);
  }
  return [];
}
