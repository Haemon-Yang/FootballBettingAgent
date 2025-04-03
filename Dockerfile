FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only necessary files (relied on .dockerignore)
COPY . .

# Create directory for persisting data if needed
RUN mkdir -p /app/data

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Expose the port Streamlit runs on
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Command to run the application
CMD ["streamlit", "run", "frontend.py", "--server.port=8501","--server.address=0.0.0.0"] 