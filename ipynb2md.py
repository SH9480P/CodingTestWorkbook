import json
import os
from pathlib import Path

def readFile(fileName):
    with open(fileName, "r", encoding="utf-8") as infile:
        content = infile.read()
    return content

def writeFile(fileName, data):
    with open(fileName, "w", encoding="utf-8") as outfile:
        outfile.write(data)

def concatNotebookCellSource(source: list):
    data = ''
    for line in source:
        data += line
    return data

def getCells(notebook: dict):
    return notebook['cells']

def concatNotebookCells(cells: list):
    data = ''
    for cell in cells:
        concatedSource = concatNotebookCellSource(cell['source'])
        if cell['cell_type'] == 'code':
            data += '```python\n'
            data += concatedSource
            data += '\n```'
        else:
            data += concatedSource
        data += '\n'
    return data

def getNotebookFiles():
    ipynb_files = []
    for dirpath, _, filenames in os.walk("."):
        for file in filenames:
            if file.endswith(".ipynb"):
                ipynb_files.append(os.path.join(dirpath, file))
    return ipynb_files

def changeExt(filePath, extName):
    return f'{os.path.splitext(filePath)[0]}.{extName}'


files = getNotebookFiles()
for file in files:
    notebookData = readFile(file)
    cells = getCells(json.loads(notebookData))
    data = concatNotebookCells(cells)
    writeFile(changeExt(file, 'md'), data)
