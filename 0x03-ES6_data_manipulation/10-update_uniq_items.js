export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }
  [...map.entries()].forEach((i) => {
    if (i[1] === 1) {
      map.set(i[0], 100);
    }
  });
}
