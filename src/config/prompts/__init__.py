import os

from .utils import load_prompt

# Define paths to the `.md` files
PROMPTS_DIR = os.path.dirname(__file__)
CONSULTANT_INSTRUCTION_PATH = os.path.join(PROMPTS_DIR, "consultant.md")

# Load prompts
CONSULTANT_INSTRUCTION = load_prompt(CONSULTANT_INSTRUCTION_PATH)