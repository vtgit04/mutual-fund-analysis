"""
Bluestock Fintech — Mutual Fund Analysis Pipeline
Master run script to execute all analysis notebooks in sequence.
"""

import subprocess
import sys
import os

def run_notebook(notebook_path):
    """Execute a Jupyter notebook and save output."""
    print(f"\n{'='*60}")
    print(f"▶ Running: {notebook_path}")
    print('='*60)
    result = subprocess.run(
        [sys.executable, "-m", "jupyter", "nbconvert",
         "--to", "notebook",
         "--execute",
         "--inplace",
         notebook_path],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        print(f"✅ {notebook_path} completed successfully!")
    else:
        print(f"❌ Error in {notebook_path}:")
        print(result.stderr)

if __name__ == "__main__":
    print("🚀 Bluestock MF Analysis Pipeline Starting...")
    os.makedirs("charts", exist_ok=True)

    notebooks = [
        "EDA_Analysis.ipynb",
        "Performance_Analytics.ipynb",
        "Advanced_Analytics.ipynb"
    ]

    for nb in notebooks:
        if os.path.exists(nb):
            run_notebook(nb)
        else:
            print(f"⚠️ Notebook not found: {nb}")

    print("\n✅ Pipeline complete! Check charts/ folder for outputs.")