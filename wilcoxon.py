from mann_whit import mann
import streamlit as st
import scipy.stats as stat
from z_test import detect
from t_test import paired_det
import pandas as pd
class wilcox(mann): #wilcoxon signed rank test
    def wilc_test(self):
                if type(self.col1)==str:
                    col1=[vals for vals in self.col1.split(',')]
                    col2=[vals for vals in self.col2.split(',')]
                else:
                    col1=self.col1
                    col2=self.col2
                try:
                    wilcoxon_type(col1, col2, self.conf,self.ho, self.h1)
                except Exception as e:
                    st.write(e)
@st.cache(suppress_st_warning=True)
def wilcoxon_type(x,y,conf,ho,h1): #obtain statistic and p-value based on type eg: one-sided
            if detect(h1)==1:
                type="greater"
                st.write("one sided test detected (greater)")
            elif detect(h1)==2:
                type="less"
                st.write("one sided test detected (less)")
            else:
                type="two-sided"
                st.write("two sided test detected")
            st.info(ho)
            st.info(h1)
            if len(x)!=len(y):
                st.warning("lenght  for both x and y should be equal")
            s,p=stat.wilcoxon(x,y,alternative=type)
            st.info("U = "+str(s))
            paired_det(p,1-(conf/100))
