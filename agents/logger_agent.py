import json
import datetime
import os

class LoggerAgent:
    def __init__(self, logfile="data/answers.json"):
        self.logfile = logfile
        os.makedirs(os.path.dirname(logfile), exist_ok=True)

    def log(self, question: str, answer: str, disability: str):
        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "question": question,
            "answer": answer,
            "disability": disability
        }
        with open(self.logfile, "a") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"[LoggerAgent] Logged: {entry}")

