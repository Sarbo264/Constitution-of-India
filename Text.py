# Importing PdfReader from the Library PyPDF2
from PyPDF2 import PdfReader
# Creating a Function for Extracting the whole text from the pdf.
def full_article ():
    # Declaring a Variable which will read the PDF
    reader = PdfReader("Constitution.pdf")
    # Declaring an empty string.
    text = ''
    # Running a For Loop from Page 0 to the (last page -1) of the Pdf
    for i in range(len(reader.pages)):
        # Logic for extracting the text from each page and then adding it to the text variable.
        text = text + reader.pages[i].extract_text()
    # Returning the text variable which contains all the text from the Pdf.
    return text

# Adding a function for reading .md Files.
def read_markdown_file(markdown_file):
    # Opening the File in Reading Mode
    with open(markdown_file, 'r', encoding = 'utf-8') as file:
        # Returning the File.
        return file.read()