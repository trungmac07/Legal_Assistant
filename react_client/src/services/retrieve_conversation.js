import React, { useState, useEffect, useRef } from 'react';
import { api } from '../utils/api';

export const get_conversation = async (url, data) => {
    try {
        const c_id = data["conversation_id"]
        let response = await api.get(
                url, 
                {
                    params : data
                },
        );

        return response;

    } catch (error) {
        console.error('Error:', error);
        return error;

    }

};
