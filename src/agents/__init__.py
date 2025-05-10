import os

from agno.models.openai import OpenAIChat
from dotenv import find_dotenv, load_dotenv

from src.config.args import GENERATION_PARAMS

load_dotenv(find_dotenv())

GPT4o = OpenAIChat(
	id=GENERATION_PARAMS["models"]["openai"]["mlm"]["name"],
	temperature=GENERATION_PARAMS["models"]["openai"]["llm"]["temperature"],
)

GPT4o_mini = OpenAIChat(
	id=GENERATION_PARAMS["models"]["openai"]["llm"]["name"],
	temperature=GENERATION_PARAMS["models"]["openai"]["llm"]["temperature"],
)

from agno.team.team import Team
from src.agents.consultant import consultant
from src.agents.contractor import contractor

banking_department = Team(
    name="banking_department",
    mode="coordinate",
    model=GPT4o,
    members=[consultant, contractor],
    description="",
    instructions="",
    add_member_tools_to_system_message=True,
    enable_agentic_context=True,
    share_member_interactions=True,
    show_members_responses=True,
    markdown=True,
    monitoring=True,
    success_criteria="",
)