import requests
from typing import Optional
from src.agents.models import IslamicFinanceContractReport, ContractFormat

async def post_request(report: Optional[IslamicFinanceContractReport], base_url: str = "http://localhost:5001") -> Optional[ContractFormat]:
    """
    Posts a request to the contractor endpoint if a report is provided.
    
    Args:
        report (Optional[IslamicFinanceContractReport]): The report to be processed
        base_url (str): The base URL of the API server
        
    Returns:
        Optional[ContractFormat]: The contract format if successful, None if no report provided
    """
    if report is None:
        return None
        
    try:
        response = requests.post(
            f"{base_url}/v1/contractor",
            json=report.model_dump()
        )
        response.raise_for_status()
        return ContractFormat(**response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error posting to contractor endpoint: {str(e)}")
        return None 