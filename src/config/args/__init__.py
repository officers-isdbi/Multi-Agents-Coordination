import os

from .utils import load_json

# Define paths to the JSON configuration files
CONFIG_DIR = os.path.dirname(__file__)
GENERATION_PARAMS_PATH = os.path.join(CONFIG_DIR, "foundation_model.json")

# Load configurations
GENERATION_PARAMS = load_json(GENERATION_PARAMS_PATH)