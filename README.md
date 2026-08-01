# AI Sales Intelligence Agent

## Overview

AI Sales Intelligence Agent is an end-to-end system that automatically discovers buying intent signals from publicly available web sources, ranks companies based on those signals, and generates personalized outreach messages.

The project uses an open-source LLM (Ollama + Mistral) to analyze web content and identify potential sales opportunities for logistics and post-purchase solutions.

---

# Features

- Search companies from a CSV file
- Scrape public webpages
- Classify webpage types
- Extract buying intent signals using Ollama (Mistral)
- Store extracted signals in SQLite
- Rank companies using weighted intent scoring
- Generate personalized LinkedIn outreach messages
- Generate personalized cold emails
- Export ranked reports as CSV
- Interactive Streamlit Dashboard

---

# Project Architecture

```
Companies.csv
        │
        ▼
Search Engine
        │
        ▼
Web Scraper
        │
        ▼
Page Classifier
        │
        ▼
Ollama (Mistral)
        │
        ▼
Signal Extractor
        │
        ▼
SQLite Database
        │
        ▼
Intent Scoring Engine
        │
        ▼
Company Ranking
        │
        ├──────────────┐
        ▼              ▼
LinkedIn Generator   Email Generator
        │
        ▼
Streamlit Dashboard
```

---

# Tech Stack

- Python 3.11+
- Streamlit
- Ollama
- Mistral
- DuckDuckGo Search
- BeautifulSoup
- SQLite
- Pandas
- Requests
- Pydantic

---

# Project Structure

```
AI-Company-Assignment/

│
├── app.py
│
├── data/
│   ├── companies.csv
│   └── signals.db
│
├── outputs/
│   ├── ranked_companies.csv
│   ├── final_report.csv
│   ├── linkedin_messages.md
│   └── emails.md
│
├── memo/
│   ├── architecture.md
│   └── technical_memo.md
│
├── src/
│   ├── database/
│   ├── llm/
│   ├── outreach/
│   ├── pipeline/
│   ├── ranking/
│   ├── reports/
│   └── search/
│
├── requirements.txt
├── README.md
└── .env.example
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>

cd AI-Company-Assignment
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Download Ollama

https://ollama.com

Pull model

```bash
ollama pull mistral
```

Run Ollama

```bash
ollama serve
```

---

# Running the Project

Process all companies

```bash
python -m src.pipeline.process_all
```

Generate rankings

```bash
python -m src.ranking.scoring_agent
```

Generate LinkedIn messages

```bash
python -m src.outreach.linkedin_generator
```

Generate cold emails

```bash
python -m src.outreach.email_generator
```

Generate report

```bash
python -m src.reports.generate_report
```

Launch Streamlit

```bash
streamlit run app.py
```

---

# Outputs

The project generates:

- ranked_companies.csv
- final_report.csv
- linkedin_messages.md
- emails.md

---

# Assumptions

- Public webpages contain useful buying intent information.
- Higher intent scores indicate stronger sales opportunities.
- All extracted information comes from publicly available sources.

---

# Limitations

- Dynamic websites may not be fully scraped.
- Search engine results can vary over time.
- LLM predictions depend on webpage quality.
- Some extracted signals may require manual validation.

---

# Future Improvements

- Semantic Search using Embeddings
- Multi-Agent Pipeline
- CRM Integration
- Automated Scheduling
- Live Monitoring
- Better Signal Validation
- Email Automation
- Dashboard Analytics

---

# Author

Aswin B