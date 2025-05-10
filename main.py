from agno.playground import Playground, serve_playground_app
from src.agents.consultant import consultant
from src.agents.contractor import contractor
from src.agents.classifier import classifier

app = Playground(agents=[consultant, contractor, classifier]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)