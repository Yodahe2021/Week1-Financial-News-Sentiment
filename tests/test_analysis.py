# tests/test_analysis.py
import pytest
import os
import sys

# --- FIX START: Correctly set up the package path ---

# 1. Get the path to the project root (one level up from 'tests')
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# 2. Add the project root to the path so Python can find 'src'
sys.path.insert(0, PROJECT_ROOT)

# Import the classes using the 'src' package prefix
# This is required because eda_pipeline and stock_analysis now use 'from . import utils'
from src.eda_pipeline import EDAPipeline
from src.stock_analysis import StockAnalyzer

# --- FIX END ---

def test_pipeline_initialization():
    """Test that the EDAPipeline initializes correctly (even without real data)."""
    # Use a dummy path; the test only checks if the class can be created
    pipeline = EDAPipeline(file_path="non_existent_news_file.csv")
    assert pipeline is not None
    assert pipeline.df is None

def test_stock_analyzer_initialization():
    """Test that the StockAnalyzer initializes correctly."""
    # Note: If running Pytest from the project root, '../' may not be necessary
    analyzer = StockAnalyzer(data_folder="data/raw/yfinance data") 
    assert analyzer is not None