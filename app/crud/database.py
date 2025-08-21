from sqlalchemy.sql.expression import func

from app.database import SessionLocal
from app.models.db_entry import QuestionEntry, StatsEntry
from app.models.schemas import QuestionCreate, StatsCreate


# Intake Pydantic model and plug values into QuestionEntry SQLAlchemy model then place commit to DB
def create_question_entry(entry_data: QuestionCreate):
    with SessionLocal() as db:
        entry = QuestionEntry(
            question=entry_data.question,
            option_1=entry_data.option_1,
            option_2=entry_data.option_2,
            option_3=entry_data.option_3,
            option_4=entry_data.option_4,
            answer=entry_data.answer,
            document_from=entry_data.document_from,
        )

        db.add(entry)
        db.commit()
        db.refresh(entry)
        return entry


def get_all_question_entries():
    with SessionLocal() as db:
        entries = db.query(QuestionEntry).order_by(QuestionEntry.id).all()
        return entries


def get_random_question_entries(limit: int):
    with SessionLocal() as db:
        entries = (
            db.query(QuestionEntry)
            .order_by(func.random())
            .limit(limit)
            .all()
        )
        return entries


def create_stat_entries(entry_stats: StatsCreate):
    with SessionLocal() as db:
        entry = StatsEntry(
            total_questions=entry_stats.total_questions,
            total_correct=entry_stats.total_correct,
        )

        db.add(entry)
        db.commit()
        db.refresh(entry)
        return entry


def get_stat_entries():
    with SessionLocal() as db:
        stats = db.query(StatsEntry).first()
        return stats


def update_stat_entries(total_questions_increment: int = 0, total_correct_increment: int = 0):
    with SessionLocal() as db:
        stats = db.query(StatsEntry).first()
        if stats:
            stats.total_questions += total_questions_increment
            stats.total_correct += total_correct_increment
            db.commit()
            db.refresh(stats)

        return stats


def reset_stat_entries():
    with SessionLocal() as db:
        stats = db.query(StatsEntry).first()
        if stats:
            stats.total_questions = 0
            stats.total_correct = 0
            db.commit()
            db.refresh(stats)

        return stats
