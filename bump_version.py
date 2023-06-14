import sys
import subprocess
import re

def get_latest_commit_message():
    command = ["git", "log", "-1", "--pretty=format:%s"]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()

def get_version_from_commit_message(commit_message):
    pattern = r"#(\d+\.\d+\.\d+)"
    matches = re.findall(pattern, commit_message)
    if matches:
        return matches[0]  # Return the first match
    return None


def bump_version(previous_version, bump_type):
    major, minor, patch = previous_version.split('.')
    if bump_type == "major":
        major = str(int(major) + 1)
        minor = "0"
        patch = "0"
    elif bump_type == "minor":
        minor = str(int(minor) + 1)
        patch = "0"
    elif bump_type == "patch":
        patch = str(int(patch) + 1)
    else:
        print("Invalid bump_type provided")
        sys.exit(1)
    
    new_version = f"{major}.{minor}.{patch}"
    return new_version

if __name__ == "__main__":
    bump_type = sys.argv[1]
    latest_commit_message = get_latest_commit_message()
    previous_version = get_version_from_commit_message(latest_commit_message)
    
    if previous_version is None:
        print("No version tag found in the commit message.")
        sys.exit(1)
    
    new_version = bump_version(previous_version, bump_type)
    print(new_version)
