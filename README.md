# PDF Merger (Python)

A simple and beginner‑friendly Python script to merge multiple PDF files into a single PDF using **PyPDF2**.

This project is useful for quickly combining reports, notes, assignments, or any PDFs directly from the command line.

---

##  Features

* Merge **multiple PDFs** into one file
* Validates file paths before merging
* Easy to use (command‑line based)
* Lightweight and fast

---

## Technologies Used

* **Python 3**
* **PyPDF2**
* **OS module**

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/pdf-merger.git
```

2. Navigate to the project directory:

```bash
cd pdf-merger
```

3. Install the required library:

```bash
pip install PyPDF2
```

---

## How to Run

1. Run the script:

```bash
python pdf_merger.py
```

2. Enter how many PDFs you want to merge.
3. Provide the **file name or full path** of each PDF.
4. The merged PDF will be created as:

```
merged-pdf.pdf
```

---

##  Example

```text
How many pdfs do you want to merge?
3
Enter the name of pdf 1: file1.pdf
Enter the name of pdf 2: file2.pdf
Enter the name of pdf 3: file3.pdf
PDFs merged successfully into 'merged-pdf.pdf'
```

---

##  Notes

* Make sure the PDFs exist in the given path.
* Output file will overwrite if `merged-pdf.pdf` already exists.

---

## Future Improvements

* GUI version (using Tkinter)
* Drag & drop support
* Custom output file name
* PDF preview before merging





