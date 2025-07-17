# Cursor IDE Usage Dashboard

A simple dashboard built with Streamlit to track Cursor IDE usage patterns and developer productivity metrics.

## Features

### �� Dashboard Overview
- **KPI Cards**: Total developers, active developers, average lines per developer, and acceptance ratio
- **Developer Performance Chart**: Bar chart showing lines accepted by each developer
- **Time Range Filter**: Filter data by 7D, 1M, 3M, 6M, 1Y, or Custom
- **API Integration**: Connect to real company data sources or use mock data

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Quick Setup

1. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the dashboard**
   ```bash
   python run.py
   ```

5. **Access the dashboard**
   - Open your web browser
   - Navigate to `http://localhost:8501`

## API Integration

### Setup API Connection

1. **Start the dashboard**
2. **Configure API settings in the sidebar:**
   - Select "Real API (Production)" for company data
   - Enter your API Base URL (e.g., `https://api.company.com/v1`)
   - Enter your API Key
   - Click "Test API Connection"

### API Requirements

Your company's API should provide these endpoints:

```json
// Health Check
GET /health
Response: {"status": "healthy", "timestamp": "2024-01-01T10:00:00Z"}

// Usage Data
GET /usage?start_date=2024-01-01&end_date=2024-01-31
Response: [{
  "user": "Alice Johnson",
  "date": "2024-01-01T10:30:00Z",
  "acceptedLinesAdded": 150,
  "totalLinesAdded": 200,
  "totalApplies": 25,
  "totalAccepts": 20,
  "totalRejects": 5
}]
```

### Data Format Requirements

**Required Fields:**
```json
{
  "user": "string",           // User's full name
  "date": "datetime",         // ISO format timestamp
  "acceptedLinesAdded": "integer",  // Lines accepted by AI
  "totalLinesAdded": "integer",     // Total lines added
  "totalApplies": "integer",        // Total applies
  "totalAccepts": "integer",        // Total accepts
  "totalRejects": "integer"         // Total rejects
}
```

## Dashboard Sections

### 1. KPI Cards
- **Total Developers**: Number of unique developers
- **Active Developers**: Developers with any activity
- **Avg Lines/Dev**: Average lines accepted per active developer
- **Acceptance Ratio**: Percentage of accepted vs suggested lines

### 2. Developer Performance Chart
- Horizontal bar chart showing lines accepted by each developer
- Sorted by performance (highest to lowest)

### 3. Time Range Filter
- Filter data by different time periods
- Options: 7D, 1M, 3M, 6M, 1Y, Custom

## Project Structure

```
Cursor_Dashboard/
├── app.py                 # Main dashboard application
├── api_integration.py     # API integration functionality
├── config.py              # Configuration settings
├── utils.py               # Utility functions
├── requirements.txt       # Python dependencies
├── README.md              # Documentation
└── API_INTEGRATION_GUIDE.md  # API setup guide
``` 