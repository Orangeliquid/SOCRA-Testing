from app.models.schemas import QuestionCreate, StatsCreate


def validate_question_entry(entry: dict):
    question_create = QuestionCreate(
        question=entry["question"],
        option_1=entry["options"][0],
        option_2=entry["options"][1],
        option_3=entry["options"][2],
        option_4=entry["options"][3],
        answer=entry["answer"],
        document_from=entry["document_from"],
    )

    return question_create


def validate_stat_entry(entry: dict):
    stats_create = StatsCreate(
        total_questions=entry["total_questions"],
        total_correct=entry["total_correct"],
    )

    return stats_create


if __name__ == '__main__':
    pass
