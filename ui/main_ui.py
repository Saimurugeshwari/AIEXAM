import gradio as gr
from agents.reader_agent import ReaderAgent
from agents.listener_agent import ListenerAgent
from agents.formatter_agent import FormatterAgent
from agents.logger_agent import LoggerAgent
from agents.integrity_agent import IntegrityAgent
from utils.question_parser import parse_questions_from_text

from dotenv import load_dotenv
import os
load_dotenv()


#Initialize agents
reader = ReaderAgent()
listener = ListenerAgent()
formatter = FormatterAgent()
logger = LoggerAgent()
integrity = IntegrityAgent()

current_question_index = 0
questions = []

def run_exam(file, disability):
    global questions, current_question_index
    current_question_index = 0

    if not file:
        return "Please upload a question file.", "", gr.update(visible=False)

    try:
        with open(file.name, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}", "", gr.update(visible=False)

    questions = parse_questions_from_text(text)
    if not questions:
        return "No questions found in file.", "", gr.update(visible=False)

    if disability == "Deaf + Blind":
        return "Deaf + Blind not supported in MVP.", "", gr.update(visible=False)

    # For Blind: start auto Q&A loop
    if disability == "Blind":
        return auto_record_blind(disability) + (gr.update(visible=False),)


    # For Deaf or Mute
    question = questions[current_question_index]
    return "Please type your answer below and click submit.", question, gr.update(visible=True), gr.update(visible=True)


def submit_answer(answer_text, disability):
    global current_question_index, questions

    if current_question_index >= len(questions):
        return "Exam already complete.", "", "", gr.update(visible=False)

    question = questions[current_question_index]
    cleaned = formatter.format(answer_text)
    logger.log(question, cleaned, disability)

    current_question_index += 1
    if current_question_index < len(questions):
        next_question = questions[current_question_index]
        if disability == "Blind":
            reader.speak(next_question)
            return " Question being read aloud...", next_question, "", gr.update(visible=False)
        else:
            return " Please type your answer below and click Submit.", next_question, "", gr.update(visible=True)

    # When all questions are done
    return "Exam completed and logged.", "", "", gr.update(visible=False)
def record_answer(disability):
    global current_question_index, questions

    if disability != "Blind":
        return "Recording only supported for Blind users.", "", gr.update(visible=False)

    if current_question_index >= len(questions):
        return "Exam complete.", "", gr.update(visible=False)

    question = questions[current_question_index]
    answer = listener.listen()
    cleaned = formatter.format(answer)
    logger.log(question, cleaned, disability)

    current_question_index += 1

    if current_question_index < len(questions):
        next_question = questions[current_question_index]
        reader.speak(next_question)
        return "Question being read aloud...", next_question, gr.update(visible=False)
    else:
        return "Exam completed and logged.", "", gr.update(visible=False)
    
def auto_record_blind(disability):
    global questions, current_question_index

    while current_question_index < len(questions):
        q = questions[current_question_index]
        reader.speak(q)
        answer = listener.listen()

        if answer.strip():  # Only log if answer is not empty
            cleaned = formatter.format(answer)
            logger.log(q, cleaned, disability)
        else:
            print("No answer detected — skipping log.")

        current_question_index += 1

    listener.save_session()  # Save final full audio
    return "Exam completed and logged.", "", gr.update(visible=False)

def build_ui():
    with gr.Blocks() as demo:
        gr.Markdown("# AIEXAM - Adaptive Exam Assistant")

        file = gr.File(label="Upload .txt Question File", file_types=[".txt"])
        disability = gr.Dropdown(["Blind", "Deaf", "Mute"], label="Select Disability")

        start_btn = gr.Button("Start Exam")
        submit_btn = gr.Button("Submit Answer", visible=False)

        status = gr.Textbox(label="Status", interactive=False)
        question_display = gr.Textbox(label="Question", interactive=False)
        answer_input = gr.Textbox(label="Your Answer", visible=False)

        start_btn.click(run_exam, inputs=[file, disability], outputs=[status, question_display, answer_input, submit_btn])
        submit_btn.click(
            submit_answer,
            inputs=[answer_input, disability],
            outputs=[status, question_display, answer_input, submit_btn]
        )
    return demo
