# Text Processing API with LLM Integration

## Description:
This project provides a RESTful API built using **Django** that processes input text using pre-trained **Hugging Face** models. The API supports tasks like **summarization** and **sentiment analysis**. The processed results are stored in-memory and can be accessed via an endpoint to retrieve the history of processed results.

## Features:
1. **POST /process**: Accepts a JSON payload containing a `text` field and a `task` field (either 'summarization' or 'sentiment') and returns the processed result.
2. **GET /history**: Retrieves all previously processed results stored in-memory.

## Requirements:
- Python 3.7+
- Install the required Python packages by running:
    ```bash
    pip install -r requirements.txt
    ```

## Installation Instructions:

### 1. Clone the repository:
   ```bash
  https://github.com/anushribarsaiyan/llm_project.git
   cd llm_project
```

2. Install the dependencies:
     ```bash
     pip install -r requirements.txt
    ```
3. API Documentation:
      ```bash
     
    POST /process
 
    Description: Accepts a JSON payload containing text (the input text) and task (the type of processing task). The API processes the text according to the specified task and     returns the processed result.

    Request Payload
    {
        "text": "Your input text here",
        "task": "summarization"  # or "sentiment"
    }
    Response (Summarization Example):
    {
        "input_text": "Your input text here",
        "result": "Summarized text here",
        "task": "summarization"
    }
    GET /history
    Description: Retrieves all processed results from the in-memory storage.
        [
            {
                "input_text": "Text 1",
                "result": "Result 1",
                "task": "summarization"
            },

            {
                "input_text": "Text 2",
                "result": "Result 2",
                "task": "sentiment"
            }
        ]   
    DELETE /clear_history
    Description: Clears all processed results from the database.
    {
        "message": "All history cleared."
    }
    GET /supported_tasks
    Description: Lists the tasks that can be processed by the API
    {
    "supported_tasks": ["summarization", "sentiment"]

    }
    ```
