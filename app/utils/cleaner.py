import re


def clean_option(text: str) -> str:
    return re.sub(r"^[a-d][).]\s*", "", text.strip(), flags=re.IGNORECASE)


def parse_question_and_options(raw_html_segment: str):
    # Example input:
    # "What is X?<br/>a) Option 1<br/>b) Option 2<br/>c) Option 3<br/>d) Option 4"

    parts = raw_html_segment.split("<br/>")
    first_part = parts[0]
    rest_parts = parts[1:]

    # Check if 'a)' is glued to question text
    match = re.search(r"(.*?)(a\).*)", first_part, flags=re.IGNORECASE)
    if match:
        question = match.group(1).strip()
        first_option = match.group(2).strip()
        options_raw = [first_option] + rest_parts
    else:
        question = first_part.strip()
        options_raw = rest_parts

    # Clean options - remove "a) " - "d) " prefixes
    options = [clean_option(opt) for opt in options_raw]

    return question, options


def parse_answer(raw_html_segment: str):
    if "true" in raw_html_segment.lower() or "false" in raw_html_segment.lower():
        parts = raw_html_segment.split("<br/>")
        first_part = parts[0].replace(" ", "")
        rest_parts = parts[1:]
        cleaned_raw_html_segment = ": ".join([first_part] + rest_parts)
    else:
        cleaned_raw_html_segment = raw_html_segment.replace("<br/>", " ")

    return clean_option(cleaned_raw_html_segment)


def normalize_text(s: str) -> str:
    return re.sub(r"[^\w\s]", "", s).strip().lower()


def does_option_equal_answer(options, answer):
    norm_answer = normalize_text(answer)
    for opt in options:
        norm_opt = normalize_text(opt)
        if norm_opt and norm_opt in norm_answer:
            return True, opt
    return False, None
