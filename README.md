# Nova Financial Solutions - Stock Sentiment Analysis

## 📊 Project Overview
This repository contains the end-to-end data pipeline for analyzing the correlation between financial news sentiment and stock market movements. Using the **FNSPID** (Financial News and Stock Price Integration Dataset), we bridge unstructured text with quantitative price action to identify market-moving signals.

---

## 🛠️ Task 1: Professional Environment & EDA

### 1. Engineering & Environment Setup
* **Virtualization:** Utilized `venv` to isolate dependencies.
* **Modular Architecture:** * `data/`: Local storage for datasets (Git-ignored for efficiency).
    * `notebooks/`: EDA and research environment.
    * `scripts/`: Production-ready Python modules for data automation.
    * `visuals/`: Repository for analysis-driven plots.
* **Git Strategy:** Managed via feature branches (`task-1`, `task-2`) to ensure code integrity.

### 2. Key EDA & Topic Findings
I processed over **1.4 million financial headlines** to establish a baseline for sentiment modeling:

#### **A. Topic & Keyword Analysis (New)**
Using keyword extraction, I identified that the dataset is primarily **event-driven**. Dominant keywords include "Earnings," "Dividend," "Quarterly," and "Bullish." This confirms that sentiment signals are tied to corporate performance cycles.
![Topic Analysis](visuals/wordcloud_topics.png)

#### **B. Publisher Dominance**
Analysis identified **Benzinga** as the primary news source. This dominance suggests that our sentiment model will be heavily influenced by their editorial style, which we will account for in Task 3.
![Top Publishers](visuals/top_publishers.png)

#### **C. Headline Density & Modeling Strategy**
Peak headline length is **25–50 characters**. This high density suggests that concise models like **FinBERT** or **VADER** are optimal for extracting polarity from this specific dataset.
![Headline Distribution](visuals/headline_len_dist.png)

#### **D. Publication Volatility**
Massive spikes in 2020 provide high-signal windows for our upcoming correlation study.
![Publication Trends](visuals/publication_trends.png)

---

## 📈 Task 2: Quantitative Progress (Proof of Concept)
I have successfully initialized the quantitative pipeline to fetch and process stock data:
* **Automation:** Developed `scripts/stock_processor.py` using `yfinance` to automate data retrieval.
* **Technical Indicators:** Implemented **SMA (Simple Moving Average)** and **RSI** using the `PyNance` library to establish a price-action baseline.

> **Visual Proof: AAPL Price vs. 20-Day SMA**
> ![Technical Indicators](visuals/aapl_technical_indicators.png)

---

## 🚀 Roadmap to Task 3
* **Sentiment Scoring:** Implementing **VADER** for sentiment polarity due to its high performance on short-form financial text.
* **Statistical Validation:** Applying **Pearson Correlation** and **Lag-Analysis** to determine if news sentiment predicts price breakouts.

---

## 🔧 Installation
1. **Clone & Setup:**
   ```bash
   git clone [https://github.com/Solih06/nova-financial-analysis.git](https://github.com/Solih06/nova-financial-analysis.git)
   cd nova-financial-analysis
   .\venv\Scripts\activate
   pip install -r requirements.txt