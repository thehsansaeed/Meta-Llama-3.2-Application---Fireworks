import requests
import json

# Function to call Fireworks API for chatbot response
def get_chatbot_response(image_url=None, user_question=None):
    url = "https://api.fireworks.ai/inference/v1/chat/completions"
    
    # Set the payload for the image or question
    if image_url:
        payload = {
            "model": "accounts/fireworks/models/llama-v3p2-11b-vision-instruct",
            "max_tokens": 16384,
            "top_p": 1,
            "top_k": 40,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "temperature": 0.6,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Describe this image"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url
                            }
                        }
                    ]
                }
            ]
        }
    elif user_question:
        payload = {
            "model": "accounts/fireworks/models/llama-v3p2-11b-vision-instruct",
            "max_tokens": 16384,
            "top_p": 1,
            "top_k": 40,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "temperature": 0.6,
            "messages": [
                {
                    "role": "user",
                    "content": user_question
                }
            ]
        }
    else:
        return "No input provided."
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f""
    }
    
    # Send the request to the Fireworks API
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    # Handle the response
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

# Main function to run the chatbot in the console
def chatbot_console():
    while True:
        user_input = input("Enter 'image' for image URL or 'question' for a question (or type 'exit' to quit): ").strip().lower()
        if user_input == 'exit':
            print("Exiting chatbot...")
            break
        elif user_input == 'image':
            image_url = input("Enter image URL: ").strip()
            response = get_chatbot_response(image_url=image_url)
        elif user_input == 'question':
            user_question = input("Enter your question: ").strip()
            response = get_chatbot_response(user_question=user_question)
        else:
            response = "Invalid input."
        
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot_console()