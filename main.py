import os

from config import INIT_STATS
from app.utils.validation import validate_question_entry, validate_stat_entry
from app.crud.database import create_question_entry, get_all_question_entries, create_stat_entries, get_stat_entries
from app.crud.database import reset_stat_entries
from app.utils.scraping import get_all_flash_cards, fetch_page, save_scrapped_html
from app.database import init_db


def clean_cards(html_file_path, html_file_name):
    return get_all_flash_cards(html_file_path=html_file_path, html_title=html_file_name)


def validate_and_enter(cards):
    qa_matches = []
    for idx, card in enumerate(cards):
        validated_entry = validate_question_entry(entry=card)
        create_question_entry(entry_data=validated_entry)
    return qa_matches


# no need to scrape and save currently
def scrape_questions(url_to_scrape, name_of_new_html):
    get_page_response = fetch_page(url=url_to_scrape)
    save_scrapped_html(response=get_page_response, name_for_html_file=name_of_new_html)


def enter_stats():
    validated_entry = validate_stat_entry(entry=INIT_STATS)
    create_stat_entries(entry_stats=validated_entry)


if __name__ == '__main__':
    pass  # when ready remove pass and uncomment steps needed for setup

    # Step 1 - Initial setup of database and entering of tracked questions answered and correct answers - Set both to 0
    # init_db()  # needed if no db is made yet - first run through
    # enter_stats()  # needed if no db set - init stats to 0

    # Step 2 - Clean, validate, ingest SOCRA questions outside of scraping url
    # html_files = [
    #     "SOCRA_2_67_Full",
    #     "SOCRA_Full",
    # ]

    # for file_name in html_files:
    #     html_name = file_name
    #     current_dir = os.path.dirname(os.path.abspath(__file__))
    #     html_file_path_created = os.path.join(current_dir, "data", html_name)
    #
    #     cleaned_cards = clean_cards(html_file_path=html_file_path_created, html_file_name=html_name)
    #     validate_and_enter(cards=cleaned_cards)

    # If you have already validated QA pairs -> move to running app in terminal
    # TO RUN IN TERMINAL -> streamlit run streamlit_app.py

    # OPTIONAL - Step 3 - Validate question and answer pairs match
    # all_entries = get_all_question_entries()
    # print(len(all_entries))
    # correct_matches = 0
    # for entry in all_entries:
    #     print(entry.question)
    #     print(entry.answer)
    #     print(entry.document_from)
    #
    #     for opt in [entry.option_1, entry.option_2, entry.option_3, entry.option_4]:
    #         if entry.answer == opt:
    #             correct_matches += 1
    #     print(f"Total qa matches = {correct_matches}")
    #     print("----")

    # OPTIONAL - Would be step 1 - getting data from desired URL -
    # Remember scraping logic is designed for already gathered html files
    # for scrape_questions with a URL
    # url_wanted = "https://quizlet.com/999231950/socra-exam-prep-2024-flash-cards/"
    # new_html_file_name = "SOCRA_2_67"
    # scrape_questions(url_to_scrape=url_wanted, name_of_new_html=new_html_file_name)

