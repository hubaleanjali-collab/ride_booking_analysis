
# Ride Booking Dataset — Analysis Project

This repo analyzes a ride-booking dataset: cleaning, descriptive stats, customer behavior, driver performance, and operational metrics.

## Folder Structure
```
ride-booking-analysis/
├── data/                # Put CSV/Excel here (e.g., Dataset.csv)
├── notebooks/           # Jupyter notebooks
├── scripts/             # Reusable Python modules
├── reports/             # Exported charts, tables, PDFs
├── requirements.txt     # Python dependencies
└── README.md            # Docs (this file)
```

---

## How to Run (Local Machine)

### 1) Install prerequisites
- **Python 3.10+**: https://www.python.org/downloads/
- **Git**: https://git-scm.com/downloads
- **VS Code** (recommended): https://code.visualstudio.com/

### 2) Get the project
- If you already created a GitHub repo, **clone it**. Otherwise, extract the zip I provided and open the folder in VS Code.

### 3) Create a virtual environment and install packages
```bash
# in the project root (ride-booking-analysis)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### 4) Start Jupyter
```bash
jupyter lab
# or
jupyter notebook
```
Open the notebook in `notebooks/` and run the cells top-to-bottom.

### 5) Where to put things
- Raw **data** → `data/` (e.g., `data/Dataset.csv`)
- **Cleaning & EDA** → `notebooks/`
- **Reusable functions** → `scripts/`
- **Charts & tables** → `reports/`
- **Docs** → `README.md`

### 6) Git workflow (typical day)
```bash
git init                         # only once if starting fresh
git remote add origin <your-github-repo-url>

git checkout -b data-cleaning    # make a feature branch
# do work, run notebooks, edit scripts
git add .
git commit -m "Cleaned data and added EDA notebook"
git push -u origin data-cleaning

# open a Pull Request on GitHub, review, then merge to main
```

> First time pushing `main` from local?
```bash
git checkout -b main
git add .
git commit -m "Initial project structure"
git push -u origin main
```

---

## How to Run (Google Colab)

1. Zip the project (or use the zip I provided), upload to Google Drive, then in Colab mount Drive.
2. Alternatively, if your code is on GitHub, open Colab and do:
```python
!git clone <your-repo-url>
%cd ride-booking-analysis
!pip install -r requirements.txt
```
3. Open the notebooks in `/notebooks/`, and ensure paths like `../data/Dataset.csv` are correct.

---

## How to Run (GitHub Codespaces)

1. Open your repo on GitHub → **Code** → **Codespaces** → *Create codespace*.
2. In the integrated terminal:
```bash
pip install -r requirements.txt
jupyter lab --ip=0.0.0.0 --no-browser
```
3. Use the forwarded port to open Jupyter in the browser and run notebooks in `/notebooks/`.

---

## Notebooks Included
- `01_data_cleaning.ipynb` — load, inspect, clean, standardize types & categories, save `data/cleaned_Dataset.csv`
- `02_analysis.ipynb` — descriptive analysis, cancellations, behavior, driver performance, operational metrics, export charts to `reports/`

## Scripts Included
- `scripts/data_cleaning.py` — helper functions for parsing datetimes, fixing categories, handling missing values
- `scripts/analysis.py` — functions to compute KPIs & plots

---

## Repro Tips
- Keep raw data immutable; write cleaned data to `data/cleaned_*.csv`.
- Prefer functions in `scripts/` and import them into notebooks to avoid copy-paste.
- Commit little and often. Use branches per feature (_data-cleaning_, _driver-metrics_, etc.).

## License
Personal/educational use.
