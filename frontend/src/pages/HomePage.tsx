import React from 'react';
import styled, { keyframes } from 'styled-components';
import { theme } from '../styles/theme';
import { Header } from '../components/Header/Header';
import { Chat } from '../components/Chat/Chat';
import { ChatProvider } from '../features/chat/ChatContext';

const fadeIn = keyframes`
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
`;

const PageContainer = styled.div`
  min-height: 100vh;
  background-color: var(--background-main);
  background-image: 
    radial-gradient(circle at 100% 0%, rgba(100, 255, 218, 0.08) 0%, transparent 50%),
    radial-gradient(circle at 0% 100%, rgba(0, 180, 216, 0.08) 0%, transparent 50%);
`;

const MainContent = styled.main`
  max-width: 1200px;
  margin: 0 auto;
  padding: ${theme.spacing.lg} ${theme.spacing.xl};
  display: flex;
  flex-direction: column;
  gap: ${theme.spacing.lg};
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

const FeatureGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: ${theme.spacing.md};
  margin-top: ${theme.spacing.lg};
`;

const FeatureCard = styled.div`
  background-color: var(--background-card);
  padding: ${theme.spacing.lg};
  border-radius: ${theme.borderRadius.lg};
  box-shadow: ${theme.shadows.medium};
  transition: all ${theme.transitions.default};
  
  &:hover {
    transform: translateY(-4px);
    box-shadow: ${theme.shadows.large};
  }
`;

const FeatureIcon = styled.div`
  font-size: 28px;
  margin-bottom: ${theme.spacing.sm};
  color: var(--text-accent);
`;

const FeatureTitle = styled.h3`
  font-size: ${theme.typography.fontSize.large};
  color: var(--text-primary);
  margin-bottom: ${theme.spacing.xs};
  font-weight: ${theme.typography.fontWeight.bold};
`;

const FeatureDescription = styled.p`
  font-size: ${theme.typography.fontSize.medium};
  color: var(--text-secondary);
  line-height: 1.4;
`;

const ChatSection = styled.section`
  background-color: var(--background-light);
  border-radius: ${theme.borderRadius.lg};
  box-shadow: ${theme.shadows.medium};
  height: 600px;
  overflow: hidden;
  border: 1px solid var(--border-color);
  transition: box-shadow ${theme.transitions.default};
  
  &:hover {
    box-shadow: ${theme.shadows.large};
  }
`;

export const HomePage: React.FC = () => {
  return (
    <ChatProvider>
      <PageContainer>
        <MainContent>
          <Header />
          <WelcomeSection>
            <WelcomeTitle>
              Welcome to Your <span>Smart Betting</span> Assistant
            </WelcomeTitle>
            <WelcomeText>
              Get real-time insights, analysis, and predictions to make informed betting decisions.
              Our AI-powered assistant is here to help you navigate the world of sports betting.
            </WelcomeText>
            <FeatureGrid>
              <FeatureCard>
                <FeatureIcon>🎯</FeatureIcon>
                <FeatureTitle>Smart Analysis</FeatureTitle>
                <FeatureDescription>
                  Get detailed match analysis and predictions based on historical data and current form.
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
          </WelcomeSection>
          <ChatSection>
            <Chat />
          </ChatSection>
        </MainContent>
      </PageContainer>
    </ChatProvider>
  );
}; 