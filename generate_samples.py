#!/usr/bin/env python3
"""
Script to generate sample datasets in different formats for testing
"""
import csv
import json
import pandas as pd
from pathlib import Path


def create_sample_csv():
    """Create sample CSV file"""
    data = [
        ['Product_ID', 'Sales_Amount', 'Units_Sold', 'Customer_Segment', 'Region', 'Profit'],
        [1, 15000, 100, 'Premium', 'North', 3500],
        [2, 22000, 150, 'Standard', 'South', 5200],
        [3, 18500, 120, 'Premium', 'East', 4100],
        [4, 25000, 180, 'Standard', 'West', 6200],
        [5, 16200, 110, 'Budget', 'North', 3800],
        [6, 23500, 160, 'Premium', 'South', 5600],
        [7, 20100, 135, 'Standard', 'East', 4700],
        [8, 26200, 190, 'Standard', 'West', 6500],
        [9, 14800, 95, 'Budget', 'North', 3200],
        [10, 21500, 145, 'Premium', 'South', 5100],
    ]
    
    with open('sample_sales_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    
    print("✓ Created sample_sales_data.csv")


def create_sample_json():
    """Create sample JSON file with more diverse data"""
    data = [
        {'Employee_ID': 1, 'Age': 28, 'Salary': 52000, 'Department': 'Sales', 'Experience': 3, 'Performance': 'Good'},
        {'Employee_ID': 2, 'Age': 35, 'Salary': 68000, 'Department': 'IT', 'Experience': 8, 'Performance': 'Excellent'},
        {'Employee_ID': 3, 'Age': 32, 'Salary': 65000, 'Department': 'HR', 'Experience': 6, 'Performance': 'Good'},
        {'Employee_ID': 4, 'Age': 29, 'Salary': 55000, 'Department': 'Sales', 'Experience': 4, 'Performance': 'Average'},
        {'Employee_ID': 5, 'Age': 41, 'Salary': 78000, 'Department': 'Management', 'Experience': 15, 'Performance': 'Excellent'},
        {'Employee_ID': 6, 'Age': 26, 'Salary': 48000, 'Department': 'IT', 'Experience': 1, 'Performance': 'Good'},
        {'Employee_ID': 7, 'Age': 38, 'Salary': 72000, 'Department': 'Sales', 'Experience': 12, 'Performance': 'Excellent'},
        {'Employee_ID': 8, 'Age': 31, 'Salary': 60000, 'Department': 'HR', 'Experience': 5, 'Performance': 'Good'},
    ]
    
    with open('sample_employee_data.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print("✓ Created sample_employee_data.json")


def create_sample_xlsx():
    """Create sample XLSX file"""
    data = {
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Website_Visits': [45000, 52000, 48500, 61000, 58500, 67000],
        'Conversion_Rate': [2.1, 2.3, 2.0, 2.8, 2.6, 3.1],
        'Avg_Session_Duration': [3.2, 3.5, 3.1, 3.8, 3.6, 4.1],
        'Bounce_Rate': [45, 43, 46, 38, 41, 35],
    }
    
    df = pd.DataFrame(data)
    df.to_excel('sample_website_data.xlsx', index=False)
    print("✓ Created sample_website_data.xlsx")


def main():
    """Generate all sample files"""
    print("Generating sample datasets...\n")
    
    try:
        create_sample_csv()
        create_sample_json()
        create_sample_xlsx()
        
        print("\n" + "="*50)
        print("Sample files created successfully!")
        print("="*50)
        print("\nYou can now test with these files:")
        print("\n  python main.py sample_sales_data.csv sales_report.docx")
        print("  python main.py sample_employee_data.json employee_report.docx")
        print("  python main.py sample_website_data.xlsx website_report.docx")
        print("\n")
        
    except Exception as e:
        print(f"Error creating sample files: {e}")


if __name__ == '__main__':
    main()
