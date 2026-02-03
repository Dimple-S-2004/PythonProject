from PyPDF2 import PdfWriter
import os

merger = PdfWriter()

pdfs = []
n = int(input("How many pdfs do you want to merge?\n"))

for i in range(n):
    while True:
        name = input(f"Enter the name of pdf {i + 1}: ").strip()
        if os.path.isfile(name):
            pdfs.append(name)
            break
        else:
            print(f"File '{name}' not found. Please enter a valid filename or full path.")

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
print("PDFs merged successfully into 'merged-pdf.pdf'")
