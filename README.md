# 📧🧠 Mailvora — AI Email & Communication Tracker

Turn Your Inbox into Actionable Intelligence

Python · Streamlit · Rule-based NLP · Modular Architecture

---

## 🏆 Overview

Mailvora is an intelligent email assistant that transforms raw emails into meaningful insights.
Instead of just displaying emails, it helps users:

* Identify important tasks
* Detect deadlines
* Track pending follow-ups
* Get a quick summary of inbox activity

---

## 🚀 Problem Statement

Managing emails manually is inefficient and error-prone:

* Important tasks get buried in long threads
* Deadlines are often missed
* Follow-ups are forgotten
* Users lack a clear overview of inbox activity

Most systems only display emails — they don’t **analyze or assist**.

---

## 💡 Our Solution

Mailvora acts as a **smart assistant** that:

```
📥 READ emails  
📌 CLASSIFY importance  
📋 EXTRACT tasks  
🔔 DETECT follow-ups  
📊 SUMMARIZE insights  
```

👉 Result: A cleaner, smarter, and actionable inbox

---

## 🧠 Key Features

### 📌 Email Classification

Categorizes emails into:

* Action Required
* Meeting
* Follow-up
* Informational

---

### 📋 Task & Deadline Extraction

* Identifies tasks from email content
* Detects deadlines like "Friday", "Tomorrow"

---

### 🔔 Follow-up Detection

* Detects pending responses
* Highlights emails needing user action

---

### 📊 Summary Dashboard

Provides quick insights:

* Total emails
* Action required
* Meetings
* Pending follow-ups

---

### 🔍 Search & Filter

* Search emails instantly
* Filter by category

---

## 🏗️ System Architecture

```
Mailvora/
│
├── app.py                  # Streamlit UI
├── data/
│   └── emails.json        # Sample email dataset
│
└── utils/
    ├── loader.py          # Load emails
    ├── classifier.py      # Email classification
    ├── extractor.py       # Task & deadline extraction
    ├── followup.py        # Follow-up detection
    └── summary.py         # Summary generation
```

---

## 🔄 Workflow Pipeline

```
Load Emails
   ↓
Classify Emails
   ↓
Extract Tasks & Deadlines
   ↓
Detect Follow-ups
   ↓
Generate Summary
   ↓
Display in UI
```

---

## 📅 Development Progress

### 📅 Day 1

* Project setup
* Streamlit app initialization
* Displayed emails from dataset

---

### 📅 Day 2

* Implemented email classification logic
* Categorized emails into meaningful groups

---

### 📅 Day 3

* Added task and deadline extraction
* Improved backend modular structure

---

### 📅 Day 4

* Implemented follow-up detection module
* Identified emails requiring user response
* Integrated follow-up status into UI

---

### 📅 Day 5

* Implemented summary module (summary.py)
* Displayed key insights (emails, tasks, follow-ups)
* Enhanced UI with dashboard and structured layout

---

## 🚀 Current Status

The project is now a **working intelligent email assistant prototype** with:

* Functional UI (Streamlit)
* Modular backend architecture
* Email intelligence features
* Summary dashboard for insights

---

## 🔑 Key Improvements (Day 1 → Day 5)

* Static email viewer → Intelligent assistant
* Added classification and extraction logic
* Introduced follow-up tracking
* Built summary dashboard
* Improved UI and usability

---

## 🛠️ Tech Stack

| Layer    | Technology     |
| -------- | -------------- |
| Frontend | Streamlit      |
| Backend  | Python         |
| Data     | JSON           |
| Logic    | Rule-based NLP |

---

## ⚡ Quick Start

```bash
git clone <https://github.com/nivedithav04/H2H-Echo-Mailvora>
cd Mailvora

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

---

## 🎯 Future Scope

* 🤖 AI-based email summarization
* 📅 Smart deadline prioritization
* ⭐ Highlight urgent emails
* 📱 UI/UX enhancements
* 🔔 Notifications for follow-ups

---

## 🤝 Team

* Developer 1: UI & Integration
* Developer 2: Backend Logic & Processing

---

## 📄 License

This project is developed for hackathon purposes.
