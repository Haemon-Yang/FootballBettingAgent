import React from 'react';
import styled from 'styled-components';
import { theme } from '../../styles/theme';

const InfoBoxContainer = styled.div`
  background-color: var(--background-card);
  border-left: 4px solid var(--text-accent);
  padding: ${theme.spacing.lg};
  margin: ${theme.spacing.lg} 0;
  border-radius: ${theme.borderRadius.md};
  box-shadow: ${theme.shadows.small};
`;

const InfoIcon = styled.span`
  color: var(--text-accent);
  margin-right: ${theme.spacing.sm};
`;

const InfoText = styled.p`
  color: var(--text-secondary);
  font-size: ${theme.typography.fontSize.medium};
  line-height: 1.6;
`;

interface InfoBoxProps {
  message: string;
}

export const InfoBox: React.FC<InfoBoxProps> = ({ message }) => {
  return (
    <InfoBoxContainer>
      <InfoText>
        <InfoIcon>💡</InfoIcon>
        {message}
      </InfoText>
    </InfoBoxContainer>
  );
}; 