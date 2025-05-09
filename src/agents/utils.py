from agno.team.team import Team
from agno.agent import Agent


def getTeamAnswer(team: Team, query: str) -> str:
    return team.run(query)

def getAgentAnswer(agent: Agent, query: str) -> str:
    return agent.run(query)

