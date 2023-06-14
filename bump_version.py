import sys

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
    previous_version = sys.argv[2]
    
    new_version = bump_version(previous_version, bump_type)
    print(new_version)
