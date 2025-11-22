# 📰 Week 1 Challenge: Financial News Sentiment & Stock Prediction

### Project: Predicting Stock Price Moves with News Sentiment Analysis

This repository documents the foundational infrastructure and analysis for the 10 Academy Financial News Sentiment challenge. The objective is to merge financial news data with technical stock indicators to analyze potential correlations.

---

## 🚀 Project Status and Deliverables (Interim Report)

| Component | Status | Deliverable |
| :--- | :--- | :--- |
| **Task 1: Infrastructure** | **COMPLETE** ✅ | Full Git/GitHub workflow, clear structure, and active CI/CD pipeline. |
| **Task 2: Quantitative Prep** | **COMPLETE** ✅ | Technical indicators (RSI, MACD, SMA) calculated using TA-Lib. |
| **Interim Report** | **COMPLETED** ✅ | Report submitted detailing initial findings and methodology. |
| **Next Phase** | Sentiment Scoring & Correlation Testing (Task 3). | |

---

## 🛠️ Project Structure and Infrastructure

The project follows a standard, reproducible structure:
Project Structure
.
├── .github/
│   └── workflows/
│       └── unittests.yml
│
├── data/
│   ├── clean/
│   └── raw/
│       ├── news_data/
│       │   └── raw_analyst_ratings.csv
│       └── yfinance_data/
│           ├── AAPL.csv
│           └── ... (other tickers)
│
├── notebooks/
│   └── 1_exploratory_data_analysis.ipynb
│
├── scripts/
│
├── src/
│   ├── eda_pipeline.py
│   └── stock_analysis.py
│
├── tests/
│   └── test_analysis.py
│
└── requirements.txt
### **Continuous Integration (CI/CD)**

A robust CI pipeline using **GitHub Actions** is active. Any code push triggers `pytest` to ensure all core modules are functional and stable.

---

## 📊 Key Initial Findings (Task 1 EDA)

| Finding | Detail |
| :--- | :--- |
| **Headline Density** | Average headline length is approximately **75 characters**. The distribution is **right-skewed**, confirming concise text concentration. |
| **Publisher Dominance** | The top three most active publishers are **Paul Quintaro**, **Lisa Levin**, and **Benzinga Newsdesk**. |

### **Visualization Example**

```markdown
![Top 10 Active Publishers Bar Chart](assets/figure_3.png)

