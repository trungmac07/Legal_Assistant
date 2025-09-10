import React from 'react';

const AppLayout = ({ sidebar, children }) => {
  const container = {
    display: 'flex',
    height: '100vh',
    backgroundColor: '#e0f7fa',
    overflow: 'hidden',
  };
  const sidebarStyle = {
    width: 300,
    backgroundColor: '#ffffff',
    borderRight: '1px solid #ccc',
    padding: 10,
    boxSizing: 'border-box',
    display: 'flex',
    flexDirection: 'column',
  };
  const content = {
    flex: 1,
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  };
  return (
    <div style={container}>
      <aside style={sidebarStyle}>{sidebar}</aside>
      <main style={content}>{children}</main>
    </div>
  );
};

export default AppLayout;



