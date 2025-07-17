import streamlit as st
import os

def load_css():
    """Load CSS styles from external file"""
    css_file_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'css', 'styles.css')
    
    try:
        with open(css_file_path, 'r') as f:
            css_content = f.read()
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        # Fallback to inline CSS if file doesn't exist
        st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
            width: 100vw !important;
            max-width: 100vw !important;
        }
        .main .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            max-width: 100% !important;
            width: 100% !important;
            margin: 0 !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }
        </style>
        """, unsafe_allow_html=True)

def create_header(title="🚀 Cursor Analytics"):
    """Create the dashboard header"""
    st.markdown(f'<h1 style="text-align: left; color: #2E86AB; margin-bottom: 1rem; font-size: 2rem; font-weight: 700;">{title}</h1>', unsafe_allow_html=True) 