export default function createInt8TypedArray(length, position, value) {
  const buff = new ArrayBuffer(length);
  const view = new Int8Array(buff);
  view[position] = value;
  return new DataView(buff);
}
