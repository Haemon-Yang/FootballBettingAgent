import styled, { keyframes } from 'styled-components';

const bounce = keyframes`
  0%, 80%, 100% { 
    transform: translateY(0);
  }
  40% { 
    transform: translateY(-10px);
  }
`;

const Container = styled.div`
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 8px 12px;
  background: ${({ theme }) => theme.colors.background};
  border-radius: 12px;
  width: fit-content;
`;

const Dot = styled.div<{ delay: number }>`
  width: 8px;
  height: 8px;
  background: ${({ theme }) => theme.colors.primary};
  border-radius: 50%;
  animation: ${bounce} 1.4s infinite ease-in-out;
  animation-delay: ${({ delay }) => delay}s;
`;

const ThinkingEffect = () => {
  return (
    <Container>
      <Dot delay={0} />
      <Dot delay={0.2} />
      <Dot delay={0.4} />
    </Container>
  );
};

export default ThinkingEffect; 