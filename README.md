# AI-Powered Workflow Automation for Internal Ticketing

## 🎯 Objective
To build an automated system that classifies and routes internal IT/maintenance tickets using a Large Language Model (LLM) API like OpenAI’s GPT-4, simulating an internal operations tool for a company like FreeAxez.

This project is an intelligent internal support ticket classifier that uses OpenAI's GPT-4 to automatically label and route tickets to the appropriate department. Designed to help operations and IT teams reduce manual triage and streamline internal workflows.

> 🔧 Built with: Python, Streamlit, OpenAI GPT-4, Pandas

---

## 🚀 Demo

![Ticket Classifier in Action](assets/demo.mp4)

## 🧠 Problem Statement
Operations teams often receive a large volume of unstructured issue reports (emails, form submissions, Slack messages). Manual triaging is inefficient and prone to delays. The goal is to create an intelligent assistant that automatically tags the issue type and routes it to the appropriate department head.

## 🏗️ Project Architecture Overview
1. Data Ingestion
   - Simulated tickets in CSV or Google Sheets format

2. Text Classification
   - Prompt-based classification using OpenAI API
   - Tags: ["Facilities", "IT Support", "HR", "Finance", "Sales Enablement"]

3. Routing Logic
   - Rule-based assignment (e.g., Facilities → ops@freeaxez.com)

4. Frontend (Optional)
   - Streamlit interface for uploading a CSV and exporting results

5. Output
   - Labeled and routed tickets in Excel or Google Sheets

## 🧾 Simulated Input Dataset (ticket_data.csv)

| ticket\_id | submitted\_by   | subject            | description                                                                |
| ---------- | --------------- | ------------------ | -------------------------------------------------------------------------- |
| T001       | jdoe\@company   | Laptop overheating | My laptop gets very hot during Zoom calls and reboots randomly.            |
| T002       | asmith\@company | Light not working  | The overhead light in Conference Room B has been flickering since Tuesday. |
| T003       | mtan\@company   | Payroll Issue      | My paycheck was short this month. Please review deductions.                |

## 🧪 Sample Prompt for OpenAI API
prompt = f"""
Classify the following internal support ticket into one of the categories: 
["Facilities", "IT Support", "HR", "Finance", "Sales Enablement"].

Ticket Description:
{ticket_text}

Only return the category name.
"""


## 🧰 Technologies Used
- Python

- OpenAI API (or Claude/Gemini)

- Pandas for data handling

- Streamlit for optional user interface

- Google Sheets API or ExcelWriter for export

## 🧑‍💻 Code Structure
ticket_classifier/
│
├── main.py                 # Script entry point
├── classify.py             # Prompt-based classification logic
├── router.py               # Routing logic and email mapping
├── utils.py                # Helper functions (e.g., CSV read/write)
├── streamlit_app.py        # (Optional) UI for uploading and exporting

## 📈 Impact
Reduces manual triage time by ~80%

Gives non-technical staff access to AI without writing code

Provides a production-ready LLM use case in an internal ops context
└── data/
    └── ticket_data.csv     # Simulated ticket data

