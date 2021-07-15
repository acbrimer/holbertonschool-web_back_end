import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  return Promise.allSettled([uploadPhoto(), createUser()]).then((vals) => ({
    photo: vals[0].status === 'fulfilled' ? vals[0].value : null,
    user: vals[1].status === 'fulfilled' ? vals[1].value : null,
  }));
}
