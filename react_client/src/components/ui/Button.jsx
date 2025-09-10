import React from 'react';

const Button = ({ children, onClick, type = 'button', style = {}, disabled = false }) => {
  const baseStyle = {
    padding: '12px 16px',
    backgroundColor: disabled ? '#9e9e9e' : '#00796b',
    border: 'none',
    borderRadius: '8px',
    color: '#ffffff',
    fontSize: '16px',
    cursor: disabled ? 'not-allowed' : 'pointer',
  };
  return (
    <button type={type} onClick={onClick} style={{ ...baseStyle, ...style }} disabled={disabled}>
      {children}
    </button>
  );
};

export default Button;



