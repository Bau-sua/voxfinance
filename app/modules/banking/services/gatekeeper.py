from pydantic import BaseModel, Field
from typing import Optional
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
from app.core.exceptions import InvalidDocumentException

class GatekeeperResponse(BaseModel):
    \"\"\"LLM classification response.\"\"\"
    is_bank_statement: bool
    bank_name: Optional[str] = Field(None)
    confidence: float
    reason: str

PROMPT = PromptTemplate.from_template("""
You are a financial document auditor. Classify if text is bank statement (Spanish/English banks).

Criteria: Bank names, 'saldo inicial', CBU/IBAN, 'fecha cierre', 'movimientos', 'cuenta', transactions.

Filename: {filename}
Metadata: {meta}
Text (first 2 pages): {text}

Strict JSON response only no other text:
""" + GatekeeperResponse.model_json_schema())

class GatekeeperService:
    def __init__(self):
        self.llm = ChatGroq(
            model="llama3-groq-70b-8192-tool-use-preview",
            temperature=0,
            json_mode=True
        )
        self.chain = PROMPT | self.llm | JsonOutputParser(pydantic_object=GatekeeperResponse)

    async def classify(self, text: str, filename: str, meta: dict) -> GatekeeperResponse:
        result = await self.chain.ainvoke({
            "text": text,
            "filename": filename,
            "meta": str(meta)
        })
        if not result.is_bank_statement or result.confidence < 0.8:
            raise InvalidDocumentException(result.reason)
        return result