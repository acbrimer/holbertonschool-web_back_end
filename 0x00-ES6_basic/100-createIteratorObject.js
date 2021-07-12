export default function createIteratorObject(report) {
  if (report && Object.keys(report).length > 0) {
    Object.keys(report)
      .map((k) => report[k].allEmployees)
      .reduce((c, acc) => acc.append(...c), []);
  }
}
