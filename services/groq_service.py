import os
from dotenv import load_dotenv
from groq import Groq
from services.krishna_prompt import KRISHNA_PROMPT

# Load environment variables
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_krishna_response(user_message):
    response = client.chat.completions.create(
       model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": KRISHNA_PROMPT},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content
