def parse_questions_from_text(text):
    return [q.strip() for q in text.split("\n\n") if q.strip()]
