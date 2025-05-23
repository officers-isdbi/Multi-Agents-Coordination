from fastapi import APIRouter, File, HTTPException, UploadFile
import logging

from src.agents.models import BankingDepartmentRequest, BankingDepartmentResponse, ConsultantRequest, ConsultantResponse, IslamicFinanceContractReport, ContractFormat, ClassificationResult, ContractFormatRequest
from src.agents.utils import getTeamAnswer, getAgentAnswer
from src.agents import banking_department, consultant, contractor, classifier

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
	Consults a query and optionally generates a contract report.
	"""
	try:
		result = getAgentAnswer(consultant, request.query)
		response_dict = {
			"response": result.response,
			"detailed_summary": result.detailed_summary
		}

		return ConsultantResponse(**response_dict)
	except Exception as e:
		logger.exception("Answer failed")
		raise HTTPException(status_code=500, detail=str(e))
	
@router.post("/contractor", response_model=ContractFormat)
async def contractor_endpoint(request: ContractFormatRequest) -> ContractFormat:
	"""
	Generates a contract format.
	"""
	try:
		result = getAgentAnswer(contractor, request.detailed_summary)
		response_dict = {
			"title": result.title,
			"preamble": result.preamble,
			"applicable_standards": result.applicable_standards,
			"chapters": result.chapters,
			"closing": result.closing
		}
		return ContractFormat(**response_dict)
	except Exception as e:
		logger.exception("Answer failed")
		raise HTTPException(status_code=500, detail=str(e))
	
@router.post("/classifier", response_model=ClassificationResult)
async def classifier_endpoint(request: UploadFile) -> ClassificationResult:
	"""
	Classifies a transaction.
	"""
	try:
		result = getAgentAnswer(classifier, query="Classify the following transaction", file=File(content=request.file.read()))
		response_dict = {
			"classifier_decision": result.classifier_decision,
			"explanation": result.explanation
		}
		return ClassificationResult(**response_dict)
	except Exception as e:
		logger.exception("Answer failed")
		raise HTTPException(status_code=500, detail=str(e))
	
# test endpoint
@router.get("/test")
async def test_endpoint():
	return {"message": "Hello, World!"}