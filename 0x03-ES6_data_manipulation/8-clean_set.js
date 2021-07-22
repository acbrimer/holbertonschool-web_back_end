export default function cleanSet(set, startString) {
  return startString === '' ? '' : [...set].filter((f) => f && f.startsWith(startString))
    .map((s) => s.substr(startString.length, s.length)).join('-');
}
