// 7-job_creator
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

const main = () => {
  const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account',
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account',
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account',
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account',
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account',
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account',
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account',
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account',
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account',
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account',
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account',
    },
  ];
  jobs.forEach((job) => new JobCreator('push_notification_code_2', job));
};

main();
