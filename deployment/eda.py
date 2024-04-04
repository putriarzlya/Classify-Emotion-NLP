import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
from PIL import Image

def run():
    '''
    Function for EDA page
    '''
    st.title('Exploration Data Analysis Section')
    # ============================= Showing Data ==========================
    df = pd.read_csv('Emotion_classify_Data.csv')
    horizontal_radio_css = """<style>div.row-widget.stRadio > div{flex-direction:row;}</style>"""
    st.markdown(horizontal_radio_css, unsafe_allow_html=True)
    data_show = st.radio("**Viewing Options**", ['Top 10 Entries', 'Bottom 10 Entries'])
    if data_show == 'Top 10 Entries':
        st.table(df.head(10))
    else:
        st.table(df.tail(10))
    # ============================= Simple Analysis ========================
    eda=pd.read_csv('eda.csv')
    # basic summary analysis
    emotion_counts = eda['Emotion'].value_counts()
    eda['Comment Length'] = eda['Comment'].apply(len)
    eda['Word Count'] = eda['Comment'].apply(lambda x: len(x.split()))

    # Emotion distribution
    fig_emotions = px.bar(emotion_counts,
                          x=emotion_counts.index,
                          y=emotion_counts.values,
                          labels={'x': 'Emotion', 'y': 'Count'},
                          title='Distribution of Emotions')
    fig_emotions.update_traces(marker_line_width=1, marker_line_color='black')
    fig_emotions.update_layout(xaxis_title='Emotions', yaxis_title='Count', width=700)

    # Comment length distribution
    fig_comment_length = alt.Chart(eda).mark_bar().encode(
        x=alt.X('Comment Length:Q', bin=alt.Bin(maxbins=30), title='Length of Comment'),
        y='count():Q',
        color=alt.value('skyblue')
    ).properties(
        width=600,
        height=400,
        title='Distribution of Comment Length'
    )

    # Word count distribution
    fig_word_count = alt.Chart(eda).mark_bar().encode(
        x=alt.X('Word Count:Q', bin=alt.Bin(maxbins=30), title='Word Count'),
        y='count():Q',
        color=alt.value('salmon')
    ).properties(
        width=600,
        height=400,
        title='Distribution of Word Count'
    )

    # Display the figures in Streamlit
    st.write(fig_emotions)
    st.write(fig_comment_length)
    st.write(fig_word_count)

    with st.expander('Explanation'):
        st.caption(
            '''
            1. The dataset exhibits a balanced distribution among the target classes, which include 'anger', 'joy', and 'fear'.
            2. Comment length distribution skews towards the right, with the majority falling within the range of 30 to 130 characters.
            3. Outliers are observed in comment lengths exceeding 244 characters.
            Similarly, word count distribution is skewed to the right, with most falling between 5 to 30 words.
            4. These findings suggest varying levels of expressiveness among individuals in the dataset. While the majority are concise, there are notable instances of individuals expressing themselves more openly and extensively.
            '''
        )

    # ============================= Joy Word Cloud ==================================
    st.subheader('Joy Word Cloud')
    image1 = Image.open('joy_wordcloud.png')
    st.image(image1, caption='Figure 1 Joy Emotion Word Cloud',  width=700)

    # explaination
    with st.expander('Explanation'):
        st.caption(
            '''
            The Joy word cloud offers a condensed glimpse into the prevalent sentiments associated with joy. It showcases frequently used words like "life," "good," "day," "something," "going," and "well," illuminating the common vocabulary employed to articulate joyful experiences. This visualization effectively encapsulates the essence of joy by highlighting the recurring themes and expressions that resonate with individuals experiencing happiness and contentment.
            '''
        )

    # ============================= Anger Word Cloud =====================================
    st.subheader('Anger Word Cloud')
    image2 = Image.open('anger_wordcloud.png')
    st.image(image2, caption='Figure 2 Anger Emotion Word Cloud',  width=700)

    # explaination
    with st.expander('Explanation'):
        st.caption(
            '''
            The Anger word cloud reveals prevalent expressions linked to feelings of anger, with notable words including "would," "even," "way," "think," and "angry." These terms are frequently used during episodes of anger, signifying the common language associated with this emotion. Notably, the presence of auxiliary verbs like "would" and "even" suggests a nuanced aspect, potentially indicating mood or tense in the context of anger. This analysis provides valuable insights into the linguistic patterns surrounding anger, shedding light on the vocabulary employed during moments of heightened emotional intensity.
            '''
        )

    # =============================== Fear Word Cloud ====================================
    st.subheader('Fear Word Cloud')
    image3 = Image.open('fear_wordcloud.png')
    st.image(image3, caption='Figure 3 Fear Emotion Word Cloud',  width=700)

    # explaination
    with st.expander('Explanation'):
        st.caption(
            '''
            The Fear word cloud showcases prevalent words linked to feelings of fear, including "still," "bit," "strange," and "think." These terms frequently emerge when individuals express worry or anxiousness, reflecting the multifaceted nature of fear. In particular, fear of the unknown often triggers feelings of worry and anxiety, as individuals grapple with uncertainty and anticipation. However, fear encompasses a broad spectrum of emotions, ranging from a sense of unease to being scared or terrified, eliciting physical reactions like goosebumps. This analysis provides valuable insights into the diverse ways fear manifests, capturing both the cognitive and physiological aspects of this complex emotion.
            '''
        )

# ================================ Additional Explanation ================================
    st.subheader('Additional Explanation')
    st.write('''
        The visualization provides insight into the dataset's emotions, along with comment length and word count distributions. These insights are vital for subsequent analysis and modeling. Additionally, the word clouds visually depict the most common words linked to each emotion, enhancing our understanding of the dataset.
    ''')

if __name__ == '__main__':
    run()
