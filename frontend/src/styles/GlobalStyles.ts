import { createGlobalStyle } from 'styled-components';
import { theme } from './theme';

export const GlobalStyles = createGlobalStyle`
  :root {
    --primary-color: ${theme.colors.primary};
    --secondary-color: ${theme.colors.secondary};
    --background-main: ${theme.colors.background.main};
    --background-light: ${theme.colors.background.light};
    --background-card: ${theme.colors.background.card};
    --text-primary: ${theme.colors.text.primary};
    --text-secondary: ${theme.colors.text.secondary};
    --text-accent: ${theme.colors.text.accent};
    --border-color: ${theme.colors.border};
  }

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  body {
    font-family: ${theme.typography.fontFamily};
    background-color: var(--background-main);
    color: var(--text-primary);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  h1, h2, h3, h4, h5, h6 {
    color: var(--text-primary);
    margin-bottom: ${theme.spacing.md};
  }

  p {
    color: var(--text-secondary);
    margin-bottom: ${theme.spacing.md};
  }

  a {
    color: var(--text-accent);
    text-decoration: none;
    transition: color 0.2s ease;

    &:hover {
      color: var(--primary-color);
    }
  }

  button {
    font-family: ${theme.typography.fontFamily};
  }

  input, textarea {
    font-family: ${theme.typography.fontFamily};
    background-color: var(--background-light);
    color: var(--text-primary);
    border: 1px solid var(--border-color);
    border-radius: ${theme.borderRadius.md};
    padding: ${theme.spacing.sm} ${theme.spacing.md};
    
    &:focus {
      outline: none;
      border-color: var(--primary-color);
    }
  }
`; 