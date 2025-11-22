import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class EDAPipeline:
    def __init__(self, file_path):
        """
        Initialize the pipeline with the dataset path.
        """
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """
        Load data from CSV and convert date column to datetime objects.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")
        
        print("Loading data...")
        self.df = pd.read_csv(self.file_path)
        
        # Convert date to datetime (handling UTC-4 offset if present, or generic)
        # infer_datetime_format is deprecated in newer pandas, but strictly useful for speed if applicable
        try:
            self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce', utc=True)
        except Exception as e:
            print(f"Date conversion warning: {e}")
            
        print(f"Data loaded successfully. Shape: {self.df.shape}")
        return self.df

    def calculate_headline_stats(self):
        """
        Calculate and visualize headline lengths.
        """
        print("Calculating headline statistics...")
        
        # Calculate length
        self.df['headline_length'] = self.df['headline'].astype(str).apply(len)
        
        # Basic Stats
        print(self.df['headline_length'].describe())
        
        # Visualization
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df['headline_length'], bins=30, kde=True, color='blue')
        plt.title('Distribution of Headline Lengths')
        plt.xlabel('Length of Headline (characters)')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()

    def analyze_publishers(self, top_n=10):
        """
        Count articles per publisher and visualize the top N active ones.
        """
        print("Analyzing publishers...")
        
        publisher_counts = self.df['publisher'].value_counts().head(top_n)
        print(f"Top {top_n} Publishers:\n", publisher_counts)
        
        # Visualization
        plt.figure(figsize=(12, 6))
        sns.barplot(x=publisher_counts.values, y=publisher_counts.index, palette='viridis')
        plt.title(f'Top {top_n} Active Publishers')
        plt.xlabel('Number of Articles')
        plt.ylabel('Publisher')
        plt.show()

    def analyze_publication_dates(self):
        """
        Analyze publication trends over time.
        """
        print("Analyzing publication trends...")
        
        # Extract date only (ignoring time for daily count)
        daily_counts = self.df['date'].dt.date.value_counts().sort_index()
        
        # Visualization
        plt.figure(figsize=(14, 7))
        daily_counts.plot(kind='line', color='green', marker='o')
        plt.title('Article Publication Frequency Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    # This allows you to test the script directly
    # Update the filename to match your actual csv file name
    file_path = 'data/raw/news data/raw_analyst_ratings.csv' 
    
    pipeline = EDAPipeline(file_path)
    pipeline.load_data()
    pipeline.calculate_headline_stats()
    pipeline.analyze_publishers()
    pipeline.analyze_publication_dates()
