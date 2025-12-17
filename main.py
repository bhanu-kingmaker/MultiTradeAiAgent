import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- FIX: Force Remove OpenAI Key if it exists ---
if "OPENAI_API_KEY" in os.environ:
    del os.environ["OPENAI_API_KEY"]
# -------------------------------------------------

# --- Diagnostic Check ---
api_key = os.getenv("GROQ_API_KEY")

if api_key:
    print(f"✅ Groq API Key found: {api_key[:4]}...")
else:
    print("❌ Groq API Key NOT found. Check your .env file.")
    exit()
# ------------------------

from crew import stock_crew

def run(stock_symbol: str):
    # Kickoff the crew with the stock symbol
    result = stock_crew.kickoff(inputs={"stock": stock_symbol})
    print("\n\n########################")
    print("## FINAL TRADING PLAN ##")
    print("########################\n")
    print(result)

if __name__ == "__main__":
    run("TSLA")