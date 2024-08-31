
export const styles = {
    container: {
      display: 'flex',
      height: '100vh',
      backgroundColor: '#e0f7fa',
      overflow: 'hidden',
    },
    sidebar: {
      width: '300px',
      backgroundColor: '#ffffff',
      borderRight: '1px solid #ccc',
      padding: '10px',
      boxSizing: 'border-box',
      display: 'flex',
      flexDirection: 'column',
    },
    sidebarTitle: {
      margin: 0,
      fontSize: '18px',
      fontWeight: 'bold',
      color: '#004d40',
    },
    historyList: {
      marginTop: '10px',
      overflowY: 'auto',
    },
    historyItem: {
      padding: '10px',
      borderRadius: '8px',
      margin: '5px 0',
      cursor: 'pointer',
      backgroundColor: '#e0f2f1',
      color: '#004d40',
    },
    chatArea: {
      flex: 1,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      padding: '20px',
    },
    chatFrame: {
      width: '70%',
      maxWidth: '800px',
      height: '100%',
      display: 'flex',
      flexDirection: 'column',
      borderRadius: '8px',
      backgroundColor: '#ffffff',
      boxShadow: '0px 4px 6px rgba(0, 0, 0, 0.1)',
      overflow: 'hidden',
      
    },
    chatContainer: {
      flex: 1,
      display: 'flex',
      flexDirection: 'column',
      padding: '10px',
      overflowY: 'auto',
    },
    message: {
      maxWidth: '90%',
      margin: '5px 0',
      padding: '5px 15px',
      borderRadius: '15px',
      color: '#004d40',
      fontSize: '17px',
      lineHeight: '17px',
      wordWrap: 'break-word',
      // Prevent XSS vulnerabilities
      whiteSpace: 'pre-wrap',
    },
    inputContainer: {
      display: 'flex',
      alignItems: 'center',
      padding: '10px',
      borderTop: '1px solid #ccc',
      backgroundColor: '#ffffff',
    },
    input: {
      flex: 1,
      border: 'none',
      outline: 'none',
      padding: '10px',
      fontSize: '21px',
      borderRadius: '8px',
      backgroundColor: '#e0f7fa',
    },
    sendButton: {
      marginLeft: '10px',
      padding: '10px 20px',
      backgroundColor: '#00acc1',
      color: '#ffffff',
      border: 'none',
      borderRadius: '8px',
      cursor: 'pointer',
    },
    '@media (max-width: 768px)': {
      sidebar: {
        width: '100%',
        borderRight: 'none',
        borderBottom: '1px solid #ccc',
      },
      chatArea: {
        padding: '10px',
      },
      chatFrame: {
        width: '100%',
        height: '80vh',
      },
    },
    '@media (max-width: 480px)': {
      sidebar: {
        display: 'none',
      },
      chatFrame: {
        width: '100%',
        height: '90vh',
      },
    },
  };
  