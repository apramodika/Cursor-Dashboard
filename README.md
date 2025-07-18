# Cursor IDE Usage Dashboard

A Streamlit dashboard to track Cursor IDE usage patterns and developer productivity metrics.

## Features

- **KPI Cards**: Total developers, active developers, average lines per developer, acceptance ratio
- **Developer Performance Chart**: Lines accepted by each developer
- **Time Range Filter**: 7D, 1M, 3M, 6M, 1Y, Custom
- **Real-time Data**: Connect to Cursor Admin API

## Quick Start

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the dashboard**
   ```bash
   streamlit run run.py
   ```

3. **Access dashboard**
   - Open browser to `http://localhost:8501`

## Configuration

### Environment Variables

Copy `env.sample` to `.env` and configure:

```bash
# Company Settings
DASHBOARD_TITLE=Your Company - Cursor Analytics

# API Configuration (Optional)
API_BASE_URL=https://api.cursor.com
API_KEY=your_cursor_api_key
```

### Getting Cursor API Key

1. **Go to Cursor Dashboard**
   - Visit [cursor.com/dashboard](https://cursor.com/dashboard)
   - Sign in to your account

2. **Navigate to Settings**
   - Click on "Settings" in the sidebar
   - Look for "Cursor Admin API Keys"

3. **Generate API Key**
   - Click "Generate New Key"
   - Copy the generated API key
   - Add it to your `.env` file as `API_KEY`

4. **API Base URL**
   - Use `https://api.cursor.com` as the base URL
   - Add it to your `.env` file as `API_BASE_URL`

## Project Structure

```
src/cursor_dashboard/
├── app.py                 # Main dashboard
├── api/integration.py     # API integration
├── config/settings.py     # Configuration
├── components/            # UI components
├── utils/                 # Utilities
└── static/css/           # Styles
``` 