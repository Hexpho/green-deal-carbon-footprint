import os, sys, subprocess, pathlib

def main():
    nb = "notebooks/green_deal.ipynb"
    if not os.path.exists(nb):
        print("Notebook not found:", nb)
        sys.exit(1)
    # Convert to HTML using nbconvert if installed
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "nbconvert", "jupyter"])
        subprocess.check_call([sys.executable, "-m", "jupyter", "nbconvert", "--to", "html", nb, "--output-dir=outputs"])
        print("Exported HTML to outputs/")
    except subprocess.CalledProcessError as e:
        print("Failed to export. Install jupyter/nbconvert and try again.")
        sys.exit(2)

if __name__ == "__main__":
    main()
