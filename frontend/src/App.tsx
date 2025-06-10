import React from 'react';
import { ThemeProvider } from 'styled-components';
import { theme } from './styles/theme';
import { GlobalStyles } from './styles/GlobalStyles';
import { HomePage } from './pages/HomePage';

function App() {
  return (
    <ThemeProvider theme={theme}>
      <GlobalStyles />
      <HomePage />
    </ThemeProvider>
  );
}

export default App;
