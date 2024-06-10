import os
import subprocess

# Increment version number
def increment_version(version):
    parts = version.split('.')
    if len(parts) == 2:
        parts.append('0')  # Assume patch is 0 if missing
    major, minor, patch = map(int, parts)
    return f"{major}.{minor}.{patch + 1}"

# Read setup.py and update version
with open('setup.py', 'r') as file:
    setup_content = file.readlines()

for i, line in enumerate(setup_content):
    if 'version=' in line:
        current_version = line.split('=')[1].strip().strip("'").strip(",").strip()
        current_version = current_version.replace("'", "").replace(",", "").strip()
        print(f"Current version raw: {line.split('=')[1]}")
        print(f"Current version cleaned: {current_version}")
        new_version = increment_version(current_version)
        setup_content[i] = f"    version='{new_version}',\n"
        break

with open('setup.py', 'w') as file:
    file.writelines(setup_content)

# Set TWINE_PASSWORD environment variable
os.environ['TWINE_PASSWORD'] = "pypi-AgEIcHlwaS5vcmcCJGNiNDhhY2Y5LWEzNDgtNDQ0Ny1hZGIwLWI1YjVmY2E3NjJlOAACFFsxLFsiYWdlbnR4LXRvb2xzIl1dAAIsWzIsWyIyMGEzNWFmNy05NTgwLTQzOTItODllYS1kOGViMTk3OWMwOWEiXV0AAAYgIHPdyWr-S8L-LdLZsrABUH872W_dK0c0LiJ8K1UzPZw"

# Remove dist directory
if os.path.exists('dist'):
    subprocess.run(['rm', '-rf', 'dist'])

# Build the package
subprocess.run(['python', '-m', 'build'])

# Upload to PyPI
subprocess.run(['twine', 'upload', 'dist/*'])

# Push changes to GitHub
subprocess.run(['git', 'add', 'setup.py'])
subprocess.run(['git', 'commit', '-m', f'Release version {new_version}'])
subprocess.run(['git', 'push', 'origin', 'main'])