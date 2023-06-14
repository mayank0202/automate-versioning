import sys
import semver

bump_type = sys.argv[1]

# Read the previous version from the version.txt file
with open("version.txt", "r") as file:
    previous_version = file.read().strip()

# Bump the version
if bump_type == "major":
    new_version = semver.bump_major(previous_version)
elif bump_type == "minor":
    new_version = semver.bump_minor(previous_version)
else:
    new_version = semver.bump_patch(previous_version)

# Write the new version to the version.txt file
with open("version.txt", "w") as file:
    file.write(new_version)

print(new_version)
