import { developmentConfig } from './development';
import { productionConfig } from './production';

const getConfig = () => {
  const env = import.meta.env.MODE || 'development';
  return env === 'production' ? productionConfig : developmentConfig;
};

export const config = getConfig(); 