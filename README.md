# RESTful API with LLM Integration

## Description:
This project provides a RESTful API built using Django and the Django Rest Framework (DRF) for processing text using pre-trained LLM models (via Hugging Face's transformers library). The API supports tasks like text summarization and sentiment analysis. The processed results are stored in a database and can be accessed via endpoints to retrieve or clear history.

## Features:
1. **POST /process**: Accepts a JSON payload with text and a task (either 'summarization' or 'sentiment') and returns the processed result.
2. **GET /history**: Retrieves all processed results from the database.
3. **DELETE /clear_history**: Clears all processed results stored in the database.
4. **GET /supported_tasks**: Lists all supported tasks that can be performed by the API.

## Installation Instructions:

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/my_project.git

### API Documentation:
Description: Accepts a JSON payload containing text (the input text) and task (the type of processing task). The API processes the text according to the specified task and returns the processed result.

```bash {
  "input_text": "Your input text here",
  "result": "Summarized text here",
  "task": "summarization",
  "created_at": "2025-01-22T12:34:56Z"
}

GET /history

[
  {
    "input_text": "Your input text here",
    "result": "Summarized text here",
    "task": "summarization",
    "created_at": "2025-01-22T12:34:56Z"
  },
  // Other processed results
]

DELETE /clear_history
This endpoint clears all processed results from the database and returns a confirmation message:
{
  "message": "History cleared successfully"
}


Requirements
Python 3.8+
Django 4.x
Django Rest Framework
Hugging Face transformers library
PostgreSQL (or any other database of your choice)



