
from backend.gemini_brain import ask_gemini

print("\nTesting JARVIS AI Brain...\n")

question = "Hello JARVIS! Introduce yourself in two sentences."

answer = ask_gemini(question)

print("JARVIS:", answer)
