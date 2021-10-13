import streamlit as st
from page1 import page_1
from scraper_html import scraped,csv_download,scrape_pdf
from page2 import page_2
from page3 import streamer
from PIL import Image
from calculus import calc
st.get_option("theme.textColor")
st.sidebar.write("**pages navigator**")
side_b=st.sidebar.radio("",["scraping","Cleaning->Analysis->Modelling","calculus","Tracker"])
if side_b=="scraping":
    page_1()
if side_b=="Cleaning->Analysis->Modelling":
    exp=st.expander("Cleaning->Analysis->Modelling")
    exp.write("""
    **Cleaning datasets**
    * removing Nan Values/ replacing them
    * Detecting outliers
    * Removing outliers
    """)
    page_2()
if side_b=="calculus":
    calc()

if side_b=="Tracker":
    streamer()
