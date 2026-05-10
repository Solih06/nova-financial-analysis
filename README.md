# Nova Financial Analysis: News & Stock Correlation

## 🚀 Project Overview
This repository focuses on identifying **Temporal Correlation** between 1.4 million financial news headlines and stock market price actions. The goal is to determine if sentiment polarity acts as a leading or lagging indicator for market volatility.

## 📊 Key Visual Insights

### 1. Keyword & Topic Analysis (Task 1)
Our extraction revealed that the news dataset is primarily "Event-Driven," focusing on corporate performance cycles rather than general macro-economic noise.
![Topic Wordcloud](./visuals/wordcloud_topics.png)
*Figure 1: Word cloud representing high-frequency financial tokens.*

### 2. Publisher Distribution & Bias (Task 1)
Analysis identified a significant concentration of articles from Benzinga. This finding necessitates source-normalization to ensure predictive models are not biased by a single editorial style.
![Publisher Analysis](./visuals/top_publishers.png)
*Figure 2: Distribution of news articles by publisher.*

### 3. Technical Indicator Baseline (Task 2)
We established a quantitative baseline using the 20-day Simple Moving Average (SMA) and RSI for AAPL to track price trends against news volume.
![Technical Analysis](./visuals/aapl_technical_indicators.png)
*Figure 3: AAPL price action overlaid with 20-day SMA baseline.*

### 4. Engineering & Automation
This project utilizes GitHub Actions to ensure code quality and environment reproducibility. A green checkmark in the Actions tab confirms that the CI/CD pipeline and unit tests are functional.
![CI/CD Status](./visuals/github_actions_proof.png)
*Figure 4: Proof of automated testing and modular repository structure.*

## 📁 Repository Structure
* **`.github/workflows/`**: CI/CD pipeline (`unittests.yml`) for automated quality checks.
* **`notebooks/`**: Exploratory Data Analysis (EDA) and Quantitative analysis documentation.
* **`scripts/`**: Modular Python logic and helper functions, initialized with `__init__.py`.
* **`visuals/`**: Exported plots and charts for reporting and transparency.
* **`tests/`**: Unit testing suite for environment and logic validation.

## 🛠️ Setup and Installation
1.  **Clone & Navigate:**
    ```bash
    git clone [https://github.com/Solih06/nova-financial-analysis.git](https://github.com/Solih06/nova-financial-analysis.git)
    cd nova-financial-analysis
    ```
2.  **Environment Setup:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Use 'source venv/bin/activate' on Mac/Linux
    pip install -r requirements.txt
    ```

## 📈 Future Roadmap
* **Task 3:** Implement VADER sentiment scoring and calculate Pearson Correlation between sentiment and daily log returns.
* **Task 4:** Perform lag analysis to determine the predictive strength of news sentiment.