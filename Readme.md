# Console Chatbot Using Fireworks API

This project is a simple console-based chatbot that interacts with the Fireworks AI API to generate responses based on user inputs. The chatbot can handle both text-based questions and image-based prompts by providing an image URL.

## Features

- Supports user questions in text format.
- Describes images based on their URL using Fireworks' image understanding model.
- Uses the `llama-v3p2-11b-vision-instruct` model from Fireworks API for both text and image inputs.

## Prerequisites

- Python 3.x
- `requests` library for making API calls.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/fireworks-chatbot.git
   ```
2. Navigate to the project directory:

   ```bash
   cd fireworks-chatbot
   ```
3. Install the required dependencies:

   ```bash
   pip install requests
   ```

## Usage

1. Run the chatbot:

   ```bash
   python app.py
   ```
2. You can choose to ask a question or provide an image URL for analysis.

   - Type `image` to provide an image URL.
   - Type `question` to ask a text-based question.
   - Type `exit` to exit the chatbot.

## API Configuration

This chatbot uses the Fireworks API to generate responses. Make sure to replace the placeholder API key with your own API key in the script:

```python
"Authorization": f"Bearer YOUR_API_KEY"
```

## Contact Information

https://www.linkedin.com/in/ahsensaeed/
