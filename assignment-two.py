#age calculator

import streamlit as st
from datetime import date

st.title("Age Calculator")

dob = st.date_input("Enter Your Date of Birth",
                    value=date(2000, 1, 1), # default date
                    min_value=date(1900, 1, 1),
                    max_value=date.today())

if dob:
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    st.write(f"Your current age is: {age}")