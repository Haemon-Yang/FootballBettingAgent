import React, { useState } from 'react';
import type { KeyboardEvent } from 'react';
import styled, { keyframes, css } from 'styled-components';
import { theme } from '../../styles/theme';
import { Button } from '../Button/Button';
import { DeepResearchButton } from '../Button/DeepResearchButton';

const slideUp = keyframes`
  from { transform: translateY(100%); }
  to { transform: translateY(0); }
`;

const pulse = keyframes`
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
`;

const shimmer = keyframes`
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
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

const SendButton = styled(Button)<{ isResponding: boolean }>`
  min-width: 100px;
  height: 48px;
  transition: all ${theme.transitions.default};
  position: relative;
  overflow: hidden;
  
  ${({ isResponding }) =>
    isResponding &&
    css`
      animation: ${pulse} 1.5s infinite;
      cursor: not-allowed;
      &::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(
          90deg,
          transparent,
          rgba(255, 255, 255, 0.2),
          transparent
        );
        animation: ${shimmer} 1.5s infinite;
      }
    `}
  
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
  isAiResponding?: boolean;
}

export const ChatInput: React.FC<ChatInputProps> = ({
  onSendMessage,
  onToggleDeepResearch,
  isDeepResearchActive = false,
  isAiResponding = false,
}) => {
  const [message, setMessage] = useState('');

  const handleSend = () => {
    if (message.trim() && !isAiResponding) {
      onSendMessage(message.trim());
      setMessage('');
    }
  };

  const handleKeyPress = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && !e.shiftKey && !isAiResponding) {
      e.preventDefault();
      handleSend();
    } else if (e.key === 'Enter' && isAiResponding) {
      e.preventDefault(); // Block sending with Enter
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
        {!message && !isAiResponding && (
          <InputHint>
            Press Enter to send
          </InputHint>
        )}
        <SendButton
          onClick={handleSend}
          disabled={!message.trim() || isAiResponding}
          isResponding={isAiResponding}
        >
          Send
        </SendButton>
      </InputWrapper>
    </InputContainer>
  );
}; 