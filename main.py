import streamlit as st
from page1 import page_1
from scraper_html import scraped,csv_download,scrape_pdf
from page2 import page_2
from page3 import streamer
from PIL import Image
from ltx import editor
from calculus import calc
st.get_option("theme.textColor") #load custom theme
st.info("set your browser to desktop mode (recommended) if you are using phone")
st.sidebar.write("**pages navigator**")
#set page navigator using radio button
side_b=st.sidebar.radio("",["scraping","Cleaning->Analysis->Modelling","calculus","Algebra"])
if side_b=="scraping": #call scrapping section
    page_1()
if side_b=="Cleaning->Analysis->Modelling": #analysis section
    exp=st.expander("Cleaning->Analysis->Modelling")
    exp.write("""
    **Cleaning datasets**
    * removing Nan Values/ replacing them
    * Detecting outliers
    * Removing outliers
    """)
    page_2()
if side_b=="calculus":#calculus section
    calc()

if side_b=="Algebra":
    st.header("Algebra")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
