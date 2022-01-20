// 6-job_processor
import { createQueue } from 'kue';

class JobProcessor {
  constructor(queue_name) {
    this.que = createQueue();

    this.que.process(queue_name, (job, done) => {
      this.sendNotification(job.data.phoneNumber, job.data.message);
      done();
    });
  }

  sendNotification = (phoneNumber, message) =>
    console.log(
      `Sending notification to ${phoneNumber}, with message: ${message}`
    );
}

const main = () => {
  new JobProcessor('push_notification_code');
};

main();
