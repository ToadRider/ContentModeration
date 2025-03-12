# Content Moderation API

A Flask application that uses OpenAI's Moderation API to analyze text for potentially harmful content.

## Features

- Clean, responsive web interface for submitting text
- Real-time analysis using OpenAI's Moderation API
- Detailed breakdown of content categories and confidence scores

## Prerequisites

- Python 3.9+
- OpenAI API key
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

4. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
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

2. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

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