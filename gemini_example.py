from dotenv import load_dotenv
import os
import google.generativeai as genai

# 1. Load your API key from the .env file
load_dotenv()

# 2. Configure the library with your key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 3. Use 'gemini-1.5-flash' instead of 'gemini-pro'
model = genai.GenerativeModel("gemini-1.5-flash-8b")

def query_gemini(prompt):
    try:
        # 4. Send the user input to the AI
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # 5. Handle errors (like network issues or invalid keys)
        return "Error: " + str(e)

if __name__ == "__main__":
    user_input = input("Enter your question for Gemini: ")
    print("Response:")
    print(query_gemini(user_input))