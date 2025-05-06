import time

class StockTradingExpertSystem:
    def __init__(self):
        self.stock_data = {
            "AAPL": {"price": 145.09, "volume": 1000000},
            "GOOG": {"price": 2720.56, "volume": 500000},
            "TSLA": {"price": 780.55, "volume": 1200000},
            "AMZN": {"price": 3300.00, "volume": 700000},
            "NFLX": {"price": 500.00, "volume": 400000},
        }

    def analyze_and_trade(self, stock_symbol):
        stock_symbol = stock_symbol.upper()
        if stock_symbol not in self.stock_data:
            print("Stock symbol not found.")
            return

        stock_info = self.stock_data[stock_symbol]
        price = stock_info["price"]
        volume = stock_info["volume"]

        # Example logic for making trade decisions based on price and volume
        if price > 2500 and volume > 800000:
            decision = "Buy"
        elif price < 800 and volume < 1000000:
            decision = "Sell"
        else:
            decision = "Hold"

        print("\n--- Trade Analysis ---")
        print(f"Stock: {stock_symbol}")
        print(f"Price: ${price}")
        print(f"Volume: {volume}")
        print(f"Trade Decision: {decision}")
        
        # Real-time alert (simulated)
        print(f"ALERT: Execute {decision} for {stock_symbol} at ${price}!\n")

# Interactive session
def run_stock_trading_system():
    system = StockTradingExpertSystem()

    while True:
        print("\n=== Stock Market Expert System ===")
        print("Available Stocks:", ', '.join(system.stock_data.keys()))
        print("1. Analyze Stock")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            stock_symbol = input("Enter stock symbol (e.g., AAPL, GOOG): ").strip()
            system.analyze_and_trade(stock_symbol)
        elif choice == "2":
            print("Exiting Stock Trading System.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the system
run_stock_trading_system()
