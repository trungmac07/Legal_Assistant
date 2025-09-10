import React from 'react';

const AuthLayout = ({ title, children }) => {
  const container = {
    display: 'flex',
    height: '100vh',
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#e0f7fa',
  };
  const card = {
    backgroundColor: '#ffffff',
    padding: 30,
    borderRadius: 12,
    boxShadow: '0px 8px 30px rgba(0,0,0,0.08)',
    width: '100%',
    maxWidth: 420,
  };
  const heading = {
    textAlign: 'center',
    color: '#00796b',
    marginBottom: 20,
  };
  return (
    <div style={container}>
      <div style={card}>
        {title ? <h2 style={heading}>{title}</h2> : null}
        {children}
      </div>
    </div>
  );
};

export default AuthLayout;



