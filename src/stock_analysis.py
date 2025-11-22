import pandas as pd
import talib
import matplotlib.pyplot as plt
# REMOVE: import os (Now handled by utils.py)

# NEW: Import the utility functions
from . import utils 

class StockAnalyzer:
    def __init__(self, data_folder):
        """
        Initialize with the folder where stock CSVs are located.
        """
        # We no longer need data_folder; we'll construct the full path on load_stock_data
        self.data_folder = data_folder
        self.df = None

    def load_stock_data(self, ticker):
        """
        Load a specific stock CSV (e.g., AAPL.csv) from the data folder.
        """
        # --- REPLACED CODE ---
        # Construct the relative path to the file
        relative_path = os.path.join(self.data_folder, f"{ticker}.csv")
        
        # Use the reusable utility function to load the stock data
        self.df = utils.load_csv_data(relative_path)
        
        # Ensure date is datetime and set as index (rest of the logic remains the same)
        if 'Date' in self.df.columns:
            self.df['Date'] = pd.to_datetime(self.df['Date'])
            self.df.set_index('Date', inplace=True)
        elif 'date' in self.df.columns:
            self.df['Date'] = pd.to_datetime(self.df['date'])
            self.df.set_index('Date', inplace=True)
            
        print(f"Loaded {len(self.df)} rows for {ticker}.")
        return self.df

# The __main__ block remains the same since DATA_FOLDER is correctly defined
# ...