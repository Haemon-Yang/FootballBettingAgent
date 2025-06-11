import React from 'react';
import styled, { css } from 'styled-components';

interface DeepResearchButtonProps {
  active: boolean;
  onClick: () => void;
  disabled?: boolean;
}

const Button = styled.button<{ active: boolean; disabled?: boolean }>`
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border-radius: 8px;
  border: none;
  background: var(--background-card);
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 0.9rem;
  font-weight: 500;

  ${({ active }) => active && css`
    background: var(--primary-color);
    color: var(--text-light);
    box-shadow: 0 2px 8px rgba(0, 180, 216, 0.3);
  `}

  ${({ disabled }) => disabled && css`
    opacity: 0.5;
    cursor: not-allowed;
    pointer-events: none;
  `}

  &:hover:not(:disabled) {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0, 180, 216, 0.2);
  }
`;

const Icon = styled.span`
  font-size: 1.1rem;
`;

export const DeepResearchButton: React.FC<DeepResearchButtonProps> = ({
  active,
  onClick,
  disabled = false,
}) => {
  return (
    <Button
      active={active}
      onClick={onClick}
      disabled={disabled}
    >
      <Icon>🔍</Icon>
      Deep Research
    </Button>
  );
}; 