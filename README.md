# Content Moderation API

A Flask application that uses OpenAI's Moderation API to analyze text for potentially harmful content. Supports both Azure OpenAI and regular OpenAI services.

## Features

- Clean, responsive web interface for submitting text
- Real-time analysis using OpenAI's Moderation API
- Support for both Azure OpenAI and regular OpenAI services
- Detailed breakdown of content categories and confidence scores

## Prerequisites

- Python 3.9+
- OpenAI API key (for regular OpenAI) or Azure OpenAI credentials
- Docker (optional, for containerized deployment)

## Setup and Installation

### Local Development Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd content-moderation-api
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory:

   For regular OpenAI:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

   For Azure OpenAI:
   ```
   USE_AZURE_OPENAI=true
   AZURE_OPENAI_API_KEY=your_azure_api_key_here
   AZURE_OPENAI_API_VERSION=2024-02-15-preview
   AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

### Docker Deployment

1. Make sure Docker and Docker Compose are installed on your system.

2. Create a `.env` file in the root directory with your API credentials (see above for both OpenAI and Azure OpenAI options).

3. Build and start the container:
   ```bash
   docker-compose -f docker/docker-compose.yml up -d
   ```

4. Access the application:
   ```
   http://localhost:5000
   ```

5. To stop the container:
   ```bash
   docker-compose -f docker/docker-compose.yml down
   ```

## Project Structure

```
content-moderation-api/
├── app.py                 # Main application file
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (not version controlled)
├── templates/
│   └── index.html         # Web interface
├── docker/
│   ├── Dockerfile         # Docker image definition
│   ├── docker-compose.yml # Docker Compose configuration
│   └── .dockerignore      # Files to exclude from Docker build
└── venv/                  # Virtual environment (not version controlled)
```

## API Usage

You can also use the API directly by sending POST requests to the `/analyze` endpoint:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text":"Your text to analyze here"}' http://localhost:5000/analyze
```

Response format:
```json
{
  "success": true,
  "flagged": true|false,
  "model": "text-moderation-latest",
  "id": "modr-XXXX",
  "scores": {
    "Category Name": "0.123456"
  }
}
```

## License

[MIT License](LICENSE) 