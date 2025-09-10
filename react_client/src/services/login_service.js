import { api, setAuthTokens } from '../utils/api';

const getAccessToken = () => {
  return window.accessToken;
}

const setAccessToken = (token) => {
  window.accessToken = token;
}

const removeAccessToken = () => {
  window.accessToken = "";
}

export const post_login = async (url, email, password) => {
  try {   
    const data = {
      'email': email,
      'password': password,
    }
    
    
    const response = await api.post(url, JSON.stringify(data), {
      withCredentials: true, 
    });
    
    setAccessToken(response.data["access_token"]);

    sessionStorage.setItem('user_id', response.data["user_id"]);
    
    return response;
  } 
  catch (error) {
    try {  
      alert('An error occurred. Please try again:\n' + error.response.data.message);
      return error.response;
    }
    catch(error2) {
      alert(error);
      return error;
    }
  }
};


export const refreshAccessTokenService = async () => {
  try {
    const response = await api.post('/api/token/refresh/', {}, {
      withCredentials: true, 
    });
    
    setAccessToken(response.data["access_token"]);
    return response.data["access_token"];
  } catch (error) {
    
    
    removeAccessToken();
    sessionStorage.removeItem('user_id');
    return null;
  }
};


export const logout = async () => {
  try {
    await api.post('/api/logout/', {}, {
      withCredentials: true,
    });
  } catch (error) {
    console.error('Logout error:', error);
  } finally {
    removeAccessToken();
    sessionStorage.removeItem('user_id');
    window.location.href = '/login';
  }
};