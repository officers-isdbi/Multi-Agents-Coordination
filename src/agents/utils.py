from agno.team.team import Team
from agno.agent import Agent


def getTeamAnswer(team: Team, query: str) -> str:
    return team.run(query)

def getAgentAnswer(agent: Agent, query: str) -> str:
    result = agent.run(query, structured_outputs=True)
    return result.content

