import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from ..config.settings import get_timezone, get_current_datetime

def calculate_kpis(df):
    """Calculate all KPI metrics from the dataframe"""
    if df.empty:
        return {
            'total_developers': 0,
            'active_developers': 0,
            'avg_lines_per_dev': 0,
            'acceptance_ratio': 0
        }
    
    # Calculate total developers
    total_developers = df['user'].nunique()
    
    # Check if this is Cursor API data (has acceptedLinesAdded) or mock data (has usage_time_minutes)
    if 'acceptedLinesAdded' in df.columns:
        # Cursor API data format
        activity_columns = ['totalLinesAdded', 'totalLinesDeleted', 'acceptedLinesAdded', 'acceptedLinesDeleted',
                           'totalApplies', 'totalAccepts', 'totalRejects', 'totalTabsShown', 'totalTabsAccepted',
                           'composerRequests', 'chatRequests', 'agentRequests', 'cmdkUsages']
        
        available_activity_cols = [col for col in activity_columns if col in df.columns]
        
        if available_activity_cols:
            activity_condition = df[available_activity_cols].sum(axis=1) > 0
            active_developers = df[activity_condition]['user'].nunique()
        else:
            active_developers = df[df['acceptedLinesAdded'] > 0]['user'].nunique()
        
        total_accepted_lines = df['acceptedLinesAdded'].sum()
        avg_lines_per_dev = total_accepted_lines / active_developers if active_developers > 0 else 0
        total_suggested_lines = df['totalLinesAdded'].sum()
        acceptance_ratio = (total_accepted_lines / total_suggested_lines * 100) if total_suggested_lines > 0 else 0
        
    else:
        # Mock data format - use usage metrics instead
        active_developers = df[df['usage_time_minutes'] > 0]['user'].nunique()
        
        # For mock data, simulate lines metrics based on usage
        total_usage_minutes = df['usage_time_minutes'].sum()
        avg_lines_per_dev = int(total_usage_minutes / active_developers * 10) if active_developers > 0 else 0  # Simulate lines based on usage
        acceptance_ratio = 75.0  # Simulate acceptance ratio
    
    return {
        'total_developers': total_developers,
        'active_developers': active_developers,
        'avg_lines_per_dev': avg_lines_per_dev,
        'acceptance_ratio': acceptance_ratio
    }

def filter_data_by_date(df, date_option):
    """Filter dataframe by date range using configured timezone"""
    if 'date' not in df.columns or not date_option:
        return df
    
    # Use configured timezone from settings
    tz = get_timezone()
    now = get_current_datetime()
    
    date_ranges = {
        '7D': 7,
        '1M': 30,
        '3M': 90,
        '6M': 180,
        '1Y': 365
    }
    
    if date_option in date_ranges:
        start_date = now - timedelta(days=date_ranges[date_option])
        end_date = now
    else:
        # Custom date range - return original df for now
        return df
    
    # Convert date column to datetime and localize to configured timezone
    df['date'] = pd.to_datetime(df['date'])
    
    # If dates don't have timezone info, assume they're in configured timezone
    if df['date'].dt.tz is None:
        df['date'] = df['date'].dt.tz_localize(tz)
    
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    
    # If no data found for the selected range, return the original data
    # This ensures we always show something rather than empty dashboard
    if filtered_df.empty and not df.empty:
        return df
    
    return filtered_df

def prepare_chart_data(df):
    """Prepare data for the lines accepted chart"""
    if df.empty:
        return pd.DataFrame()
    
    if 'acceptedLinesAdded' in df.columns:
        # Cursor API data format
        user_accepted_lines = df.groupby('user')['acceptedLinesAdded'].sum().sort_values(ascending=False)
        
        return pd.DataFrame({
            'Developer': user_accepted_lines.index,
            'Lines_Accepted': user_accepted_lines.values
        })
    else:
        # Mock data format - simulate lines based on usage
        user_usage = df.groupby('user')['usage_time_minutes'].sum().sort_values(ascending=False)
        
        return pd.DataFrame({
            'Developer': user_usage.index,
            'Lines_Accepted': (user_usage.values * 10).astype(int)  # Simulate lines based on usage
        }) 