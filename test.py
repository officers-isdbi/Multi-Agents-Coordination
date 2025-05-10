# from agno.knowledge.website import WebsiteKnowledgeBase

from neo4j import GraphDatabase

# Aura credentials
AURA_URI = "neo4j+s://70014ae6.databases.neo4j.io"
AURA_USER = "neo4j"
AURA_PASSWORD = "password"

try:
    driver = GraphDatabase.driver(AURA_URI, auth=(AURA_USER, AURA_PASSWORD))
    driver.verify_connectivity()
    print("Successfully connected to Neo4j Aura!")
except Exception as e:
    print(f"Failed to connect: {str(e)}")
finally:
    if 'driver' in locals():
        driver.close()
# website_kb = WebsiteKnowledgeBase(
#     urls=["https://docs.oracle.com/cd/E86273_01/html/CI/CITOC.htm"],
#     max_links=1000,
# )