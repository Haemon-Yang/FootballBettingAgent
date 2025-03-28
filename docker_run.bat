@echo off
echo Stopping existing containers...
docker-compose down

echo Building and starting containers...
docker-compose up --build -d

echo Container is running! View logs with:
echo docker-compose logs -f

echo Application available at: http://localhost:8501
pause 