export default function taskBlock(trueOrFalse) {

    if (trueOrFalse) {
      task = true;
      task2 = false;
    }
    else {
        task = false;
        task2 = true;
    }
  
    var task, task2
    return [task, task2];
  }