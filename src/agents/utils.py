from agno.team.team import Team
from agno.agent import Agent
from agno.media import File


def getTeamAnswer(team: Team, query: str) -> str:
    return team.run(query)

def getAgentAnswer(agent: Agent, query: str, file: File | None = None) -> str:
    result = agent.run(query, structured_outputs=True, file=[file])
    return result.content
