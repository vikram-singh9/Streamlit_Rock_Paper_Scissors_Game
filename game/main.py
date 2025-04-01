import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", page_icon="✊📄✂", layout="centered")

st.markdown("""
    <style>
        body {background-color: #f4f4f4;}
        .stButton button {border-radius: 10px; font-size: 18px; padding: 10px 20px;}
        .stRadio div {display: flex; justify-content: center;}
        .stRadio div label {font-size: 20px; margin: 10px;}
        .title {text-align: center; font-size: 40px; font-weight: bold;}
        .subheader {text-align: center; font-size: 20px;}
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title'>Rock Paper Scissors Game 🎮</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subheader'>Play against the computer! 🤖</h3>", unsafe_allow_html=True)

choices = ["rock ✊", "paper 📄", "scissors ✂"]
player = st.radio("Choose your move:", choices, horizontal=True)

if st.button("Play! 🎯"):
    computer = random.choice(choices)
    st.markdown(f"<h2 style='text-align: center;'>You chose: {player}</h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center;'>Computer chose: {computer}</h2>", unsafe_allow_html=True)
    
    player = player.split()[0]
    computer = computer.split()[0]
    
    if player == computer:
        st.info("It's a tie! 🤝")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        st.success("You win! 🎉")
        st.balloons()
    else:
        st.error("Computer wins! 😔")
