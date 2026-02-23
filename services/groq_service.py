import os
from dotenv import load_dotenv
from groq import Groq
from services.krishna_prompt import KRISHNA_PROMPT

# Load environment variables
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_krishna_response(messages):
    """
    Send a list of message dicts to the chat completion API.
    `messages` should already include the system prompt as the first item.
    Example: [{"role":"system","content":...}, {"role":"user","content":...}, ...]
    """
    response = client.chat.completions.create(
       model="llama-3.1-8b-instant",
        messages=messages
    )
    return response.choices[0].message.content
