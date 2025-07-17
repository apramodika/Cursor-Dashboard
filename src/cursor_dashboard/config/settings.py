import os
from datetime import datetime, timedelta
import json
from dotenv import load_dotenv
import pytz

# Load environment variables from .env file
load_dotenv('.env')

# Dashboard Configuration
DASHBOARD_CONFIG = {
    'title': os.getenv('DASHBOARD_TITLE', 'Cursor IDE Usage Dashboard'),
    'description': os.getenv('DASHBOARD_DESCRIPTION', 'Interactive dashboard to track Cursor IDE usage patterns and productivity metrics'),
    'version': '1.0.0',
    'author': 'Dashboard Team'
}

# API Configuration
API_CONFIG = {
    'base_url': os.getenv('API_BASE_URL', ''),
    'api_key': os.getenv('API_KEY', ''),
    'timeout': int(os.getenv('API_TIMEOUT', 30)),
    'headers': json.loads(os.getenv('API_HEADERS', '{"Content-Type": "application/json"}'))
}

# Feature categories for better organization
FEATURE_CATEGORIES = {
    'Core Features': ['code_editing', 'ai_assistance', 'tab_completion'],
    'AI Tools': ['chat_requests', 'agent_requests', 'composer_requests'],
    'Productivity': ['command_palette', 'bugbot'],
    'Overall': ['overall_productivity']
}

# Time periods for analysis
TIME_PERIODS = {
    'Last 7 days': 7,
    'Last 30 days': 30,
    'Last 90 days': 90,
    'Last 6 months': 180,
    'Last year': 365
}

# Productivity score thresholds
PRODUCTIVITY_THRESHOLDS = {
    'Excellent': float(os.getenv('PRODUCTIVITY_EXCELLENT', 0.9)),
    'Good': float(os.getenv('PRODUCTIVITY_GOOD', 0.7)),
    'Average': float(os.getenv('PRODUCTIVITY_AVERAGE', 0.5)),
    'Poor': float(os.getenv('PRODUCTIVITY_POOR', 0.3))
}

# Color schemes for different chart types
COLOR_SCHEMES = {
    'default': os.getenv('CHART_COLORS_DEFAULT', 'viridis'),
    'productivity': os.getenv('CHART_COLORS_PRODUCTIVITY', 'RdYlGn'),
    'usage': os.getenv('CHART_COLORS_USAGE', 'plasma'),
    'users': os.getenv('CHART_COLORS_USERS', 'Set3'),
    'features': os.getenv('CHART_COLORS_FEATURES', 'tab10')
}

# Company settings
COMPANY_SETTINGS = {
    'name': os.getenv('COMPANY_NAME', 'Your Company Name'),
    'logo_url': os.getenv('COMPANY_LOGO_URL', ''),
    'teams': os.getenv('TEAMS', 'Development,QA,Design,Product,Management').split(','),
    'projects': os.getenv('PROJECTS', 'Project-A,Project-B,Project-C,Project-D').split(',')
}

# Performance settings
PERFORMANCE_CONFIG = {
    'cache_duration': int(os.getenv('CACHE_DURATION', 300)),
    'max_records': int(os.getenv('MAX_RECORDS', 10000)),
    'data_refresh_interval': int(os.getenv('DATA_REFRESH_INTERVAL', 5)),
    'default_analysis_period': int(os.getenv('DEFAULT_ANALYSIS_PERIOD', 30))
}

# Authentication settings
AUTH_CONFIG = {
    'admin_username': os.getenv('ADMIN_USERNAME', 'admin'),
    'admin_password': os.getenv('ADMIN_PASSWORD', 'admin123'),
    'default_username': os.getenv('DEFAULT_USERNAME', 'user1'),
    'default_password': os.getenv('DEFAULT_PASSWORD', 'user123'),
    'session_timeout_days': int(os.getenv('SESSION_TIMEOUT_DAYS', 30))
}

# Development settings
DEV_CONFIG = {
    'debug_mode': os.getenv('DEBUG_MODE', 'false').lower() == 'true',
    'enable_mock_data': os.getenv('ENABLE_MOCK_DATA', 'true').lower() == 'true',
    'auto_refresh_data': os.getenv('AUTO_REFRESH_DATA', 'true').lower() == 'true',
    'show_debug_info': os.getenv('SHOW_DEBUG_INFO', 'false').lower() == 'true'
}

# Timezone Configuration
TIMEZONE_CONFIG = {
    'default_timezone': os.getenv('DEFAULT_TIMEZONE', 'Asia/Colombo'),
    'timezone_name': os.getenv('TIMEZONE_NAME', 'Sri Lanka Time'),
    'timezone_offset': os.getenv('TIMEZONE_OFFSET', '+05')
}

# Cursor features to track based on Cursor Admin API
CURSOR_FEATURES = ['code_editing', 'ai_assistance', 'tab_completion', 'chat_requests', 'agent_requests', 'composer_requests', 'command_palette', 'bugbot', 'overall_productivity']

def get_data_file_path():
    """Get the path to the data file"""
    return os.path.join(os.getcwd(), 'usage_data.json')

def get_config_file_path():
    """Get the path to the config file"""
    return os.path.join(os.getcwd(), 'dashboard_config.json')

def save_config(config_data):
    """Save configuration to file"""
    with open(get_config_file_path(), 'w') as f:
        json.dump(config_data, f, indent=2)

def load_config():
    """Load configuration from file"""
    try:
        with open(get_config_file_path(), 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return DASHBOARD_CONFIG

def get_timezone():
    """Get the configured timezone object"""
    timezone_name = TIMEZONE_CONFIG['default_timezone']
    return pytz.timezone(timezone_name)

def get_timezone_config():
    """Get timezone configuration"""
    return TIMEZONE_CONFIG

def get_current_datetime():
    """Get current datetime in configured timezone"""
    tz = get_timezone()
    return datetime.now(tz)

def get_date_range(period_days):
    """Get date range for analysis in configured timezone"""
    tz = get_timezone()
    end_date = datetime.now(tz)
    start_date = end_date - timedelta(days=period_days)
    return start_date, end_date

def format_time(minutes):
    """Format time in minutes to human readable format"""
    if minutes < 60:
        return f"{minutes} minutes"
    elif minutes < 1440:  # less than 24 hours
        hours = minutes // 60
        remaining_minutes = minutes % 60
        return f"{hours}h {remaining_minutes}m"
    else:
        days = minutes // 1440
        remaining_hours = (minutes % 1440) // 60
        return f"{days}d {remaining_hours}h"

def get_productivity_level(score):
    """Get productivity level based on score"""
    if score >= PRODUCTIVITY_THRESHOLDS['Excellent']:
        return 'Excellent'
    elif score >= PRODUCTIVITY_THRESHOLDS['Good']:
        return 'Good'
    elif score >= PRODUCTIVITY_THRESHOLDS['Average']:
        return 'Average'
    else:
        return 'Poor'

def get_api_config():
    """Get API configuration"""
    return API_CONFIG

def get_company_settings():
    """Get company settings"""
    return COMPANY_SETTINGS

def get_performance_config():
    """Get performance configuration"""
    return PERFORMANCE_CONFIG

def get_auth_config():
    """Get authentication configuration"""
    return AUTH_CONFIG

def get_dev_config():
    """Get development configuration"""
    return DEV_CONFIG

def get_cursor_features():
    """Get Cursor features to track"""
    return CURSOR_FEATURES 