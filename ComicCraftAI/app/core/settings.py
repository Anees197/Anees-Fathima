from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
OUTPUT_DIR = BASE_DIR / "outputs"