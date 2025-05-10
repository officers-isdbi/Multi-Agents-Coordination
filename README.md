# Multi-Agent Islamic Finance Contract System

A sophisticated multi-agent system designed to handle Islamic finance contract generation, consultation, and classification. The system leverages multiple specialized AI agents working in coordination to provide comprehensive Islamic finance contract services.

## System Architecture

The system consists of three main agents working in coordination:

1. **Consultant Agent**
   - Primary interface for user interactions
   - Handles contract consultation and information gathering
   - Generates detailed Islamic finance contract reports
   - Uses knowledge base and Neo4j database for accurate information

2. **Contractor Agent**
   - Specializes in contract document generation
   - Creates structured contract documents following Islamic finance standards
   - Ensures compliance with AAOIFI standards
   - Generates well-formatted contract documents with proper sections and chapters

3. **Classifier Agent (FAS-Classifier)**
   - Classifies contracts into specific Islamic finance categories
   - Currently supports classification between "Ijarah" and "Ijarah Muntahia Bittamleek"
   - Provides explanations for classification decisions

## Key Features

- **Multi-Agent Coordination**: Agents work together in a coordinated team environment
- **Knowledge Integration**: Combines website knowledge base with Neo4j graph database
- **Structured Output**: Well-defined data models for all responses
- **Islamic Finance Focus**: Specialized in Islamic finance contracts and standards
- **Comprehensive Documentation**: Detailed contract reports with risk assessment and compliance notes

## Technical Stack

- **Framework**: Built using the Agno framework for multi-agent systems
- **AI Models**: Utilizes OpenAI's GPT-4 for agent intelligence
- **Database**: Neo4j Aura DB for storing and querying Islamic finance standards
- **API**: FastAPI for handling HTTP requests
- **Containerization**: Docker support for easy deployment

## Data Models

The system uses several Pydantic models for structured data handling:

- `IslamicFinanceContractReport`: Comprehensive contract report model
- `ContractFormat`: Structured contract document format
- `ClassificationResult`: Contract classification output
- `ConsultantResponse`: Response model for consultation queries

## Setup and Installation

1. Clone the repository
2. Install dependencies (uv recommended):
   ```bash
   uv sync
   ```
3. Set up environment variables:
   - Create a `.env` file with necessary API keys and configuration or use the `.env.example` file as a template.
   - Configure Neo4j database connection details in src/tools/__init__.py

4. Run the application:
   ```bash
   uvicorn app:app --reload
   ```

## Docker Deployment

The system can be deployed using Docker:

```bash
docker-compose up --build
```

## API Endpoints

The system exposes several API endpoints for different functionalities:

- `v1/consultant`: For contract consultation
- `v1/classifier`: For contract classification
- `v1/contractor`: For contract document generation
- `v1/banking_department`: For banking department queries (not yet supported --> in 2nd phase)