'''
Putri Arzalya Maharani

Objective : Creating a main page of the webapps.
'''

import streamlit as st
import eda
import model

# navigating pages
page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Emotion Classification'])

if page == 'Home Page':
    st.header('Home Page') 
    st.write('')
    st.write('Name  : Putri Arzalya Maharani')
    st.markdown('Dataset    : [Emotion Dataset] (https://www.kaggle.com/datasets/abdallahwagih/emotion-dataset)')
    st.image('https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2I4Y3FtenA5NWs5YjVoMGdzNm85eXp5MGZldHA5bzJ2cHRnYzhydCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Yat5wnwisEV2iXbt4x/giphy.gif')
    st.write("Objective : Mental health is crucial, and many individuals often question or struggle to understand their emotions. Validating emotions can provide reassurance to individuals, affirming that others share similar feelings. By leveraging NLP machine learning techniques with high accuracy, we aim to effectively classify emotions, brightening individuals' days.")
    st.write('')
    st.caption('Please select a page from the options listed on the left^^')
    st.write('')
    st.write('')
    
#============================= Background Info ==========================
    
    with st.expander("Background Information"):
        st.caption("The dataset was obtained from Kaggle, consisting of 5937 entries with 2 object columns. These columns contain individuals' comments and their respective emotions.")
        
#============================= Work Flow ================================
    
    with st.expander("Work Flow"):
        st.caption(
        '''
            - Data loading from Kaggle
            - Basic Analysis
            - EDA on most common words
            - Text processing for feature engineering
            - Vectorization
            - Building the models
            - Tuning the models
            - Inference
            - Deployment
        '''
        )

#============================= Conclussion =================================
    with st.expander("Conclusion"): 
        st.caption(
            '''
            The dataset is well-structured with balanced target classes. Exploratory Data Analysis reveals that most individuals are concise in expressing their feelings, with only a few providing detailed descriptions. Common words used to describe joyful experiences include 'life', 'good', 'day', 'something', 'going', and 'well'. Conversely, words commonly associated with anger include 'would', 'even', 'way', 'think', and 'angry'. Fear-related words such as 'still', 'bit', 'strange', and 'think' are also prevalent. The best-performing model utilizes an GRU network with 99% accuracy and 90% validation accuracy. However, there is still room for improvement, particularly in reducing noise through preprocessing techniques like adding more stopwords. Additionally, incorporating data on a wider range of emotions would enhance the model's ability to classify diverse emotional states.
            '''
        )

#============================ Other Page ======================================
elif page == 'Exploration Data Analysis':
    eda.run()
else:
    model.run()