import os

head = """\\documentclass[a4paper,12pt]{article}
\\usepackage[T1]{fontenc}
\\usepackage[utf8x]{inputenc}
\\usepackage[spanish]{babel}
\\usepackage{fullpage}
\\usepackage{tikz-uml}
\\sloppy
\\hyphenpenalty 10000000
"""

bodyStart = """\\begin{document}
\\maketitle
\\section{Class Diagram}
\\begin{center}
\\begin{tikzpicture}
"""
bodyEnd = """
\\end{tikzpicture}
\\end{center}
\\end{document}
"""
#title = ""
bodyMiddle = ""
yCorrection = 0
xCorrection = 0
clasesEncontradas = []
proteccion = False
variablesPublicasEncontradas = {}
variablesPrivadasEncontradas = {}
"""
    tipos de variables en c++:
        int
        double
        float
        char
        bool
        enum
        struct
        typedef
"""
tiposVariables = ["int", "double", "float", "char", "bool", "enum", "struct", "typedef"]
funcionesEncontradas = []

def selectFiles(currentPathFiles):
    #global title
    cppFiles = []
    hFiles = []
    for file in currentPathFiles:
        if file.endswith(".cpp"):
            cppFiles.append(file)
        elif file.endswith(".h"):
            hFiles.append(file)
    #title = "\\title{UML Diagram for " +  str(hFiles) + " files}"
    return cppFiles, hFiles

def generateUmlFunctions(line):
    global funcionesEncontradas
    if " " in line:
        for i in range(len(line)):
            if line[i] != " ":
                startFuncion = i
                break
    else:
        for i in range(len(line)):
            if line[i] != "\t":
                startFuncion = i
                break
    if "{" in line:
        endFunction = line.find("{")
    else:
        endFunction = line.find(";")
    nombreFuncion = line[startFuncion:endFunction]
    funcionesEncontradas.append(nombreFuncion)

def generateUmlVariables(line):
    global variablesPublicasEncontradas, variablesPrivadasEncontradas, proteccion, tiposVariables
    for tipo in tiposVariables:
        if tipo in line:
            startDeclarationName = line.find(tipo + " ") + len(tipo) + 1
            if tipo == "enum":
                endDeclarationName = line.find(" ", startDeclarationName)
            else:
                endDeclarationName = line.find(";", startDeclarationName)
            variableName = line[startDeclarationName:endDeclarationName]
            if not proteccion:
                variablesPublicasEncontradas[variableName]=tipo
            else:
                    variablesPrivadasEncontradas[variableName]=tipo
    

def generateUmlPackages(line):
    global clasesEncontradas
    startClassName = line.find("class ") + 6
    endClassName = line.find(" ", startClassName)
    className = line[startClassName:endClassName]
    clasesEncontradas.append(className)

def readFile(file):
    global proteccion, tiposVariables
    f = open(file, "r")
    for x in f:
        if "class" in x:
            generateUmlPackages(x)
        elif "private" in x:
            proteccion = True
        elif "(" in x:
            generateUmlFunctions(x)
        else:
            for tipo in tiposVariables:
                if tipo in x:
                    generateUmlVariables(x)

def walkOnFiles(files):
    for file in files:
        readFile(file)

def generateClases():
    global bodyMiddle, yCorrection, xCorrection, clasesEncontradas, variablesPublicasEncontradas, variablesPrivadasEncontradas, funcionesEncontradas
    for clase in clasesEncontradas:
        bodyMiddle += "\\begin{umlpackage}[x = " + str(xCorrection) + ", y = " + str(yCorrection) + "]{" + clase + "}\n"
        bodyMiddle += "\\umlclass{" + clase + "}{\nPublic:\\\\\n"
        for variable in variablesPublicasEncontradas.items():
            bodyMiddle += variable[0] + " : " + variable[1] + "\\\\"
        bodyMiddle += "\nPrivate:\\\\\n"
        for variable in variablesPrivadasEncontradas.items():
            bodyMiddle += variable[0] + ":" + variable[1] + "\\\\"
        bodyMiddle += "\n}{\\\\\n"
        for function in funcionesEncontradas:
            bodyMiddle += function + "\\\\"
        bodyMiddle += "}\n"
        bodyMiddle += "\\end{umlpackage}"
        yCorrection -= 10

def main():
    global bodyMiddle
    currentPathFiles = os.listdir()
    cppFiles, hFiles = selectFiles(currentPathFiles)
    walkOnFiles(cppFiles)
    walkOnFiles(hFiles)
    generateClases()
    file = open("output.tex", "w+")
    final = head + bodyStart + bodyMiddle + bodyEnd 
    file.write(final)
    

if __name__ == '__main__':
    main()