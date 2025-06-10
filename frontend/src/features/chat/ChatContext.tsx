import React, { createContext, useContext, useReducer, useCallback } from 'react';
import { v4 as uuidv4 } from 'uuid';
import type { ChatState, ChatContextType, Message } from './types';

const initialState: ChatState = {
  messages: [],
  isLoading: false,
  error: null,
};

type Action =
  | { type: 'SEND_MESSAGE_START' }
  | { type: 'SEND_MESSAGE_SUCCESS'; payload: Message }
  | { type: 'SEND_MESSAGE_ERROR'; payload: string }
  | { type: 'CLEAR_MESSAGES' };

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
    default:
      return state;
  }
};

const ChatContext = createContext<ChatContextType | undefined>(undefined);

export const ChatProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [state, dispatch] = useReducer(chatReducer, initialState);

  const sendMessage = useCallback(async (content: string) => {
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

      // TODO: Implement actual API call here
      // For now, simulate AI response
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      const aiMessage: Message = {
        id: uuidv4(),
        role: 'ai',
        content: 'This is a simulated AI response. API integration pending.',
        timestamp: Date.now(),
      };
      dispatch({ type: 'SEND_MESSAGE_SUCCESS', payload: aiMessage });
    } catch (error) {
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