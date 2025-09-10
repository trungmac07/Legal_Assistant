import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import LoginView from './views/login_view';
import SignupView from './views/signup_view';
import HomeView from './views/home_view';
import { jwtDecode } from 'jwt-decode';
import { refreshAccessToken } from './controllers/refresh_controller';

const login_view = <LoginView />
const signup_view = <SignupView />
const home_view = <HomeView />

const check_token_expired = (token) => {
  try {
    if (!token) {
      return true; 
    }
    const decodedToken = jwtDecode(token);
    const currentTime = Date.now() / 1000; 
    return decodedToken.exp < currentTime;
  } catch (error) {
    
    return true;
  }
}

const getAccessToken = () => {
  return window.accessToken;
}


const ProtectedRoute = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(null); 

  useEffect(() => {
    const checkAuth = async () => {
      try {
        let token = window.accessToken;
        if (!token || check_token_expired(token)) {
          token = await refreshAccessToken();
        }

        if (token && !check_token_expired(token)) {
          setIsAuthenticated(true);
          window.accessToken = token;
        } else {
          setIsAuthenticated(false);
        }
      } catch (err) {
        console.error("Token refresh failed", err);
        setIsAuthenticated(false);
      }
    };

    checkAuth();
  }, []);

  if (isAuthenticated === null) {
    return <div>Loading...</div>;
  }

  return isAuthenticated ? children : <Navigate to="/login" />;
};


const PublicRoute = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(null); 

  useEffect(() => {
    const checkAuth = async () => {
      try {
        let token = window.accessToken;

        if (!token || check_token_expired(token)) {
            token = await refreshAccessToken();
        }

        if (token && !check_token_expired(token)) {
          setIsAuthenticated(true);
          window.accessToken = token;
        } else {
          setIsAuthenticated(false);
        }
      } catch (err) {
        console.error("Token refresh failed", err);
        setIsAuthenticated(false);
      }
    };

    checkAuth();
  }, []);

  if (isAuthenticated === null) {
    return <div>Loading...</div>;
  }

  return isAuthenticated ? <Navigate to="/home" /> : children;
};


function RoutesApp() {
  return (
    <Router>
      <Routes>
        <Route path="" element={<Navigate to="/login" />} />
        
        <Route 
          path="/login" 
          element={
            <PublicRoute>
              {login_view}
            </PublicRoute>
          } 
        />
        
        <Route 
          path="/signup" 
          element={
            <PublicRoute>
              {signup_view}
            </PublicRoute>
          } 
        />
        
        <Route 
          path="/home" 
          element={
            <ProtectedRoute>
              {home_view}
            </ProtectedRoute>
          } 
        />
      </Routes>
    </Router>
  );
}

export default RoutesApp;