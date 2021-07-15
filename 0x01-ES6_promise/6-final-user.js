import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, filename) {
  const signup = signUpUser(firstName, lastName);
  const upload = uploadPhoto(filename);
  return Promise.allSettled([signup, upload]).then((values) => [
    values[0],
    values[1],
  ]);
}
