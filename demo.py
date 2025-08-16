#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo Script for MML to DB Uploader
Demonstrates the application functionality without requiring actual database connection

Author: Hadi Fauzan Hanif
Version: 2.1.1
"""

import tkinter as tk
from core.gui import MMLUploaderGUI
from core.auth import AuthenticationManager
from core.database import DatabaseManager

def main():
    """Demo main function"""
    print("🚀 Starting MML to DB Uploader Demo...")
    print("📋 This is a demonstration version with simulated functionality")
    print("🔒 No actual database connection required")
    print("=" * 50)
    
    try:
        # Create root window
        root = tk.Tk()
        
        # Initialize managers (simulated)
        auth_manager = AuthenticationManager()
        db_manager = DatabaseManager()
        
        # Simulate authentication (accept any credentials for demo)
        auth_manager.authenticate_user("demo_user", "demo_password")
        
        # Create and run GUI
        app = MMLUploaderGUI(root, auth_manager, db_manager)
        
        print("✅ Application started successfully!")
        print("💡 Features available in demo mode:")
        print("   • File folder selection")
        print("   • Simulated file detection")
        print("   • Simulated upload process")
        print("   • Professional GUI interface")
        print("   • About tab with scrolling")
        print("   • Donation button (opens Saweria)")
        print("\n🎯 Try selecting a folder and starting the upload process!")
        
        # Start GUI main loop
        root.mainloop()
        
    except Exception as e:
        print(f"❌ Demo failed to start: {e}")
        print("💡 Make sure all required modules are present")

if __name__ == "__main__":
    main()
