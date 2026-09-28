from google import genai 
from google.genai import types 

def talk_to_gemini(prompt):
    client = genai.Client()
    my_instructions = (
        "You are JARVIS, a concise and efficient AI assistant. "
        "Keep your answers short, direct, and conversational unless "
        "the user explicitly asks for a detailed explanation or code block.")

    response=client.models.generate_content(model="gemini-3.6-flash",contents=prompt,config=types.GenerateContentConfig(
            system_instruction=my_instructions))

    return response.text