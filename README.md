# Nova Financial Analysis: News & Stock Correlation

## 🚀 Project Overview
This repository focuses on identifying **Temporal Correlation** between 1.4 million financial news headlines and stock market price actions. The goal is to determine if sentiment polarity and publication frequency act as leading indicators for market volatility.

## 📊 Key Visual Insights

### 1. Keyword & Topic Analysis (Task 1)
Our extraction revealed that the news dataset is primarily "Event-Driven," focusing on corporate performance cycles (Earnings, Dividends).
![Topic Wordcloud](./visuals/wordcloud_topics.png)
*Figure 1: Word cloud representing high-frequency financial tokens.*

### 2. Publication Trends & Volume (Task 1)
We analyzed the frequency of articles over time to identify specific periods of high news density, which often correlate with market earnings seasons.
![Publication Trends](./visuals/publication_trends.png)
*Figure 2: Time-series analysis of publication frequency showing news volume trends over time.*

### 3. Headline Length Analysis (Task 1)
Analysis of headline character counts shows most titles are between 25–50 characters. This justifies the use of **VADER**, which is optimized for high-density, short-form text.
![Headline Length Distribution](./visuals/headline_length.png)
*Figure 3: Distribution of headline character counts across the dataset.*

### 4. Publisher Dominance & Source Bias (Task 1)
The data shows a heavy concentration of articles from Benzinga, necessitating a source-normalization step in future modeling.
![Publisher Analysis](./visuals/top_publishers.png)
*Figure 4: Distribution of news articles by publisher highlighting source concentration.*

### 5. Technical Indicator Baseline (Task 2)
Established a quantitative baseline using the 20-day Simple Moving Average (SMA) and RSI for AAPL to track price trends against news volume.
![Technical Analysis](./visuals/aapl_technical_indicators.png)
*Figure 5: AAPL price action overlaid with 20-day SMA baseline.*

## 📁 Repository Structure
* **`.github/workflows/`**: CI/CD pipeline configuration for environment stability.
* **`notebooks/`**: Exploratory Data Analysis (EDA) and Quantitative analysis.
* **`scripts/`**: Modular Python logic, initialized with `__init__.py`.
* **`visuals/`**: Exported plots and charts for reporting and transparency.
* **`tests/`**: Unit testing suite for environment validation.

## 🛠️ Setup and Installation
1. **Clone & Navigate:**
   ```bash
   git clone [https://github.com/Solih06/nova-financial-analysis.git](https://github.com/Solih06/nova-financial-analysis.git)
   cd nova-financial-analysis
2. **Environment setup**
python -m venv venv
3. **Activate the environment**
for windows
.\venv\Scripts\activate
for mac/linux
source venv/bin/activate
4. **Install dependencies**
pip install -r requirements.txt
5. **Verify Installation**
python -m unittest discover tests
