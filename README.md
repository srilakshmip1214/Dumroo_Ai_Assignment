# Dumroo AI Developer Assignment

This project demonstrates an AI-based data query system that understands plain English questions and fetches filtered results from structured CSV datasets. The solution follows the requirements mentioned in the Dumroo.ai Developer Assignment.

##  Project Overview

The system allows admins to type natural language questions such as:

- “Which students haven’t submitted their homework yet?”
- “Show me performance data for Grade 8 from last week.”
- “List all upcoming quizzes scheduled for next week.”

The AI interprets the question, applies role-based access controls (scope for grade, class, and region), and returns relevant filtered results.

##  Tech Stack

| Purpose | Technology Used |
|----------|-----------------|
| Programming Language | Python 3 |
| Data Handling | Pandas |
| AI / NLU Model | Transformers (`valhalla/distilbart-mnli-12-1`) |
| Interface | Streamlit |
| Access Control | Custom RBAC logic |
| Date Handling | Python datetime |

##  Project Structure

```
dumroo_ai_project/
│
├── data/
│   ├── students.csv
│   ├── submissions.csv
│   ├── quizzes.csv
│   └── scores.csv
│
├── data_runner.py
├── rbac.py
├── time_helper.py
├── nlu_local.py
└── main_app.py
```

##  Features

- Understands natural language queries (no keywords required)
- Filters data automatically using admin’s scope (grade, class, region)
- Displays structured query interpretation for transparency
- Works fully offline using local AI model
- Streamlit UI with result visualization
- Supports follow-up queries for refinement

##  Role-Based Scope

Admins are limited to their assigned data context:
```
Grade: 8
Class: A
Region: South
```
They can view results only within this scope.

##  Dataset Description

| File | Description |
|------|--------------|
| students.csv | Basic student details (ID, name, grade, class, region) |
| submissions.csv | Assignment submission records with status and date |
| quizzes.csv | Quiz schedules by grade, class, and region |
| scores.csv | Student quiz performance data |

Each dataset contains diverse scenarios across multiple grades, classes, and regions for testing.

##  Setup & Run Instructions

### 1️ Install Dependencies
```bash
pip install streamlit pandas transformers torch sentencepiece
```

### 2️ Run Streamlit App
Navigate to your project folder:
```bash
cd dumroo_ai_project
python -m streamlit run main_app.py
```

### 3️ Open in Browser
Once started, open the URL shown in terminal:
```
http://localhost:8501
```

##  Example Queries

| Query | Expected Action |
|--------|-----------------|
| Which students haven’t submitted their homework yet? | Shows list of pending submissions |
| Show me performance data for grade 8 from last week | Displays average quiz scores for Grade 8 last week |
| List all upcoming quizzes scheduled for next week | Displays quizzes within the next week |
| Show performance for class B in South region | Filters results to class B and region South |

##  Bonus Features Implemented

- Streamlit-based user interface
- Dynamic query interpretation and table view
- Scope display in UI
- Follow-up query support (modify previous results dynamically)

##  Submission Includes

- Complete Python project with all modules
- Sample dataset (4 CSV files)
- Streamlit UI ready to run
- Example queries tested successfully

##  Author
**SriLakshmi P**  
Email: srilakshmip1214@gmail.com

