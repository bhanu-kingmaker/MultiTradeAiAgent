__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
import os
from dotenv import load_dotenv

from crew import stock_crew
load_dotenv()

os.environ["OTEL_SDK_DISABLED"] = "true" 
if "OPENAI_API_KEY" in os.environ:
    del os.environ["OPENAI_API_KEY"]

import yfinance as yf
import pandas as pd
from crew import stock_crew 

st.set_page_config(page_title="AI Stock Strategist", page_icon="📈", layout="wide")

st.title("🚀 Autonomous Multi-Agent Stock Analysis")
st.markdown("This system uses **Llama 3.3 (Groq)** and **CrewAI** to provide strategic insights.")

with st.sidebar:
    st.header("Configuration")
    stock_ticker = st.text_input(
        "Enter Stock Ticker:", 
        value=None, 
        placeholder="e.g. NVDA, AAPL, RELIANCE.NS"
    )
    
    if stock_ticker:
        stock_ticker = stock_ticker.upper()
        
    analyze_btn = st.button("Run AI Analysis")
    
    st.divider()
    st.info("The Analyst fetches live data, and the Trader provides the final strategy.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader(f"Market Overview: {stock_ticker if stock_ticker else 'Waiting for Input...'}")
    
    if stock_ticker:
        # We add a clean-up step to ensure the chart refreshes
        try:
            # Adding a clearer download logic
            ticker_data = yf.Ticker(stock_ticker)
            data = ticker_data.history(period="1mo") # history() is more stable than download() for single tickers
            
            if not data.empty:
                # We extract only the 'Close' price and rename it for a cleaner look
                chart_df = data[['Close']].copy()
                
                # Plotting with a specific key to force Streamlit to treat it as a new object
                st.line_chart(chart_df, use_container_width=True)
            else:
                st.warning(f"No price history found for: {stock_ticker}")
        except Exception as e:
            st.error(f"Chart Update Error: {e}")
    else:
        st.write("Enter a ticker symbol in the sidebar to see the price chart.")

with col2:
    st.subheader("Agent Execution & Results")
    
    if analyze_btn:
        if not stock_ticker:
            st.warning("Please enter a stock ticker first!")
        else:
            with st.spinner(f"🤖 Agents are analyzing {stock_ticker}..."):
                try:
                    result = stock_crew.kickoff(inputs={"stock": stock_ticker})
                    
                    st.success("#### Final Trading Strategy")
                    st.markdown(result.raw) 
                    
                except Exception as e:
                    st.error(f"Execution Error: {e}")
    else:
        st.info("Click 'Run AI Analysis' to start the process.")

st.divider()
st.caption("Disclaimer: For educational purposes only.")