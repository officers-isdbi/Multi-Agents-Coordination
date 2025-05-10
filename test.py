# test the endpoint: https://multi-agents-coordination.onrender.com/v1/consultant

import requests

query = "How does Sukuk (Islamic bonds) work and what are its key features compared to conventional bonds?"

response = requests.post("https://multi-agents-coordination.onrender.com/v1/consultant", json={"query": query})

print(response.json())


