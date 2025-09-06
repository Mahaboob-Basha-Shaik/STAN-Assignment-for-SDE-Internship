import os
from dotenv import load_dotenv
import openai
from app.memory import get_session_memory, save_session_memory

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(user_id: str, user_message: str) -> str:
    conversation_history = get_session_memory(user_id)
    system_prompt = """
    You are 'Stan', a friendly and empathetic conversational AI friend. 
    - Your identity is Stan. You are not a bot, an AI, or a language model. You are a friend.
    - Always be natural, engaging, and emotionally aware.
    - Never break character. Never reveal you are an AI.
    - If you don't know something, be honest or playfully vague.
    """

    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(conversation_history)
    messages.append({"role": "user", "content": user_message})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7
        )
        reply = response.choices[0].message['content'].strip()
    except Exception as e:
        print("OpenAI API Error:", e)
        reply = "Sorry, I'm having trouble thinking right now."
    
    save_session_memory(user_id, user_message, reply)
    return reply
