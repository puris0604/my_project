import os
from dotenv import load_dotenv
import subprocess

load_dotenv()
repo_url = os.getenv("GITHUB_REPO_SSH")

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    print(result.stdout)
    if result.stderr:
        print("⚠️", result.stderr)

def push_to_github():
    run_cmd("git init")

    # 🔹 파일 먼저 만들고 add 해야 git이 인식함
    with open("auto_hello.py", "w") as f:
        f.write('print("Hello from auto script!")\n')

    run_cmd("git add .")
    run_cmd('git commit -m "💻 Auto push from Python script"')
    run_cmd("git branch -M main")
    run_cmd(f"git remote add origin {repo_url}")
    run_cmd("git push -u origin main")

if __name__ == "__main__":
    push_to_github()
    
