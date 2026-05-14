import streamlit as st

st.title("Voting Poll")

col1, col2, col3= st.columns(3)

with col1:
    st.header("BJP")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Logo_of_the_Bharatiya_Janata_Party.svg/500px-Logo_of_the_Bharatiya_Janata_Party.svg.png", width=100)
    vote1 = st.button("Vote bjp")

with col2:
    st.header("Congress")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Indian_National_Congress_hand_logo.svg/330px-Indian_National_Congress_hand_logo.svg.png", width=100)
    vote2 = st.button("Vote congress")

with col3:
    st.header("NOTA")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/A_coloured_voting_box_%28no_bg%29_%28cropped%29.svg/250px-A_coloured_voting_box_%28no_bg%29_%28cropped%29.svg.png", width=100)
    vote3 = st.button("None of the above")

if vote1:
    st.success("Thanks for voting BJP")
elif vote2:
    st.success("Thanks for voting Congress")
elif vote3:
    st.success("Thanks for voting")

name = st.sidebar.text_input("Enter your name")
vote = st.sidebar.selectbox("Choose your vote", ["BJP", "Congress", "NOTA"])

st.write(f"Welcome {name} and Thanks for voting {vote}" )

with st.expander("Show How to Give a Vote Instructions"):
    st.write("""
    1. Prepare voter id card  
    2. Find Your Vooting
    3. Go to Booth
    4. Press the icon which you wanna vote
    """)

st.markdown('### Welcome to Voting App')
st.markdown('> Blockquote')
