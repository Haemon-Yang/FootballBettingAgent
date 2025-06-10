export interface Message {
  id: string;
  role: 'user' | 'ai';
  content: string;
  timestamp: number;
}

export interface ChatState {
  messages: Message[];
  isLoading: boolean;
  error: string | null;
}

export interface ChatContextType {
  state: ChatState;
  sendMessage: (content: string) => Promise<void>;
  clearMessages: () => void;
} 