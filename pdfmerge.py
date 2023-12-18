# list all files in the current directory with .pdf extension
# merge all files into one pdf file
#
# usage: python pdfmerge.py
#
# It will then list all files with .pdf extension in the current directory
# and ask the user if they want to merge the files
# If the user answers yes, then it will merge the files into result.pdf
# If the user answers no, then it will exit without merging any files
#
import os
from PyPDF2 import PdfMerger

pdfs = [a for a in os.listdir('.') if a.endswith(".pdf")]

# If no pdf files found, then print message and exit
if len(pdfs) == 0:
    print("No pdf files found in the current directory")
    exit(0)

merger = PdfMerger()

# print("Merge the following files?:" + str(pdfs))
# ask the user if they want to merge the files
answer = input("Merge the following files?:" + str(pdfs) + " (Y/N)? Y")
if answer == "Y" or answer == "y" or answer == "":
    for pdf in pdfs:
        merger.append(open(pdf, 'rb'))
    with open("result.pdf", "wb") as fout:
        merger.write(fout)

    print("Merged files into result.pdf")
else:
    print("No files merged")