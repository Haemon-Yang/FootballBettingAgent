import React, { useRef, useEffect, useState } from 'react';
import styled, { keyframes } from 'styled-components';
import { theme } from '../../styles/theme';
import { ChatMessage } from './ChatMessage';
import { ChatInput } from './ChatInput';
import { useChat } from '../../features/chat/ChatContext';
import { config } from '../../config';

const fadeIn = keyframes`
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
`;

const ChatContainer = styled.div`
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 100%;
  min-width: 0;
  min-height: 0;
  background: transparent;
  position: relative;
  box-sizing: border-box;
  @media (max-width: 800px) {
    width: 98vw;
    margin: 10px auto;
    height: 90vh;
  }
`;

const MessagesContainer = styled.div`
  flex: 1;
  overflow-y: auto;
  padding: 32px 32px 16px 32px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  background: transparent;
  scrollbar-width: thin;
  scrollbar-color: #3ecfff #232b3b;
  &::-webkit-scrollbar {
    width: 10px;
    background: #232b3b;
    border-radius: 8px;
  }
  &::-webkit-scrollbar-thumb {
    background: linear-gradient(120deg, #3ecfff 30%, #00b4d8 100%);
    border-radius: 8px;
    min-height: 40px;
    border: 2px solid #232b3b;
  }
  &::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(120deg, #00b4d8 30%, #3ecfff 100%);
  }
  &::-webkit-scrollbar-track {
    background: #232b3b;
    border-radius: 8px;
  }
  @media (max-width: 600px) {
    padding: 16px 8px 8px 8px;
    gap: 12px;
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
  padding: 48px 0 0 0;
  animation: ${fadeIn} 0.5s ease;
  max-width: 600px;
  margin: 0 auto;
`;

const EmptyStateIcon = styled.div`
  font-size: 48px;
  margin-bottom: ${theme.spacing.md};
  color: var(--text-accent);
`;

const TypewriterText = styled.div`
  color: var(--text-secondary);
  font-size: ${theme.typography.fontSize.large};
  line-height: 1.6;
  white-space: pre-line;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const TypewriterLine = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-bottom: 16px;
`;

const Word = styled.span`
  opacity: 0;
  transform: translateY(8px);
  animation: fadeIn 0.5s cubic-bezier(0.4, 0, 0.2, 1) forwards;
  @keyframes fadeIn {
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  margin-right: 4px;
`;

const FeatureGrid = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: stretch;
  gap: 32px;
  margin: 32px auto 0 auto;
  width: 100%;
  max-width: 1200px;
  padding: 0 16px;
  @media (max-width: 1200px) {
    gap: 20px;
    max-width: 98vw;
  }
  @media (max-width: 900px) {
    gap: 12px;
  }
  @media (max-width: 700px) {
    flex-direction: column;
    gap: 18px;
    margin-top: 20px;
    align-items: center;
  }
`;

const FeatureCard = styled.div`
  background-color: var(--background-card);
  flex: 1 1 0;
  min-width: 360px;
  max-width: 520px;
  min-height: 90px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 16px 40px 12px 40px;
  border-radius: 18px;
  box-shadow: 0 4px 24px 0 rgba(0,0,0,0.10);
  transition: box-shadow 0.18s, transform 0.18s;
  cursor: pointer;
  &:hover {
    box-shadow: 0 8px 32px 0 rgba(0,180,216,0.18);
    transform: translateY(-4px) scale(1.03);
  }
  @media (max-width: 900px) {
    min-width: 200px;
    max-width: 98vw;
    padding: 10px 10px 8px 10px;
    border-radius: 12px;
  }
`;

const FeatureIcon = styled.div`
  font-size: 2.2rem;
  margin-bottom: 18px;
  color: var(--text-accent);
`;

const FeatureTitle = styled.h3`
  font-size: 1.08rem;
  color: var(--text-primary);
  margin-bottom: 8px;
  font-weight: 700;
  letter-spacing: 0.3px;
  text-align: center;
`;

const FeatureDescription = styled.p`
  font-size: 0.93rem;
  color: var(--text-secondary);
  line-height: 1.5;
  font-weight: 400;
  text-align: center;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 100%;
  word-break: break-word;
`;

export const Chat: React.FC = () => {
  const { state, sendMessage } = useChat();
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const [welcomeMessage, setWelcomeMessage] = useState<string>('');
  const [isTyping, setIsTyping] = useState(true);
  const [isDeepResearchActive, setIsDeepResearchActive] = useState(false);
  const [typedLines, setTypedLines] = useState<string[]>([]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    let isMounted = true;
    setWelcomeMessage('');
    setTypedLines([]);
    setIsTyping(true);

    const fetchWelcomeMessage = async () => {
      try {
        const response = await fetch(`${config.API_URL}/`);
        const data = await response.json();
        const lines = [`${data.welcome_message}`, `${data.description}`];
        typeLines(lines);
      } catch (error) {
        console.error('Error fetching welcome message:', error);
      }
    };

    const typeLines = (lines: string[]) => {
      let currentLine = 0;
      let currentLines: string[] = [];
      function typeLine() {
        if (!isMounted) return;
        if (currentLine < lines.length) {
          let wordIndex = 0;
          const words = lines[currentLine].split(' ');
          let line = '';
          function typeWord() {
            if (!isMounted) return;
            if (wordIndex < words.length) {
              line += (wordIndex === 0 ? '' : ' ') + words[wordIndex];
              currentLines[currentLine] = line;
              setTypedLines([...currentLines]);
              wordIndex++;
              setTimeout(typeWord, 150);
            } else {
              currentLine++;
              setTimeout(() => {
                typeLine();
              }, 800);
            }
          }
          typeWord();
        } else {
          setIsTyping(false);
        }
      }
      typeLine();
    };

    fetchWelcomeMessage();
    return () => { isMounted = false; };
  }, []);

  useEffect(() => {
    scrollToBottom();
  }, [state.messages]);

  const handleSendMessage = (message: string) => {
    sendMessage(message, isDeepResearchActive);
  };

  return (
    <ChatContainer>
      <MessagesContainer>
        {state.messages.length === 0 ? (
          <EmptyState>
            <EmptyStateIcon>💬</EmptyStateIcon>
            <FeatureGrid>
              <FeatureCard>
                <FeatureIcon>🎯</FeatureIcon>
                <FeatureTitle>Smart Analysis</FeatureTitle>
                <FeatureDescription>
                  Get match analysis and predictions based on data and team form.
                </FeatureDescription>
              </FeatureCard>
              <FeatureCard>
                <FeatureIcon>📊</FeatureIcon>
                <FeatureTitle>Real-time Stats</FeatureTitle>
                <FeatureDescription>
                  Access comprehensive statistics and trends to make data-driven decisions.
                </FeatureDescription>
              </FeatureCard>
              <FeatureCard>
                <FeatureIcon>🤖</FeatureIcon>
                <FeatureTitle>AI-Powered</FeatureTitle>
                <FeatureDescription>
                  Leverage advanced AI technology for accurate predictions and insights.
                </FeatureDescription>
              </FeatureCard>
            </FeatureGrid>
            {typedLines.length > 0 && (
              <div style={{marginTop: 32, color: 'var(--text-secondary)', fontSize: '1.1rem', lineHeight: 1.6, maxWidth: 600, marginLeft: 'auto', marginRight: 'auto'}}>
                {typedLines.map((line, idx) => (
                  <div key={idx} style={{marginBottom: 8}}>{line}</div>
                ))}
              </div>
            )}
          </EmptyState>
        ) : (
          state.messages.map((message) => (
            <ChatMessage key={message.id} message={message} />
          ))
        )}
        <div ref={messagesEndRef} />
      </MessagesContainer>
      <ChatInput 
        onSendMessage={handleSendMessage} 
        isDeepResearchActive={isDeepResearchActive}
        onToggleDeepResearch={setIsDeepResearchActive}
      />
    </ChatContainer>
  );
}; 