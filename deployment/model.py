'''
Putri Arzalya Maharani
'''
from functions import preprocess_text, prediction
import streamlit as st
import pandas as pd
import joblib
from PIL import Image

def run():
    st.subheader("Can you describe what you're going through right now ?")
    user_input = st.text_input(
        label='Express yourself here ↓',
        value='Today, I feel...',
        max_chars=300,
        key='text_input_key',
        placeholder='Please Type here...',
        disabled=False,
        help='Try not to think, and let your heart speak'
    )
    st.write('')

    st.write('You entered:', user_input)

    # button
    if st.button(label='Identify Your Feelings'):
        url = "https://remediindonesia.com"
        # Preprocess the text using the existing preprocess_text function
        X = preprocess_text(user_input)
        
        # Perform prediction
        result = prediction([X])
        st.write(result[1])
        if result[0] == 0:
            st.write("It's alright, you'll do just fine!")
            st.write("If ever you need help on dealing with this, EFT method could certainly help ↓")
            st.markdown(f'<a href="{url}" target="_blank">You can learn more about EFT here with Rumah Remedi</a>', unsafe_allow_html=True)
        elif result[0] == 1:
            st.write("It's alright to be angry. We believe you'll get through it eventually! If you need help calming down, we would suggest the link below ↓")
            st.markdown(f'<a href="{url}" target="_blank">You could destress with Rumah Remedi</a>', unsafe_allow_html=True)
        else:
            st.write("That's Great! We hope the rest of the day will be as wonderful!")

run()
