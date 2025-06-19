import gradio as gr
from agents.reader_agent import ReaderAgent
from agents.listener_agent import ListenerAgent
from agents.formatter_agent import FormatterAgent
from agents.logger_agent import LoggerAgent
from agents.integrity_agent import IntegrityAgent
from utils.question_parser import parse_questions_from_text

# Initialize agents
reader = ReaderAgent()
listener = ListenerAgent()
formatter = FormatterAgent()
logger = LoggerAgent()
integrity = IntegrityAgent()

def run_exam(file, disability):
    if not file:
        return "Please upload a question file."

    raw_text = file.read().decode("utf-8")
    questions = parse_questions_from_text(raw_text)

    for q in questions:
        if disability == "Blind":
            reader.speak(q)
            answer = listener.listen()  # expects pre-recorded file
        elif disability == "Deaf" or disability == "Mute":
            print(f"[Exam] {q}")
            answer = input("Type your answer: ")
        elif disability == "Deaf + Blind":
            return "Deaf + Blind not supported in MVP."

        cleaned = formatter.format(answer)
        logger.log(q, cleaned, disability)

    return "Exam completed and logged."

def build_ui():
    with gr.Blocks() as demo:
        gr.Markdown("# AIEXAM - Adaptive Exam Assistant")

        file = gr.File(label="Upload .txt Question File", file_types=[".txt"])
        disability = gr.Dropdown(
            ["Blind", "Deaf", "Mute", "Deaf + Blind"],
            label="Select Disability"
        )
        start_btn = gr.Button("Start Exam")
        output = gr.Textbox(label="Status")

        start_btn.click(run_exam, inputs=[file, disability], outputs=output)

    return demo

demo = build_ui()
