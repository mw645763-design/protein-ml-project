# GB1 protein fitness prediction

A laptop-friendly PyTorch project exploring whether models can predict the effects of amino-acid mutations on GB1 binding fitness.

## Getting started (Windows / VS Code)
1. Open this folder in VS Code.
2. Create a Python virtual environment: `py -m venv .venv`
3. Activate it in PowerShell: `.\.venv\Scripts\Activate.ps1` (or select the `.venv` interpreter in VS Code).
4. Install packages: `python -m pip install -r requirements.txt`
5. Verify installation: `python check_setup.py`
6. Open `notebooks/01_explore_data.ipynb` and select the `.venv` kernel.

## Research question
Can a small neural network predict held-out GB1 variant fitness better than an additive baseline? How does generalisation change with mutation depth?

## Workflow
- `01_explore_data.ipynb`: inspect the dataset and its provenance.
- `02_baseline.ipynb`: establish a leakage-safe additive baseline.
- `03_pytorch_model.ipynb`: build and train a small MLP.
- `04_evaluate.ipynb`: compare predictions, examine mutation-depth performance.

## Important
The notebooks are **scaffolds**, not completed analyses. No dataset is included. Obtain GB1 data and official split definitions from the [FLIP benchmark](https://github.com/J-SNACKKB/FLIP), record the exact dataset/version and split, and keep all held-out examples out of training and model selection.

Avoid interpreting predicted variants as experimentally validated improvements.
