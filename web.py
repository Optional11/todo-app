import streamlit as st
from modules import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is mydo app")
st.write("This is app for .....")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")