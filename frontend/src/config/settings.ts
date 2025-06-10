export interface BaseConfig {
  // API Settings
  API_URL: string;
  PROJECT_NAME: string;
  
  // Environment
  ENV: 'development' | 'production';
  
  // Feature Flags
  ENABLE_DEEP_RESEARCH: boolean;
}

export const baseConfig: BaseConfig = {
  API_URL: 'http://localhost:9055',
  PROJECT_NAME: 'Football Betting AI',
  ENV: 'development',
  ENABLE_DEEP_RESEARCH: true,
}; 