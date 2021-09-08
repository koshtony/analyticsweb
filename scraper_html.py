import streamlit as st
import pandas as pd
import base64
from tabula import read_pdf
import camelot
def scraped(url,table_no):
    html_df=pd.read_html(url,header=0)
    df=html_df[table_no]
    return df
def scrape_pdf(fname,table_pdf):
    tab=camelot.read_pdf(fname)
    sel_table=tab[table_pdf].df
    return sel_table
def csv_download(df):
    file_csv=df.to_csv(index=False)
    b64=base64.b64encode(file_csv.encode()).decode()
    href=f'<a href="data:file/file_csv;base64,{b64}" download="scraped_data.csv">Download CSV File</a>'
    return href
