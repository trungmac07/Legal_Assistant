import React from 'react';

const Input = ({ type = 'text', name, value, onChange, placeholder, style = {} }) => {
  const baseStyle = {
    width: '100%',
    padding: '12px',
    border: '1px solid #b2dfdb',
    borderRadius: '8px',
    fontSize: '16px',
    boxSizing: 'border-box',
  };
  return (
    <input type={type} name={name} value={value} onChange={onChange} placeholder={placeholder} style={{ ...baseStyle, ...style }} />
  );
};

export default Input;



