# Heart Attack Symptom Checker

A decision-support tool designed to raise awareness of heart attack symptoms in women, with particular focus on atypical presentations often missed in traditional diagnostics.

##  Project Overview

This project was created as part of the CREST Silver Award. It addresses the diagnostic gap where women are 50% more likely to be misdiagnosed during a heart attack due to atypical symptom presentations.

**Key Features:**
- Rule-based weighted symptom scoring (1-5 scale)
- Safety override rules for critical combinations
- Graphical user interface (GUI) with Tkinter
- Command-line interface (CLI) for testing
- 20 validated test vignettes

## How to Run

### Requirements
- Python 3.7 or higher
- No external dependencies (uses built-in libraries only!)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR-USERNAME/heart-attack-symptom-checker.git
cd heart-attack-symptom-checker
```

2. Run the GUI version:
```bash
python gui_checker.py
```

Or run the CLI version:
```bash
python tiny_checker.py
```

##  How It Works

The tool uses a weighted scoring system:
- **Chest pain:** 5 points (strong predictor)
- **Radiating pain:** 4 points
- **Shortness of breath:** 4 points
- **Sweating, nausea, back pain, jaw pain:** 3 points
- **Indigestion, anxiety, fatigue:** 2 points
- **Dizziness:** 1 point

**Risk Levels:**
- **Emergency** (≥7 or safety rule): Call 999 immediately
- **A&E** (4-6): Seek urgent care
- **GP** (1-3): Book appointment soon
- **Monitor** (0): Watch for changes

**Safety Override Rules:**
- Chest pain + any symptom ≥3 → Emergency
- Shortness of breath + any other symptom → Emergency
- Radiating pain alone → Emergency

##  Project Structure
```
heart-attack-symptom-checker/
├── tiny_checker.py          # CLI version
├── gui_checker.py           # GUI version with Tkinter
├── symptoms_table.csv       # Symptom data
├── vignettes.md            # 20 test cases
├── limitations.md          # Known limitations
├── research_notes.md       # Background research
├── README.md               # This file
└── documentation/          # Full CREST write-up
```

## Important Disclaimer

**This tool cannot diagnose heart attacks or replace medical judgment.**

If you think you're experiencing a heart attack:
-  Call 999 (UK) or your local emergency number immediately
- Do not wait to use this tool
- Do not drive yourself to hospital

##  Research Sources

- NHS (2024). Heart attack symptoms
- British Heart Foundation (2016, 2019). Gender gap research
- American Heart Association (2022). Women's heart health

## About This Project

Created by: [Your Name]
Award: CREST Silver
Date: January 2026
Time invested: ~25 hours

##  License

This project is open source for educational purposes.

---

**Note:** This is a student project created for educational purposes. It is not intended for clinical use.
