import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# REMOVE: import os (Now handled by utils.py)

# NEW: Import the utility functions
from . import utils # Use relative import since utils is in the same package (src)

class EDAPipeline:
    def __init__(self, file_path):
        """
        Initialize the pipeline with the dataset path.
        """
        self.file_path = file_path # e.g., 'data/raw/news data/raw_analyst_ratings.csv'
        self.df = None

    def load_data(self):
        """
        Load data from CSV and convert date column to datetime objects.
        """
        # --- REPLACED CODE ---
        # Instead of local os.path.exists and pd.read_csv, use the utility:
        self.df = utils.load_csv_data(self.file_path)
        
        # Convert date to datetime (rest of the logic remains the same)
        try:
            self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce', utc=True)
        except Exception as e:
            print(f"Date conversion warning: {e}")
            
        print(f"Data loaded successfully. Shape: {self.df.shape}")
        return self.df

# The __main__ block needs a slight path adjustment for the utility:
if __name__ == "__main__":
    # The file_path is now relative to the project root
    file_path = 'data/raw/news data/raw_analyst_ratings.csv' 
    
    pipeline = EDAPipeline(file_path)
    # ... rest of the main block remains the same