from agno.knowledge.website import WebsiteKnowledgeBase

from neo4j import GraphDatabase

# Aura credentials
AURA_URI = "neo4j+s://<your-database-id>.databases.neo4j.io"
AURA_USER = "neo4j"
AURA_PASSWORD = "password"

driver = GraphDatabase.driver(AURA_URI, auth=(AURA_USER, AURA_PASSWORD))

website_kb = WebsiteKnowledgeBase(
    urls=["https://docs.oracle.com/cd/E86273_01/html/CI/CITOC.htm"],
    max_links=1000,
)