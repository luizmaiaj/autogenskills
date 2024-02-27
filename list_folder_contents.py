import os
import glob

def list_pyfiles_with_content(directory):
    """Lists Python files (.py) in the given directory and subdirectories along with their content."""
    
    pyfiles = []

    # Use glob to find .py files recursively
    for path in glob.iglob(os.path.join(directory, '**'), recursive=True):
        if os.path.isfile(path) and path.endswith('.py'):
            with open(path, 'r') as file:
                content = file.read()
                pyfiles.append((path, content))

    return pyfiles

def copy_to_clipboard(text):
    """Copies the given text to the macOS clipboard."""
    import subprocess
    
    pbcopy_cmd = 'pbcopy'
    process = subprocess.Popen(pbcopy_cmd, stdin=subprocess.PIPE, shell=True)
    process.communicate(input=text.encode('utf-8'))

# Example usage:
directory = '/Users/luizmaiaj/projects/togoo'

pyfiles_with_content = list_pyfiles_with_content(directory)

print("Python files and their content:")

# Concatenate the output to copy it to clipboard
output = ""
for path, content in pyfiles_with_content:
    output += f"File: {path}\nContent:\n{content}\n\n"

# Copy the output to clipboard
copy_to_clipboard(output)