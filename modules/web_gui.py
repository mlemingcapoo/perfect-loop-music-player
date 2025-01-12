# web_gui.py

import threading
import sys
import os
import json
import logging
import locale
import base64
import traceback
from pathlib import Path
# from modules.employee_exporter import EmployeeExporter
import tkinter as tk
from tkinter import filedialog
import shutil

# Set default encoding to UTF-8
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

class Api:
    def __init__(self):
        try:
            self.window = None
            self.is_save_dialog_open = False
            # self.temp_dir = Path("data/working")

            # Configure system encoding
            if sys.stdout.encoding != "utf-8":
                sys.stdout.reconfigure(encoding="utf-8")
            if sys.stderr.encoding != "utf-8":
                sys.stderr.reconfigure(encoding="utf-8")

            # Create temp directory if it doesn't exist
            # try:
            #     self.temp_dir.mkdir(exist_ok=True)
            #     logging.info(f"Temporary directory created/verified at: {self.temp_dir}")
            # except Exception as e:
            #     logging.error(f"Failed to create temporary directory: {e}")
            #     raise

            # Configure logging
            try:
                logging.basicConfig(
                    level=logging.DEBUG,  # Changed to DEBUG for more verbose logging
                    format="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
                    handlers=[
                        logging.StreamHandler(sys.stdout),
                        logging.FileHandler("app.log", encoding="utf-8", mode="a"),
                    ],
                    force=True,
                )
                logging.info("Logging system initialized successfully")
            except Exception as e:
                print(f"Failed to initialize logging: {e}")
                raise

            logging.info("API initialization completed successfully.")
            # self.quick_test_run()
            # raise RuntimeError("Test run completed. Exiting...")
            

        except Exception as e:
            error_msg = f"Failed to initialize API: {str(e)}\n{traceback.format_exc()}"
            print(error_msg)
            logging.error(error_msg)
            raise

    def hey_python(self):
        try:
            logging.info("hey_python function called")
            return "Here is Python!"
        except Exception as e:
            error_msg = f"Error in hey_python: {str(e)}\n{traceback.format_exc()}"
            logging.error(error_msg)
            return f"Error: {str(e)}"

    def call_backend(self, data):
        logging.info(data)
        
    def quick_test_run(self):
        pass
    
    