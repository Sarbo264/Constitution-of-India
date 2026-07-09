# Importing Library Streamlit
import streamlit as st
# Importing Functions from the Program.py File
from Program import extraction
# Importing Functions from the Text.py File
from Text import read_markdown_file
# Importing articles_list, Omitted_articles from ArticleList File
from ArticleList import articles_list, Omitted_articles
# Main Function
def main():
    # Making the Page Configurations of the Webpage
    st.set_page_config(
        page_title = "THE ARTICLE ENGINE",
        page_icon = "📜",)
    # Storing the Search History
    if 'search_history' not in st.session_state:
        st.session_state.search_history = []
    # Making the Header and Title of the Webpage.
    st.title("THE ARTICLE ENGINE", text_alignment = 'center', width= 700)
    st.header("Precision Extraction from the Constituition of India.", text_alignment = 'center', width = 700)
    st.divider()
    st.space("medium")
    # Making the Body of the Web Page
    content = read_markdown_file("Description.md")
    st.markdown(content)
    st.divider()
    # Declaring the Text Box and a Switch
    with st.form(key = 'Extraction', border = False):
        col1, col2 = st.columns([6,1])
    # Making the Text Box
    with col1:
        keyword = st.text_input(
            label = 'Article Number',
            placeholder = 'Enter the Article Number you want to find the Description(e.g., 2A): ',
            label_visibility = 'collapsed',
        )
    # Making the Switch
    with col2:
        press = st.form_submit_button("EXTRACT", icon_position= 'right')
    if press:
        if keyword:
            # Storing the Article numbers to a Search History
            if keyword not in st.session_state.search_history:
                st.session_state.search_history.append(keyword)
    st.divider()
    # Making the Extracting Box
    if press:
        if not keyword:
            st.error("No Input found from the User.")
        else:
            with st.spinner(f"Extracting Article {keyword}: "):
                # Calling the extraction function.
                output = extraction(keyword)
            with st.container(border = True):
                # For those Inputs which are either Invalid or the Article is Ommited from the Constituition
                if 'Please Try Again.' in output:
                    st.error(output)
                # For those Inputs which are Valid
                else:
                    st.success(f"Extraction Complete of Article {keyword}.")
                    st.text(output)
    # Making the Side Bar of the Webpage
    st.sidebar.header('Platform Guide ⚙️')
    st.sidebar.info('This engine extracts official legal text directly from the Constitution of India.')
    st.sidebar.divider()
    st.sidebar.caption('Rules: Only Valid Article Numbers are Accepted.')
    st.sidebar.caption('No Inputs other than Articles Numbers are not Encouraged.')
    st.sidebar.divider()
    # Making Search History in the Side Bar.
    st.sidebar.subheader("Search History: ")
    search_article = st.sidebar.text_input("Enter the Article Number to search in Search History: ")
    if search_article in st.session_state.search_history and search_article in articles_list:
        press_searchhistory = st.sidebar.button(f"Article No. {search_article}", width = 'stretch', key = 'Search_History')
        if press_searchhistory:
            with st.container(border = True):
                st.text(extraction(search_article))
    # Logic for Search History
    if len(st.session_state.search_history) > 0:
        for i in reversed(st.session_state.search_history):
            if i in articles_list:
                press_sidebutton = st.sidebar.button(f"Article No. {i}", width = 'stretch')
                if press_sidebutton:
                    with st.container(border = True):
                        st.text(extraction(i))
            elif i in Omitted_articles:
                press_sidebutton = st.sidebar.button(f"Article No. {i}", width = 'stretch')
                if press_sidebutton:
                    with st.container(border = True):
                        st.text(extraction(i))
            else:
                st.sidebar.error(f"Invalid Input of {i}")          
    else:
        st.sidebar.code('No History Found')
# Calling the Main Function
if __name__ == '__main__':
    main()