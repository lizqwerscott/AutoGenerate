import os
import sys
import getopt

dirPath = ""
className = ""

def getInput(argv):
    global dirPath
    global className
    try:
        opts, args = getopt.getopt(argv, "hn:p", ["name=", "path="])
    except getopt.GetoptError:
        print("main.py -n <class name> -p <path dir>")
        print("or main.py --name <class name> --path <path dir>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("main.py -n <class name> -p <path dir>")
            print("or main.py --name <class name> --path <path dir>")
            sys.exit()
        elif opt in ("-n", "--name"):
            className = arg
        elif opt in ("-p", "--path"):
            if os.path.isdir(arg):
                dirPath = arg
            else:
                print("path: ", arg)
                print("path is not dir")
                sys.exit()
            
def replaceFile(fileName, key, new_content):
    with open(fileName, encoding="UTF-8") as f:
        content = f.read()
        content = content.replace(key, new_content)
        return content
    
def replaceContent(key, old_content, new_content):
    return old_content.replace(key, new_content)
    
def saveFile(fileName, content):
    with open(fileName, encoding="UTF-8", mode="w") as f:
        f.write(content)

def generateClass():
    global dirPath
    global className
    
    path = os.path.dirname(__file__) + "/templetes/c++/"
    
    classHFile = path + "class.h"
    classCppFile = path + "class.cpp"

    contentH = replaceFile(classHFile, "$D", className.upper())
    contentH = replaceContent("$c", contentH, className)
    contentCpp = replaceFile(classCppFile, "$c", className)
    
    newFileHName = dirPath+ className + ".h"
    newFileCppName = dirPath + className + ".cpp"
    
    saveFile(newFileHName, contentH)
    saveFile(newFileCppName, contentCpp)
    print("Finish generate!")
    
if __name__ == "__main__":
    getInput(sys.argv[1:])
    if dirPath != "" and className != "":
        generateClass()

