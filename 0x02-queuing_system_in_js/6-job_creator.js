// 6-job_creator
import { createQueue } from 'kue';

class JobCreator {
  /**
   * JobCreator - creates a job an dhandles completion
   */
  constructor(queue_name, job_data) {
    this.que = createQueue();
    this.job = this.que.create(queue_name, job_data);
    this.job.save(
      (err) => !err && console.log(`Notification job created: ${this.job.id}`)
    );
    this.job.on('complete', this.handleJobComplete);
    this.job.on('failed', this.handleJobFailure);
  }

  handleJobComplete = () => console.log('Notification job completed');

  handleJobFailure = () => console.log('Notification job failed');
}

const main = () => {
  const data = {
    phoneNumber: 123456789,
    message: 'hello, job queue!',
  };
  new JobCreator('push_notification_code', data);
};

main();
