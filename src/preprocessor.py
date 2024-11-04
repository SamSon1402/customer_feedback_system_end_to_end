import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from typing import List, Optional
import pandas as pd
import logging

logger = logging.getLogger(__name__)

class TextPreprocessor:
    def __init__(self):
        try:
            nltk.download('punkt')
            nltk.download('stopwords')
            nltk.download('wordnet')
            nltk.download('averaged_perceptron_tagger')
            
            self.stop_words = set(stopwords.words('english'))
            self.lemmatizer = WordNetLemmatizer()
        except Exception as e:
            logger.error(f"Error initializing preprocessor: {str(e)}")
            raise
            
    def clean_text(self, text: str) -> str:
        if pd.isna(text):
            return ""
            
        text = text.lower()
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        text = re.sub(r'\S+@\S+', '', text)
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = ' '.join(text.split())
        
        return text
        
    def tokenize(self, text: str) -> List[str]:
        return word_tokenize(text)
        
    def remove_stopwords(self, tokens: List[str]) -> List[str]:
        return [token for token in tokens if token not in self.stop_words]
        
    def lemmatize(self, tokens: List[str]) -> List[str]:
        return [self.lemmatizer.lemmatize(token) for token in tokens]
        
    def preprocess(self, text: str) -> Optional[str]:
        try:
            cleaned_text = self.clean_text(text)
            tokens = self.tokenize(cleaned_text)
            tokens = self.remove_stopwords(tokens)
            tokens = self.lemmatize(tokens)
            return ' '.join(tokens)
        except Exception as e:
            logger.error(f"Error in preprocessing: {str(e)}")
            return None