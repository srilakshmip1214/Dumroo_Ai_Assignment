import pandas as pd
from rbac import apply_scope
from time_helper import get_dates

def load_all():
    students = pd.read_csv("data/students.csv")
    subs = pd.read_csv("data/submissions.csv", parse_dates=["submitted_at"])
    quizzes = pd.read_csv("data/quizzes.csv", parse_dates=["scheduled_at"])
    scores = pd.read_csv("data/scores.csv", parse_dates=["taken_at"])
    return students, subs, quizzes, scores

def handle_query(parsed, scope, data):
    students, subs, quizzes, scores = data
    intent = parsed.get("intent")
    filters = parsed.get("filters", {})
    window = parsed.get("time_window", {})
    start, end = get_dates(window.get("preset"))
    if intent == "pending_submissions":
        df = subs.merge(students, on="student_id", how="left")
        df = apply_scope(df, scope)
        df = df[df["submitted"].astype(str).str.lower() == "false"]
        if start and end:
            df = df[(df["submitted_at"] >= pd.Timestamp(start)) & (df["submitted_at"] <= pd.Timestamp(end))]
        return df[["student_name", "grade", "class", "region", "assignment_title", "submitted_at"]]
    if intent == "upcoming_quizzes":
        df = apply_scope(quizzes, scope)
        if start and end:
            df = df[(df["scheduled_at"] >= pd.Timestamp(start)) & (df["scheduled_at"] <= pd.Timestamp(end))]
        return df[["title", "grade", "class", "region", "scheduled_at"]]
    if intent == "performance":
        df = scores.merge(quizzes[["quiz_id", "grade", "class", "region"]], on="quiz_id", how="left")
        df = apply_scope(df, scope)
        if start and end:
            df = df[(df["taken_at"] >= pd.Timestamp(start)) & (df["taken_at"] <= pd.Timestamp(end))]
        df["percentage"] = (df["score"] / df["max_score"]) * 100
        result = df.groupby(["grade", "class"], as_index=False)["percentage"].mean()
        result.rename(columns={"percentage": "avg_percent"}, inplace=True)
        return result.sort_values("avg_percent", ascending=False)
    return students.head(10)
