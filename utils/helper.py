# helper.py
import sys
import os
class Helper:
    def __init__(self):
        pass
    def getExecutablePath():
        """ Get the executable's directory """
        # Get the executable's directory
        if getattr(sys, 'frozen', False):
            # If running as exe
            app_dir = os.path.dirname(sys.executable)
        else:
            # If running as script
            app_dir = os.path.dirname(os.path.abspath(__file__))
        return app_dir

class TokenManager:
    def __init__(self):
        pass

