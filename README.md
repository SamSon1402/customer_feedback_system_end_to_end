# Customer Feedback Analytics Platform

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen)

A comprehensive platform for analyzing customer feedback and reviews using advanced NLP and machine learning techniques. The platform provides sentiment analysis, customer segmentation, and interactive visualizations to derive actionable insights from customer feedback data.

## 🚀 Features

- **Advanced Text Processing**
  - NLTK-based text preprocessing
  - Lemmatization and stopword removal
  - Special character and noise cleaning

- **Sentiment Analysis**
  - BERT-based sentiment classification
  - Batch processing capabilities
  - Sentiment trend analysis over time

- **Customer Segmentation**
  - K-means clustering with automated feature scaling
  - PCA for dimensionality reduction
  - Customer segment analysis and profiling

- **Interactive Visualizations**
  - Sentiment trends over time
  - Customer segment visualization
  - Rating-sentiment distribution
  - Topic frequency analysis
  - Interactive Plotly dashboards

- **Database Integration**
  - PostgreSQL support
  - Efficient batch processing
  - Automated data loading and saving

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL
- CUDA-capable GPU (optional, for faster processing)

## 🛠️ Installation

1. Clone the repository
    ```bash
    git clone https://github.com/yourusername/customer-feedback-analytics.git
    cd customer-feedback-analytics
    ```

2. Create virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Configure database settings
    ```bash
    cp config/settings.example.py config/settings.py
    # Edit config/settings.py with your database credentials
    ```

## 📊 Usage

### Quick Start
```python
from main import CustomerFeedbackAnalytics

# Initialize the analyzer
analyzer = CustomerFeedbackAnalytics()

# Run analysis for the last 30 days
analyzer.run_analysis(
    start_date='2024-01-01',
    end_date='2024-02-01',
    output_dir='output'
)
