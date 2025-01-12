# main.py

import webview
import os
import sys
import logging
from datetime import datetime
from modules.web_gui import Api
from utils.helper import Helper

def on_loaded():
    # This function is called after the webview window has loaded
    window.evaluate_js("allReady()")
    pass

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def setup_logging():
    app_dir = Helper.getExecutablePath()
    
    # Create logs directory if it doesn't exist
    logs_dir = os.path.join(app_dir, 'logs', 'app')
    os.makedirs(logs_dir, exist_ok=True)
    
    # Create log file with timestamp
    log_file = os.path.join(logs_dir, f'app_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
    
    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)  # Also print to console
        ]
    )
    logging.info("-" * 50)
    logging.info("New session started")

if __name__ == "__main__":
    setup_logging()
    logging.info("Starting application...")
    api = Api()
    html_file = resource_path("gui/index.html")
    # size of window
    window = webview.create_window("Perfect Loop Music Player", f"file://{html_file}", js_api=api, width=1179, height=686)
    webview.start(on_loaded, debug=False)
    api.window = window
