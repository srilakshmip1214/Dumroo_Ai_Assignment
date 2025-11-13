import streamlit as st
from data_runner import load_all, handle_query
from nlu_local import interpret_question

st.set_page_config(page_title="Dumroo AI Developer Assignment", layout="centered")
st.title(" Dumroo AI Developer Assignment")
st.write("Ask questions in plain English about student data (submissions, performance, quizzes).")

scope = {"grade": ["8"], "class": ["A"], "region": ["South"]}
st.info(f"Active Scope → Grade: {scope['grade'][0]}, Class: {scope['class'][0]}, Region: {scope['region'][0]}")

if "last_query" not in st.session_state:
    st.session_state.last_query = None

user_input = st.text_input(" Type your question:", placeholder="e.g. Show me performance for grade 8 last week")

if st.button("Run Query"):
    if user_input.strip():
        with st.spinner("Processing..."):
            structured = interpret_question(user_input)
            st.session_state.last_query = structured
            data = load_all()
            result = handle_query(structured, scope, data)
            st.subheader(" Parsed Query")
            st.json(structured)
            if not result.empty:
                st.write("Showing results within your assigned scope.")
                st.dataframe(result)
                st.success("Query executed successfully!")
            else:
                st.warning("No records found.")
    else:
        st.warning("Please enter a question first.")

if st.session_state.last_query:
    st.markdown("---")
    st.subheader(" Follow-up Query")
    new_filter = st.text_input("Refine previous query (e.g. 'only for class B'):")
    if st.button("Apply Filter"):
        q = st.session_state.last_query
        if "class" in new_filter.lower():
            q["filters"]["class"] = "B"
        elif "grade" in new_filter.lower():
            q["filters"]["grade"] = "9"
        elif "region" in new_filter.lower():
            q["filters"]["region"] = "North"
        data = load_all()
        result = handle_query(q, scope, data)
        if not result.empty:
            st.write("Updated results based on your follow-up query.")
            st.dataframe(result)
            st.success(" Follow-up applied successfully!")
        else:
            st.warning("No records match the refined filters.")
