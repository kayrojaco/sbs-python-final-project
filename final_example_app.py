from langchain_openai import ChatOpenAI
import streamlit as st

with st.sidebar: 
    st.session_state["api_key"] = st.text_input("place your api key here")
if st.session_state["api_key"]:
    model = ChatOpenAI(model="gpt-4o-mini", 
    api_key=st.session_state["api_key"])
else: 
    st.error('no api key provided')
import streamlit as st
if "journals" not in st.session_state:
    st.session_state["journals"] =[]

tabs = st.tabs(["add new journal", "show all journals"])
with tabs[0]:

    journal_content = st.text_area("write your journal here")

    journal_date = st.date_input("pick a date")

    journal_image = st.file_uploader("upload a picture")

    if st.button("click to add"):
        if journal_content and journal_date and journal_image:
            st.success("journal added")
    #create new journal entry 
        response = model.invoke(input="please fix the grammer: "+ journal_content)
        journal = {"content": response.content, "date": journal_date, "picture":journal_image}
        st.session_state.journals.append(journal)

    else:
        st.error("something is missing")

with tabs[1]:
    for journal in st.session_state.journals: 
        with st.expander("click here"):
          col1,col2,col3 = st.columns(3)
          col1.markdown (journal["content"])
          col2.markdown (journal["date"])
          col3.image(journal["picture"])

           



