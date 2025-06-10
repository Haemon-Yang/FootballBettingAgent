import React from 'react';
import styled, { css } from 'styled-components';

interface DeepResearchButtonProps {
  active: boolean;
  onClick: () => void;
}

const Button = styled.button<{ active: boolean }>`
  display: flex;
  align-items: center;
  gap: 8px;
  background: ${({ active }) => active ? 'var(--primary-color)' : 'var(--background-light)'};
  color: ${({ active }) => active ? 'var(--text-primary)' : 'var(--text-secondary)'};
  border: 1.5px solid ${({ active }) => active ? 'var(--primary-color)' : 'var(--border-color)'};
  border-radius: 20px;
  padding: 6px 18px 6px 12px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.4,0,0.2,1);
  outline: none;
  box-shadow: ${({ active }) => active ? '0 0 8px 0 var(--primary-color)' : 'none'};
  
  &:hover {
    background: var(--primary-color);
    color: var(--text-primary);
    border-color: var(--primary-color);
    box-shadow: 0 0 8px 0 var(--primary-color);
    
    svg {
      stroke: var(--text-primary);
    }
  }

  ${({ active }) => active && css`
    svg {
      stroke: var(--text-primary);
    }
  `}
`;

const Icon = styled.span`
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1em;
`;

export const DeepResearchButton: React.FC<DeepResearchButtonProps> = ({ active, onClick }) => (
  <Button active={active} onClick={onClick} type="button">
    <Icon>
      {/* Magnifier SVG icon */}
      <svg width="18" height="18" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <circle cx="9" cy="9" r="7" />
        <line x1="15" y1="15" x2="19" y2="19" />
      </svg>
    </Icon>
    Deep Research
  </Button>
); 