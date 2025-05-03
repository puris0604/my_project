import os
import subprocess
from dotenv import load_dotenv

# ⛳ .env 파일 불러오기
load_dotenv()
repo_url = os.getenv("GITHUB_REPO_SSH")

# ⛳ 명령어 실행 함수
def run_cmd(cmd):
    print(f"\n📦 실행 중: {cmd}")
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print("⚠️", result.stderr.strip())

# ⛳ 메인 기능 함수
def push_to_github():
    run_cmd("git init")

    # 🔹 테스트용 파일 자동 생성
    with open("auto_hello.py", "w") as f:
        f.write('print("Hello from auto script!")\n')

    run_cmd("git add .")
    run_cmd('git commit -m "💻 Auto push from Python script"')
    run_cmd("git branch -M main")

    # 🔹 기존 origin 제거 (있을 경우)
    run_cmd("git remote remove origin")
    run_cmd(f"git remote add origin {repo_url}")

    # 🔹 푸시
    run_cmd("git push -u origin main")

# ⛳ 시작점
if __name__ == "__main__":
    push_to_github()
    
