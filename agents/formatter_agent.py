class FormatterAgent:
    def format(self, text: str) -> str:
        # Basic cleanup for MVP
        return text.strip().capitalize()
