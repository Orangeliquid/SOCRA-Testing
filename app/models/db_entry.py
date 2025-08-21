from sqlalchemy import Column, Integer, String

from app.database import Base


# Create SQLAlchemy model
class QuestionEntry(Base):
    __tablename__ = "Socra_Test_Questions"

    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    option_1 = Column(String, nullable=False)
    option_2 = Column(String, nullable=False)
    option_3 = Column(String, nullable=True)
    option_4 = Column(String, nullable=True)
    answer = Column(String, nullable=False)
    document_from = Column(String, nullable=False)


class StatsEntry(Base):
    __tablename__ = "stats"

    id = Column(Integer, primary_key=True)
    total_questions = Column(Integer, default=0)
    total_correct = Column(Integer, default=0)
