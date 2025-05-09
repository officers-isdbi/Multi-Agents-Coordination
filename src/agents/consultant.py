from agno.agent import Agent

from src.config.prompts import CONSULTANT_INSTRUCTION
from src.agents import GPT4o
from src.agents.models import ConsultantResponse
from agno.tools.tavily import TavilyTools

consultant = Agent(
	name="consultant",
	model=GPT4o,
	instructions=CONSULTANT_INSTRUCTION,
	tools=[TavilyTools()],
    response_model=ConsultantResponse,
)