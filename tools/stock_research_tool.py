import yfinance as yf
from crewai.tools import tool

@tool("Live Stock Information Tool")
def get_stock_price(stock_symbol: str) -> str:
    """
    Retrieves the latest stock price and other relevant info for a given stock symbol using Yahoo Finance.
    Parameters:
        stock_symbol (str): The ticker symbol of the stock (e.g., AAPL, TSLA, MSFT).
    Returns:
        str: A Summary of the stock's current price, daily change, and other Key data.
    """
    try:
        stock = yf.Ticker(stock_symbol)
        info = stock.info
        
        # Safe access to keys in case yfinance changes format
        current_price = info.get('regularMarketPrice') or info.get('currentPrice')
        change = info.get('regularMarketChange')
        change_percent = info.get('regularMarketChangePercent')
        currency = info.get('currency', 'USD')

        if current_price is None:
            return f"Could not fetch price for {stock_symbol}. Please check the symbol."
        
        # Handle cases where change is None (sometimes happens with yfinance)
        change_display = change if change is not None else 0.0
        pct_display = round(change_percent * 100, 2) if change_percent is not None else 0.0

        return (
            f"Stock: {stock_symbol.upper()}\n"
            f"Price: {current_price} {currency}\n"
            f"Change: {change_display} ({pct_display}%)"
        )
    except Exception as e:
        return f"Error fetching data for {stock_symbol}: {str(e)}"