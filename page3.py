import pandas as pd
import streamlit as st
import numpy as np
from stream import curr
import time
from datetime import datetime
def streamer():
    pairs=pd.read_csv('currency.csv')
    pairs_list=[]
    for i in pairs["new"]:
        pairs_list.append(i)
    sel_pairs=st.selectbox("select pairs",pairs_list)
    ss="streaming"+" "+str(sel_pairs)+" "+"pairs closing price"
    st.write(ss)
    if True:
        plots=st.line_chart()
        st.markdown(f'<p style="background-color:red disclaimer;"> Disclaimer: The data is streamed as it is and not intended for trading</p>',unsafe_allow_html=True)
        i=0
        while True:
            i+=1
            dats=pd.DataFrame([[curr(sel_pairs)]],columns=["closing price"])
            plots.add_rows(dats)
            time.sleep(0.5)
