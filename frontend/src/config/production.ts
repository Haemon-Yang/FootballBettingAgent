import type { BaseConfig } from './settings';

export const productionConfig: BaseConfig = {
  API_URL: import.meta.env.VITE_API_URL || 'https://api.your-domain.com',
  PROJECT_NAME: 'Football Betting AI',
  ENV: 'production',
  ENABLE_DEEP_RESEARCH: true,
}; 