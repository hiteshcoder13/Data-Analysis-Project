import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import StandardScaler


class DataAnalyzer:
    """Comprehensive data analysis including statistics, distributions, and imbalance detection"""
    
    def __init__(self, df):
        """
        Initialize analyzer with dataframe
        
        Args:
            df: Pandas DataFrame to analyze
        """
        self.df = df
        self.numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        self.categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    
    def get_overview(self):
        """Get basic overview of the data"""
        return {
            'total_rows': len(self.df),
            'total_columns': len(self.df.columns),
            'numeric_columns': len(self.numeric_cols),
            'categorical_columns': len(self.categorical_cols),
            'memory_usage_mb': self.df.memory_usage(deep=True).sum() / 1024**2,
            'duplicate_rows': self.df.duplicated().sum(),
            'duplicate_percentage': (self.df.duplicated().sum() / len(self.df) * 100) if len(self.df) > 0 else 0,
        }
    
    def get_missing_data_analysis(self):
        """Analyze missing values"""
        missing_data = {
            'missing_count': self.df.isnull().sum().to_dict(),
            'missing_percentage': (self.df.isnull().sum() / len(self.df) * 100).to_dict(),
            'total_missing_cells': self.df.isnull().sum().sum(),
            'total_cells': len(self.df) * len(self.df.columns),
            'missing_cell_percentage': (self.df.isnull().sum().sum() / (len(self.df) * len(self.df.columns)) * 100)
        }
        return missing_data
    
    def get_numeric_statistics(self):
        """Detailed statistical analysis of numeric columns"""
        stats_dict = {}
        
        for col in self.numeric_cols:
            col_data = self.df[col].dropna()
            
            if len(col_data) == 0:
                continue
            
            stats_dict[col] = {
                'count': len(col_data),
                'mean': col_data.mean(),
                'median': col_data.median(),
                'std_dev': col_data.std(),
                'variance': col_data.var(),
                'min': col_data.min(),
                'max': col_data.max(),
                'q25': col_data.quantile(0.25),
                'q50': col_data.quantile(0.50),
                'q75': col_data.quantile(0.75),
                'iqr': col_data.quantile(0.75) - col_data.quantile(0.25),
                'range': col_data.max() - col_data.min(),
                'skewness': stats.skew(col_data),
                'kurtosis': stats.kurtosis(col_data),
                'coefficient_of_variation': (col_data.std() / col_data.mean() * 100) if col_data.mean() != 0 else 0,
            }
        
        return stats_dict
    
    def get_distribution_analysis(self):
        """Analyze data distribution (normal, skewed, etc.)"""
        distribution_dict = {}
        
        for col in self.numeric_cols:
            col_data = self.df[col].dropna()
            
            if len(col_data) < 3:
                continue
            
            # Normality test
            _, p_value_normality = stats.normaltest(col_data)
            is_normal = p_value_normality > 0.05
            
            # Skewness interpretation
            skewness = stats.skew(col_data)
            if abs(skewness) < 0.5:
                skew_type = "Approximately Symmetric"
            elif skewness > 0:
                skew_type = "Positively Skewed (Right-tailed)"
            else:
                skew_type = "Negatively Skewed (Left-tailed)"
            
            # Kurtosis interpretation
            kurtosis = stats.kurtosis(col_data)
            if abs(kurtosis) < 0.5:
                kurt_type = "Mesokurtic (Normal-like)"
            elif kurtosis > 0:
                kurt_type = "Leptokurtic (Heavy-tailed)"
            else:
                kurt_type = "Platykurtic (Light-tailed)"
            
            distribution_dict[col] = {
                'is_normal': is_normal,
                'normality_p_value': p_value_normality,
                'skewness': skewness,
                'skew_type': skew_type,
                'kurtosis': kurtosis,
                'kurt_type': kurt_type,
            }
        
        return distribution_dict
    
    def get_categorical_analysis(self):
        """Analyze categorical columns"""
        categorical_dict = {}
        
        for col in self.categorical_cols:
            value_counts = self.df[col].value_counts()
            
            categorical_dict[col] = {
                'unique_values': self.df[col].nunique(),
                'top_value': value_counts.index[0] if len(value_counts) > 0 else None,
                'top_value_count': value_counts.iloc[0] if len(value_counts) > 0 else 0,
                'value_counts': value_counts.to_dict(),
                'missing_count': self.df[col].isnull().sum(),
            }
        
        return categorical_dict
    
    def detect_outliers(self):
        """Detect outliers using IQR method"""
        outliers_dict = {}
        
        for col in self.numeric_cols:
            col_data = self.df[col].dropna()
            
            Q1 = col_data.quantile(0.25)
            Q3 = col_data.quantile(0.75)
            IQR = Q3 - Q1
            
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outlier_mask = (self.df[col] < lower_bound) | (self.df[col] > upper_bound)
            outlier_count = outlier_mask.sum()
            outlier_percentage = (outlier_count / len(self.df) * 100) if len(self.df) > 0 else 0
            
            outliers_dict[col] = {
                'lower_bound': lower_bound,
                'upper_bound': upper_bound,
                'outlier_count': outlier_count,
                'outlier_percentage': outlier_percentage,
            }
        
        return outliers_dict
    
    def get_class_balance(self):
        """Analyze class balance in categorical columns"""
        balance_dict = {}
        
        for col in self.categorical_cols:
            value_counts = self.df[col].value_counts()
            total = value_counts.sum()
            
            balance_dict[col] = {
                'unique_classes': len(value_counts),
                'class_distribution': (value_counts / total * 100).to_dict(),
                'is_balanced': self._check_balance(value_counts),
                'imbalance_ratio': value_counts.max() / value_counts.min() if len(value_counts) > 1 else 1,
            }
        
        return balance_dict
    
    def _check_balance(self, value_counts, threshold=30):
        """Check if classes are balanced"""
        if len(value_counts) < 2:
            return True
        
        percentages = value_counts / value_counts.sum() * 100
        return (percentages.max() - percentages.min()) < threshold
    
    def get_correlation_analysis(self):
        """Analyze correlations between numeric columns"""
        if len(self.numeric_cols) < 2:
            return {}
        
        corr_matrix = self.df[self.numeric_cols].corr()
        
        # Find strong correlations (abs > 0.7)
        strong_corr = {}
        for i, col1 in enumerate(self.numeric_cols):
            for col2 in self.numeric_cols[i+1:]:
                corr_value = corr_matrix.loc[col1, col2]
                if abs(corr_value) > 0.7:
                    strong_corr[f"{col1} - {col2}"] = corr_value
        
        return {
            'correlation_matrix': corr_matrix.to_dict(),
            'strong_correlations': strong_corr,
        }
    
    def generate_full_analysis(self):
        """Generate comprehensive analysis report"""
        return {
            'overview': self.get_overview(),
            'missing_data': self.get_missing_data_analysis(),
            'numeric_statistics': self.get_numeric_statistics(),
            'distribution': self.get_distribution_analysis(),
            'categorical': self.get_categorical_analysis(),
            'outliers': self.detect_outliers(),
            'class_balance': self.get_class_balance(),
            'correlation': self.get_correlation_analysis(),
        }
