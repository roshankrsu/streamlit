import streamlit as st

st.title("Welcome to Online Editor")
st.subheader("made with streamlit")
st.text("Choose Your Programming Language")

lang = st.selectbox("Your Language", ["C++" , "Javascript", "Python", "Java", "PHP", "Golang", "Rust"])
st.write(f"You choosed {lang}. programming language")
st.success(f"Successfully Selected {lang}")