/* eslint-disable no-var */
/* eslint-disable no-use-before-define */
/* eslint-disable vars-on-top */
export default function taskBlock(trueOrFalse) {
  if (trueOrFalse) {
    task = true;
    task2 = false;
  }
  var task = false;
  var task2 = true;
  return [task, task2];
}
