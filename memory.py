import os
import json
import redis
from dotenv import load_dotenv

load_dotenv()

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

def get_session_memory(user_id: str):
    key = f"user:{user_id}:history"
    history_json = redis_client.get(key)
    if history_json:
        return json.loads(history_json)
    return []

def save_session_memory(user_id: str, user_message: str, bot_message: str):
    key = f"user:{user_id}:history"
    history = get_session_memory(user_id)
    history.append({"role": "user", "content": user_message})
    history.append({"role": "assistant", "content": bot_message})
    if len(history) > 10:
        history = history[-10:]
    redis_client.set(key, json.dumps(history))
