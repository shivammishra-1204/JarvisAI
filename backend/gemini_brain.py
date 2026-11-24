
import os
from dotenv import load_dotenv
from google import genai

# Find the project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load API key from the root .env file
load_dotenv(os.path.join(BASE_DIR, ".env"))

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Gemini API key not found. Check your .env file.")

# Connect to Gemini
client = genai.Client(api_key=API_KEY)

# JARVIS personality
SYSTEM_INSTRUCTION = """
You are JARVIS, a smart, polite and friendly personal AI assistant.
You are assisting your creator.
Speak naturally and clearly.
Keep answers concise when possible.
You can explain technology, science, education and general topics.
Do not claim that you have performed actions on the computer unless
the program has actually performed them.
"""

def ask_gemini(question):
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=question,
            config={
                "system_instruction": SYSTEM_INSTRUCTION
            }
        )

        return response.text or "Sorry sir, I could not generate a response."

    except Exception as error:
        print("Gemini API Error:", error)
        return "Sorry sir, I am having trouble connecting to my intelligence system."
