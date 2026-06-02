import os
import uuid
import shutil
from pathlib import Path
from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse

from data_loader import DataLoader
from data_analyzer import DataAnalyzer
from report_generator import ReportGenerator

app = FastAPI(
    title="Data Analysis API",
    description="API to upload files and generate comprehensive data analysis reports in DOCX format.",
    version="1.0.0"
)

TEMP_DIR = Path(__file__).parent / "temp"
TEMP_DIR.mkdir(exist_ok=True)


@app.get("/health", summary="Health check")
async def health_check():
    return {"status": "ok"}


def cleanup_files(paths: list[Path]):
    """Background task to delete temporary files after response is sent"""
    for path in paths:
        try:
            if path.exists():
                path.unlink()
        except Exception as e:
            print(f"Error deleting temp file {path}: {e}")


@app.post("/analyze", summary="Upload file and get data analysis DOCX report")
async def analyze_data(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...)
):
    # Validate file extension
    file_ext = Path(file.filename).suffix.lower()
    if file_ext not in DataLoader.SUPPORTED_FORMATS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file format: {file_ext}. Supported formats: {list(DataLoader.SUPPORTED_FORMATS.keys())}"
        )
    
    # Create unique filenames for this request
    request_id = str(uuid.uuid4())
    temp_input_path = TEMP_DIR / f"{request_id}{file_ext}"
    temp_output_path = TEMP_DIR / f"{request_id}_report.docx"
    
    try:
        # Save uploaded file to temp path
        with temp_input_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # Run loading
        df = DataLoader.load_data(temp_input_path)
        
        # Run validation / profiling
        DataLoader.validate_data(df)
        
        # Perform analysis
        analyzer = DataAnalyzer(df)
        analysis = analyzer.generate_full_analysis()
        
        # Generate report
        report_gen = ReportGenerator(df, analysis, str(temp_output_path))
        report_gen.generate_report()
        
        # Schedule cleanup of temp files in background
        background_tasks.add_task(cleanup_files, [temp_input_path, temp_output_path])
        
        # Return generated document
        original_filename = Path(file.filename).stem
        return FileResponse(
            path=temp_output_path,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            filename=f"{original_filename}_analysis_report.docx"
        )
        
    except Exception as e:
        # If error occurs, clean up immediately
        cleanup_files([temp_input_path, temp_output_path])
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")
