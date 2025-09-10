import { api } from '../utils/api';



export const post_signup = async (url, data) => {
    try 
    {   
        data.gender = data.gender[0].toUpperCase()
        const response = await api.post(url, JSON.stringify(data));
        return response;
    } 
    catch (error) 
    {
        try
        {
            alert('An error occurred. Please try again:\n' + error.response.data.error_message);
            return error.response
        }
        catch(error2)
        {
            alert(error)
            return error 
        }
        
    }


};

