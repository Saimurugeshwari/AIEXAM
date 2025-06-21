import json
import datetime
import os

class LoggerAgent:
    def __init__(self, logfile="data/answers.json"):
        self.logfile = logfile
        os.makedirs(os.path.dirname(logfile), exist_ok=True)
        # Initialize empty array if file does not exist
        if not os.path.exists(self.logfile):
            with open(self.logfile, "w") as f:
                json.dump([], f)

    def log(self, question, answer, disability):
        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "question": question,
            "answer": answer,
            "disability": disability
        }

        try:
            with open(self.logfile, "r") as f:
                data = json.load(f)
        except Exception:
            data = []

        data.append(entry)

        with open(self.logfile, "w") as f:
            json.dump(data, f, indent=2)

        print(f"[LoggerAgent] Logged: {entry}")