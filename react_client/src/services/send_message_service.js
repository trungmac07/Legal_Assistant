import React, { useState, useEffect, useRef } from 'react';
import { api } from '../utils/api';

export const send_message = async (url, data, kwargs) => {

    const token = sessionStorage.getItem('access_token');

    try {
        const response = await api.post(url, JSON.stringify(data));
    
        if (response.status !== 200) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
    
        const headers = response.headers;
        const full_response = response.data;
        const oldMessages = kwargs["selectedConversation"];
        let newMessages = {
          sender: "bot",
          text: full_response, 
        };
        kwargs["setSelectedConversation"]([...oldMessages, newMessages]);
        kwargs["setCurrentMessage"]("");
    
        return { headers };
      } catch (error) {
        console.error("Error getting response:", error);
        throw error;
      }
};