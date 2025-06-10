import React, { useRef, useEffect } from 'react';
import styled, { keyframes } from 'styled-components';
import { theme } from '../../styles/theme';
import { ChatMessage } from './ChatMessage';
import { ChatInput } from './ChatInput';
import { useChat } from '../../features/chat/ChatContext';

const fadeIn = keyframes`
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
`;

const ChatContainer = styled.div`
  display: flex;
  flex-direction: column;
  height: 100%;
  background-color: var(--background-main);
  position: relative;
`;

const MessagesContainer = styled.div`
  flex: 1;
  overflow-y: auto;
  padding: ${theme.spacing.md};
  display: flex;
  flex-direction: column;
  gap: ${theme.spacing.md};
  
  /* Custom scrollbar */
  &::-webkit-scrollbar {
    width: 8px;
  }
  
  &::-webkit-scrollbar-track {
    background: var(--background-light);
    border-radius: ${theme.borderRadius.md};
  }
  
  &::-webkit-scrollbar-thumb {
    background: var(--border-color);
    border-radius: ${theme.borderRadius.md};
    
    &:hover {
      background: var(--text-secondary);
    }
  }
`;

const LoadingContainer = styled.div`
  display: flex;
  align-items: center;
  gap: ${theme.spacing.sm};
  padding: ${theme.spacing.md};
  margin: ${theme.spacing.md} 0;
  background-color: var(--background-card);
  border-radius: ${theme.borderRadius.md};
  box-shadow: ${theme.shadows.small};
  animation: ${fadeIn} 0.3s ease;
`;

const LoadingText = styled.span`
  color: var(--text-secondary);
  font-style: italic;
  font-size: ${theme.typography.fontSize.medium};
`;

const LoadingDots = styled.div`
  display: flex;
  gap: 4px;
`;

const Dot = styled.span<{ delay: number }>`
  width: 8px;
  height: 8px;
  background-color: var(--text-accent);
  border-radius: 50%;
  animation: bounce 1.4s infinite;
  animation-delay: ${({ delay }) => delay}s;
  
  @keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-6px); }
  }
`;

const EmptyState = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  color: var(--text-secondary);
  text-align: center;
  padding: ${theme.spacing.xl};
  animation: ${fadeIn} 0.5s ease;
`;

const EmptyStateIcon = styled.div`
  font-size: 48px;
  margin-bottom: ${theme.spacing.md};
  color: var(--text-accent);
`;

const EmptyStateText = styled.p`
  font-size: ${theme.typography.fontSize.large};
  max-width: 400px;
  line-height: 1.6;
`;

export const Chat: React.FC = () => {
  const { state, sendMessage } = useChat();
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [state.messages]);

  return (
    <ChatContainer>
      <MessagesContainer>
        {state.messages.length === 0 ? (
          <EmptyState>
            <EmptyStateIcon>💬</EmptyStateIcon>
            <EmptyStateText>
              Start a conversation by asking about a match or betting strategy.
              I'm here to help you make informed decisions!
            </EmptyStateText>
          </EmptyState>
        ) : (
          state.messages.map((message) => (
            <ChatMessage key={message.id} message={message} />
          ))
        )}
        {state.isLoading && (
          <LoadingContainer>
            <LoadingText>Thinking</LoadingText>
            <LoadingDots>
              <Dot delay={0} />
              <Dot delay={0.2} />
              <Dot delay={0.4} />
            </LoadingDots>
          </LoadingContainer>
        )}
        <div ref={messagesEndRef} />
      </MessagesContainer>
      <ChatInput
        onSendMessage={sendMessage}
        isLoading={state.isLoading}
      />
    </ChatContainer>
  );
}; 