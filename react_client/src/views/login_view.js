import React, { useState } from 'react';
import {login} from '../controllers/login_controller'
import AuthLayout from '../layouts/AuthLayout';
import Input from '../components/ui/Input';
import Button from '../components/ui/Button';
import { ROUTES } from '../utils/config';
import { useNavigate } from 'react-router-dom';

const LoginView = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const loginClick = async (e) => {
    e.preventDefault();
    
    if (!email || !password) {
      alert('Please fill in both email and password.');
      return;
    }

    try {
      const response = await login(email, password);
      
      if (response.status === 200) {
        alert(response.data.message);
        navigate('/home');
      }
    } catch (error) {
      console.error('Login error:', error);
    }
  };

  return (
    <AuthLayout title="Welcome to Legal Miracle!">
      <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
        <Input 
          type="email" 
          placeholder="Email" 
          value={email} 
          onChange={(e) => setEmail(e.target.value)} 
        />
        <Input 
          type="password" 
          placeholder="Password" 
          value={password} 
          onChange={(e) => setPassword(e.target.value)} 
        />
        <Button type="submit" onClick={loginClick}>
          Login
        </Button>
        <p style={{ marginTop: 12, fontSize: 14, color: '#555' }}>
          Don't have an account?{' '}
          <a href={ROUTES.signup} style={{ color: '#007bff', textDecoration: 'none' }}>
            Sign Up
          </a>
        </p>
      </div>
    </AuthLayout>
  );
};

export default LoginView;