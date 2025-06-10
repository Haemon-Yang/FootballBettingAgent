import React, { useState } from 'react';
import type { KeyboardEvent } from 'react';
import styled, { keyframes } from 'styled-components';
import { theme } from '../../styles/theme';
import { Button } from '../Button/Button';
import { DeepResearchButton } from '../Button/DeepResearchButton';

const slideUp = keyframes`
  from { transform: translateY(100%); }
  to { transform: translateY(0); }
`;

const InputContainer = styled.div`
  display: flex;
  flex-direction: column;
  gap: ${theme.spacing.sm};
  padding: ${theme.spacing.lg};
  background-color: var(--background-light);
  border-top: 1px solid var(--border-color);
  position: sticky;
  bottom: 0;
  animation: ${slideUp} 0.3s ease;
  box-shadow: ${theme.shadows.medium};
`;

const ButtonRow = styled.div`
  display: flex;
  align-items: flex-start;
  width: 100%;
  margin-bottom: 8px;
`;

const InputWrapper = styled.div`
  flex: 1;
  position: relative;
  display: flex;
  gap: ${theme.spacing.md};
  align-items: center;
`;

const StyledInput = styled.input`
  flex: 1;
  background-color: var(--background-input);
  color: var(--text-primary);
  border: 2px solid var(--border-color);
  border-radius: ${theme.borderRadius.lg};
  padding: ${theme.spacing.md} ${theme.spacing.xl} ${theme.spacing.md} ${theme.spacing.lg};
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
  right: 110px; /* leave space for Send button */
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-muted);
  font-size: ${theme.typography.fontSize.small};
  pointer-events: none;
  opacity: 0.7;
  background: transparent;
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
  onToggleDeepResearch?: (isActive: boolean) => void;
  isDeepResearchActive?: boolean;
}

export const ChatInput: React.FC<ChatInputProps> = ({
  onSendMessage,
  onToggleDeepResearch,
  isDeepResearchActive = false,
}) => {
  const [message, setMessage] = useState('');

  const handleSend = () => {
    if (message.trim()) {
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
      <ButtonRow>
        <DeepResearchButton
          active={isDeepResearchActive}
          onClick={() => onToggleDeepResearch && onToggleDeepResearch(!isDeepResearchActive)}
        />
      </ButtonRow>
      <InputWrapper>
        <StyledInput
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Type your question..."
        />
        {!message && (
          <InputHint>
            Press Enter to send
          </InputHint>
        )}
        <SendButton
          onClick={handleSend}
          disabled={!message.trim()}
        >
          Send
        </SendButton>
      </InputWrapper>
    </InputContainer>
  );
}; 