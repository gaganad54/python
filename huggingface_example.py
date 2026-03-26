from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/gpt2"

headers = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"
}

def query_hf(prompt):
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        return response.json()
    except Exception as e:
        return "Error: " + str(e)

if __name__ == "__main__":
    user_input = input("Enter your question: ")
    print("Response:")
    print(query_hf(user_input))