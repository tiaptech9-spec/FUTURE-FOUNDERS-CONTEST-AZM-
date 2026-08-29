# AI Resume Ranker

AI Resume Ranker is an NLP and Machine-Learning powered resume screening system built with **Flask**, **scikit-learn**, and **python-docx**.
It lets recruiters upload a batch of `.docx` resumes against a job description, automatically scores every candidate using TF-IDF cosine similarity and keyword-overlap matching, and returns a ranked, filterable shortlist.

## BLOG LINK 
https://medium.com/@tiaptech9/ai-resume-ranker-7bf98d5a1a61

## Features

- **Job Description Input** — paste or type the job requirements to screen against
- **Bulk Resume Upload** — upload multiple `.docx` resumes in a single screening run
- **Automated Resume Parsing** — extracts full text, name, email, and phone number from every resume
- **Dual-Signal Matching Engine** — TF-IDF cosine similarity + keyword-overlap scoring, blended into one final match score
- **Auto-Shortlisting** — candidates are automatically classified as Shortlisted / Under Review / Rejected against fixed thresholds
- **Ranked Dashboard** — searchable, filterable, sortable candidate rankings with live statistics
- **Candidate Profile View** — per-candidate score breakdown, assessment, rank, and full resume content
- **Persistent Storage** — all screening results are saved automatically to a local SQLite database

## Dataset Link From Kaggle
   https://www.kaggle.com/datasets/palaksood97/resume-dataset?utm_source=chatgpt.com

## Installation

**Python version requirement:** This project has been tested with **Python 3.10+**.
Using a much older or newer version may cause compatibility issues with some libraries.

1. **Clone this repository**

   ```
   git clone https://github.com/tiaptech9-spec/FUTURE-FOUNDERS-CONTEST-AZM-

2. **Create and activate a virtual environment**

   ```
   python -m venv venv
   venv\Scripts\activate    # On Windows
   source venv/bin/activate # On Linux/Mac
   ```

3. **Install required dependencies**

   ```
   pip install -r requirements.txt
   ```

---

## Usage

Run the Flask app:

```
python app.py
```

Then open the local address shown in the terminal (by default `http://127.0.0.1:5000/`). The app has three views:

1. **Screening Page** (`/`) – enter a job description and upload one or more `.docx` resumes
2. **Dashboard** (`/dashboard`) – view ranked candidates, live statistics, and search/filter by name, status, or minimum score
3. **Candidate Profile** (`/candidate/<id>`) – view a single candidate's score breakdown, assessment, rank, and full resume text

Screening results are stored automatically in `resume_ranker.db` (SQLite), and uploaded resumes are saved inside the `uploads/` folder.

---

## Project Structure

```
AI_Resume_Ranker/
├── app.py                 # Main Flask app: routes, NLP pipeline, matching engine
├── database.py             # SQLite data layer (init, save, search, update, delete)
├── templates/
│   ├── index.html          # Screening page (job description + resume upload)
│   ├── dashboard.html      # Ranked candidate dashboard
│   └── candidate.html      # Candidate profile page
├── static/
│   └── style.css           # Shared stylesheet for all pages
├── uploads/                 # Uploaded resumes (auto-created at runtime)
├── resume_ranker.db         # SQLite database (auto-created at runtime)
├── requirements.txt          # Python dependencies
└── README.md                 # Project info (this file)
```

---

## Notes

- The SQLite database and `uploads/` folder are created automatically the first time the app runs — no manual setup required.
- Only `.docx` resumes are currently supported (see the SRS "Constraints" section for planned PDF support).
- Final match score = `(TF-IDF score × 0.5) + (Keyword-overlap score × 0.5)`.
- Status thresholds: **≥ 70%** → Shortlisted, **50–69%** → Under Review, **< 50%** → Rejected.

---

## Credits

Developed by **Future Founders** — Tanzeela Iftikhar, Dua Shehzadi, and Maryam Waqar — for **TechWiz 6**, under the mentorship of **Sir Ali Raza**.
