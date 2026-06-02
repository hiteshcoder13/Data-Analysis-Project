import pandas as pd
import json
import os
from pathlib import Path


class DataLoader:
    """Load data from multiple file formats"""
    
    SUPPORTED_FORMATS = {
        '.csv': 'csv',
        '.json': 'json',
        '.xlsx': 'excel',
        '.xls': 'excel',
        '.tsv': 'csv',
        '.txt': 'csv',
    }
    
    @staticmethod
    def load_data(file_path):
        """
        Load data from various file formats
        
        Args:
            file_path: Path to the data file
            
        Returns:
            pd.DataFrame: Loaded data
        """
        file_path = str(file_path)
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        file_ext = Path(file_path).suffix.lower()
        
        if file_ext not in DataLoader.SUPPORTED_FORMATS:
            raise ValueError(f"Unsupported file format: {file_ext}. Supported formats: {list(DataLoader.SUPPORTED_FORMATS.keys())}")
        
        file_type = DataLoader.SUPPORTED_FORMATS[file_ext]
        
        try:
            if file_type == 'csv':
                # Try common delimiters
                if file_ext == '.tsv':
                    df = pd.read_csv(file_path, delimiter='\t')
                else:
                    df = pd.read_csv(file_path)
                    
            elif file_type == 'json':
                df = pd.read_json(file_path)
                
            elif file_type == 'excel':
                df = pd.read_excel(file_path)
            
            if df.empty:
                raise ValueError("Loaded dataframe is empty")
                
            return df
            
        except Exception as e:
            raise Exception(f"Error loading {file_path}: {str(e)}")
    
    @staticmethod
    def validate_data(df):
        """
        Validate loaded data
        
        Args:
            df: DataFrame to validate
            
        Returns:
            dict: Validation report
        """
        report = {
            'rows': len(df),
            'columns': len(df.columns),
            'column_names': df.columns.tolist(),
            'dtypes': df.dtypes.to_dict(),
            'missing_values': df.isnull().sum().to_dict(),
            'duplicates': df.duplicated().sum(),
            'memory_usage': df.memory_usage(deep=True).sum() / 1024**2  # MB
        }
        return report
