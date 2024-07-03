# PDF Summary API

This is a simple Django REST Framework API that allows users to upload a 1-page PDF file and get a summary of its content. The application is containerized using Docker.

## Endpoints

- `POST /api/summarize/`: Accepts a PDF file and returns a summary of its content.

## Setup

### Requirements

- Docker
- Docker Compose (optional but recommended)

### Running the Application

1. Clone the repository:
    ```bash
    git clone https://github.com/PylypArsen/pdf_sum
    ```

2. Build and run the Docker container:
    ```bash
    cd pdf_sum
    docker-compose build
    docker-compose up
    ```

3. The API will be available at `http://localhost:8000`.

### Usage

You can use tools like `curl` or Postman to test the API.

Example with `curl`:
```bash
curl -X POST http://localhost:8000/api/summarize/ -F 'file=@/path/to/your/file.pdf'
```

### Final Notes

- Ensure you replace `'your-openai-api-key' in `'settings.py' with your actual OpenAI API key.
- This setup uses `gpt-3.5-turbo` as the engine, which may need to be updated based on your OpenAI subscription or usage requirements.

This guide covers the essential steps to create and deploy a containerized Django application for summarizing PDF files using the OpenAI API. You can further enhance the project by adding authentication, validation, and other necessary features based on your needs.
