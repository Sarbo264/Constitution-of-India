# Importing Library Streamlit
import streamlit as st
# Importing Functions from the Program.py File
from Program import extraction, read_markdown_file
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
    col1, col2 = st.columns([6,1])
    # Making the Text Box
    with col1:
        keyword = st.text_input(
            label = 'Article Number',
            placeholder = 'Enter the Article Number you want to find the Description(e.g., 9): ',
            label_visibility = 'collapsed',
        )
    # Making the Switch
    with col2:
        press = st.button("EXTRACT", icon_position= 'right')
    if press:
        if keyword:
            # Storing the Article numbers to a Search History
            if keyword not in st.session_state.search_history:
                st.session_state.search_history.append(keyword)
    st.divider()
    # Making the Extracting Box
    if press:
        with st.spinner("Extracting: "):
            # Calling the extraction function.
            output = extraction(keyword)
        st.success("Extraction Complete.")
        with st.container(border = True):
            # For those Inputs which are either Invalid or the Article is Ommited from the Constituition
            if 'Please Try Again.' in output:
                st.error(output)
            # For those Inputs which are Valid
            else:
                st.write(output)
    else:
        st.error("No Input found from the User.")
    # Making the Side Bar of the Webpage
    st.sidebar.header('Platform Guide ⚙️')
    st.sidebar.info('This engine extracts official legal text directly from the Constitution of India.')
    st.sidebar.divider()
    st.sidebar.caption('Rules: Only integers 1-395 accepted.')
    st.sidebar.caption('No Inputs other than Whole Numbers are Accepted.')
    st.sidebar.divider()
    st.sidebar.subheader("Search History: ")
    # Logic for Search History
    if len(st.session_state.search_history) > 0:
        for i in reversed(st.session_state.search_history):
            st.sidebar.code(f"Article No. {i}")
    else:
        st.sidebar.code('No History Found')
# Calling the Main Function
if __name__ == '__main__':
    main()