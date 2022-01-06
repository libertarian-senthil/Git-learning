import sys 
import os


cmd = sys.argv  # command from the terminal or shell.

def document()->None:
    """
    Read and print the content in the doc.txt file
    """

    with open("doc.txt") as handle:     # File handling.
        documentation = handle.readlines()

    for i in documentation:     # Printing the lines in the doocument. 
        print(i,end = " ")

# version format: year-month-version_number(type)
__version__ = "2022.1.1(Pre-release)"

try:

    if cmd[1] in ["-h", "--help"]:   # For help -h or --help
        document()

    elif cmd[1] in ["-d", "--delete"]:    # For delete option.
        if cmd[2] == "-f":      # for delteting particular file.
            os.remove(os.getcwd()+"\\"+cmd[3])
        elif cmd[2] == "e":
            extension = cmd[3]
            
    elif cmd[1] in ["-v", "--version"]:     # For version 
        print("\nThe current version of LDS: ",__version__)
    

except IndexError:
    document()

finally:
    print("\n\nExecution was successful\n")