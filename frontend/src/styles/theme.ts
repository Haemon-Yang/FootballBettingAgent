export const theme = {
  colors: {
    primary: '#00B4D8', // Tech blue
    secondary: '#0077B6', // Darker blue
    background: {
      main: '#0A192F', // Dark navy
      light: '#112240', // Lighter navy
      card: '#1D2D50', // Card background
      input: '#1E3A5F', // Input background
    },
    text: {
      primary: '#F8F9FA', // Brighter white for better contrast
      secondary: '#A8B2D1', // Muted blue-gray
      accent: '#64FFDA', // Tech cyan
      muted: '#8892B0', // Muted text
    },
    border: '#233554', // Subtle border color
    success: '#4CAF50',
    error: '#FF5252',
    warning: '#FFC107',
  },
  spacing: {
    xs: '4px',
    sm: '8px',
    md: '16px',
    lg: '24px',
    xl: '32px',
    xxl: '48px',
  },
  borderRadius: {
    sm: '4px',
    md: '8px',
    lg: '12px',
    xl: '16px',
  },
  typography: {
    fontFamily: "'Inter', 'Helvetica Neue', sans-serif",
    fontSize: {
      small: '14px',
      medium: '16px',
      large: '20px',
      xlarge: '24px',
      xxlarge: '32px',
    },
    fontWeight: {
      regular: 400,
      medium: 500,
      semibold: 600,
      bold: 700,
    },
  },
  shadows: {
    small: '0 2px 4px rgba(0, 0, 0, 0.1)',
    medium: '0 4px 8px rgba(0, 0, 0, 0.12)',
    large: '0 8px 16px rgba(0, 0, 0, 0.14)',
    glow: '0 0 20px rgba(100, 255, 218, 0.15)',
  },
  transitions: {
    default: '0.2s ease',
    smooth: '0.3s cubic-bezier(0.4, 0, 0.2, 1)',
  },
  zIndex: {
    base: 1,
    dropdown: 10,
    modal: 100,
    tooltip: 1000,
  },
} as const;

export type Theme = typeof theme; 