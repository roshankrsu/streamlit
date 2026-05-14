import streamlit as st

st.title("Hello Drink App")
st.subheader("made with streamlit")
st.text("Welcome to your first interactive app")
st.write("Choose your fav. Drink")

drinks = st.selectbox("your fav drink: ", ["Diet coke", "Butter milk","Coca Cola", "Lassi", "Monster", "Red Bull"])
st.write(f"You choose {drinks}. Excellent choice")

st.success("Your Drink is availabel")