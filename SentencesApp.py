import pandas as pd
import streamlit as st


@st.cache_data
def fetch_data():
    data_1 = pd.read_csv("Top100s.csv")
    data_2 = pd.read_csv("Top100_sim.csv")
    data_3 = pd.read_csv("Tail100_sim.csv")
    data_4 = pd.read_csv("Top100TFIDF.csv")
    return data_1, data_2, data_3, data_4


if 'last' not in st.session_state:
    st.session_state['last'] = 0

tops, top_sim, tail_sim, top_tfidf = fetch_data()
with st.sidebar:
    option = st.selectbox(
        'The method and sentences to see:',
        ('Top 100 By times of a word shows', 'Top 100 by similarity', 'Lowest 100 by similarity', 'TOP 100 by TFIDF'))

values = st.number_input("Please choose any JD you are interested:", min_value=0, max_value=99, step=1)

if option == 'Top 100 By times of a word shows':
    value = tops.loc[values, "score"]
    text = tops.loc[values, "JobText"]
elif option == 'Top 100 by similarity':
    value = top_sim.loc[values, "score"]
    text = top_sim.loc[values, "JobText"]
elif option == 'Lowest 100 by similarity':
    value = tail_sim.loc[values, "score"]
    text = tail_sim.loc[values, "JobText"]
elif option == 'TOP 100 by TFIDF':
    value = top_tfidf.loc[values, "score"]
    text = top_tfidf.loc[values, "JobText"]
else:
    value = 0
    text = ""

st.metric(label="**Score**", value=value, delta=str(round(value - st.session_state['last'], 2)))
st.session_state['last'] = value
st.write(text)
