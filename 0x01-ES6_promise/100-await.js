import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  return Promise.allSettled([uploadPhoto(), createUser()])
    .then((vals) => (vals.map((v) => v.status).includes('rejected')
      ? ({ photo: null, user: null })
      : ({
        photo: vals[0].value,
        user: vals[1].value,
      })
    ));
}
