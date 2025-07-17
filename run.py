#!/usr/bin/env python3
"""
Entry point for the Cursor Dashboard application.
"""
import sys
from pathlib import Path

# Add the src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from cursor_dashboard.app import main

if __name__ == "__main__":
    main()
