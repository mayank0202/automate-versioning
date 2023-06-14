import sys
import semver
from github import Github

# Get the commit message from the latest commit
latest_commit_message = sys.argv[1]

# Get the previous tag
previous_tag = sys.argv[2]

# Check if the latest commit message contains a version bump indicator
if '#major' in latest_commit_message:
    bump_type = 'major'
elif '#minor' in latest_commit_message:
    bump_type = 'minor'
elif '#patch' in latest_commit_message:
    bump_type = 'patch'
else:
    # If no version bump indicator is found, search the previous commits
    g = Github()
    repo = g.get_repo('your/repo')  # Replace with your repository information

    # Iterate through previous commits
    for commit in repo.get_commits():
        commit_message = commit.commit.message
        if '#major' in commit_message:
            bump_type = 'major'
            break
        elif '#minor' in commit_message:
            bump_type = 'minor'
            break
        elif '#patch' in commit_message:
            bump_type = 'patch'
            break
    else:
        # If no suitable indicator is found in any previous commit, default to 'patch'
        bump_type = 'patch'

# Bump the version based on the identified bump type
new_version = semver.bump_version(previous_tag, bump_type)
print(new_version)
