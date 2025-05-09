from fastapi import APIRouter, HTTPException
import logging

from src.agents.models import BankingDepartmentRequest, BankingDepartmentResponse, ConsultantRequest, ConsultantResponse
from src.agents.utils import getTeamAnswer, getAgentAnswer
from src.agents import banking_department, consultant

logger = logging.getLogger("uvicorn.error")

router = APIRouter(prefix="/v1")

# answer endpoint
@router.post("/banking_department", response_model=BankingDepartmentResponse)
async def banking_department_endpoint(request: BankingDepartmentRequest) -> BankingDepartmentResponse:
	"""
	Consults a query.
	"""
	try:
		result = getTeamAnswer(banking_department, request.query)
		return result
	except Exception as e:
		logger.exception("Answer failed")
		raise HTTPException(status_code=500, detail=str(e))
	
@router.post("/consultant", response_model=ConsultantResponse)
async def consultant_endpoint(request: ConsultantRequest) -> ConsultantResponse:
	"""
	Consults a query.
	"""
	try:
		result = getAgentAnswer(consultant, request.query)
		return result
	except Exception as e:
		logger.exception("Answer failed")
		raise HTTPException(status_code=500, detail=str(e))
    
# test endpoint
@router.get("/test")
async def test_endpoint():
	return {"message": "Hello, World!"}
