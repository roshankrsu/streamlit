import streamlit as st

st.title("Tshirt Designing App")


if st.button("Make Design"):
    st.success("Your design is submitted")

add_design = st.checkbox("Add Design")

if add_design:
    st.write("Design added to your Tshirt")

tshirt_texture = st.radio("Pick your Tshirt texture ", ["silk", "Cutton", "Polyster", "Fabric"])
st.write(f"Selected {tshirt_texture} Cloth")
cloth_type = st.selectbox(f"Choose Tshirt type: ", ["OverSized", "Slim Fit", "Normal Size" "Baggy Fit", "Street Style",])

size = st.slider("T-Shirt Size (S-XXL)",34, 60, 40)
st.write(f"Selected Tshirt Size: {size}")

quantity = st.number_input("How many Tshirts", min_value=1, max_value=10, step=1)
st.write(f"Tshirt Quantity: {quantity}")

name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome, {name} ! Your Tshirt is OTW")

dob = st.date_input("Selected your date of birth")
st.write(f"Your date of birth {dob}")