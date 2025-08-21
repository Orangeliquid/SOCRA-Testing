import streamlit as st

from config import EXAM_OVERVIEW
from ui.test_options import display_test_options
from ui.begin_test import begin_test
from app.crud.database import get_stat_entries, reset_stat_entries


def get_all_stats():
    overall_stats = get_stat_entries()
    st.session_state.overall_questions_answered = overall_stats.total_questions
    st.session_state.overall_correct_answers = overall_stats.total_correct


def reset_current_stats():
    reset_stat_entries()
    get_all_stats()
    st.rerun()


def run_start():
    if "page" not in st.session_state:
        st.session_state.page = "start"

    if st.session_state.page == "start":
        get_all_stats()

        percentage_correct = round(
            st.session_state.overall_correct_answers / st.session_state.overall_questions_answered, 2
        ) * 100 if st.session_state.overall_questions_answered else 0
        with st.expander("SOCRA Overview"):
            for key, val in EXAM_OVERVIEW.items():
                cleaned_key = key.replace("_", " ").title()
                with st.expander(cleaned_key):
                    st.markdown(f"**{val}**")

        with st.expander("Overall Stats"):
            st.markdown(f"**Total Correct Answers:** {st.session_state.overall_correct_answers}")
            st.markdown(f"**Total Questions Answered:** {st.session_state.overall_questions_answered}")
            st.markdown(f"**Correct Percentage:** {percentage_correct}%")
            if st.button("Reset Stats"):
                reset_current_stats()

        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("Choose Your Path", key="choose-your-path", width="stretch"):
                st.session_state.page = "test_options"
                st.rerun()

    elif st.session_state.page == "test_options":
        display_test_options()

    elif st.session_state.page == "begin_test":
        begin_test(question_amount=st.session_state.question_amount)
