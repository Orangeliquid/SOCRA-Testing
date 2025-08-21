from curl_cffi import requests as cureq
from bs4 import BeautifulSoup

from app.utils.cleaner import parse_question_and_options, parse_answer, does_option_equal_answer


def fetch_page(url: str):
    """
    Issues with using impersonate="chrome"
    Open Source Versions:
    chrome99, chrome100, chrome101, chrome104, chrome107, chrome110, chrome116[1], chrome119[1], chrome120[1],
    chrome123[3], chrome124[3], chrome131[4], chrome133a[5][6], chrome136[6]

    - chrome136 has worked so far
    """
    response = cureq.get(url, impersonate="chrome136")
    print(f"RESPONSE: {response}")

    if not response.ok:
        raise Exception(f"Failed to fetch page: {response.status_code} - {response.reason}")

    return response


def save_scrapped_html(response, name_for_html_file: str):
    with open(f"{name_for_html_file}.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"Created html file - {name_for_html_file}.html")


def load_saved_html(name_of_html_file: str):
    with open(f"{name_of_html_file}.html", "r", encoding="utf-8") as f:
        return f.read()


# retrieves tags required to create qa_pairs - questions/ options/ answer - is not clean yet
def get_all_flash_cards(html_file_path, html_title) -> list:
    html = load_saved_html(name_of_html_file=html_file_path)
    soup = BeautifulSoup(html, "html.parser")
    cards = soup.find_all("div", class_=lambda x: x and "SetPageTermsList-term" in x)
    print(f"Found {len(cards)} cards.")

    qa_pairs = []
    correct_qa_found = 0
    for idx, card in enumerate(cards):
        # Get question (inside span.s1q0b356 > span.TermText)
        question_container = card.find("span", class_="s1q0b356")
        question_span = question_container.find(
            "span",
            class_="TermText notranslate lang-en"
        ) if question_container else None

        question_options = question_span.decode_contents()
        question, options = parse_question_and_options(raw_html_segment=question_options)
        if "true or false" in question.lower():
            options = ["True", "False", None, None]

        # Get answer (inside span.hcszxtp > span.TermText)
        answer_container = card.find("span", class_="hcszxtp")
        answer_span = answer_container.find("span", class_="TermText notranslate lang-en") if answer_container else None

        raw_answer = answer_span.decode_contents()
        answer = parse_answer(raw_html_segment=raw_answer)

        is_pair, correct_option = does_option_equal_answer(options=options, answer=answer)
        if not is_pair:
            print(question)
            print(options)
            print(answer)
        else:
            correct_qa_found += 1

            qa_pairs.append({
                "question": question,
                "options": options,
                "answer": correct_option,
                "document_from": html_title,
            })

    print(f"correct_qa_found = {correct_qa_found}")
    return qa_pairs


if __name__ == '__main__':
    pass
