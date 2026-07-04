# Importing PdfReader from the Library PyPDF2
from PyPDF2 import PdfReader
# Defining a Variable for reading the Pdf
reader = PdfReader("Constituition.pdf")
# Taking a Variable which will take input of the Article Number from the User.
keyword = input("Enter the Article Number you want to find the Description: ")
# Checking if the given Input is a integer or not.
if not keyword.isdigit():
    print("Invalid Input.")
    print("Please Try Again.")
# Excluding Article No. 238 since it is ommited in the constituition and it does not exist.
elif keyword == '238':
    print("This Article does not Exist.")
    print("Try Again with another Article Number.")
# Working with those Articles which does not satisfy those above conditions.
else:
    # Declaring an empty String.
    text = ''
    # Declaring a for loop to iterate through the pages of the Pdf and extract the text from each page and store it in the text variable.
    for i in range(len(reader.pages)):
        # Extracting the text from each page and storing it in the text variable.
        text = text + reader.pages[i].extract_text()
    # Declaring a variable to find the index of the keyword in the text variable.
    index1 = text.index(' ' + keyword + '.')
    # Making logics for the Article Numbers apart from the Last Article number which is 395.
    if keyword != '395':
        # Declaring a variable to find the index of the next keyword in the text variable.
        index2 = text.index(' ' + str(int(keyword)+1)+ '.')
         # Printing the text from the index1 to index2 which will give the description of the Article Number entered by the User.
        print(text[index1:index2])
    # Making logic for the Article number 395.
    else:
        print(text[index1:])