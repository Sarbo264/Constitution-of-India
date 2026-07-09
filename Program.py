# Importing articles_list and Omitted_articles from the ArticleList file
from ArticleList import articles_list, Omitted_articles
# Importing full_article from Text file
from Text import full_article
# Declairing a main function.
def main():
    # Taking a Variable which will take input of the Article Number from the User.
    keyword = input("Enter the Article Number you want to find the Description: ")
    # Storing the extracted text in the output.
    output = extraction(keyword)
    # Printing the Output.
    print(output)

# Declairing a extraction function whose parameters will be keywords.
def extraction (keyword):
    # Extracting all the text of the PDF in the text variable.
    text = full_article()
    # Checking if the keyword is in the articles_list or not.
    if keyword in articles_list:
        try:
            # Finding the index number of the keyword in the articles_list
            article_index = articles_list.index(keyword)
            # Finding the index number of the required article number in the text variable.
            index1 = text.index(keyword+'.')
            # Checking if the article number is not the last Article number in the Constitution.
            if keyword != articles_list[len(articles_list)-1]:
                # Finding the next article number.
                next_article = articles_list[article_index + 1]
                # Finding the index number of the next_article in the text variable.
                index2 = text.index(next_article+'.',index1 + len(keyword))
                # Checking for Duplication in the Text Variable
                duplicate = text.find(keyword+'.',index1+len(keyword),index2)
                # Checking if the any duplication is found or not.
                if duplicate != -1:
                    # Making the new value of index2 to the duplicate value.
                    index2 = duplicate
                # Returning the text from thr index1 to index2
                return text[index1:index2]
            else:
                # Returning the text from the index1 to the end of the text variable.
                return text[index1:]
        except:
            return f'Formatting Error in the PDF.\n{keyword} not found in the PDF.\nPlease Try Again.'
    # Checking if the keyword is in the Omitted_articles or not.
    elif keyword in Omitted_articles:
        # Returning the Error Message for Ommited Articles.
        return 'The Article Number is Ommited in the Constituition of India.\nPlease Try Again.'
    # If the keyword is not in the articles_list or Omitted_articles then returning the Error Message.
    else:
        # Returning the Error Message for Invalid Articles.
        return 'Invalid Article Number.\n Please Try Again.'
# Calling the main function.
if __name__ == '__main__':
    main()