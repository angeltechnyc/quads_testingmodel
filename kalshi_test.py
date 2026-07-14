import kalshi_python
from kalshi_python.api import MarketsApi
import pandas as pd

def test_kalshi_connection():
    print("Initializing Kalshi Demo Client...")
    
    # Point configuration to the paper trading environment
    config = kalshi_python.Configuration()
    config.host = "https://demo-api.kalshi.co/trade-api/v2"
    
    # Initialize the API client and correct Markets API class
    api_client = kalshi_python.ApiClient(config)
    market_client = MarketsApi(api_client)
    
    try:
        print("Fetching current event markets from Kalshi Demo...")
        response = market_client.get_markets(limit=5, status="open")
        
        # Parse the JSON response into a Pandas DataFrame
        markets = response.markets
        data = []
        for m in markets:
            data.append({
                "Ticker": m.ticker,
                "Title": m.title,
                "Yes Price": m.yes_bid,
                "No Price": m.no_bid
            })
            
        df = pd.DataFrame(data)
        print("\n--- Connection Successful! Previewing Data Struct: ---")
        print(df.to_string(index=False))
        
    except Exception as e:
        print(f"\nAn error occurred while connecting to Kalshi: {e}")

if __name__ == "__main__":
    test_kalshi_connection()
