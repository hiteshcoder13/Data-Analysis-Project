# Data Analysis Project

A comprehensive Python-based data analysis tool that accepts multiple file formats (CSV, JSON, Excel, etc.) and generates professional DOCX reports with complete statistical analysis, visualizations, and data profiling.

## 🎯 Features

### Data Input Support
- **CSV Files** - Standard comma-separated values
- **JSON Files** - JSON formatted data
- **Excel Files** - XLSX and XLS formats
- **TSV Files** - Tab-separated values
- **TXT Files** - Text-based data formats

### Comprehensive Analysis
- **Data Overview** - Row/column counts, data types, memory usage
- **Missing Data Analysis** - Detection and visualization of missing values
- **Statistical Analysis** - Mean, median, std dev, quartiles, skewness, kurtosis
- **Distribution Analysis** - Normality tests, skewness types, kurtosis types
- **Categorical Analysis** - Unique values, top values, distribution
- **Outlier Detection** - IQR-based outlier identification and percentage
- **Class Balance Analysis** - Imbalance ratio and class distribution
- **Correlation Analysis** - Strong correlations between numeric variables

### Professional DOCX Reports
- Executive summary
- Data overview with column information
- Detailed statistical tables
- Distribution analysis with visualization
- Missing data patterns and visualizations
- Outlier detection results
- Class balance assessment
- Correlation matrices and heatmaps
- High-quality histograms, box plots, and bar charts

## 📋 Requirements

```
python-docx==0.8.11
pandas>=2.0.0
numpy>=1.24.0
scipy>=1.11.0
matplotlib>=3.7.0
seaborn>=0.12.0
scikit-learn>=1.3.0
openpyxl>=3.1.0
Pillow>=10.0.0
```

## 🚀 Installation & Setup

### 1. Navigate to project directory
```bash
cd /home/Unthinkable/Documents/Data-analysis-Project
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Basic Usage
```bash
source venv/bin/activate
python main.py <input_file> [output_file]
```

### Examples

#### Using CSV file
```bash
python main.py sample_data.csv analysis_report.docx
```

#### Using JSON file
```bash
python main.py sample_data.json analysis_report.docx
```

#### Using Excel file
```bash
python main.py data.xlsx analysis_report.docx
```

#### Using default output filename
```bash
python main.py sample_data.csv
# Output will be saved as: data_analysis_report.docx
```

## 📊 Report Contents

The generated DOCX report includes:

1. **Title Page** - Professional header with generation timestamp
2. **Table of Contents** - Complete navigation guide
3. **Executive Summary** - High-level dataset statistics
4. **Data Overview** - Column names and data types
5. **Missing Data Analysis** - Missing value patterns with visualizations
6. **Numeric Statistics** - Mean, median, std dev, quartiles, IQR, skewness
7. **Distribution Analysis** - Normality tests, skewness/kurtosis interpretation
8. **Categorical Analysis** - Value counts and distributions
9. **Outlier Detection** - IQR bounds and outlier percentages
10. **Class Balance Analysis** - Imbalance ratios and class distribution
11. **Correlation Analysis** - Strong correlations between variables
12. **Visualizations**:
    - Distribution plots (histograms and box plots)
    - Categorical bar charts
    - Correlation heatmaps
    - Missing data visualizations

## 🔍 Analysis Details

### Statistical Metrics
- **Count**: Number of non-null values
- **Mean**: Average value
- **Median**: Middle value (50th percentile)
- **Std Dev**: Standard deviation
- **Variance**: Variance of values
- **Min/Max**: Minimum and maximum values
- **Quartiles**: 25th, 50th, 75th percentiles
- **IQR**: Interquartile range
- **Range**: Max - Min
- **Skewness**: Measure of asymmetry
- **Kurtosis**: Measure of tail behavior
- **Coefficient of Variation**: Relative standard deviation

### Distribution Types
- **Symmetric** - Approximately symmetric distribution
- **Positively Skewed** - Right-tailed distribution
- **Negatively Skewed** - Left-tailed distribution
- **Normal Distribution** - Tested using Shapiro-Wilk test
- **Leptokurtic** - Heavy-tailed distribution
- **Platykurtic** - Light-tailed distribution

### Class Balance Assessment
- **Balanced**: Classes with similar proportions
- **Imbalanced**: Classes with significantly different proportions
- **Imbalance Ratio**: Ratio of most common to least common class

### Outlier Detection
- Uses Interquartile Range (IQR) method
- Lower bound: Q1 - 1.5 × IQR
- Upper Bound: Q3 + 1.5 × IQR
- Values outside bounds are marked as outliers

## 📁 Project Structure

```
Data-analysis-Project/
├── main.py                 # Main entry point
├── data_loader.py         # Data loading module (CSV, JSON, Excel, etc.)
├── data_analyzer.py       # Statistical analysis module
├── report_generator.py    # DOCX report generation
├── requirements.txt       # Python dependencies
├── sample_data.csv        # Example CSV file
├── sample_data.json       # Example JSON file
├── venv/                  # Virtual environment (created after setup)
└── README.md             # This file
```

## 🎓 Example Workflow

### Step 1: Prepare your data
- Ensure your data is in one of the supported formats (CSV, JSON, XLSX, etc.)
- Data should have meaningful column headers
- Include both numeric and categorical columns for best analysis

### Step 2: Run analysis
```bash
source venv/bin/activate
python main.py your_data.csv your_report.docx
```

### Step 3: Review report
- Open the generated DOCX file in Word/LibreOffice
- Review all sections for insights
- Export to PDF if needed for sharing

## 🔧 Advanced Usage

### Using as a module
```python
from data_loader import DataLoader
from data_analyzer import DataAnalyzer
from report_generator import ReportGenerator

# Load data
df = DataLoader.load_data('data.csv')

# Analyze
analyzer = DataAnalyzer(df)
analysis = analyzer.generate_full_analysis()

# Generate report
report = ReportGenerator(df, analysis, 'report.docx')
report.generate_report()
```

## 🐛 Troubleshooting

### Issue: Module not found errors
**Solution**: Ensure virtual environment is activated
```bash
source venv/bin/activate
```

### Issue: Unsupported file format
**Solution**: Ensure file is in one of the supported formats
Supported: CSV, JSON, XLSX, XLS, TSV, TXT

### Issue: Memory errors on large files
**Solution**: The tool should handle most datasets efficiently. For very large datasets (>1GB):
- Consider preprocessing the data
- Use data sampling if appropriate

### Issue: Matplotlib display errors
**Solution**: These are expected in non-GUI environments. Charts are saved as images in the DOCX file.

## 📊 Sample Data Format

### CSV Format
```
Name,Age,Income,Department
John,28,50000,Sales
Jane,32,65000,IT
```

### JSON Format
```json
[
  {"Name": "John", "Age": 28, "Income": 50000, "Department": "Sales"},
  {"Name": "Jane", "Age": 32, "Income": 65000, "Department": "IT"}
]
```

## 🎨 Report Customization

To customize the report:

1. Edit `report_generator.py`
2. Modify `_add_heading()`, `_add_paragraph()` for styling
3. Adjust chart properties in visualization methods
4. Change table styles via `table.style` parameter

## 📝 Performance Notes

- Processing time depends on data size:
  - Small datasets (<1MB): ~5-10 seconds
  - Medium datasets (1-50MB): ~15-30 seconds
  - Large datasets (>50MB): ~30-120 seconds

## 🤝 Contributing

To add new analysis features:

1. Add analysis method to `DataAnalyzer` class
2. Add visualization to `ReportGenerator` class
3. Update report generation to include new section

## 📄 License

This project is open source and available for educational use.

## 🎯 Future Enhancements

- [ ] Support for more formats (Parquet, HDF5)
- [ ] Machine learning insights (clustering, anomaly detection)
- [ ] Interactive HTML reports
- [ ] Time series analysis
- [ ] Custom analysis templates
- [ ] Batch processing multiple files
- [ ] PDF export option

## 📧 Support

For issues or questions, refer to the documentation or check the code comments.

---

**Version**: 1.0  
**Last Updated**: 2026-06-01  
**Python**: 3.8+
