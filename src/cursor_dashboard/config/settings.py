import os
from datetime import datetime, timedelta
import json
from dotenv import load_dotenv
import pytz

# Load environment variables from .env file
load_dotenv('.env')

# Dashboard Configuration
DASHBOARD_CONFIG = {
    'title': os.getenv('DASHBOARD_TITLE', "Arcadea Group - Cursor Analytics"),
    'description': os.getenv('DASHBOARD_DESCRIPTION', f'Interactive dashboard to track Cursor IDE usage patterns and productivity metrics for {os.getenv("COMPANY_NAME", "Arcadea Group")}'),
    'version': '1.0.0',
    'author': 'AI Team'
}

# API Configuration
API_CONFIG = {
    'base_url': os.getenv('API_BASE_URL', ''),
    'api_key': os.getenv('API_KEY', ''),
    'timeout': int(os.getenv('API_TIMEOUT', 30)),
    'headers': json.loads(os.getenv('API_HEADERS', '{"Content-Type": "application/json"}'))
}

# Development settings
DEV_CONFIG = {
    'debug_mode': os.getenv('DEBUG_MODE', 'false').lower() == 'true',
    'enable_mock_data': os.getenv('ENABLE_MOCK_DATA', 'false').lower() == 'true',
    'auto_refresh_data': os.getenv('AUTO_REFRESH_DATA', 'true').lower() == 'true',
    'show_debug_info': os.getenv('SHOW_DEBUG_INFO', 'false').lower() == 'true'
}

# Timezone Configuration
TIMEZONE_CONFIG = {
    'default_timezone': os.getenv('DEFAULT_TIMEZONE', 'Asia/Colombo')
}

def get_timezone():
    """Get the configured timezone object"""
    timezone_name = TIMEZONE_CONFIG['default_timezone']
    return pytz.timezone(timezone_name)

def get_current_datetime():
    """Get current datetime in configured timezone"""
    tz = get_timezone()
    return datetime.now(tz)

def get_api_config():
    """Get API configuration"""
    return API_CONFIG

def get_company_settings():
    """Get company settings"""
    return COMPANY_SETTINGS

def get_dev_config():
    """Get development configuration"""
    return DEV_CONFIG 