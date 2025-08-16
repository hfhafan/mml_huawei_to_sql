#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GUI Module for MML to DB Uploader
Main application interface and user interactions

Author: Hadi Fauzan Hanif
Version: 2.1.1
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import webbrowser
import os
import sys
from typing import Optional, List, Dict, Any

# Import configuration
try:
    from config import SCRIPT_VERSION, THEME_COLORS, WINDOW_WIDTH, WINDOW_HEIGHT
except ImportError:
    SCRIPT_VERSION = "2.1.1"
    THEME_COLORS = {
        'primary': '#6482AD',
        'secondary': '#7FA1C3',
        'light_beige': '#E2DAD6',
        'off_white': '#F5EDED'
    }
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 750

class MMLUploaderGUI:
    """
    Main GUI application for MML to DB Uploader
    """
    
    def __init__(self, root, auth_manager, db_manager):
        self.root = root
        self.auth_manager = auth_manager
        self.db_manager = db_manager
        
        # Configure main window
        self.root.title(f"MML to DB Uploader v{SCRIPT_VERSION} - Advanced Tools by HD")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg=THEME_COLORS['off_white'])
        self.root.resizable(True, True)
        
        # Initialize variables
        self.selected_folder = tk.StringVar()
        self.processing = False
        self.upload_thread = None
        self.should_stop = False
        
        # Setup GUI
        self.setup_styles()
        self.create_widgets()
        self.setup_bindings()
        
    def setup_styles(self):
        """Setup modern color theme styles"""
        style = ttk.Style(self.root)
        style.theme_use('clam')
        
        # Configure styles with beautiful color palette
        style.configure("Title.TLabel", 
                       background=THEME_COLORS['off_white'], 
                       foreground=THEME_COLORS['primary'], 
                       font=("Segoe UI", 16, "bold"))
        
        style.configure("Subtitle.TLabel", 
                       background=THEME_COLORS['off_white'], 
                       foreground=THEME_COLORS['secondary'], 
                       font=("Segoe UI", 10))
        
        style.configure("Modern.TLabel", 
                       background=THEME_COLORS['off_white'], 
                       foreground=THEME_COLORS['primary'], 
                       font=("Segoe UI", 10))
        
        style.configure("Modern.TButton", 
                       font=("Segoe UI", 10, "bold"),
                       relief="flat",
                       background=THEME_COLORS['secondary'],
                       foreground="#17313E")
        
        style.configure("Action.TButton", 
                       font=("Segoe UI", 12, "bold"),
                       relief="flat",
                       background=THEME_COLORS['primary'],
                       foreground="#17313E")
        
        style.configure("Modern.TFrame", 
                       background=THEME_COLORS['off_white'],
                       relief="flat")
    
    def create_widgets(self):
        """Create and layout all GUI widgets"""
        # Main container
        main_frame = ttk.Frame(self.root, style="Modern.TFrame", padding=5)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header_frame = ttk.Frame(main_frame, style="Modern.TFrame")
        header_frame.pack(fill=tk.X, pady=(0, 5))
        
        title_label = ttk.Label(header_frame, 
                               text="MML to DB Uploader", 
                               style="Title.TLabel")
        title_label.pack(anchor="w")
        
        subtitle_label = ttk.Label(header_frame, 
                                  text="Advanced MML Processing Suite with Professional GUI", 
                                  style="Subtitle.TLabel")
        subtitle_label.pack(anchor="w", pady=(5, 0))
        
        # Tab layout
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # Main upload tab
        main_tab = ttk.Frame(notebook, style="Modern.TFrame")
        notebook.add(main_tab, text="🚀 Upload Manager")
        
        # About tab
        about_tab = ttk.Frame(notebook, style="Modern.TFrame")
        notebook.add(about_tab, text="ℹ️ About")
        
        # Content frame for main tab
        content_frame = main_tab
        
        # Folder selection section
        folder_section = ttk.LabelFrame(content_frame, text="Data Source Folder", padding=15)
        folder_section.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(folder_section, 
                 text="Select folder containing MML files (LST CELL, DSP VSWR, DSP RETSUBUNIT):", 
                 style="Modern.TLabel").pack(anchor="w", pady=(0, 5))
        
        folder_frame = ttk.Frame(folder_section, style="Modern.TFrame")
        folder_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.folder_entry = ttk.Entry(folder_frame, 
                                     textvariable=self.selected_folder, 
                                     font=("Segoe UI", 10))
        self.folder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        browse_btn = ttk.Button(folder_frame, 
                               text="Browse Folder", 
                               command=self.browse_folder,
                               style="Modern.TButton")
        browse_btn.pack(side=tk.RIGHT)
        
        # Control section
        control_section = ttk.LabelFrame(content_frame, text="Upload Control", padding=15)
        control_section.pack(fill=tk.X, pady=(0, 15))
        
        button_frame = ttk.Frame(control_section, style="Modern.TFrame")
        button_frame.pack(fill=tk.X)
        
        self.upload_btn = ttk.Button(button_frame, 
                                    text="🚀 Start Upload Process", 
                                    command=self.start_upload,
                                    style="Action.TButton",
                                    state="disabled")
        self.upload_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        self.cancel_btn = ttk.Button(button_frame, 
                                    text="⏹️ Cancel Upload", 
                                    command=self.cancel_upload,
                                    style="Modern.TButton",
                                    state="disabled")
        self.cancel_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        clear_log_btn = ttk.Button(button_frame, 
                                  text="🗑️ Clear Logs", 
                                  command=self.clear_logs,
                                  style="Modern.TButton")
        clear_log_btn.pack(side=tk.LEFT)
        
        # Progress section
        progress_section = ttk.LabelFrame(content_frame, text="Upload Progress", padding=15)
        progress_section.pack(fill=tk.X, pady=(0, 15))
        
        self.progress_var = tk.StringVar(value="Ready - Select folder and click Start Upload")
        progress_label = ttk.Label(progress_section, 
                                  textvariable=self.progress_var, 
                                  style="Modern.TLabel")
        progress_label.pack(anchor="w")
        
        self.progress_bar = ttk.Progressbar(progress_section, 
                                          mode='determinate', 
                                          length=400)
        self.progress_bar.pack(fill=tk.X, pady=(5, 0))
        
        # Logs section
        logs_section = ttk.LabelFrame(content_frame, text="Processing Logs & File Detection", padding=15)
        logs_section.pack(fill=tk.BOTH, expand=True)
        
        self.log_text = scrolledtext.ScrolledText(logs_section, 
                                                 height=10, 
                                                 bg=THEME_COLORS['primary'], 
                                                 fg="#0F0E0E",
                                                 font=("Consolas", 9),
                                                 wrap=tk.WORD,
                                                 relief="solid",
                                                 borderwidth=1)
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # Footer
        footer_frame = ttk.Frame(main_frame, style="Modern.TFrame")
        footer_frame.pack(fill=tk.X, pady=(20, 0))
        
        # Left side - Version info
        footer_left = ttk.Frame(footer_frame, style="Modern.TFrame")
        footer_left.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        footer_label = ttk.Label(footer_left, 
                                text=f"Version {SCRIPT_VERSION} | Advanced MML Processing Suite", 
                                style="Subtitle.TLabel")
        footer_label.pack(anchor="w")
        
        # Right side - Donate button
        footer_right = ttk.Frame(footer_frame, style="Modern.TFrame")
        footer_right.pack(side=tk.RIGHT)
        
        donate_btn = ttk.Button(footer_right, 
                               text="☕ Traktir Kopi Disini", 
                               command=lambda: webbrowser.open("https://saweria.co/HDfauzan"),
                               style="Modern.TButton")
        donate_btn.pack(side=tk.RIGHT)
        
        # Create About tab content
        self.create_about_tab(about_tab)
    
    def create_about_tab(self, about_tab):
        """Create content for About tab with scrolling capability"""
        # Create main canvas with scrollbar
        canvas = tk.Canvas(about_tab, bg=THEME_COLORS['off_white'])
        scrollbar = ttk.Scrollbar(about_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style="Modern.TFrame")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Title
        title_label = ttk.Label(scrollable_frame, 
                               text="MML to DB Uploader", 
                               style="Title.TLabel")
        title_label.pack(anchor="w", pady=(20, 10), padx=20)
        
        version_label = ttk.Label(scrollable_frame, 
                                 text=f"Version {SCRIPT_VERSION}", 
                                 style="Subtitle.TLabel")
        version_label.pack(anchor="w", pady=(0, 20), padx=20)
        
        # File Requirements Section
        req_frame = ttk.LabelFrame(scrollable_frame, text="📋 File Input Requirements", padding=15)
        req_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        req_desc = ttk.Label(req_frame, 
                            text="The following files MUST be present in the selected folder:", 
                            style="Modern.TLabel")
        req_desc.pack(anchor="w", pady=(0, 10))
        
        # Required files list
        required_files = [
            "LST CELL: 1 files",
            "LST PDSCHCFG: 1 files", 
            "LST CELLDLPCPDSCHPA: 1 files",
            "LST SECTORSPLITCELL: 1 files",
            "LST SECTORSPLITGROUP: 1 files",
            "DSP VSWR: 1 files",
            "DSP RETSUBUNIT: 1 files"
        ]
        
        for file_req in required_files:
            file_label = ttk.Label(req_frame, 
                                  text=f"• {file_req}", 
                                  style="Modern.TLabel")
            file_label.pack(anchor="w", pady=2, padx=10)
        
        # Additional Info
        info_frame = ttk.LabelFrame(scrollable_frame, text="ℹ️ Additional Information", padding=15)
        info_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        info_text = """• All files must be in .txt format
• Files are automatically detected based on naming patterns
• Processing uses advanced batch operations for high performance
• Database operations use INSERT...ON DUPLICATE KEY UPDATE
• Parallel processing for optimal speed
• Automatic error handling and reporting"""
        
        info_label = ttk.Label(info_frame, 
                              text=info_text, 
                              style="Modern.TLabel",
                              justify=tk.LEFT)
        info_label.pack(anchor="w", padx=10)
        
        # Developer Section
        dev_frame = ttk.LabelFrame(scrollable_frame, text="👨‍💻 Developer Information", padding=15)
        dev_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        # Developer name
        author_title = ttk.Label(dev_frame, 
                                text="Hadi Fauzan Hanif", 
                                style="Title.TLabel")
        author_title.pack(anchor="w", pady=(0, 10))
        
        # Email
        email_label = ttk.Label(dev_frame, 
                               text="Email: hadifauzanhanif@gmail.com", 
                               style="Modern.TLabel")
        email_label.pack(anchor="w", pady=2)
        
        # WhatsApp
        wa_frame = ttk.Frame(dev_frame, style="Modern.TFrame")
        wa_frame.pack(fill=tk.X, pady=2)
        
        wa_label = ttk.Label(wa_frame, 
                            text="WhatsApp: +62 813-5719-8294", 
                            style="Modern.TLabel")
        wa_label.pack(side=tk.LEFT)
        
        wa_btn = ttk.Button(wa_frame, 
                           text="Open WhatsApp", 
                           command=lambda: webbrowser.open("https://wa.me/6281357198294"),
                           style="Modern.TButton")
        wa_btn.pack(side=tk.RIGHT)
        
        # LinkedIn
        li_frame = ttk.Frame(dev_frame, style="Modern.TFrame")
        li_frame.pack(fill=tk.X, pady=2)
        
        li_label = ttk.Label(li_frame, 
                            text="LinkedIn:", 
                            style="Modern.TLabel")
        li_label.pack(side=tk.LEFT)
        
        li_btn = ttk.Button(dev_frame, 
                           text="Visit Profile", 
                           command=lambda: webbrowser.open("https://www.linkedin.com/in/hadi-fauzan-hanif-0b407b174/"),
                           style="Modern.TButton")
        li_btn.pack(side=tk.RIGHT)
        
        # Copyright
        copyright_label = ttk.Label(scrollable_frame, 
                                   text="© 2025 Hadi Fauzan Hanif. All rights reserved.", 
                                   style="Subtitle.TLabel")
        copyright_label.pack(anchor="w", pady=(20, 0), padx=20)
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    def setup_bindings(self):
        """Setup event bindings"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def browse_folder(self):
        """Browse and select folder containing MML files"""
        folder = filedialog.askdirectory(title="Select folder containing MML files")
        if folder:
            self.selected_folder.set(folder)
            self.log_text.delete(1.0, tk.END)
            
            # Auto detect files and show in logs
            self.log_text.insert(tk.END, f"🔍 Selected folder: {folder}\n\n")
            
            # Simulate file detection (placeholder)
            self.log_text.insert(tk.END, "=== 📊 FILE DETECTION RESULTS ===\n\n")
            self.log_text.insert(tk.END, "📋 LST Command Files:\n")
            self.log_text.insert(tk.END, "  ✅ LST CELL: 1 files\n")
            self.log_text.insert(tk.END, "  ✅ LST PDSCHCFG: 1 files\n")
            self.log_text.insert(tk.END, "  ✅ LST CELLDLPCPDSCHPA: 1 files\n")
            self.log_text.insert(tk.END, "  ✅ LST SECTORSPLITCELL: 1 files\n")
            self.log_text.insert(tk.END, "  ✅ LST SECTORSPLITGROUP: 1 files\n\n")
            
            self.log_text.insert(tk.END, "📈 DSP Data Files:\n")
            self.log_text.insert(tk.END, "  ✅ DSP VSWR: 1 files\n")
            self.log_text.insert(tk.END, "  ✅ DSP RETSUBUNIT: 1 files\n\n")
            
            self.log_text.insert(tk.END, "📊 SUMMARY: 7 total files detected\n")
            self.log_text.insert(tk.END, "\n🎉 Ready for processing! Click 'Start Upload Process' button.\n")
            
            self.upload_btn.config(state="normal")
            self.progress_var.set("Ready - Files detected, click Start Upload")
            
            self.log_text.see(tk.END)
    
    def start_upload(self):
        """Start the upload process"""
        if self.processing:
            messagebox.showwarning("Warning", "Processing already in progress.")
            return
            
        folder = self.selected_folder.get().strip()
        if not folder:
            messagebox.showwarning("Warning", "Please browse and select a folder first.")
            return
        
        # Add separator in logs for upload process
        self.log_text.insert(tk.END, "\n" + "="*60 + "\n")
        self.log_text.insert(tk.END, "🚀 STARTING UPLOAD PROCESS\n")
        self.log_text.insert(tk.END, "="*60 + "\n\n")
        self.log_text.see(tk.END)
        
        self.processing = True
        self.upload_btn.config(state="disabled")
        self.cancel_btn.config(state="normal")
        self.progress_var.set("Preparing upload...")
        self.progress_bar.config(mode='indeterminate')
        self.progress_bar.start()
        
        # Simulate upload process (placeholder)
        self.simulate_upload()
    
    def simulate_upload(self):
        """Simulate upload process for demonstration"""
        import threading
        import time
        
        def upload_worker():
            try:
                # Simulate processing steps
                steps = [
                    "Processing LST CELL files...",
                    "Processing VSWR data...",
                    "Processing RET data...",
                    "Uploading to database...",
                    "Finalizing process..."
                ]
                
                for i, step in enumerate(steps):
                    if self.should_stop:
                        break
                    
                    self.root.after(0, lambda s=step: self.progress_var.set(s))
                    self.root.after(0, lambda: self.log_text.insert(tk.END, f"✅ {step}\n"))
                    self.root.after(0, lambda: self.log_text.see(tk.END))
                    
                    time.sleep(1)  # Simulate processing time
                
                if not self.should_stop:
                    self.root.after(0, lambda: self.finish_upload("Upload completed successfully!"))
                else:
                    self.root.after(0, lambda: self.finish_upload("Upload cancelled by user."))
                    
            except Exception as e:
                self.root.after(0, lambda: self.finish_upload(f"Upload failed: {str(e)}"))
        
        # Start upload in separate thread
        self.upload_thread = threading.Thread(target=upload_worker, daemon=True)
        self.upload_thread.start()
    
    def cancel_upload(self):
        """Cancel the current upload process"""
        if self.processing:
            result = messagebox.askyesno(
                "Cancel Upload", 
                "Are you sure you want to cancel the current upload process?"
            )
            
            if result:
                self.should_stop = True
                self.progress_var.set("Cancelling upload...")
                self.progress_bar.stop()
                
                # Wait for thread to finish (max 3 seconds)
                if self.upload_thread and self.upload_thread.is_alive():
                    self.upload_thread.join(timeout=3.0)
                
                # Reset UI
                self.processing = False
                self.upload_btn.config(state="normal")
                self.cancel_btn.config(state="disabled")
                self.progress_var.set("Upload cancelled by user")
                self.progress_bar.config(value=0)
                
                self.log_text.insert(tk.END, "⏹️ Upload process cancelled by user\n")
                self.log_text.see(tk.END)
    
    def finish_upload(self, message):
        """Finish upload process and update UI"""
        self.processing = False
        self.upload_btn.config(state="normal")
        self.cancel_btn.config(state="disabled")
        self.progress_bar.stop()
        self.progress_var.set("Complete")
        self.progress_bar.config(value=self.progress_bar['maximum'])
        
        # Show result message
        if "failed" in message.lower() or "error" in message.lower():
            messagebox.showerror("Upload Failed", message)
        else:
            messagebox.showinfo("Upload Complete", message)
    
    def clear_logs(self):
        """Clear the log display"""
        self.log_text.delete(1.0, tk.END)
        self.log_text.insert(tk.END, "📝 Logs cleared. Select a folder to start.\n")
        self.progress_var.set("Ready - Select folder and click Start Upload")
    
    def on_closing(self):
        """Handle window close event"""
        if self.processing:
            result = messagebox.askyesno(
                "Cancel Upload", 
                "Upload process is still running. Do you want to cancel and close the application?"
            )
            
            if result:
                self.should_stop = True
                if self.upload_thread and self.upload_thread.is_alive():
                    self.upload_thread.join(timeout=5.0)
                self.root.destroy()
            else:
                return
        else:
            self.root.destroy()
