// 8-job
import { createQueue } from 'kue';

class JobCreator {
  /**
   * JobCreator - creates a job an dhandles completion
   */
  constructor(queue, job_data) {
    this.que = queue;
    this.job = this.que.create('push_notification_code_3', job_data);
    this.job.save(
      (err) => !err && console.log(`Notification job created: ${this.job.id}`)
    );
    this.job.on('complete', this.handleJobComplete);
    this.job.on('failed', this.handleJobFailure);
    this.job.on('progress', this.handleJobProgress);

    this.handleJobComplete = this.handleJobComplete.bind(this);
    this.handleJobFailure = this.handleJobFailure.bind(this);
    this.handleJobProgress = this.handleJobProgress.bind(this);
  }

  handleJobComplete = () =>
    console.log(`Notification job ${this.job.id} completed`);

  handleJobFailure = (err) =>
    console.log(`Notification job ${this.job.id} failed: ${err}`);

  handleJobProgress = (progress) =>
    console.log(`Notification job ${this.job.id} ${progress}% complete`);
}

const createPushNotificationsJob = (list, queue) => {
  if (!Array.isArray(list)) {
    new Error('Jobs is not an array');
  } else {
    list.forEach((job) => new JobCreator(queue, job));
  }
};

export default createPushNotificationsJob;
