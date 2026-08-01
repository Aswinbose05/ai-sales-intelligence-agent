"""
Application Configuration
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ==========================
# Ollama
# ==========================

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "mistral"
)

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434"
)

TEMPERATURE = float(
    os.getenv(
        "TEMPERATURE",
        "0"
    )
)

MAX_TOKENS = int(
    os.getenv(
        "MAX_TOKENS",
        "512"
    )
)

# ==========================
# Search
# ==========================

MAX_SEARCH_RESULTS = int(
    os.getenv(
        "MAX_SEARCH_RESULTS",
        "3"
    )
)

REQUEST_TIMEOUT = int(
    os.getenv(
        "REQUEST_TIMEOUT",
        "15"
    )
)

# ==========================
# Database
# ==========================

DATABASE_PATH = os.getenv(
    "DATABASE_PATH",
    "data/signals.db"
)

# ==========================
# Logging
# ==========================

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)