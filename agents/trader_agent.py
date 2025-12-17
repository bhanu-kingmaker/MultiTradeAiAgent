from crewai import Agent, LLM
import os

llm = LLM(
    model="openai/llama-3.3-70b-versatile", 
    base_url="https://api.groq.com/openai/v1", 
    api_key=os.getenv("GROQ_API_KEY") 
)

trader_agent = Agent(
    role="Risk-Adjusted Strategic Trader",
    goal=("Provide a pragmatic 'Buy', 'Sell', or 'Hold' recommendation by balancing "
          "market opportunity against strict risk management protocols. Your primary "
          "priority is capital preservation over speculative gains."),
    backstory=("You are a veteran institutional trader known for your discipline. "
               "You understand that a 15% drop often indicates a fundamental break, "
               "not just a buying opportunity. You are skeptical of 'cheap' stocks and "
               "require strong evidence of a price floor before recommending a Buy. "
               "If volatility is extreme or the cause of a crash is unknown/promoter-led, "
               "you default to a 'Sell' or 'Hold' to protect the portfolio."),
    llm=llm,
    tools=[], 
    verbose=True,
    allow_delegation=False,
    # Added parameters for better control
    max_iter=5,
    memory=False 
)