# Cursor IDE Usage Dashboard

An interactive dashboard built with Streamlit and Plotly to track Cursor IDE usage patterns and productivity metrics for each user with API integration support.

## Features

### 📊 Interactive Dashboard
- **Real-time Analytics**: Track usage patterns, productivity scores, and feature utilization
- **User-friendly Interface**: Clean, modern design with intuitive navigation
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **API Integration**: Connect to your company's real data sources

### 📈 Comprehensive Analytics
- **Overview Metrics**: Total users, usage time, sessions, and productivity scores
- **Feature Analysis**: Detailed breakdown of feature usage with treemap visualizations
- **User Analytics**: Compare user performance and productivity across different metrics
- **Temporal Analysis**: Track usage trends over time with interactive charts
- **Usage Heatmap**: Visualize usage patterns by day and hour
- **Productivity Analysis**: Scatter plots showing productivity vs usage time

### 🔧 Key Features
- **Authentication System**: Secure login with user management
- **API Integration**: Connect to real company data sources
- **Data Export**: Export data in CSV, JSON, or Excel formats
- **Filtering & Search**: Advanced filtering options for detailed analysis
- **Insights Generation**: Automated insights and recommendations
- **Real-time Updates**: Live data updates and refresh capabilities

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Quick Setup

1. **Create a virtual environment**
   ```bash
   python -m venv cursor_env
   ```

2. **Activate the virtual environment**
   - Windows:
     ```bash
     cursor_env\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source cursor_env/bin/activate
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the dashboard**
   ```bash
   streamlit run app.py
   ```

5. **Access the dashboard**
   - Open your web browser
   - Navigate to `http://localhost:8501`
   - Login with default credentials:
     - Username: `admin`, Password: `admin123`
     - Username: `user1`, Password: `user123`

## API Integration

### Setup API Connection

1. **Start the dashboard and login**
2. **In the sidebar, configure API settings:**
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

// Users List
GET /users
Response: [{"id": "user1", "name": "Alice Johnson", "email": "alice@company.com", "role": "Developer"}]

// Usage Data
GET /usage?start_date=2024-01-01&end_date=2024-01-31
Response: [{
  "user": "Alice Johnson",
  "user_id": "user1",
  "feature": "Code Completion",
  "date": "2024-01-01T10:30:00Z",
  "usage_time_minutes": 45,
  "sessions": 1,
  "productivity_score": 0.85,
  "project": "Project-A",
  "team": "Development"
}]
```

### Data Format Requirements

**Required Fields:**
```json
{
  "user": "string",           // User's full name
  "user_id": "string",        // Unique user identifier
  "feature": "string",        // Cursor IDE feature name
  "date": "datetime",         // ISO format timestamp
  "usage_time_minutes": "integer",  // Usage time in minutes
  "sessions": "integer",      // Number of sessions
  "productivity_score": "float"     // Score between 0.0 and 1.0
}
```

**Optional Fields:**
```json
{
  "project": "string",        // Project name
  "team": "string",           // Team/department
  "role": "string"            // User role
}
```

## Dashboard Sections

### 1. Overview
- Key metrics and KPIs
- Quick insights and trends
- Summary statistics

### 2. Feature Analysis
- Feature usage breakdown
- Treemap visualization
- Session distribution

### 3. User Analytics
- User comparison charts
- Productivity analysis
- Usage patterns by user

### 4. Temporal Analysis
- Daily usage trends
- Active user tracking
- Time-based patterns

### 5. Heatmap
- Usage patterns by day and hour
- Visual heatmap representation
- Peak usage identification

### 6. Productivity
- Productivity vs usage correlation
- Performance metrics
- Improvement suggestions

### 7. Raw Data
- Filterable data table
- Export functionality
- Detailed records

### 8. API Settings
- API configuration
- Connection status
- Data quality metrics

## Configuration

### Customization
- Modify `config.py` to adjust dashboard settings
- Update color schemes and thresholds
- Add new feature categories

### Environment Configuration

1. **Create the environment file:**
   ```bash
   # Create .env file with your settings
   ```

2. **Create a `.env` file with your settings:**
   ```bash
   # API Configuration
   API_BASE_URL=https://api.company.com/v1
   API_KEY=your_api_key_here
   
   # Dashboard Configuration
   DASHBOARD_TITLE=Cursor IDE Usage Dashboard
   COMPANY_NAME=Your Company Name
   
   # Authentication (change for production)
   ADMIN_USERNAME=admin
   ADMIN_PASSWORD=admin123
   ```

3. **Available Configuration Options:**
   - **API Settings**: Base URL, API key, timeout, headers
   - **Dashboard Settings**: Title, description, refresh intervals
   - **Authentication**: Admin and default user credentials
   - **Productivity Thresholds**: Score thresholds for performance levels
   - **Visualization**: Color schemes for different chart types
   - **Performance**: Cache duration, max records, data refresh
   - **Company Settings**: Company name, logo, teams, projects
   - **Development**: Debug mode, mock data, auto-refresh settings

## Dependencies

### Core Libraries
- **Streamlit**: Web application framework
- **Plotly**: Interactive visualizations
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Requests**: HTTP library for API calls

### Additional Libraries
- **streamlit-option-menu**: Navigation menu
- **streamlit-authenticator**: User authentication
- **python-dotenv**: Environment variable management

## Troubleshooting

### Common Issues

1. **Python 3.12 Compatibility**
   ```bash
   pip install setuptools wheel
   pip install --upgrade pip
   ```

2. **Package Installation Errors**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **API Connection Issues**
   - Verify API URL and key
   - Check network connectivity
   - Test with mock API first

4. **Streamlit Not Starting**
   ```bash
   streamlit run app.py --server.port 8502
   ```

### Performance Tips
- Use `@st.cache_data` for expensive computations
- Limit data size for large datasets
- Optimize chart rendering with appropriate figure sizes

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

## Usage Examples

### Adding New Users
```python
# In app.py, modify the setup_authentication function
users = {
    'newuser': {
        'name': 'New User',
        'password': stauth.Hasher(['password123']).generate()[0]
    }
}
```

### Customizing Charts
```python
# In utils.py, modify chart functions
fig.update_layout(
    title="Custom Title",
    height=500,
    width=800
)
```

### Adding New Metrics
```python
# In utils.py, extend the create_usage_summary function
summary['new_metric'] = df['new_column'].sum()
```

## Support

For support and questions:
- Check the troubleshooting section above
- Review the API integration guide
- Test with mock API first
- Verify data format requirements

## License

This project is licensed under the MIT License.

---

**Happy Dashboarding! 🎉** 