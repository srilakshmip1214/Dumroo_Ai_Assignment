from transformers import pipeline
import re

classifier = pipeline("zero-shot-classification", model="valhalla/distilbart-mnli-12-1")

def interpret_question(question):
    intents = ["pending_submissions", "performance", "upcoming_quizzes"]
    intent_result = classifier(question, intents)
    intent = intent_result["labels"][0]
    time_map = {
        "last week": "last_week",
        "this week": "this_week",
        "next week": "next_week",
        "last month": "last_month"
    }
    time_preset = "none"
    for key, val in time_map.items():
        if key in question.lower():
            time_preset = val
            break
    grade = None
    match = re.search(r"grade\s*(\d+)", question.lower())
    if match:
        grade = match.group(1)
    class_match = re.search(r"class\s*([A-C])", question.upper())
    cls = class_match.group(1) if class_match else None
    region = None
    for reg in ["South", "North", "East", "West"]:
        if reg.lower() in question.lower():
            region = reg
    return {
        "intent": intent,
        "filters": {
            "grade": grade,
            "class": cls,
            "region": region
        },
        "time_window": {
            "preset": time_preset
        }
    }
