# Data Analysis Project - Quick Start Guide

## 🚀 Getting Started in 5 Minutes

### Step 1: Activate Virtual Environment
```bash
cd /home/Unthinkable/Documents/Data-analysis-Project
source venv/bin/activate
```

### Step 2: Run Analysis on Sample Data
```bash
# Analyze CSV file
python main.py sample_data.csv my_csv_report.docx

# Analyze JSON file
python main.py sample_data.json my_json_report.docx
```

### Step 3: Open Generated Report
Open the generated `.docx` file in:
- Microsoft Word
- Google Docs
- LibreOffice Writer
- Any modern document editor

## 📚 Understanding Your Report

### What Each Section Tells You

**Executive Summary**
- Quick statistics about your dataset
- Row/column counts, data types, duplicates

**Data Overview**
- All column names and their data types
- Reference for what variables you're working with

**Missing Data Analysis**
- Where data is incomplete
- Percentage of missing values
- Visualization showing which columns have missing data
- **Action**: Consider imputation or exclusion of columns with >30% missing

**Numeric Statistics**
- Mean, median, standard deviation for numeric columns
- Quartiles and ranges
- **Action**: Use these to understand data spread and central tendency

**Distribution Analysis**
- Whether data follows normal distribution
- Skewness (is data leaning left or right?)
- Kurtosis (are there extreme values?)
- **Example**: If skewness > 1, consider log transformation

**Categorical Analysis**
- Unique values in text/category columns
- Most common value (mode)
- **Action**: Review for data quality issues

**Outlier Detection**
- Values that don't fit the pattern
- Count and percentage of outliers
- **Action**: Investigate causes or decide on treatment

**Class Balance Analysis**
- For target variables in classification
- Whether classes are fairly represented
- Imbalance ratio tells how skewed it is
- **Example**: Imbalance ratio 1.2 means fairly balanced; 10+ means highly imbalanced

**Correlation Analysis**
- How strongly numeric variables relate
- Values >0.7 or <-0.7 show strong relationships
- **Action**: Remove highly correlated features to reduce multicollinearity

**Visualizations**
- Distribution plots (histograms + box plots)
- Categorical bar charts
- Correlation heatmap
- Missing data patterns

## 🎯 Common Use Cases

### Use Case 1: Understanding a Dataset Before ML
```bash
python main.py your_data.csv eda_report.docx
```
Check for:
- Missing values to decide imputation strategy
- Class imbalance in target variable
- Outliers that might need treatment
- Skewness suggesting need for transformation

### Use Case 2: Data Quality Assessment
```bash
python main.py dataset.csv quality_report.docx
```
Look for:
- Missing data patterns (>20% is concerning)
- Duplicate rows
- Suspicious outliers
- Inconsistent categories

### Use Case 3: Feature Engineering Insights
```bash
python main.py features.csv features_report.docx
```
Review:
- Correlations between features
- Skewness needing transformation
- Categorical features for encoding strategy
- Numeric features needing scaling

## 📊 Data Format Examples

### CSV Format
```
Name,Age,Salary,Department
John,28,50000,Sales
Jane,32,65000,IT
Bob,45,75000,Management
```

### JSON Format
```json
[
  {"Name": "John", "Age": 28, "Salary": 50000, "Department": "Sales"},
  {"Name": "Jane", "Age": 32, "Salary": 65000, "Department": "IT"},
  {"Name": "Bob", "Age": 45, "Salary": 75000, "Department": "Management"}
]
```

### Excel (XLSX/XLS)
Open Excel → Create columns with headers → Save as .xlsx

## ⚙️ Customizing Your Analysis

### Edit Analysis Parameters
Edit `data_analyzer.py` to change:
- Outlier detection sensitivity (line with `1.5 * IQR`)
- Class balance threshold (default: 30%)
- Normality significance level (default: 0.05)

### Add Custom Visualizations
Edit `report_generator.py` to add:
- Scatter plots
- Time series plots
- Custom charts

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| "module not found" | Activate venv: `source venv/bin/activate` |
| "file not found" | Check file path and extension |
| "unsupported format" | Use CSV, JSON, XLSX, XLS, TSV, or TXT |
| Large file slow? | Normal. >100MB may take 1-2 minutes |
| Report is small file? | Normal. Depends on data size |

## 📈 Interpreting Key Metrics

### Skewness
- `-0.5 to 0.5`: Fairly symmetric ✓
- `0.5 to 1`: Moderately right-skewed
- `> 1`: Highly right-skewed
- `< -1`: Highly left-skewed

### Coefficient of Variation (CV)
- `< 15%`: Low variability (consistent)
- `15-30%`: Moderate variability
- `> 30%`: High variability (diverse)

### Imbalance Ratio
- `1.0`: Perfect balance
- `1-3`: Well balanced
- `3-10`: Moderately imbalanced
- `> 10`: Highly imbalanced

### Correlation
- `0.0 to 0.3`: Weak correlation
- `0.3 to 0.7`: Moderate correlation
- `0.7 to 1.0`: Strong correlation
- `1.0`: Perfect correlation (same variable)

## 💡 Pro Tips

1. **Always check for missing data first** - Plan your imputation strategy
2. **Review outliers carefully** - Could be data quality issues or legitimate extremes
3. **Check class balance early** - Highly imbalanced data needs special treatment
4. **Transform skewed data** - Log or power transformations can help
5. **Remove highly correlated features** - Keep model simpler and faster
6. **Validate findings** - Visualizations confirm statistical findings

## 🎓 Next Steps

After analyzing your data:
1. Clean data based on findings
2. Handle missing values
3. Remove/treat outliers
4. Balance classes if needed
5. Transform skewed variables
6. Scale numeric features
7. Encode categorical variables
8. Build your model!

## 📞 Need Help?

1. Check this guide first
2. Review code comments in Python files
3. Refer to detailed README.md
4. Check data format examples

---

**Happy Analyzing!** 📊✨
