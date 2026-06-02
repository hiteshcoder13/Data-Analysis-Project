"""
Main entry point for Data Analysis Project
"""
import sys
import argparse
from pathlib import Path
from data_loader import DataLoader
from data_analyzer import DataAnalyzer
from report_generator import ReportGenerator


def main():
    """Main function to orchestrate data analysis"""
    parser = argparse.ArgumentParser(
        description='Comprehensive Data Analysis Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python main.py data.csv output_report.docx
  python main.py data.json output_report.docx
  python main.py data.xlsx output_report.docx
  
Supported formats: CSV, JSON, XLSX, XLS, TSV, TXT
        '''
    )
    
    parser.add_argument('input_file', help='Path to input data file (CSV, JSON, XLSX, XLS, TSV, TXT)')
    parser.add_argument('output_file', nargs='?', default='data_analysis_report.docx', 
                       help='Path to output DOCX report (default: data_analysis_report.docx)')
    
    args = parser.parse_args()
    
    input_path = Path(args.input_file)
    output_path = Path(args.output_file)
    
    try:
        print(f"Loading data from: {input_path}")
        df = DataLoader.load_data(input_path)
        
        print("Validating data...")
        validation_report = DataLoader.validate_data(df)
        print(f"  - Rows: {validation_report['rows']}")
        print(f"  - Columns: {validation_report['columns']}")
        print(f"  - Duplicates: {validation_report['duplicates']}")
        print(f"  - Missing values: {sum(validation_report['missing_values'].values())}")
        
        print("Performing comprehensive analysis...")
        analyzer = DataAnalyzer(df)
        analysis = analyzer.generate_full_analysis()
        
        print("Generating report...")
        report_gen = ReportGenerator(df, analysis, str(output_path))
        report_gen.generate_report()
        
        print(f"\n✓ Analysis complete! Report saved to: {output_path}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
