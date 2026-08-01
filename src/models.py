"""
Pydantic Models
"""

from pydantic import BaseModel, Field
from typing import Optional


class SearchResult(BaseModel):
    company: str
    query_type: str
    title: str
    url: str


class Signal(BaseModel):
    company: str

    signal_type: str = Field(
        description="Hiring, Funding, Expansion, Complaints, Technology, Leadership"
    )

    evidence: str

    confidence: float

    reason: str

    page_type: str

    title: str

    url: str


class RankedCompany(BaseModel):
    company: str

    score: float

    hiring: int = 0

    funding: int = 0

    complaints: int = 0

    technology: int = 0

    leadership: int = 0

    explanation: str


class Outreach(BaseModel):
    company: str

    linkedin_message: str

    followup_email: str