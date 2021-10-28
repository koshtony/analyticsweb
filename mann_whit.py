import streamlit as st
import scipy.stats as stat
from t_test import paired_det
from z_test import detect
class mann: # peroform mannwhitney u-test
    def __init__(self,col1,col2,conf,ho,h1):
        self.col1=col1
        self.col2=col2
        self.conf=conf
        self.ho=ho
        self.h1=h1
    def mann_test(self):
        if type(self.col1)==str:
            col1=[vals for vals in self.col1.split(',')]
            col2=[vals for vals in self.col2.split(',')]
        else:
            col1=self.col1
            col2=self.col2
        mann_type(col1, col2, self.conf,self.ho, self.h1)
def mann_type(x,y,conf,ho,h1): #obtain statistic and p-value based on type eg: one-sided
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
    s,p=stat.mannwhitneyu(x=x,y=y,alternative=type)
    st.info("U = "+str(s))
    paired_det(p,1-(conf/100))
