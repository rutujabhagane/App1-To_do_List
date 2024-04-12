import streamlit as st
import Functions_module
todos = Functions_module.read_file()
st.title('Todo App')
st.subheader("Welcome to Todo APP!")
st.text("This app is used to improve your productivity")
def add_new_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    Functions_module.write_to_file(todos)



for index,todo in enumerate(todos):

    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        Functions_module.write_to_file(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a Todo",placeholder="Enter a new todo",on_change=add_new_todo,key="new_todo")
