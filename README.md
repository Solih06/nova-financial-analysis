# Nova Financial Solutions - Stock Sentiment Analysis

## 📊 Project Overview
This repository contains the end-to-end data pipeline for analyzing the correlation between financial news sentiment and stock market movements. Using the **FNSPID** (Financial News and Stock Price Integration Dataset), this project identifies how news volume and editorial sentiment act as indicators for price volatility.

---

## 🛠️ Task 1: Professional Environment & EDA

### 1. Engineering & Environment Setup
To ensure the project is scalable and production-ready, I implemented the following:
* **Virtualization:** Utilized `venv` to isolate dependencies, ensuring the project remains reproducible. All libraries are documented in `requirements.txt`.
* **Modular Architecture:** Established a clean directory structure:
    * `notebooks/`: Iterative research and Exploratory Data Analysis (EDA).
    * `scripts/`: Reusable Python modules for data fetching and processing.
    * `visuals/`: Automated storage for analysis-driven plots.
* **Version Control:** Managed the development lifecycle using Git with a **Feature Branch Strategy** (`task-1`) and conventional commit standards.

### 2. Key EDA Findings
I processed over **1.4 million financial headlines** to establish a baseline for sentiment modeling:

#### **A. Publication Volatility (Time-Series)**
The analysis identified significant publication "bursts," most notably a massive spike in **2020**. These spikes align with global economic shifts, providing high-signal periods for our upcoming correlation study.
![Publication Trends](visuals/publication_trends.png)

#### **B. Publisher Dominance**
Identified **Benzinga** as the primary news source in the dataset. Recognizing publisher dominance is essential for neutralizing editorial bias in the sentiment scoring phase.
![Top Publishers](visuals/top_publishers.png)

#### **C. Headline Density**
Analysis of character counts showed a peak between **25–50 characters**. This high density suggests that concise, transformer-based models (like **FinBERT**) will be the most effective for extracting sentiment polarity.
![Headline Distribution](visuals/headline_len_dist.png)

---

## 🚀 Future Roadmap: Task 2 & 3
* **Quantitative Analysis:** Downloading historical price data via `yfinance` and calculating technical indicators (SMA, RSI, MACD).
* **Correlation Study:** Merging news sentiment with stock volatility to determine if news acts as a leading or lagging indicator for market movement.

---

## 🔧 Installation & Setup
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/nova-financial-analysis.git](https://github.com/YOUR_USERNAME/nova-financial-analysis.git)
    ```
2.  **Activate Virtual Environment:**
    ```bash
    .\venv\Scripts\activate
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```