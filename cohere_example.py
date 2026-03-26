from dotenv import load_dotenv
import os
import cohere

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

def query_cohere(prompt):
    try:
        response = co.generate(
            model="command",
            prompt=prompt,
            max_tokens=100
        )
        return response.generations[0].text
    except Exception as e:
        return "Error: " + str(e)

if __name__ == "__main__":
    user_input = input("Enter your question: ")
    print("Response:")
    print(query_cohere(user_input))