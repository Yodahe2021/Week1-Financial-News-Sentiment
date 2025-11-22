📰 Week 1 Challenge: Financial News Sentiment & Stock PredictionProject: Predicting Stock Price Moves with News Sentiment AnalysisThis repository contains the infrastructure setup, exploratory data analysis (EDA), and quantitative analysis pipeline developed during Week 1 of the 10 Academy Artificial Intelligence Mastery challenge.The primary goal is to establish a robust foundation for merging financial news data with stock market indicators to later investigate potential correlations between news sentiment and stock price movements.🚀 Project Status and Deliverables (Interim Report)ComponentStatusDeliverableTask 1: InfrastructureCOMPLETE ✅Full Git/GitHub workflow, clean folder structure, and active CI/CD.Task 2: Quantitative PrepCOMPLETE ✅Technical indicators (RSI, MACD, SMA) calculated and visualized.Interim ReportCOMPLETED ✅Report submitted covering initial findings and methodology.Next PhaseSentiment Scoring & Correlation Testing (Task 3).🛠️ Project Structure and InfrastructureThe project follows industry-standard conventions to separate logic, analysis, and infrastructure:├── .github/                      # CI/CD pipeline configuration
│   └── workflows/
│       └── unittests.yml         # GitHub Actions script for automated testing (pytest)
├── src/                          # Core Python logic (reusable modules)
│   ├── eda_pipeline.py           # Class for loading data and running EDA
│   └── stock_analysis.py         # Class for calculating technical indicators (TA-Lib)
├── notebooks/                    # Interactive analysis and visualization
│   ├── 1_eda_analysis.ipynb      # Exploration of news data (headline length, publishers)
│   └── 2_quant_analysis.ipynb    # Testing the StockAnalyzer class (AAPL, indicators)
├── tests/                        # Unit tests for core Python modules
├── data/                         # Placeholder for large data files (ignored by .gitignore)
└── requirements.txt              # List of all project dependencies (pandas, TA-Lib, etc.)
Continuous Integration (CI/CD)A robust CI pipeline using GitHub Actions is active. Any push to main or a feature branch (task-*) automatically runs pytest to ensure that core modules (eda_pipeline.py, stock_analysis.py) are functional and initialize correctly.📊 Key Initial Findings (Task 1 EDA)The initial analysis of the news dataset revealed essential characteristics for downstream modeling:Headline Density: The average headline length is approximately 75 characters. The right-skewed distribution confirms the data is concentrated in concise, high-density text.Publisher Dominance: News activity is highly concentrated. The top three most active publishers are Paul Quintaro, Lisa Levin, and Benzinga Newsdesk.EDA Visualization Example💻 How to Run the ProjectClone the Repository:Bashgit clone https://github.com/Yodahe2021/Week1-Financial-News-Sentiment.git
cd Week1-Financial-News-Sentiment
Setup Environment: Create a virtual environment and install dependencies.Bashpython -m venv venv
source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate
pip install -r requirements.txt
Run Analysis: Open the Jupyter notebooks to execute the pipeline.Bashjupyter notebook
Navigate to the notebooks/ folder and open 1_eda_analysis.ipynb or 2_quant_analysis.ipynb.💡 Key Technical Challenge (Focus for Task 3)The project's most significant technical hurdle is the Time Zone and Date Alignment between the two datasets:News timestamps are precise (e.g., 2020-05-22 12:45:06-04:00).Stock data is based only on trading days.Solution: The next phase will implement meticulous normalization to convert all news events to the next open trading day based on US market hours (4 PM ET close) to prevent data leakage and ensure accurate correlation testing.
