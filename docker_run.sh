#!/bin/bash

# Stop any running containers
echo "Stopping existing containers..."
docker-compose down

# Build and start the container
echo "Building and starting containers..."
docker-compose up --build -d

# Show logs
echo "Container is running! View logs with:"
echo "docker-compose logs -f"

echo "Application available at: http://localhost:8501" 