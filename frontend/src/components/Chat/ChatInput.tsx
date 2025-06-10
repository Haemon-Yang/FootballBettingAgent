import React, { useState } from 'react';
import type { KeyboardEvent } from 'react';
import styled, { keyframes } from 'styled-components';
import { theme } from '../../styles/theme';
import { Button } from '../Button/Button';

const slideUp = keyframes`
  from { transform: translateY(100%); }
  to { transform: translateY(0); }
`;

const InputContainer = styled.div`
  display: flex;
  gap: ${theme.spacing.md};
  padding: ${theme.spacing.lg};
  background-color: var(--background-light);
  border-top: 1px solid var(--border-color);
  position: sticky;
  bottom: 0;
  animation: ${slideUp} 0.3s ease;
  box-shadow: ${theme.shadows.medium};
`;

const InputWrapper = styled.div`
  flex: 1;
  position: relative;
`;

const StyledInput = styled.input`
  width: 100%;
  background-color: var(--background-input);
  color: var(--text-primary);
  border: 2px solid var(--border-color);
  border-radius: ${theme.borderRadius.lg};
  padding: ${theme.spacing.md} ${theme.spacing.lg};
  font-size: ${theme.typography.fontSize.medium};
  transition: all ${theme.transitions.default};
  
  &:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: ${theme.shadows.glow};
  }
  
  &:disabled {
    opacity: 0.7;
    cursor: not-allowed;
  }
  
  &::placeholder {
    color: var(--text-muted);
  }
`;

const InputHint = styled.div`
  position: absolute;
  right: ${theme.spacing.md};
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-muted);
  font-size: ${theme.typography.fontSize.small};
  pointer-events: none;
  opacity: 0.7;
`;

const SendButton = styled(Button)`
  min-width: 100px;
  height: 48px;
  transition: all ${theme.transitions.default};
  
  &:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: ${theme.shadows.glow};
  }
  
  &:disabled {
    opacity: 0.7;
    cursor: not-allowed;
  }
`;

interface ChatInputProps {
  onSendMessage: (message: string) => void;
  isLoading: boolean;
}

export const ChatInput: React.FC<ChatInputProps> = ({ onSendMessage, isLoading }) => {
  const [message, setMessage] = useState('');

  const handleSend = () => {
    if (message.trim() && !isLoading) {
      onSendMessage(message.trim());
      setMessage('');
    }
  };

  const handleKeyPress = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <InputContainer>
      <InputWrapper>
        <StyledInput
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Type your question..."
          disabled={isLoading}
        />
        {!message && !isLoading && (
          <InputHint>Press Enter to send</InputHint>
        )}
      </InputWrapper>
      <SendButton
        onClick={handleSend}
        disabled={!message.trim() || isLoading}
      >
        {isLoading ? 'Sending...' : 'Send'}
      </SendButton>
    </InputContainer>
  );
}; 