from pydantic import BaseModel, Field
from fastapi import UploadFile
from typing import List

class BankingDepartmentRequest(BaseModel):
    files: List[UploadFile] = Field(description="The file to be consulted")

class BankingDepartmentResponse(BaseModel):
    response: str = Field(description="consultancy response")
    source: str = Field(description="The source of the response")

class ConsultantRequest(BaseModel):
    query: str = Field(description="The query to be consulted")

class ConsultantResponse(BaseModel):
    response: str = Field(description="consultancy response")
    source: str = Field(description="The source of the response")

