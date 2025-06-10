import React, { createContext, useContext, useReducer, useCallback } from 'react';
import { v4 as uuidv4 } from 'uuid';
import type { ChatState, ChatContextType, Message } from './types';
import { config } from '../../config';

const initialState: ChatState = {
  messages: [],
  isLoading: false,
  error: null,
};

type Action =
  | { type: 'SEND_MESSAGE_START' }
  | { type: 'SEND_MESSAGE_SUCCESS'; payload: Message }
  | { type: 'SEND_MESSAGE_ERROR'; payload: string }
  | { type: 'CLEAR_MESSAGES' }
  | { type: 'ADD_THINKING_MESSAGE'; payload: Message }
  | { type: 'REMOVE_THINKING_MESSAGE' };

const chatReducer = (state: ChatState, action: Action): ChatState => {
  switch (action.type) {
    case 'SEND_MESSAGE_START':
      return { ...state, isLoading: true, error: null };
    case 'SEND_MESSAGE_SUCCESS':
      return {
        ...state,
        messages: [...state.messages, action.payload],
        isLoading: false,
      };
    case 'SEND_MESSAGE_ERROR':
      return { ...state, isLoading: false, error: action.payload };
    case 'CLEAR_MESSAGES':
      return { ...state, messages: [] };
    case 'ADD_THINKING_MESSAGE':
      return {
        ...state,
        messages: [...state.messages, action.payload],
      };
    case 'REMOVE_THINKING_MESSAGE':
      return {
        ...state,
        messages: state.messages.filter(msg => msg.role !== 'thinking'),
      };
    default:
      return state;
  }
};

const ChatContext = createContext<ChatContextType | undefined>(undefined);

export const ChatProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [state, dispatch] = useReducer(chatReducer, initialState);

  const sendMessage = useCallback(async (content: string, isDeepResearch: boolean = false) => {
    dispatch({ type: 'SEND_MESSAGE_START' });

    try {
      // Add user message
      const userMessage: Message = {
        id: uuidv4(),
        role: 'user',
        content,
        timestamp: Date.now(),
      };
      dispatch({ type: 'SEND_MESSAGE_SUCCESS', payload: userMessage });

      // Add thinking message
      const thinkingMessage: Message = {
        id: uuidv4(),
        role: 'thinking',
        content: '',
        timestamp: Date.now(),
      };
      dispatch({ type: 'ADD_THINKING_MESSAGE', payload: thinkingMessage });

      // Make API call based on whether deep research is active
      const endpoint = isDeepResearch ? '/api/deep-research/analyze' : '/api/agent/chat';
      const response = await fetch(`${config.API_URL}${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: content,
          ...(isDeepResearch && { context: {} }), // Add context for deep research
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to get response from server');
      }

      const data = await response.json();
      
      // Remove thinking message
      dispatch({ type: 'REMOVE_THINKING_MESSAGE' });
      
      const aiMessage: Message = {
        id: uuidv4(),
        role: 'ai',
        content: data.response,
        timestamp: Date.now(),
      };
      dispatch({ type: 'SEND_MESSAGE_SUCCESS', payload: aiMessage });
    } catch (error) {
      // Remove thinking message on error
      dispatch({ type: 'REMOVE_THINKING_MESSAGE' });
      dispatch({ type: 'SEND_MESSAGE_ERROR', payload: 'Failed to send message' });
    }
  }, []);

  const clearMessages = useCallback(() => {
    dispatch({ type: 'CLEAR_MESSAGES' });
  }, []);

  return (
    <ChatContext.Provider value={{ state, sendMessage, clearMessages }}>
      {children}
    </ChatContext.Provider>
  );
};

export const useChat = () => {
  const context = useContext(ChatContext);
  if (context === undefined) {
    throw new Error('useChat must be used within a ChatProvider');
  }
  return context;
}; 