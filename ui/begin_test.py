import streamlit as st

from config import TEST_OPTIONS
from app.crud.database import update_stat_entries


def is_correct(question: str, option: str, answer: str, test_from: str):
    was_correct = (option == answer)
    st.session_state.results.append({
        "question": question,
        "option_selected": option,
        "correct_answer": answer,
        "was_correct": was_correct,
        "test_from": test_from,
    })
    st.session_state.current_question += 1
    st.rerun()


def count_total_correct():
    return sum(1 for k in st.session_state.results if k["was_correct"])


def begin_test(question_amount: int):
    if st.session_state.page == "begin_test":
        current_q = st.session_state.current_question
        questions = st.session_state.all_random_questions

        _, title_col, exit_col = st.columns([1, 3, 1])

        with title_col:
            st.markdown(
                f"<h2 style='color:{TEST_OPTIONS[question_amount]['option_color']};"
                f"text-align: center; text-style: italic; '>{TEST_OPTIONS[question_amount]['option_name']}</h2>",
                unsafe_allow_html=True
            )

        with exit_col:
            if st.button("Exit", type="primary", width="stretch"):
                correct_answers = count_total_correct()
                # check if correct_answers and current_q are not 0 - add to db if not 0
                if current_q or correct_answers:
                    update_stat_entries(
                        total_questions_increment=current_q,
                        total_correct_increment=correct_answers,
                    )

                keys_to_clear = [
                    "current_question",
                    "results",
                    "all_random_questions",
                    "question_amount",
                    "page",
                    "overall_questions_answered",
                    "overall_correct_answers",
                ]

                for key in keys_to_clear:
                    if key in st.session_state:
                        del st.session_state[key]
                st.rerun()

        # Show test summary when all questions are answered
        if current_q >= question_amount:
            total_correct = count_total_correct()

            st.markdown(
                f"<h3 style='color:{TEST_OPTIONS[question_amount]['option_color']}; "
                f"text-align: center; text-style: italic; '>Results: ({total_correct}/{question_amount})</h3>",
                unsafe_allow_html=True
            )

            for i, res in enumerate(st.session_state.results, 1):
                question_label = f"✅ Q{i}" if res["was_correct"] else f"❌ Q{i}"
                with st.expander(f"{question_label}: {res['question']}"):
                    st.markdown(f"**Correct answer:** {res['correct_answer']}")
                    st.markdown(f"**Your answer:** {res['option_selected']}")
                    st.markdown(f"**Test from:** {res['test_from']}")
                    status_color = "#0FFF50" if res["was_correct"] else "#EE4B2B"
                    st.markdown(
                        f"<span style='color:{status_color}; font-weight:bold;'"
                        f">{'Correct' if res['was_correct'] else 'Incorrect'}</span>",
                        unsafe_allow_html=True)

            return  # stop the testing logic from being called if test is over

        # current question
        question = questions[current_q]

        st.markdown(
            f"<h3 style='color:#FFF5EE; text-align: center; text-style: italic; '><i>{current_q + 1}. {question.question}</i></h3>",
            unsafe_allow_html=True
        )

        # Gather options, questions should always have a minimum of two options
        options = [question.option_1, question.option_2]
        if question.option_3:
            options.append(question.option_3)
        if question.option_4:
            options.append(question.option_4)

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button(f"{options[0]}", key=f"test-button-{question_amount}-1", width="stretch"):
                is_correct(
                    question=question.question,
                    option=options[0],
                    answer=question.answer,
                    test_from=question.document_from,
                )

            if len(options) >= 4:
                if st.button(f"{options[2]}", key=f"test-button-{question_amount}-2", width="stretch"):
                    is_correct(
                        question=question.question,
                        option=options[2],
                        answer=question.answer,
                        test_from=question.document_from,
                    )

        with col2:
            if st.button(f"{options[1]}", key=f"test-button-{question_amount}-3", width="stretch"):
                is_correct(
                    question=question.question,
                    option=options[1],
                    answer=question.answer,
                    test_from=question.document_from,
                )

            if len(options) >= 4:
                if st.button(f"{options[3]}", key=f"test-button-{question_amount}-4", width="stretch"):
                    is_correct(
                        question=question.question,
                        option=options[3],
                        answer=question.answer,
                        test_from=question.document_from
                    )

        st.write(f"Test Bank: {question.document_from}")
