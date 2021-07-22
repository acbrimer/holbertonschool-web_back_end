export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || startString === '') {
    return '';
  }
  return [...set].filter((f) => f && f.startsWith(startString))
    .map((s) => s.substr(startString.length, s.length)).join('-');
}
