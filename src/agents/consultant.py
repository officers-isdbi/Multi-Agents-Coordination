from agno.agent import Agent

from src.config.prompts import CONSULTANT_INSTRUCTION
from src.agents import GPT4o
from src.agents.models import ConsultantResponse
from src.tools.consultant import website_kb_as_tool, query_aura

consultant = Agent(
	name="consultant",
	model=GPT4o,
	instructions=CONSULTANT_INSTRUCTION,
	tools=[website_kb_as_tool, query_aura],
    response_model=ConsultantResponse,
)