# ⚽ Soccer Betting Agent

## 📝 Description

This project aims to increase the winning rate in a soccer betting game. We utilize agent to analyze team stats and provide solid suggestion on a betting game.

## ✨ Features

- **🤖 AI-Powered Analysis**: Leverages AI agents to provide intelligent betting recommendations
- **💬 Interactive Chat Interface**: User-friendly Streamlit frontend with typing effect for a responsive experience
- **📊 Premier League Data Scraping**: Automatically collects and processes real-time statistics
- **📈 Comprehensive Match Analysis**: Evaluates team performance, historical data, and current form
- **🎯 Personalized Betting Advice**: Tailored recommendations based on user preferences and risk tolerance

## 🏗️ Architecture

![Architecture of System](Doc/Europe%20Football%20workflow-v2.drawio.png)

## 🚀 Getting Started

### 🐳 Run with Docker

1. Make sure you have Docker and Docker Compose installed on your system:
   - [Install Docker](https://docs.docker.com/get-docker/)
   - [Install Docker Compose](https://docs.docker.com/compose/install/)

2. Clone the repository:

   ```bash
   git clone [repository-url]
   cd [repository-directory]
   ```

3. Create a `.env` file with the required API keys:

   ```bash
   cp .env_example .env
   # Edit .env and add your API keys
   ```

4. Build and run the Docker container:

   ```bash
   docker-compose up -d
   ```

5. Access the application in your browser:

   ```
   http://localhost:8501
   ```

6. To stop the container:

   ```bash
   docker-compose down
   ```

### 💻 Run Locally

## 🤝 Contributing

Feel free to submit pull request or open an issue for any suggestion or improvements.

## 📄 License

This project is licensed under the MIT license.