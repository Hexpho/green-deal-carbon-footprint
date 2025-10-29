# Green Deal Carbon Footprint (Colab Notebook)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/USER/REPO/blob/main/notebooks/green_deal.ipynb)

An educational, notebook-based prototype for estimating and explaining carbon footprint metrics aligned with EU Green Deal ideas.  
This repo contains a ready-to-run Jupyter/Colab notebook and a minimal Python environment for local execution.

## Quick Start (Colab)
1. Click the **Open in Colab** badge above.  
2. If the badge link hasn't been updated yet, open the notebook directly on GitHub, click **Raw**, then **Save As** to download `green_deal.ipynb`.  
3. In Colab, **File ▸ Upload notebook...** and run all cells.

> **Note:** The notebook is self-contained. If an optional API key (e.g., Groq/OpenAI) is used in some cells, leave it empty to run in rule-based demo mode.

## Quick Start (Local)
```bash
# 1) Create & activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) Install requirements
pip install -r requirements.txt

# 3) Launch Jupyter
pip install notebook
jupyter notebook notebooks/green_deal.ipynb
```

## Repository Structure
```
.
├── notebooks/
│   └── green_deal.ipynb
├── src/
├── data/               # place input csv/json here (ignored by git)
├── outputs/            # figures/exports land here (ignored by git)
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Configuration & Secrets
If the notebook references API keys, create a file named `.env` in the project root:
```
GROQ_API_KEY=...
OPENAI_API_KEY=...
```
> If you don't have keys, cells should still run in **fallback (rule-based) mode** where applicable.

## Reproducibility
- Use the exact package versions from `requirements.txt` for consistent results.
- For long runs, set a random seed where noted in the notebook.

## Citing
If this helps your thesis or research:
```
Burmaoğlu, B. (2025). Green Deal Carbon Footprint (Colab Notebook). GitHub repository.
```


## License
MIT — see `LICENSE`.
