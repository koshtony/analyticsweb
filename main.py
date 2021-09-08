import streamlit as st
from page1 import page_1
from scraper_html import scraped,csv_download,scrape_pdf
from page2 import page_2
from PIL import Image
st.sidebar.write("**pages navigator**")
side_b=st.sidebar.radio("",["scraping","cleaning","Analysis"])
if side_b=="scraping":
    page_1()
if side_b=="cleaning":
    exp=st.expander("data cleaning")
    exp.write("""
    **Cleaning datasets**
    * removing Nan Values/ replacing them
    * Detecting outliers
    * Removing outliers
    """)
    page_2()
