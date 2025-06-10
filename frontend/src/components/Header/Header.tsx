import React from 'react';
import styled, { keyframes } from 'styled-components';
import { theme } from '../../styles/theme';

const fadeInDown = keyframes`
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
`;

const pulse = keyframes`
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
`;

const HeaderContainer = styled.div`
  text-align: left;
  padding: ${theme.spacing.xl} ${theme.spacing.xxl};
  position: relative;
  width: 100%;
  background: linear-gradient(
    to right,
    var(--background-main) 0%,
    var(--background-light) 100%
  );
  border-bottom: 1px solid var(--border-color);
  
  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: ${theme.spacing.xxl};
    width: 60px;
    height: 4px;
    background: var(--text-accent);
    border-radius: 2px;
  }
`;

const HeaderContent = styled.div`
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
`;

const TitleSection = styled.div`
  flex: 1;
`;

const MainTitle = styled.h1`
  font-size: 2.8rem;
  color: var(--text-primary);
  margin-bottom: ${theme.spacing.sm};
  animation: ${fadeInDown} 0.8s ease;
  font-weight: ${theme.typography.fontWeight.bold};
  line-height: 1.2;
  
  span {
    color: var(--text-accent);
    position: relative;
    display: inline-block;
    
    &::after {
      content: '';
      position: absolute;
      bottom: -4px;
      left: 0;
      width: 100%;
      height: 3px;
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

const EmojiWrapper = styled.span`
  display: inline-block;
  margin-right: ${theme.spacing.sm};
  animation: ${pulse} 2s infinite;
  font-size: 2.6rem;
  vertical-align: middle;
`;

const SubTitle = styled.h3`
  font-size: 1.2rem;
  color: var(--text-secondary);
  font-weight: ${theme.typography.fontWeight.medium};
  max-width: 500px;
  margin: 0;
  line-height: 1.4;
  animation: ${fadeInDown} 0.8s ease 0.2s backwards;
  opacity: 0.9;
`;

// Navigation components kept for future use
const NavSection = styled.nav`
  display: flex;
  gap: ${theme.spacing.lg};
  align-items: center;
`;

const NavItem = styled.a`
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 1rem;
  font-weight: ${theme.typography.fontWeight.medium};
  padding: ${theme.spacing.sm} ${theme.spacing.md};
  border-radius: ${theme.borderRadius.md};
  transition: all ${theme.transitions.default};
  
  &:hover {
    color: var(--text-accent);
    background-color: var(--background-light);
  }
`;

export const Header: React.FC = () => {
  return (
    <HeaderContainer>
      <HeaderContent>
        <TitleSection>
          <MainTitle>
            <EmojiWrapper>🎯</EmojiWrapper>
            Smart <span>Betting</span> Assistant
          </MainTitle>
          <SubTitle>
            Your AI-Powered Betting Strategy Partner
          </SubTitle>
        </TitleSection>
        {/* Navigation section commented out for future use */}
        {/* <NavSection>
          <NavItem href="#analysis">Analysis</NavItem>
          <NavItem href="#predictions">Predictions</NavItem>
          <NavItem href="#stats">Statistics</NavItem>
          <NavItem href="#settings">Settings</NavItem>
        </NavSection> */}
      </HeaderContent>
    </HeaderContainer>
  );
}; 