import os

for dirpath, _, filenames in os.walk("."):
    for file in filenames:
        if file.endswith(".ipynb"):
            file_path = os.path.join(dirpath, file)
            os.remove(file_path)
