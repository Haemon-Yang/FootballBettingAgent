import React from 'react';
import styled, { keyframes } from 'styled-components';
import { theme } from '../../styles/theme';
import type { Message } from '../../features/chat/types';
import ThinkingEffect from '../ThinkingEffect/ThinkingEffect';
import ReactMarkdown from 'react-markdown';
import rehypeSanitize from 'rehype-sanitize';
import remarkGfm from 'remark-gfm';
import { unified } from 'unified';
import remarkParse from 'remark-parse';
import remarkStringify from 'remark-stringify';
import { visit } from 'unist-util-visit';
import type { Node, Parent } from 'unist';

const fadeIn = keyframes`
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
`;

const MessageContainer = styled.div<{ role: Message['role'] }>`
  display: flex;
  flex-direction: column;
  align-items: ${({ role }) => (role === 'user' ? 'flex-end' : 'flex-start')};
  margin: ${theme.spacing.md} 0;
  max-width: 80%;
  margin-left: ${({ role }) => (role === 'user' ? 'auto' : '0')};
  animation: ${fadeIn} 0.3s ease;
`;

const MessageBubble = styled.div<{ role: Message['role'] }>`
  background-color: ${({ role }) =>
    role === 'user'
      ? 'rgba(60, 207, 255, 0.18)' // user: light blue with transparency
      : 'rgba(255,255,255,0.08)'}; // ai: dark card
  color: var(--text-primary);
  padding: ${theme.spacing.md} ${theme.spacing.lg};
  border-radius: ${theme.borderRadius.lg};
  box-shadow: ${theme.shadows.small};
  position: relative;
  transition: transform ${theme.transitions.default};
  max-width: 100%;
  word-break: break-word;

  &:hover {
    transform: translateY(-2px);
    box-shadow: ${theme.shadows.medium};
  }

  &::before {
    content: '';
    position: absolute;
    top: 50%;
    ${({ role }) => (role === 'user' ? 'right: -8px;' : 'left: -8px;')}
    transform: translateY(-50%);
    border-style: solid;
    border-width: 8px;
    border-color: transparent;
    border-${({ role }) => (role === 'user' ? 'left' : 'right')}-color: ${({ role }) =>
      role === 'user'
        ? 'rgba(60, 207, 255, 0.18)'
        : 'rgba(255,255,255,0.08)'};
  }
`;

const MessageContent = styled.div<{ role?: Message['role'] }>`
  font-size: ${theme.typography.fontSize.medium};
  line-height: 1.7;
  white-space: pre-wrap;
  word-break: break-word;
  color: var(--text-primary);
  font-weight: 500;

  /* Markdown styling */
  p {
    margin: 0 0 1.1em 0;
    &:last-child {
      margin-bottom: 0;
    }
  }

  h1, h2, h3, h4, h5, h6 {
    margin: 1.5em 0 0.6em 0;
    color: var(--text-primary);
    font-weight: 700;
    line-height: 1.25;
    letter-spacing: 0.01em;
    padding-left: 0;
  }
  h1 { font-size: 1.5em; border-bottom: 2px solid var(--border-color); padding-bottom: 0.18em; }
  h2 { font-size: 1.25em; border-bottom: 1.5px solid var(--border-color); padding-bottom: 0.12em; }
  h3 { font-size: 1.1em; }
  h4, h5, h6 { font-size: 1em; }

  ul, ol {
    margin: 0.5em 0 1em 0.8em;
    padding-left: 1.2em;
    line-height: 1.7;
  }
  ul ul, ol ol, ul ol, ol ul {
    margin: 0.2em 0 0.2em 1.2em;
    padding-left: 1.2em;
  }
  li {
    margin: 0.2em 0;
    font-size: 1em;
    padding-left: 0.1em;
  }
  code {
    background-color: var(--background-light);
    padding: 0.18em 0.38em;
    border-radius: 3px;
    font-family: monospace;
    font-size: 0.97em;
    color: #ffb86c;
  }
  pre {
    background-color: var(--background-light);
    padding: 1em;
    border-radius: 5px;
    overflow-x: auto;
    margin: 1.1em 0;
    code {
      background-color: transparent;
      padding: 0;
      color: #ffb86c;
    }
  }
  blockquote {
    border-left: 4px solid var(--text-accent);
    margin: 1em 0;
    padding: 0.5em 0 0.5em 1em;
    color: var(--text-secondary);
    background: rgba(255,255,255,0.04);
    border-radius: 4px;
  }
  table {
    border-collapse: collapse;
    width: 100%;
    margin: 1.1em 0;
  }
  th, td {
    border: 1px solid var(--border-color);
    padding: 0.5em;
    text-align: left;
  }
  th {
    background-color: var(--background-light);
    font-weight: 700;
  }
  a {
    color: var(--text-accent);
    text-decoration: underline;
    &:hover {
      text-decoration: underline wavy;
    }
  }
  img {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
  }
  strong {
    font-weight: 700;
    color: var(--text-primary);
    background: none;
  }
  em {
    font-style: italic;
    color: var(--text-secondary);
  }
`;

const Timestamp = styled.span`
  font-size: ${theme.typography.fontSize.small};
  color: var(--text-muted);
  margin-top: ${theme.spacing.xs};
  opacity: 0.8;
`;

interface ChatMessageProps {
  message: Message;
}

interface MarkdownNode extends Node {
  type: string;
  children?: MarkdownNode[];
  value?: string;
}

interface ListItemNode extends Parent {
  type: 'listItem';
  children: MarkdownNode[];
}

const preprocessMarkdown = (markdown: string): string => {
  // Merge label paragraphs (e.g., '**Current Form:**') with the following list
  const lines = markdown.split('\n');
  let result: string[] = [];
  for (let i = 0; i < lines.length; i++) {
    const labelMatch = lines[i].match(/^\*\*(.+:)\*\*$/);
    if (labelMatch && i + 1 < lines.length && lines[i + 1].trim().startsWith('-')) {
      // Merge label into the first list item
      const label = labelMatch[0];
      const nextLine = lines[i + 1];
      // Insert label at the start of the first list item
      result.push(nextLine.replace(/^(-\s*)/, `$1${label} `));
      i++; // Skip the next line (already merged)
    } else {
      result.push(lines[i]);
    }
  }
  const merged = result.join('\n');

  // Existing list item double-newline fix
  const processor = unified()
    .use(remarkParse)
    .use(() => (tree) => {
      visit(tree, 'listItem', (node: any) => {
        if (node.children) {
          node.children.forEach((child: any) => {
            if (child.type === 'paragraph' && child.children) {
              child.children.forEach((grandchild: any) => {
                if (grandchild.type === 'text' && typeof grandchild.value === 'string') {
                  grandchild.value = grandchild.value.replace(/\n\n/g, ' ');
                }
              });
            }
          });
        }
      });
    })
    .use(remarkStringify);
  return processor.processSync(merged).toString();
};

export const ChatMessage: React.FC<ChatMessageProps> = ({ message }) => {
  const formatTime = (timestamp: number) => {
    return new Date(timestamp).toLocaleTimeString([], {
      hour: '2-digit',
      minute: '2-digit',
    });
  };

  // Update the markdownComponents to be simpler since we're preprocessing
  const markdownComponents = {
    li: (props: any) => (
      <li style={{ margin: '0.2em 0', display: 'list-item', listStylePosition: 'inside', paddingLeft: 0 }} {...props} />
    ),
    // Custom paragraph renderer to avoid extra margin if followed by a list
    p: (props: any) => {
      // If the paragraph only contains strong text and is immediately followed by a list, render as a span
      if (
        props.node &&
        props.node.children &&
        props.node.children.length === 1 &&
        props.node.children[0].type === 'strong'
      ) {
        return <span style={{ fontWeight: 700, color: 'var(--text-primary)', marginRight: 8 }}>{props.children}</span>;
      }
      return <p {...props} />;
    },
    // Custom unordered list renderer to display inline if preceded by a span
    ul: (props: any) => {
      // If the previous sibling is a span, render inline
      return <ul style={{ display: 'inline-block', margin: 0, paddingLeft: 16 }} {...props} />;
    },
  };

  if (message.role === 'thinking') {
    return (
      <MessageContainer role="ai">
        <RoleIndicator role="ai">
          <RoleIcon role="ai">🤖</RoleIcon>
          AI Assistant
        </RoleIndicator>
        <MessageBubble role="ai">
          <ThinkingEffect />
        </MessageBubble>
        <Timestamp>{formatTime(message.timestamp)}</Timestamp>
      </MessageContainer>
    );
  }

  const processedContent = preprocessMarkdown(message.content);

  return (
    <MessageContainer role={message.role}>
      <RoleIndicator role={message.role}>
        <RoleIcon role={message.role}>{message.role === 'user' ? '🧑' : '🤖'}</RoleIcon>
        {message.role === 'user' ? 'You' : 'AI Assistant'}
      </RoleIndicator>
      <MessageBubble role={message.role}>
        <MessageContent role={message.role}>
          <ReactMarkdown
            rehypePlugins={[rehypeSanitize]}
            remarkPlugins={[remarkGfm]}
            components={markdownComponents}
          >
            {processedContent}
          </ReactMarkdown>
        </MessageContent>
      </MessageBubble>
      <Timestamp>{formatTime(message.timestamp)}</Timestamp>
    </MessageContainer>
  );
};

const RoleIndicator = styled.div<{ role: Message['role'] }>`
  display: flex;
  align-items: center;
  gap: ${theme.spacing.xs};
  margin-bottom: ${theme.spacing.xs};
  color: var(--text-muted);
  font-size: ${theme.typography.fontSize.small};
  font-weight: normal;
  letter-spacing: 0.5px;
`;

const RoleIcon = styled.span<{ role: Message['role'] }>`
  font-size: 18px;
  color: var(--text-muted);
  filter: none;
`;
