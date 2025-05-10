from agno.tools import tool
from agno.tools.website import WebsiteTools

from src.tools import driver, website_kb

website_kb_as_tool = WebsiteTools(knowledge_base=website_kb)

@tool
def query_aura(cypher_query: str, parameters: dict = None):
    """
    Executes a Cypher query on a Neo4j Aura DB and returns results as list of dictionaries.
    To be used for querying the Aura graph database and extract information from FAS standards.
    Args:
        cypher_query (str): The Cypher query to execute.
        parameters (dict, optional): Parameters for the query. Defaults to None.
    Returns:
        list: A list of dictionaries containing the results of the query.
    """
    results = []

    with driver.session() as session:
        try:
            result = session.run(cypher_query, parameters or {})
            results = [record.data() for record in result]
        except Exception as e:
            print(f"[Neo4j Error] {e}")
        finally:
            driver.close()

    return results