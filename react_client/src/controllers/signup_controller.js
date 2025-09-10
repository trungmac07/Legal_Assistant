import { post_signup } from '../services/signup_service';

export const signup = async (formdata) => {

    return await post_signup("api/signup/", formdata);
};
