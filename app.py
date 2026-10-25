from pathlib import Path
import streamlit as st

APP_DIR = Path(__file__).resolve().parent
HTML_FILE = APP_DIR / "index.html"

st.set_page_config(
    page_title="AAS Shimadzu AA-7000 | Virtual Lab",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Make the Streamlit shell minimal so the HTML lab gets the available width.
st.markdown(
    """
    <style>
      .stApp { background: #f8fafc; }
      .block-container { padding: 0 !important; max-width: 100% !important; }
      [data-testid="stHeader"], [data-testid="stToolbar"], footer { visibility: hidden; height: 0; }
      iframe { border: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

if not HTML_FILE.is_file():
    st.error("File index.html tidak ditemukan. Pastikan index.html berada satu folder dengan app.py.")
    st.stop()

# st.iframe can embed a local HTML file while preserving its JavaScript and WebGL.
st.iframe(HTML_FILE, width="stretch", height=900, tab_index=0)
