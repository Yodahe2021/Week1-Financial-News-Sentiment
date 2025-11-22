# test_analysis.py
import pytest
import os
import sys

# Add src folder to the path for importing modules
sys.path.insert(0, os.path.abspath('src'))

# Import the class we want to test
from eda_pipeline import EDAPipeline

def test_pipeline_initialization():
    """Test that the EDAPipeline initializes correctly."""
    # Since the file path is required, we use a known-good placeholder
    # The initialization should not raise an error
    pipeline = EDAPipeline(file_path="dummy_path.csv")
    assert pipeline is not None
    assert pipeline.file_path == "dummy_path.csv"