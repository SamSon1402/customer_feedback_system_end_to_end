import pandas as pd
from sqlalchemy import create_engine
from typing import Optional, Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataLoader:
    def __init__(self, db_config: Dict[str, Any]):
        self.db_config = db_config
        self.engine = self._create_engine()
        
    def _create_engine(self) -> create_engine:
        conn_str = (f"postgresql://{self.db_config['user']}:{self.db_config['password']}"
                   f"@{self.db_config['host']}:{self.db_config['port']}"
                   f"/{self.db_config['database']}")
        return create_engine(conn_str)
    
    def load_reviews(self, start_date: str, end_date: str) -> Optional[pd.DataFrame]:
        query = """
        SELECT 
            r.review_id,
            r.customer_id,
            r.product_id,
            r.review_text,
            r.rating,
            r.created_at,
            r.updated_at,
            c.customer_segment,
            p.product_category
        FROM 
            reviews r
        LEFT JOIN 
            customers c ON r.customer_id = c.customer_id
        LEFT JOIN 
            products p ON r.product_id = p.product_id
        WHERE 
            r.created_at BETWEEN %s AND %s
        """
        
        try:
            df = pd.read_sql_query(
                query, 
                self.engine,
                params=[start_date, end_date]
            )
            logger.info(f"Loaded {len(df)} reviews successfully")
            return df
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            return None
            
    def save_results(self, df: pd.DataFrame, table_name: str) -> bool:
        try:
            df.to_sql(
                table_name,
                self.engine,
                if_exists='append',
                index=False,
                method='multi',
                chunksize=1000
            )
            logger.info(f"Successfully saved {len(df)} rows to {table_name}")
            return True
        except Exception as e:
            logger.error(f"Error saving results: {str(e)}")
            return False