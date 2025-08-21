from pydantic import BaseModel, Field
from typing import Optional


# Verify via Pydantic model that values are correctly formatted before sending to QuestionEntry
class QuestionCreate(BaseModel):
    question: str = Field(..., min_length=1)
    option_1: str = Field(..., min_length=1)
    option_2: str = Field(..., min_length=1)
    option_3: Optional[str] = Field(None, min_length=1)
    option_4: Optional[str] = Field(None, min_length=1)
    answer: str = Field(..., min_length=1)
    document_from: str = Field(..., min_length=1)


class QuestionRead(QuestionCreate):
    id: int

    class Config:
        from_attributes = True


class StatsCreate(BaseModel):
    total_questions: int = 0
    total_correct: int = 0


class StatsRead(StatsCreate):
    id: int

    class Config:
        from_attributes = True
