from pydantic import BaseModel, Field
from fastapi import UploadFile
from typing import List

class BankingDepartmentRequest(BaseModel):
    files: List[UploadFile] = Field(description="The file to be consulted")

class BankingDepartmentResponse(BaseModel):
    response: str = Field(description="consultancy response")
    source: str = Field(description="The source of the response")
