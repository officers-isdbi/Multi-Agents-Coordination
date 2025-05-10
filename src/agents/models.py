from pydantic import BaseModel, Field
from fastapi import UploadFile
from typing import List, Optional, Dict, Any, Literal

class BankingDepartmentRequest(BaseModel):
    files: List[UploadFile] = Field(description="The file to be consulted")

class BankingDepartmentResponse(BaseModel):
    response: str = Field(description="consultancy response")
    source: str = Field(description="The source of the response")

class Party(BaseModel):
    name: str = Field(description="Name of the individual or organization")
    role: str = Field(description="Role in the contract (e.g., lessor, lessee, partner)")
    contact_info: Optional[Dict[str, str]] = Field(description="Contact details including address, phone, email", default=None)
    financial_info: Optional[Dict[str, Any]] = Field(description="Relevant financial information if applicable", default=None)

class Timeline(BaseModel):
    start_date: str = Field(description="Start date of the contract")
    end_date: Optional[str] = Field(description="End date of the contract if applicable", default=None)
    key_milestones: Optional[List[Dict[str, str]]] = Field(description="List of important milestones with dates", default=None)

class Risk(BaseModel):
    description: str = Field(description="Description of the identified risk")
    likelihood: str = Field(description="Likelihood of the risk occurring (e.g., low, medium, high)")
    impact: str = Field(description="Potential impact if the risk occurs")
    mitigation: str = Field(description="Strategies to mitigate the risk")

class AccountingEntry(BaseModel):
    description: str = Field(description="Description of the accounting entry")
    debit_accounts: List[Dict[str, float]] = Field(description="Accounts to be debited with amounts")
    credit_accounts: List[Dict[str, float]] = Field(description="Accounts to be credited with amounts")
    notes: Optional[str] = Field(description="Additional notes about the entry", default=None)

class IslamicFinanceContractReport(BaseModel):
    # Basic contract information
    contract_type: str = Field(description="Type of Islamic finance contract (e.g., Murabaha, Ijara MBT, Sukuk)")
    contract_purpose: str = Field(description="Purpose and objective of the contract")
    
    # Parties involved
    parties: List[Party] = Field(description="List of all parties involved in the contract")
    
    # Detailed requirements based on contract type
    contract_details: Dict[str, Any] = Field(description="All specific information needed for this contract type")
    
    # Financial structure
    financial_structure: Dict[str, Any] = Field(description="Values, payments, profit sharing, and other financial elements")
    
    # Timeline information
    timeline: Timeline = Field(description="Timeline details including start date, end date, and milestones")
    
    # Risk assessment
    risks: Optional[List[Risk]] = Field(description="Identified risks and mitigation strategies", default=None)
    
    # Compliance information
    sharia_compliance_notes: List[str] = Field(description="Specific considerations for ensuring Sharia compliance")
    
    # Applicable standards
    applicable_standards: Dict[str, List[str]] = Field(
        description="Identification of relevant FAS and Sharia Standards",
        example={"FAS": ["FAS 4", "FAS 28"], "Sharia": ["SS 9"]}
    )
    
    # Accounting treatment
    accounting_entries: Optional[List[AccountingEntry]] = Field(
        description="Key accounting entries required based on appropriate FAS",
        default=None
    )
    
    # Additional information
    additional_notes: Optional[str] = Field(description="Any other relevant information collected during intake", default=None)
    
    # Summary for quick reference
    executive_summary: str = Field(description="A concise summary of the contract details")

class ChatHistory(BaseModel):
    role: str = Field(description="The role of the chat history, either user or assistant")
    content: str = Field(description="The content of the chat history")

class ConsultantRequest(BaseModel):
    query: str = Field(description="user query")
    chat_history: List[ChatHistory] = Field(description="The chat history of the ongoing conversation")

class ConsultantResponse(BaseModel):
    response: str = Field(description="response to the user query")
    title: Optional[str] = Field(description="title of the contract, to be generated at the end of the conversation or when the user finalize all his requests",
                                default=None)
    summary: Optional[str] = Field(description="summary of the contract, to be generated at the end of the conversation or when the user finalize all his requests",
                                default=None)
    report: Optional[IslamicFinanceContractReport] = Field(description="report of the consultancy, to be generated at the end of the conversation or when the user finalize all his requests",
                                                            default=None)

class Section(BaseModel):
    title: str = Field(description="The title of the section")
    content: str = Field(description="The content of the section")
    subsections: Optional[List["Section"]] = Field(default=None, description="Optional nested subsections")

class Chapter(BaseModel):
    title: str = Field(description="The title of the chapter")
    sections: List[Section] = Field(description="The sections of the chapter")

class ContractFormat(BaseModel):
    title: str = Field(description="The title of the contract")
    preamble: str = Field(description="The introductory text of the contract including date, parties, and recitals")
    applicable_standards: List[str] = Field(description="AAOIFI standards applicable to this contract")
    chapters: List[Chapter] = Field(description="The chapters of the contract")
    closing: str = Field(description="The closing text of the contract including signature blocks")
    
class ClassificationResult(BaseModel):
    classifier_decision: Literal["Ijarah", "Ijarah Muntahia Bittamleek"]
    explanation: str