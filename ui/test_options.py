import streamlit as st

from ui.begin_test import begin_test
from app.crud.database import get_random_question_entries
from config import TEST_OPTIONS


def confirm_option(question_amount: int):
    st.session_state.page = "begin_test"
    st.session_state.question_amount = question_amount
    st.session_state.current_question = 0
    st.session_state.all_random_questions = get_random_question_entries(limit=question_amount)
    st.session_state.results = []
    st.rerun()


def display_test_options():
    if st.session_state.page == "test_options":
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            if st.button(f"{TEST_OPTIONS[5]['option_name']}", key="fast-five", width="stretch"):
                confirm_option(question_amount=5)

            if st.button(f"{TEST_OPTIONS[20]['option_name']}", key="plenty-twenty", width="stretch"):
                confirm_option(question_amount=20)

        with col2:
            if st.button(f"{TEST_OPTIONS[10]['option_name']}", key="power-ten", width="stretch"):
                confirm_option(question_amount=10)

            if st.button(f"{TEST_OPTIONS[30]['option_name']}", key="sturdy-thirty", width="stretch"):
                confirm_option(question_amount=30)

        with col3:
            if st.button(f"{TEST_OPTIONS[15]['option_name']}", key="funky-fifteen", width="stretch"):
                confirm_option(question_amount=15)

            if st.button(f"{TEST_OPTIONS[50]['option_name']}", key="nifty-fifty", width="stretch"):
                confirm_option(question_amount=50)

    elif st.session_state.page == "begin_test":
        begin_test(question_amount=st.session_state.question_amount)
