# ExpllAI‑Mobility (Group G3, PI Project)

**Repository for the PI “Exploiting Open Data with AI – Mobility”**

---

## 📁 Repository Structure

```
PI_ExpllAI-Mobility/
├── .vscode/                   # VS Code settings (formatting, debugging, etc.)
├── data/                     # The raw data
├── data-analysis/            # notebooks and custom python modules and folders to save intermediate and final results
│   ├── data/                 # Data folder to store processed data as well as final results
│   ├── EDA reports/          # Exploratory Data Analysis reports are saved here
│   └── requirements.txt      # requirements for data analysis part           
├── prediction/               # Predictive modeling and evaluation
│   ├── data/                 # Data sources for predictions
│   ├── ev_scenarios/         # Scenarios creation
│   ├── images/               # Generated images
│   ├── notebook/             # Jupyter notebooks for predictions
│   ├── prediction-results/   # Predictions results storage
│   └── requirements.txt      # requirements for the prediction part
├── .gitignore                 # Standard ignores (e.g. data, models)
└── README.md                  # Project overview and instructions
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+  
- Create a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # macOS/Linux
  venv\Scripts\activate     # Windows
  ```
- Install dependencies for analysis and predictions:
  ```bash
  pip install -r data-analysis/requirements.txt
  pip install -r prediction/requirements.txt
  ```

---



---
