import streamlit as st
import plotly.express as px

def create_lines_accepted_chart(chart_data):
    """Create the lines accepted by developer chart"""
    if chart_data.empty:
        st.warning("No data available for chart.")
        return
    
    fig = px.bar(
        data_frame=chart_data,
        x='Lines_Accepted',
        y='Developer',
        orientation='h',
        labels={'Lines_Accepted': 'Lines Accepted', 'Developer': 'Developer'},
        color_discrete_sequence=['#1f77b4']
    )
    
    fig.update_layout(
        height=300,
        xaxis_title="Lines Accepted",
        yaxis_title="Developer",
        font=dict(size=12),
        plot_bgcolor='#f8f9fa',
        paper_bgcolor='#f8f9fa',
        margin=dict(l=20, r=20, t=30, b=20),
        showlegend=False
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(
        showgrid=False,
        tickangle=0,
        tickfont=dict(size=11)
    )
    
    st.plotly_chart(fig, use_container_width=True) 