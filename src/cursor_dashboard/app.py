import streamlit as st
import pandas as pd
from .api.integration import setup_api_config, get_api_data
from .config.settings import DASHBOARD_CONFIG
from .utils.ui_utils import load_css, create_header
from .utils.data_processing import calculate_kpis, filter_data_by_date, prepare_chart_data
from .components.kpi_cards import display_kpi_cards
from .components.charts import create_lines_accepted_chart

# Page configuration
st.set_page_config(
    page_title=DASHBOARD_CONFIG['title'],
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# Load CSS styles
load_css()

# Initialize session state
if 'api_config' not in st.session_state:
    st.session_state.api_config = None

# Load data based on source
@st.cache_data
def load_data():
    """Load data from the configured source"""
    try:
        # Check if API config exists and use real API if configured
        if st.session_state.api_config and st.session_state.api_config.get('mode') == 'real':
            return get_api_data(st.session_state.api_config)
        else:
            return get_api_data({'mode': 'mock'})
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return get_api_data({'mode': 'mock'})



def show_dashboard(df):
    """Display simplified dashboard with only specified features"""
    if df.empty:
        st.error("No data available for analysis.")
        return
    

    
    # Calculate KPIs using modular function
    kpis = calculate_kpis(df)
    
    # Display KPI cards using modular component
    display_kpi_cards(
        kpis['total_developers'],
        kpis['active_developers'],
        kpis['avg_lines_per_dev'],
        kpis['acceptance_ratio']
    )
    
    # Chart: Number of lines accepted by user
    st.markdown("<div style='margin: 2rem 0 1rem 0;'></div>", unsafe_allow_html=True)
    st.markdown("### 📈 Lines Accepted by Developer")
    
    # Prepare chart data using modular function
    chart_data = prepare_chart_data(df)
    
    # Create chart using modular component
    create_lines_accepted_chart(chart_data)

# Main app
def main():
    # Setup API configuration
    st.session_state.api_config = setup_api_config()
    
    # Load data
    df = load_data()
    
    # Header and date filter
    date_option = None
    if 'date' in df.columns:
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            create_header()
        
        with col2:
            st.markdown("")  # Spacer
        
        with col3:
            date_option = st.selectbox(
                '📅 Time Range',
                ['7D', '1M', '3M', '6M', '1Y', 'Custom'],
                index=0,  # Default to '7D'
                label_visibility="collapsed"
            )
    else:
        create_header()
    
    # Apply date filtering using modular function
    df = filter_data_by_date(df, date_option)
    
    # Main dashboard content
    show_dashboard(df)
        


if __name__ == "__main__":
    main() 