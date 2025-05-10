from agno.agent import Agent
from src.config.prompts import CLASSIFIER_INSTRUCTION
from src.agents import GPT4o
from src.agents.models import ClassificationResult
from src.tools.consultant import website_kb_as_tool, query_aura

classifier = Agent(
    name="FAS-Classifier",
    model=GPT4o,
    description=CLASSIFIER_INSTRUCTION,
    tools=[website_kb_as_tool, query_aura],
    response_model=ClassificationResult,
)

