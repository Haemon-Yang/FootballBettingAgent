import React, { useEffect, useState } from 'react';
import styled, { keyframes } from 'styled-components';
import { theme } from '../styles/theme';
import { Header } from '../components/Header/Header';
import { Chat } from '../components/Chat/Chat';
import { ChatProvider } from '../features/chat/ChatContext';
import { config } from '../config';

const fadeIn = keyframes`
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
`;

const PageContainer = styled.div`
  width: 100vw;
  height: 100vh;
  min-height: 100vh;
  background-color: var(--background-main);
  background-image: 
    radial-gradient(circle at 100% 0%, rgba(100, 255, 218, 0.08) 0%, transparent 50%),
    radial-gradient(circle at 0% 100%, rgba(0, 180, 216, 0.08) 0%, transparent 50%);
  display: flex;
  flex-direction: column;
`;

const MainContent = styled.main`
  flex: 1 1 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: ${theme.spacing.lg};
  padding: ${theme.spacing.lg} ${theme.spacing.lg};
`;

const WelcomeSection = styled.section`
  text-align: center;
  padding: ${theme.spacing.md} 0 0;
  animation: ${fadeIn} 0.8s ease;
`;

const WelcomeTitle = styled.h2`
  font-size: ${theme.typography.fontSize.xxlarge};
  color: var(--text-primary);
  margin-bottom: ${theme.spacing.md};
  font-weight: ${theme.typography.fontWeight.bold};
  
  span {
    color: var(--text-accent);
    position: relative;
    
    &::after {
      content: '';
      position: absolute;
      bottom: -2px;
      left: 0;
      width: 100%;
      height: 2px;
      background-color: var(--text-accent);
      transform: scaleX(0);
      transform-origin: right;
      transition: transform 0.3s ease;
    }
    
    &:hover::after {
      transform: scaleX(1);
      transform-origin: left;
    }
  }
`;

const WelcomeText = styled.p`
  font-size: ${theme.typography.fontSize.large};
  color: var(--text-secondary);
  max-width: 600px;
  margin: 0 auto ${theme.spacing.lg};
  line-height: 1.4;
`;

const ChatSection = styled.section`
  background-color: var(--background-light);
  border-radius: ${theme.borderRadius.lg};
  box-shadow: ${theme.shadows.medium};
  flex: 1 1 0;
  min-height: 0;
  overflow: hidden;
  border: 1px solid var(--border-color);
  transition: box-shadow ${theme.transitions.default};
  margin: 0;
  width: 100%;
  display: flex;
  flex-direction: column;
  
  &:hover {
    box-shadow: ${theme.shadows.large};
  }
`;

export const HomePage: React.FC = () => {
  const [welcomeData, setWelcomeData] = useState<{ welcome_message: string; description: string } | null>(null);

  useEffect(() => {
    const fetchWelcomeMessage = async () => {
      try {
        const response = await fetch(`${config.API_URL}/`);
        const data = await response.json();
        setWelcomeData(data);
      } catch (error) {
        console.error('Error fetching welcome message:', error);
      }
    };

    fetchWelcomeMessage();
  }, []);

  return (
    <ChatProvider>
      <PageContainer>
        <MainContent>
          <Header />
          <ChatSection>
            <Chat />
          </ChatSection>
        </MainContent>
      </PageContainer>
    </ChatProvider>
  );
}; 