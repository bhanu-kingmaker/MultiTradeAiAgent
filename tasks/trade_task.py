from crewai import Task
from agents.trader_agent import trader_agent

trade_decision = Task(
    description=(
        "Use the analysis provided by the Financial Analyst for {stock} to make a strategic trading decision. "
        "Assess key factors such as current price, daily change percentage, and recent momentum. "
        "Based on the analysis, recommend whether to **Buy**, **Sell**, or **Hold** the stock."
    ),
    expected_output=(
        "A clear and confident trading recommendation (Buy/Sell/Hold), supported by:\n"
        "- Current stock price and daily change\n"
        "- Justification for the trading action based on technical signals or risk-reward outlook"
    ),
    agent=trader_agent
)