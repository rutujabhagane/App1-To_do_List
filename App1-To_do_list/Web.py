import streamlit as st
import Functions_module
todos = Functions_module.read_file()
st.title('Todo App')
st.subheader("Welcome to Todo APP!")
st.text("This app is used to improve your productivity")


for todo in todos:

    st.checkbox(todo)

st.text_input(label="",placeholder="Enter a new todo")