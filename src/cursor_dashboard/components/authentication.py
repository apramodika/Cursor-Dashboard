"""
Authentication components for the Cursor Dashboard.
"""
import streamlit as st
import streamlit_authenticator as stauth
from ..config.settings import AUTH_CONFIG

def setup_authentication():
    """Setup authentication system"""
    credentials = {
        'usernames': {
            AUTH_CONFIG['admin_username']: {
                'name': 'Admin User',
                'password': stauth.Hasher([AUTH_CONFIG['admin_password']]).generate()[0]
            },
            AUTH_CONFIG['default_username']: {
                'name': 'AI Team User',
                'password': stauth.Hasher([AUTH_CONFIG['default_password']]).generate()[0]
            }
        }
    }
    
    authenticator = stauth.Authenticate(
        credentials,
        'cursor_dashboard',
        'auth_key',
        cookie_expiry_days=AUTH_CONFIG['session_timeout_days']
    )
    
    return authenticator

def show_login_page():
    """Display login page"""
    authenticator = setup_authentication()
    name, authentication_status, username = authenticator.login('Login', 'main')
    
    if authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')
    elif authentication_status:
        st.session_state.authenticated = True
        st.session_state.current_user = username
        return True
    
    return False
