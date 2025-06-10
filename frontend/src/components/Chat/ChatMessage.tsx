import React from 'react';
import styled, { keyframes } from 'styled-components';
import { theme } from '../../styles/theme';
import type { Message } from '../../features/chat/types';

const fadeIn = keyframes`
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
`;

const MessageContainer = styled.div<{ role: Message['role'] }>`
  display: flex;
  flex-direction: column;
  align-items: ${({ role }) => (role === 'user' ? 'flex-end' : 'flex-start')};
  margin: ${theme.spacing.md} 0;
  max-width: 80%;
  margin-left: ${({ role }) => (role === 'user' ? 'auto' : '0')};
  animation: ${fadeIn} 0.3s ease;
`;

const MessageBubble = styled.div<{ role: Message['role'] }>`
  background-color: ${({ role }) =>
    role === 'user' ? 'var(--primary-color)' : 'var(--background-card)'};
  color: ${({ role }) =>
    role === 'user' ? 'var(--text-primary)' : 'var(--text-secondary)'};
  padding: ${theme.spacing.md} ${theme.spacing.lg};
  border-radius: ${theme.borderRadius.lg};
  box-shadow: ${theme.shadows.small};
  position: relative;
  transition: transform ${theme.transitions.default};
  
  &:hover {
    transform: translateY(-2px);
    box-shadow: ${theme.shadows.medium};
  }
  
  &::before {
    content: '';
    position: absolute;
    top: 50%;
    ${({ role }) => (role === 'user' ? 'right: -8px;' : 'left: -8px;')}
    transform: translateY(-50%);
    border-style: solid;
    border-width: 8px;
    border-color: transparent;
    border-${({ role }) => (role === 'user' ? 'left' : 'right')}-color: ${({ role }) =>
      role === 'user' ? 'var(--primary-color)' : 'var(--background-card)'};
  }
`;

const MessageContent = styled.div`
  font-size: ${theme.typography.fontSize.medium};
  line-height: 1.6;
  white-space: pre-wrap;
  word-break: break-word;
`;

const Timestamp = styled.span`
  font-size: ${theme.typography.fontSize.small};
  color: var(--text-muted);
  margin-top: ${theme.spacing.xs};
  opacity: 0.8;
`;

const RoleIndicator = styled.div<{ role: Message['role'] }>`
  display: flex;
  align-items: center;
  gap: ${theme.spacing.xs};
  margin-bottom: ${theme.spacing.xs};
  color: var(--text-muted);
  font-size: ${theme.typography.fontSize.small};
`;

const RoleIcon = styled.span`
  font-size: 16px;
`;

interface ChatMessageProps {
  message: Message;
}

export const ChatMessage: React.FC<ChatMessageProps> = ({ message }) => {
  const formatTime = (timestamp: number) => {
    return new Date(timestamp).toLocaleTimeString([], {
      hour: '2-digit',
      minute: '2-digit',
    });
  };

  return (
    <MessageContainer role={message.role}>
      <RoleIndicator role={message.role}>
        <RoleIcon>{message.role === 'user' ? '👤' : '🤖'}</RoleIcon>
        {message.role === 'user' ? 'You' : 'AI Assistant'}
      </RoleIndicator>
      <MessageBubble role={message.role}>
        <MessageContent>{message.content}</MessageContent>
      </MessageBubble>
      <Timestamp>{formatTime(message.timestamp)}</Timestamp>
    </MessageContainer>
  );
}; 