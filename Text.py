from PyPDF2 import PdfReader
def full_article ():
    reader = PdfReader("Constitution.pdf")
    text = ''
    for i in range(len(reader.pages)):
        text = text + reader.pages[i].extract_text()
    return text

# Adding a function for reading .md Files.
def read_markdown_file(markdown_file):
    with open(markdown_file, 'r', encoding = 'utf-8') as file:
        return file.read()