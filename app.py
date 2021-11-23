import streamlit as st
from PyDictionary import PyDictionary
import json
from streamlit_lottie import st_lottie
import requests
from textblob import TextBlob

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f :
        return json.load(f)

st.set_page_config(page_title='Simple Dictionary',page_icon='👽')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
	content:'Made with ❤️ by om pramod'; 
	visibility: visible ;
}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center; color: green;'>Simple Dictionary</h1>", unsafe_allow_html=True)
st.markdown("***")

word = st.text_input("Enter the word to find meaning...")

dict = PyDictionary()
dic = dict.meaning(word)

corr = TextBlob(word)

if st.button("Get meaning(s)"):
    try :
        for i in dic.items() :
            st.markdown("***")
            st.success(i[0])
            for m in i[1] :
                st.text(f'• {m}')

            
        lottie_coding = load_lottiefile("success.json")

        st_lottie(
                lottie_coding,
                speed= 2,
                reverse=False,
                loop=True,
                height=300,
                width= 700,
                key=None
        )
    except  :
        lottie_coding = load_lottiefile("error.json")

        st_lottie(
            lottie_coding,
            speed= 2,
            reverse=False,
            loop=True,
            height=400,
            width= 700,
            key=None
        )

        st.error("No definitions found for this word")
        st.error(f'Try searching for - {corr.correct()}')



