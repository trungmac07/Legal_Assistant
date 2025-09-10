import React, { useState, useEffect, useRef } from 'react';
import { api } from '../utils/api';

export const get_history = async (url) => {
    try {
        let response = await api.get(
                url, 
                {
                    params: {"user_id": sessionStorage.getItem('user_id')},
                },
        );

        return response;

    } catch (error) {
        console.error('Error getting response:', error);
        return error;

    }

};
