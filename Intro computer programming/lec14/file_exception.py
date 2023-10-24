import os.path
import sys

def main():
    # Open file for output
    outfile = open("bruh.txt", "w")
    outfile.write("Hello World\n")
    outfile.write("This is a test\n")
    outfile.write("Goodbye\n")  
    outfile.close()

def main2():
    # Open file for input
    infile = open("bruh.txt", "r")
    print("(1) using read(): ")
    print(infile.read())
    infile.close()

    # Open file for input
    infile = open("bruh.txt", "r")
    print("\n(2) Using read(number): ")
    s1 = infile.read(4)
    print(s1)
    s2 = infile.read(10)
    print(s2)
    infile.close() # Close the input file

    infile = open("bruh.txt", "r")
    print("\n(3) Reading by line: ")
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    print(repr(line1))
    print(repr(line2))
    print(repr(line3))
    print(repr(line4))
    infile.close() # Close the input file

    # Open file for input
    infile = open("bruh.txt", "r")
    print("\n(4) Reading all lines: ")
    print(infile.readlines())
    infile.close() # Close the input file


def main3():
     # Prompt the user to enter filenames
    f1 = input("Enter a source file: ").strip()
    f2 = input("Enter a target file: ").strip()
    
     # Check if target file exists
    if os.path.isfile(f2) :
        print(f2 + " already exists")
        sys.exit()
    
     # Open files for input and output
    infile = open(f1, "r")
    outfile = open(f2, "w")
    
     # Copy from input file to output file
    countLines = countChars = 0
    for line in infile:
        countLines += 1
        countChars += len(line)
        outfile.write(line)
    print(countLines, "lines and", countChars, "chars copied")
    
    infile.close() # Close the input file
    outfile.close() # Close the output file
    
def main4():
    outfile = open("bruh.txt", "a")
    outfile.write("Kekw\n")
    outfile.close()

from random import randint

def main5():
    outfile = open("num.txt", "w")
    for i in range(10):
        outfile.write(str(randint(0,9)) + " ")
    outfile.close()
        
    infile = open("num.txt", "r")
    s = infile.read()
    numbers = [eval(x) for x in s.split()]
    for number in numbers:
        print(number, end=" ")
    infile.close()


