export default function cleanSet(set, startString) {
  return !(startString instanceof String) || startString === '' ? '' : [...set].filter((f) => f && f.startsWith(startString))
    .map((s) => s.substr(startString.length, s.length)).join('-');
}
