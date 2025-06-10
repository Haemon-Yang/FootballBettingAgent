import React from 'react';
import styled from 'styled-components';

interface ButtonProps {
  variant?: 'primary' | 'secondary';
  onClick?: () => void;
  children: React.ReactNode;
  disabled?: boolean;
}

const StyledButton = styled.button<{ variant: 'primary' | 'secondary' }>`
  background-color: ${({ variant }) => 
    variant === 'primary' ? 'var(--primary-color)' : 'var(--secondary-color)'};
  color: var(--text-light);
  border: none;
  border-radius: 8px;
  padding: 10px 25px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  
  &:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }
  
  &:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }
`;

export const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  onClick,
  children,
  disabled = false,
}) => {
  return (
    <StyledButton
      variant={variant}
      onClick={onClick}
      disabled={disabled}
    >
      {children}
    </StyledButton>
  );
}; 