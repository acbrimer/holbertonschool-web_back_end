// 7-job_processor
import { createQueue } from 'kue';

class JobProcessor {
  // set blacklisted numbers

  constructor(queue_name) {
    this.que = createQueue();
    this.blacklist = ['4153518780', '4153518781'];
    this.que.process(queue_name, 2, (job, done) =>
      this.sendNotification(job.data.phoneNumber, job.data.message, job, done)
    );
  }

  sendNotification = (phoneNumber, message, job, done) => {
    job.progress(0, 100);
    if (this.blacklist.includes(phoneNumber)) {
      return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }
    job.progress(50, 100);
    console.log(
      `Sending notification to ${phoneNumber}, with message: ${message}`
    );
    return done();
  };
}

const main = () => {
  new JobProcessor('push_notification_code_2');
};

main();
