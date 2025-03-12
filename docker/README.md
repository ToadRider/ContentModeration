# Content Moderation API Docker Deployment

This directory contains the necessary files to deploy the Content Moderation API as a Docker container.

## Prerequisites

- Docker installed on your system
- Docker Compose installed on your system
- OpenAI API key

## Deployment Steps

### 1. Update the API Key (if needed)

If you need to use a different OpenAI API key, you can edit it in:
- `docker-compose.yml` 
- `Dockerfile`

Or set it as an environment variable when running the container.

### 2. Build and Start the Container

From this directory, run:

```bash
docker-compose up -d
```

This will:
- Build the Docker image
- Start the container in detached mode
- Map port 5000 from the container to port 5000 on your host

### 3. Access the Application

Open your browser and go to:

```
http://localhost:5000
```

### 4. Stop the Container

To stop the container, run:

```bash
docker-compose down
```

## Configuration Options

### Changing the Port

To change the port, edit the `docker-compose.yml` file and modify the port mapping:

```yaml
ports:
  - "YOUR_PORT:5000"
```

### Running Without Docker Compose

You can also build and run the container directly with Docker:

```bash
# Build the image
docker build -t content-moderator -f docker/Dockerfile .

# Run the container
docker run -p 5000:5000 --env OPENAI_API_KEY=your_api_key content-moderator
```

## Troubleshooting

- If you encounter API key issues, ensure your key is properly set in the environment variables
- If the container fails to start, check the logs with `docker-compose logs` 