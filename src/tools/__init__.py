from agno.knowledge.website import WebsiteKnowledgeBase
from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

# Aura credentials
AURA_URI = os.getenv("NEO4J_URI")
AURA_USER = os.getenv("NEO4J_USERNAME")
AURA_PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(AURA_URI, auth=(AURA_USER, AURA_PASSWORD))

website_kb = WebsiteKnowledgeBase(
    urls=["https://docs.oracle.com/cd/E86273_01/html/CI/CITOC.htm"],
    max_links=1000,
)