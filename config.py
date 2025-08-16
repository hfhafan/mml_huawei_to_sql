# =============================================================================
# MML to DB Uploader - Configuration File
# =============================================================================
# 
# IMPORTANT: This is a template configuration file.
# Please modify the values below according to your database setup.
# 
# For security reasons, never commit actual database credentials to version control.
# Consider using environment variables or a separate .env file for production.
# =============================================================================

# Database Configuration
DB_NAME = "your_database_name"        # Replace with your database name
HOST = "your_database_host"           # Replace with your database host/IP
USER = "your_username"                # Replace with your database username
PASSWORD = "your_password"            # Replace with your database password
PORT = 3306                           # Default MySQL/MariaDB port

# Application Settings
SCRIPT_VERSION = "2.1.1"
BATCH_SIZE = 1000                     # Number of rows per batch
MAX_WORKERS = 4                       # Maximum parallel processing threads

# File Processing Settings
SUPPORTED_FILE_TYPES = [
    'LST CELL_*.txt',
    'LST PDSCHCFG_*.txt',
    'LST CELLDLPCPDSCHPA_*.txt',
    'LST SECTORSPLITCELL_*.txt',
    'LST SECTORSPLITGROUP_*.txt',
    'DSP VSWR_*.txt',
    'DSP RETSUBUNIT_*.txt'
]

# GUI Settings
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 750
THEME_COLORS = {
    'primary': '#6482AD',
    'secondary': '#7FA1C3',
    'light_beige': '#E2DAD6',
    'off_white': '#F5EDED'
}

# Logging Configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "[{timestamp}] [{level}] {message}"

# Error Handling
MAX_RETRY_ATTEMPTS = 3
ERROR_LOG_ENABLED = True
SITE_ID_REPORTING = True

# =============================================================================
# Security Notes:
# =============================================================================
# 1. Use strong, unique passwords for database access
# 2. Consider using SSL/TLS for database connections
# 3. Implement proper user authentication and authorization
# 4. Regularly update database credentials
# 5. Monitor database access logs
# =============================================================================

# Example environment variable usage (uncomment if using .env file):
# import os
# DB_NAME = os.getenv('DB_NAME', 'your_database_name')
# HOST = os.getenv('DB_HOST', 'your_database_host')
# USER = os.getenv('DB_USER', 'your_username')
# PASSWORD = os.getenv('DB_PASSWORD', 'your_password')
# PORT = int(os.getenv('DB_PORT', '3306'))
