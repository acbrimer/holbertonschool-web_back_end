export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }
  return new Map([...map.entries()].map((i) => [i[0], i[1] === 1 ? 100 : i[1]]));
}
