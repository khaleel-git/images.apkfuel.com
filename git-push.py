import os
import datetime

# Working directory
working_dir = "/home/apkfuel/htdocs/images.apkfuel.com"
# Change directory
repo_path = working_dir
os.chdir(repo_path)

# Full path to Git executable
git_executable = "/usr/bin/git"

try:
    print("Working Directory:", repo_path)

    # Check Git version
    git_version = os.popen(f"{git_executable} --version").read().strip()
    print("Git Version:", git_version)

    # Check Git status
    git_status = os.popen(f"{git_executable} status").read()
    print("Git Status:")
    print(git_status)

    # Git commands
    os.system(f"{git_executable} add .")
    os.system(f"{git_executable} commit -m '{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}'")
    os.system(f"{git_executable} fetch")
    os.system(f"{git_executable} pull")
    os.system(f"{git_executable} push -u origin master")
    print("Git operations completed successfully")
except Exception as e:
    print("Error during git operations:", e)