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
    title: str = Field(description="The title of the consultancy response")
    response: str = Field(description="response of the consultancy")
    summary: str = Field(description="summary of the final consultancy decision, to be updated at each new")
    source: str = Field(description="The source of the consultancy response, either the website or the document")

