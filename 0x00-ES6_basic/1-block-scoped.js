/* eslint-disable no-var */
/* eslint-disable no-use-before-define */
/* eslint-disable vars-on-top */
export default function taskBlock(trueOrFalse) {
  if (trueOrFalse) {
    task = true;
    task2 = false;
  } else {
    task = false;
    task2 = true;
  }
  var task;
  var task2;
  return [task, task2];
}
