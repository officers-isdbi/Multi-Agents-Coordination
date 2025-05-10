from agno.agent import Agent

from src.config.prompts import CONTRACTOR_INSTRUCTION
from src.agents import GPT4o
from src.agents.models import ContractFormat
from src.tools.consultant import website_kb_as_tool, query_aura
from src.tools.consultant import query_aura

contractor = Agent(
	name="contractor",
	model=GPT4o,
	instructions=CONTRACTOR_INSTRUCTION,
	tools=[website_kb_as_tool, query_aura],
    response_model=ContractFormat,
)