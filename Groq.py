import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

# Initialize client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def query_groq(prompt):
    """
    Sends a prompt to Groq API and returns the response
    """
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Fast and free model
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


# Main execution
if __name__ == "__main__":
    print("Groq AI Chat")
    user_prompt = input("Enter your prompt: ")

    print("\nQuerying Groq API...\n")

    result = query_groq(user_prompt)

    print("Response:")
    print(result)