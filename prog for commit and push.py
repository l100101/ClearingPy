import subprocess

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error

def add_all_changes():
    output, error = run_command("git add .")
    if error:
        print(f"Error adding changes: {error.decode('utf-8')}")
    else:
        print("All changes added.")

def commit_changes(message):
    output, error = run_command(f'git commit -m "{message}"')
    if error:
        print(f"Error committing changes: {error.decode('utf-8')}")
    else:
        print(f"Changes committed with message: {message}")

def push_changes(branch):
    output, error = run_command(f"git push origin {branch}")
    if error:
        print(f"Error pushing changes: {error.decode('utf-8')}")
    else:
        print(f"Changes pushed to branch: {branch}")

if __name__ == "__main__":
    commit_message = input("Enter commit message: ")
    branch_name = input("Enter branch name: ")

    add_all_changes()
    commit_changes(commit_message)
    push_changes("main")
