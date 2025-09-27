# ✅ Habit Tracker (Streamlit)

A minimal, local-first **Habit Tracker** built with **Python + Streamlit**. Add habits, mark them done daily, and keep streaks — all stored in a simple `data.json`.

> **Live Demo:** *(optional)* Add your Streamlit Cloud link here once deployed.

---

## ✨ Features

- Add habits via sidebar
- Mark habit as done (button auto-disables if already done today)
- Auto-updated **streak** and **last_done** date
- Local JSON persistence (`data.json`)
- One-file app: easy to read & extend

---

## 🧱 Project Structure

```plaintext
habit-tracker/
├─ app.py             # Main Streamlit app
├─ data.json          # Created automatically, stores habits & 
└─ README.md          # Project documentation
```

---

## 🚀 Quickstart

### Prerequisites
- Python **3.9+** (3.10+ recommended)
- pip

### 1) Clone
```bash
git clone https://github.com/Lior-Karayev/Habit-Tracker.git
cd Habit-Tracker
```

### 2) Create and activate a virtual environment
Windows (PowerShell)
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```
macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```
#### If you don’t have **requirements.txt** yet, create it with:
```bash
pip install streamlit
pip freeze > requirements.txt
```

### 4) Run the app
```bash
streamlit run app.py
```
#### Open the Local URL shown in your terminal (usually http://localhost:8501).

### 5) Deactivate the environment (when done)
```bash
deactivate
```