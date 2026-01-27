import subprocess

def retrain():
    subprocess.run(["dvc", "repro"], check=True)

if __name__ == "__main__":
    retrain()