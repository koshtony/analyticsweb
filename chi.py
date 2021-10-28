import researchpy as res
import streamlit as st
from t_test import paired_det
from z_test import ztests
from pandas import *
class chi_test(ztests):
    def cross_chi(self):
        if type(self.col1)==str:
            pass
        tab,stat,exp=res.crosstab(self.col1,self.col2,test="chi-square",expected_freqs= True)
        st.info("crosstab")
        st.write(tab)
        st.info("Expected Frequencies")
        st.write(exp)
        st.info("chi-sq STATS")
        st.write(stat)
        paired_det(stat["results"].loc[1],1-self.conf/100)
