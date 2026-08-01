# Technical Memo

## Problem Statement

Sales teams spend considerable time manually identifying companies that exhibit buying intent. This project automates that process by discovering buying signals from public web sources.

---

# Solution

The system consists of six stages:

1. Company Search
2. Web Scraping
3. Signal Extraction
4. Signal Storage
5. Intent Ranking
6. Personalized Outreach Generation

---

# Workflow

Companies

↓

Search Engine

↓

Web Scraper

↓

Page Classifier

↓

Ollama (Mistral)

↓

Signal Extraction

↓

SQLite

↓

Ranking

↓

LinkedIn Messages

↓

Cold Emails

↓

Reports

---

# Technologies

- Python
- Ollama
- Mistral
- SQLite
- BeautifulSoup
- Requests
- Streamlit

---

# Design Decisions

- SQLite was selected because it is lightweight and easy to use.
- Ollama enables local inference without requiring paid APIs.
- Streamlit provides a simple interface for demonstrating results.
- Buying intent is calculated using weighted scoring.

---

# Assumptions

- Public web data is sufficient for detecting buying intent.
- Recent company events indicate potential sales opportunities.
- Signal confidence reflects extraction quality.

---

# Limitations

- Search engine results may vary.
- Dynamic websites may restrict scraping.
- LLM outputs are probabilistic.
- Some extracted signals may be false positives.

---

# Future Improvements

- Vector Search
- Multi-Agent Workflow
- CRM Integration
- Automated Scheduling
- Better Confidence Calibration
- Knowledge Graph