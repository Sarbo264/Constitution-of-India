# Importing Library Streamlit
import streamlit as st
# Importing a Function from the Program.py File
from Program import extraction
# Main Function
def main():
    # Storing the Search History
    if 'search_history' not in st.session_state:
        st.session_state.search_history = []
    # Making the Header and Title of the Webpage.
    st.title("THE ARTICLE ENGINE", text_alignment = 'center', width= 700)
    st.header("Precision Extraction from the Constituition of India.", text_alignment = 'center', width = 700)
    st.divider()
    st.space("medium")
    # Making the Body of the Web Page
    st.markdown("""
        **Overview**
        The Article Engine is a highly optimized, web-based legal technology platform designed to make the Constitution of India instantly accessible and searchable. Navigating dense, multi-hundred-page legal frameworks is traditionally a slow and manual process. This application solves that by providing a streamlined, intelligent extraction tool that bridges the gap between complex legal documents and modern, user-centric UI/UX design. By inputting a specific Article number, users are instantly presented with the exact legal text, parsed and formatted for maximum readability. 

        **Core Features & Intelligent Handling**
        At the heart of the platform is a robust parsing engine built to handle the structural complexities of the Constitution. 
        * **Instantaneous Retrieval:** Users can query any integer from 1 to 395 to instantly retrieve the corresponding Article's description.
        * **Edge-Case Management:** The Indian Constitution has been amended over 100 times. The engine is programmed with intelligent error-handling to specifically identify and format Articles that have been historically omitted or repealed, ensuring users receive accurate legal context rather than a generic system crash. 
        * **Stateful Memory:** Utilizing session-state memory architecture, the application actively tracks and logs a user's search history during their active session, displaying it in a sleek, easily accessible sidebar for quick reference.

        **Technical Architecture & UI/UX Design**
        Built entirely in Python and deployed via the Streamlit framework, the platform prioritizes a premium, frictionless user experience. It breaks away from standard rigid layouts by utilizing a responsive, wide-screen configuration. The interface employs sophisticated glassmorphic design principles, custom CSS styling, and dynamic container formatting. The visual hierarchy—from the centralized search console to the dedicated, bordered reading panes—mimics the experience of using top-tier enterprise SaaS products, making legal research feel fast, analytical, and highly professional.
""")
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