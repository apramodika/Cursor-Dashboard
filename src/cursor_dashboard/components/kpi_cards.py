import streamlit as st

def create_kpi_card(title, value, description, gradient_colors, icon):
    """Create a KPI card with consistent styling"""
    return f"""
    <div style="
        background: linear-gradient(135deg, {gradient_colors});
        padding: 0.6rem;
        border-radius: 12px;
        text-align: center;
        color: white;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
        min-height: 90px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        margin: 0.1rem 0;
    ">
        <h3 style="margin: 0; font-size: 1.3rem; font-weight: 600;">{icon} {title}</h3>
        <h2 style="margin: 0.3rem 0; font-size: 2.6rem; font-weight: 700;">{value}</h2>
        <p style="margin: 0; font-size: 1rem; opacity: 0.9;">{description}</p>
    </div>
    """

def display_kpi_cards(total_developers, active_developers, avg_lines_per_dev, acceptance_ratio):
    """Display all KPI cards in a 4-column layout"""
    col1, col2, col3, col4 = st.columns(4)
    
    # KPI card configurations
    kpi_configs = [
        {
            'title': 'Total Developers',
            'value': total_developers,
            'description': 'Unique developers',
            'gradient_colors': '#667eea 0%, #764ba2 100%',
            'icon': '👥'
        },
        {
            'title': 'Active Developers',
            'value': active_developers,
            'description': 'With any activity',
            'gradient_colors': '#f093fb 0%, #f5576c 100%',
            'icon': '🚀'
        },
        {
            'title': 'Avg Lines/Dev',
            'value': f"{avg_lines_per_dev:.0f}",
            'description': 'Per active developer',
            'gradient_colors': '#4facfe 0%, #00f2fe 100%',
            'icon': '📊'
        },
        {
            'title': 'Acceptance Ratio',
            'value': f"{acceptance_ratio:.1f}%",
            'description': 'Accepted/Suggested',
            'gradient_colors': '#43e97b 0%, #38f9d7 100%',
            'icon': '✅'
        }
    ]
    
    # Display KPI cards
    with col1:
        st.markdown(create_kpi_card(**kpi_configs[0]), unsafe_allow_html=True)
    
    with col2:
        st.markdown(create_kpi_card(**kpi_configs[1]), unsafe_allow_html=True)
    
    with col3:
        st.markdown(create_kpi_card(**kpi_configs[2]), unsafe_allow_html=True)
    
    with col4:
        st.markdown(create_kpi_card(**kpi_configs[3]), unsafe_allow_html=True) 