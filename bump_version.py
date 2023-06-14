import sys

def bump_version(version_bump, previous_version):
    major, minor, patch = map(int, previous_version.split('.'))
    if version_bump == 'major':
        major += 1
        minor = 0
        patch = 0
    elif version_bump == 'minor':
        minor += 1
        patch = 0
    else:
        patch += 1
    new_version = f'{major}.{minor}.{patch}'
    with open('version.txt', 'w') as f:
        f.write(new_version)

if __name__ == '__main__':
    version_bump = sys.argv[1]
    previous_version = sys.argv[2]
    bump_version(version_bump, previous_version)
