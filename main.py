#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MML to DB Uploader - Main Application Entry Point
Advanced MML (Man Machine Language) Processing Suite

Author: Hadi Fauzan Hanif
Email: hadifauzanhanif@gmail.com
Version: 2.1.1
License: MIT

This application processes Huawei MML files and uploads them to database systems
with advanced batch processing capabilities and a modern GUI interface.
"""

import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

# Add project root to path
sys.path.append(os.path.dirname(__file__))

# Import configuration
try:
    from config import *
except ImportError:
    print("Error: config.py not found. Please create config.py with your database settings.")
    sys.exit(1)

# Import core modules
try:
    from core.gui import MMLUploaderGUI
    from core.auth import AuthenticationManager
    from core.database import DatabaseManager
except ImportError:
    print("Error: Core modules not found. Please ensure all required files are present.")
    sys.exit(1)

def show_about():
    """Show application information"""
    about_text = f"""
MML to DB Uploader v{SCRIPT_VERSION}

Advanced MML Processing Suite for Database Uploads

Developer: Hadi Fauzan Hanif
Email: hadifauzanhanif@gmail.com
WhatsApp: +62 813-5719-8294

Features:
• LST CELL file processing and enrichment
• VSWR and RET data upload
• Batch processing with error handling
• Professional GUI with modern design
• Parallel processing for high performance
• Database compatibility (MariaDB/MySQL)

For support and donations:
https://saweria.co/HDfauzan

© 2025 Hadi Fauzan Hanif. All rights reserved.
    """
    
    messagebox.showinfo("About MML to DB Uploader", about_text.strip())

def open_donation():
    """Open donation page"""
    webbrowser.open("https://saweria.co/HDfauzan")

def main():
    """Main application entry point"""
    try:
        # Initialize authentication
        auth_manager = AuthenticationManager()
        
        # Check if user is authenticated
        if not auth_manager.is_authenticated():
            messagebox.showerror("Authentication Required", 
                               "Please authenticate to continue.\n\n"
                               "Contact administrator for access credentials.")
            return
        
        # Initialize database connection
        db_manager = DatabaseManager()
        if not db_manager.test_connection():
            messagebox.showerror("Database Connection Failed", 
                               "Unable to connect to database.\n\n"
                               "Please check your configuration in config.py")
            return
        
        # Create and run GUI
        root = tk.Tk()
        app = MMLUploaderGUI(root, auth_manager, db_manager)
        root.mainloop()
        
    except Exception as e:
        error_msg = f"Application startup failed: {str(e)}"
        print(error_msg)
        messagebox.showerror("Startup Error", error_msg)
        sys.exit(1)

if __name__ == "__main__":
    # Set application properties
    if hasattr(sys, 'frozen'):
        # Running as compiled executable
        application_path = sys._MEIPASS
    else:
        # Running as script
        application_path = os.path.dirname(os.path.abspath(__file__))
    
    # Change to application directory
    os.chdir(application_path)
    
    # Start application
    main()
