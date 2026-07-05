# Importing PdfReader from the Library PyPDF2
from PyPDF2 import PdfReader
def main():
    # Taking a Variable which will take input of the Article Number from the User.
    keyword = input("Enter the Article Number you want to find the Description: ")
    output = extraction(keyword)
    print(output)
    
# Makking a function to manage this operations.
def extraction (keyword):
    # Defining a Variable for reading the Pdf
    reader = PdfReader("Constituition.pdf")
    # Checking if the given Input is a integer or not.
    if not keyword.isdigit():
        return 'Invalid Input.\nPlease Try Again.\nPlease note: This Program does not accept any inputs other than Integer.'
    # Excluding Article No. 238 since it is ommited in the constituition and it does not exist.
    elif keyword == '238':
        return 'The Article Number is Ommited in the Constituition of India.\nPlease Try Again.'
    # Excluding Negative numbers and those numbers which are greater than 395 since 395 is the last Article number.
    elif int(keyword) < 1 or int(keyword) > 395:
        return 'Invalid Article Number.\n Please Try Again.'  
    # Working with those Articles which does not satisfy those above conditions.
    else:
        # Declaring an empty String.
        text = ''
        # Declaring a for loop to iterate through the pages of the Pdf and extract the text from each page and store it in the text variable.
        for i in range(len(reader.pages)):
            # Extracting the text from each page and storing it in the text variable.
            text = text + reader.pages[i].extract_text()
        # Using try for handling Formating error and handling unexpected crashesh.
        try:
            # Declaring a variable to find the index of the keyword in the text variable.
            index1 = text.index(' ' + keyword + '.')
            # Making logics for the Article Numbers apart from the Last Article number which is 395.
            if keyword != '395':
                # Declaring a variable to find the index of the next keyword in the text variable.
                index2 = text.index(' ' + str(int(keyword)+1)+ '.')
                # Returning the text from the index1 to index2 which will give the description of the Article Number entered by the User.
                return text[index1:index2]
            # Making logic for the Article number 395.
            else:
                # Returnung text from index1 to end of the file.
                return text[index1:]
        except:
            return f'Formatting error: Could not locate the {keyword} in the PDF file.'

if __name__ == '__main__':
    main()