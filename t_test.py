import numpy as np
from z_test import ztests
import math
import streamlit as st
class ttest(ztests):
    def one_samp(self):
        mu=self.col1.split(",")
        mu=[float(mu) for mu in mu]
        if len(mu)==1:
            mu=mu[0]
        elif len(mu)>1:
            mu=np.mean(mu)
        else:
            st.warning("cell is empty")
        x=self.col2.split(",")
        x=[float(x) for x in x]
        t=(np.mean(x)-mu)/(np.std(x)/(math.sqrt(len(x))))
        st.info(t)
