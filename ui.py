import streamlit as st
import requests
from pathlib import Path
import os
import socket
import threading
import time
import uvicorn

API_HOST = os.getenv("FASTAPI_HOST", "127.0.0.1")
API_PORT = int(os.getenv("FASTAPI_PORT", "8000"))
API_BASE_URL = f"http://{API_HOST}:{API_PORT}"
DEFAULT_ANALYZE_URL = f"{API_BASE_URL}/analyze"

st.set_page_config(
    page_title="Data Analysis Profiler",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


def _is_port_open(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        return sock.connect_ex((host, port)) == 0


@st.cache_resource(show_spinner=False)
def start_fastapi_server():
    if not _is_port_open(API_HOST, API_PORT):
        config = uvicorn.Config(
            "api:app",
            host=API_HOST,
            port=API_PORT,
            log_level="warning",
            reload=False,
        )
        server = uvicorn.Server(config)
        thread = threading.Thread(target=server.run, daemon=True)
        thread.start()

    health_url = f"{API_BASE_URL}/health"
    for _ in range(30):
        try:
            response = requests.get(health_url, timeout=1)
            if response.status_code == 200:
                return True
        except requests.RequestException:
            time.sleep(0.2)

    return _is_port_open(API_HOST, API_PORT)


api_ready = start_fastapi_server()

# Custom premium styling via markdown
st.markdown("""
<style>
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.5rem 2rem !important;
        border-radius: 5px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover {
        opacity: 0.9 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">📊 Data Analysis Profiler</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload your dataset, perform statistical analysis, and generate professional DOCX reports instantly.</p>', unsafe_allow_html=True)

# Sidebar settings
st.sidebar.header("⚙️ Configuration")
api_url = st.sidebar.text_input(
    "FastAPI End-Point URL",
    value=DEFAULT_ANALYZE_URL,
    help="The API starts automatically with this Streamlit app."
)

if api_ready:
    st.sidebar.success("FastAPI server is running.")
else:
    st.sidebar.warning("FastAPI server is still starting or unavailable.")

st.sidebar.markdown("""
---
### Supported Formats:
- **CSV** (`.csv`)
- **JSON** (`.json`)
- **Excel** (`.xlsx`, `.xls`)
- **TSV** (`.tsv`)
- **Text** (`.txt`)
""")

# Main UI
uploaded_file = st.file_uploader(
    "Choose a data file to analyze",
    type=["csv", "json", "xlsx", "xls", "tsv", "txt"],
    help="Upload any of the supported formats to begin analysis."
)

if uploaded_file is not None:
    # Show file details
    file_details = {
        "Filename": uploaded_file.name,
        "File size": f"{uploaded_file.size / 1024:.2f} KB"
    }
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("📁 **File Details**")
        st.json(file_details)
        
    with col2:
        st.write("⚡ **Action**")
        analyze_btn = st.button("Start Comprehensive Analysis")

    if analyze_btn:
        with st.spinner("Uploading data and generating report. Please wait..."):
            try:
                # Prepare file for multipart upload
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                
                # Make POST request to FastAPI
                response = requests.post(api_url, files=files)
                
                if response.status_code == 200:
                    st.success("🎉 Analysis complete! Report generated successfully.")
                    
                    # Store file in memory to download
                    report_bytes = response.content
                    report_name = f"{Path(uploaded_file.name).stem}_analysis_report.docx"
                    
                    # UI feedback and download button
                    st.balloons()
                    
                    st.download_button(
                        label="📥 Download Generated DOCX Report",
                        data=report_bytes,
                        file_name=report_name,
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
                else:
                    try:
                        error_detail = response.json().get("detail", response.text)
                    except Exception:
                        error_detail = response.text
                    st.error(f"❌ API Error ({response.status_code}): {error_detail}")
                    
            except requests.exceptions.ConnectionError:
                st.error("❌ Could not connect to the FastAPI server. It should start automatically with Streamlit; please refresh once or check the endpoint URL.")
            except Exception as e:
                st.error(f"❌ An unexpected error occurred: {e}")
