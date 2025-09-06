🚀 STAN | SDE Internship Assignment

This project is a chatbot system built using FastAPI, Redis, and OpenAI API.
It allows users to chat with an AI assistant while maintaining conversation history per user session.

📂 Project Structure
STAN-Chatbot/
│── app/
│   ├── main.py        # FastAPI entry point
│   ├── llm.py         # Handles OpenAI response generation
│   ├── memory.py      # Redis session storage
│── frontend/
│   └── index.html     # Chatbot UI
│── .env               # Environment variables (API keys)
│── requirements.txt   # Python dependencies
│── README.md          # Documentation

⚙️ Prerequisites

Make sure you have installed:

Python 3.9+
Redis
Git

🗄️ Install & Run Redis
Windows

Download Redis for Windows: Redis MSI

Install and start Redis:

redis-server


Test if Redis is running:

redis-cli ping


It should return:

PONG

Linux / Mac
# Install Redis
sudo apt update && sudo apt install redis-server -y     # Ubuntu/Debian
brew install redis                                      # macOS

# Start Redis
redis-server &

# Test
redis-cli ping

⚡ Setup Project

Clone the repository

git clone https://github.com/your-username/STAN-Chatbot.git
cd STAN-Chatbot


Create a virtual environment

python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows


Install dependencies

pip install -r requirements.txt


Set up environment variables
Create a .env file in the project root:

OPENAI_API_KEY=your_openai_api_key_here
REDIS_HOST=localhost
REDIS_PORT=6379

▶️ Run the Application

Start FastAPI server:

uvicorn app.main:app --reload


The backend runs at:
👉 http://127.0.0.1:8000

Open the frontend:
👉 frontend/index.html in your browser.

📡 API Endpoints

GET / → Health check (Chatbot API is running.)

POST /chat → Send user message

{
  "user_id": "123",
  "message": "Hello"
}

✅ Verification

Redis is running (redis-cli ping → PONG)

FastAPI server is running (uvicorn logs)

Frontend connects to backend (chat works in browser)
