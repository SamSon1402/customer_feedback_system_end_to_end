import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Database settings
DATABASE = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432'),
    'database': os.getenv('DB_NAME', 'feedback_db'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'your_password')
}

# Model settings
BERT_MODEL = 'bert-base-uncased'
MAX_LENGTH = 512
BATCH_SIZE = 32

# Clustering settings
N_CLUSTERS = 5
RANDOM_STATE = 42

# Visualization settings
PLOT_STYLE = 'seaborn'
FIGURE_SIZE = (12, 8)