import scipy.stats as stat
from t_test import paired_det
import streamlit as st
def spear_corr(col1,col2,conf,ho,h1):
    if type(col1)==str:
        # converts input to list
        try:
            col1=[float(col1) for col1 in col1.split(',')]
            col2=[float(col2) for col2 in col2.split(',')]
            cal_corr(col1,col2,1-(conf/100),ho,h1)
        except Exception as e:
            pass
    else:
        try:
        # calls function for calculating correlation
            cal_corr(col1,col2,conf,ho,h1)
        except:
            pass

def cal_corr(col1,col2,conf,ho,h1):#correlation using the scipy
    st.header("SPEARMAN RANK CORRELATION")
    corr=stat.spearmanr(col1,col2)
    c,r=corr
    st.info(ho)
    st.info(h1)
    st.info("correlation="+str(c))
    paired_det(r,1-(conf/100)) # calls the function for decision
