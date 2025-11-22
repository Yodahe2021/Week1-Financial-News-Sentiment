# tests/test_analysis.py
import pytest
import os
import sys

# Add src folder to the path for importing modules
sys.path.insert(0, os.path.abspath('src'))

# Import the classes we want to test
from eda_pipeline import EDAPipeline
# Import stock_analysis.py and the class inside it
from stock_analysis import StockAnalyzer

def test_pipeline_initialization():
    """Test that the EDAPipeline initializes correctly (even without real data)."""
    # Use a dummy path; the test only checks if the class can be created
    pipeline = EDAPipeline(file_path="non_existent_news_file.csv")
    assert pipeline is not None
    assert pipeline.df is None

def test_stock_analyzer_initialization():
    """Test that the StockAnalyzer initializes correctly."""
    analyzer = StockAnalyzer(data_folder="../data/raw/yfinance data")
    assert analyzer is not None