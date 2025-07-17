import requests
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List
import streamlit as st
from ..config.settings import get_api_config, get_timezone, get_current_datetime

class CursorAPIFetcher:
    """Class to handle Cursor API data fetching for dashboard KPIs and chart"""
    
    def __init__(self, base_url: str = None, api_key: str = None):
        api_config = get_api_config()
        self.base_url = base_url or api_config['base_url']
        self.api_key = api_key or api_config['api_key']
        self.session = requests.Session()
        
        # Use Basic Auth with API key as username and empty password
        if self.api_key:
            self.session.auth = (self.api_key, '')
        self.session.headers.update(api_config['headers'])

    def fetch_usage_data(self, start_date: str = None, end_date: str = None) -> List[Dict]:
        """Fetch usage data from Cursor Admin API for dashboard KPIs and chart"""
        try:
            # Use configured timezone from settings
            tz = get_timezone()
            # Convert dates to epoch milliseconds for Cursor API
            if not start_date:
                start_date = int((get_current_datetime() - timedelta(days=30)).timestamp() * 1000)
            else:
                start_date = int(datetime.fromisoformat(start_date.replace('Z', '+00:00')).timestamp() * 1000)
            if not end_date:
                end_date = int(get_current_datetime().timestamp() * 1000)
            else:
                end_date = int(datetime.fromisoformat(end_date.replace('Z', '+00:00')).timestamp() * 1000)
            
            payload = {
                "startDate": start_date,
                "endDate": end_date
            }
            
            response = self.session.post(
                f"{self.base_url}/teams/daily-usage-data",
                json=payload,
                timeout=30
            )
            
            response.raise_for_status()
            cursor_data = response.json()

            dashboard_data = self._convert_cursor_data_to_dashboard_format(cursor_data)
            if not dashboard_data:
                st.warning("No usage data found in API response. Check your date range and team activity.")
            return dashboard_data
        except Exception as e:
            st.error(f"Failed to fetch usage data from Cursor Admin API: {e}")
            st.info("Make sure you're using the correct API key from cursor.com/dashboard → Settings → Cursor Admin API Keys")
            return []

    def _convert_cursor_data_to_dashboard_format(self, cursor_data: Dict) -> List[Dict]:
        """Convert Cursor API data to format needed for dashboard KPIs and chart"""
        dashboard_data = []
        tz = get_timezone()
        if 'data' in cursor_data:
            for day_data in cursor_data['data']:
                # Convert timestamp from milliseconds to datetime
                date_timestamp = day_data.get('date')
                if date_timestamp:
                    # Convert from milliseconds to datetime in configured timezone
                    date_obj = datetime.fromtimestamp(date_timestamp / 1000, tz=tz)
                    date_str = date_obj.isoformat()
                else:
                    date_str = get_current_datetime().isoformat()
                
                row = {
                    'user': day_data.get('email', 'Unknown').split('@')[0].replace('.', ' ').title(),
                    'email': day_data.get('email', ''),
                    'date': date_str,
                    'totalLinesAdded': day_data.get('totalLinesAdded', 0),
                    'totalLinesDeleted': day_data.get('totalLinesDeleted', 0),
                    'acceptedLinesAdded': day_data.get('acceptedLinesAdded', 0),
                    'acceptedLinesDeleted': day_data.get('acceptedLinesDeleted', 0),
                    'totalApplies': day_data.get('totalApplies', 0),
                    'totalAccepts': day_data.get('totalAccepts', 0),
                    'totalRejects': day_data.get('totalRejects', 0),
                    'totalTabsShown': day_data.get('totalTabsShown', 0),
                    'totalTabsAccepted': day_data.get('totalTabsAccepted', 0),
                    'composerRequests': day_data.get('composerRequests', 0),
                    'chatRequests': day_data.get('chatRequests', 0),
                    'agentRequests': day_data.get('agentRequests', 0),
                    'cmdkUsages': day_data.get('cmdkUsages', 0),
                    'subscriptionIncludedReqs': day_data.get('subscriptionIncludedReqs', 0),
                    'apiKeyReqs': day_data.get('apiKeyReqs', 0),
                    'usageBasedReqs': day_data.get('usageBasedReqs', 0),
                    'bugbotUsages': day_data.get('bugbotUsages', 0),
                }
                dashboard_data.append(row)
        
        return dashboard_data

def setup_api_config():
    """Setup API configuration using environment variables"""
    api_config = get_api_config()
    
    # Check if real API is configured
    has_real_api = api_config['base_url'] and api_config['api_key']
    
    if has_real_api:
        return {
            'mode': 'real',
            'base_url': api_config['base_url'],
            'api_key': api_config['api_key']
        }
    else:
        return {
            'mode': 'mock',
            'base_url': None,
            'api_key': None
        }

def get_api_data(config: Dict) -> pd.DataFrame:
    """Get data from Cursor API for dashboard KPIs and chart"""
    if config['mode'] == 'mock':
        # Return empty DataFrame for mock mode - mock data should be in tests
        st.warning("Mock mode enabled. Configure real API credentials for actual data.")
        return pd.DataFrame()
    else:
        # Use real Cursor API
        fetcher = CursorAPIFetcher(config['base_url'], config['api_key'])
        raw_data = fetcher.fetch_usage_data()
        
        # Convert to DataFrame
        df = pd.DataFrame(raw_data)
        
        # Convert date strings to datetime
        if 'date' in df.columns:
            try:
                df['date'] = pd.to_datetime(df['date'])
            except Exception as e:
                pass
        
        return df 