from agno.agent import Agent

from src.config.prompts import CONTRACTOR_INSTRUCTION
from src.agents import GPT4o
from src.agents.models import ContractFormat
from agno.tools.tavily import TavilyTools

contractor = Agent(
	name="contractor",
	model=GPT4o,
	instructions=CONTRACTOR_INSTRUCTION,
	tools=[TavilyTools()],
    response_model=ContractFormat,
)