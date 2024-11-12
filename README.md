# Customer Feedback Analytics Platform

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen)

A comprehensive platform for analyzing customer feedback and reviews using advanced NLP and machine learning techniques. The platform provides sentiment analysis, customer segmentation, and interactive visualizations to derive actionable insights from customer feedback data.

![customer-segments-view](https://github.com/user-attachments/assets/bc6970e2-20c2-45c8-848d-73cc3fbb9e04)
![realtime-monitoring](https://github.com/user-attachments/assets/523502e4-1c92-4bf3-be1f-f92fe15b0c8e)
![sentiment-analysis-view](https://github.com/user-attachments/assets/1865adb5-84da-4dab-a074-a3928eca9c88)
![voc-users-dashboard](https://github.com/user-attachments/assets/472e057c-df59-4dde-b729-4b2f67aa8c8b)

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
```

### Using the Jupyter Notebook
```bash
jupyter notebook notebooks/analysis_example.ipynb
```

## 📁 Project Structure
```
customer_feedback_analytics/
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessor.py
│   ├── sentiment_analyzer.py
│   ├── clustering.py
│   ├── visualization.py
│   └── utils.py
│
├── models/
│   └── __init__.py
│
├── tests/
│   ├── __init__.py
│   └── test_analyzer.py
│
├── notebooks/
│   └── analysis_example.ipynb
│
├── requirements.txt
└── main.py
```

## 📈 Example Visualizations

![Sentiment Trend](https://your-image-host.com/sentiment_trend.png)
![Customer Segments](https://your-image-host.com/customer_segments.png)

## 📝 Database Schema

### Reviews Table
```sql
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    review_text TEXT,
    rating INTEGER,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);
```

### Processed Reviews Table
```sql
CREATE TABLE processed_reviews (
    review_id INTEGER PRIMARY KEY,
    processed_text TEXT,
    sentiment_score FLOAT,
    sentiment_label VARCHAR(10),
    cluster_id INTEGER
);
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- BERT model from Hugging Face Transformers
- Scikit-learn for machine learning implementations
- Plotly for interactive visualizations
- NLTK for text processing

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter) - email@example.com

Project Link: [https://github.com/yourusername/customer-feedback-analytics](https://github.com/yourusername/customer-feedback-analytics)
