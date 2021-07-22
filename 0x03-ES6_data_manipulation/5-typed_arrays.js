export default function createInt8TypedArray(length, position, value) {
  if (position >= length) {
    throw new Error('Position outside range');
  }
  const buff = new ArrayBuffer(length);
  const view = new Int8Array(buff);
  view[position] = value;
  return new DataView(buff);
}
