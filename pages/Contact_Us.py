import streamlit as st
import pandas
from send_email import send_email

st.header("Get Contact With Our Company")

df = pandas.read_csv("topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    option = st.selectbox(
        'Which on topic do you wanna discuss?',
    df["topic"])
    raw_message = st.text_area("Your Message")
    edited_message = f"""\
Subject: New email from {user_email}
    
Topic: {option}
From: {user_email}
{raw_message}
"""
    submit_button = st.form_submit_button("Submit")
    print(submit_button)

    if submit_button:
        send_email(edited_message)
        st.info("your message sent successfully")


