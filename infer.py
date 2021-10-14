from statsmodels.stats import weightstats as ws
import numpy as np
import streamlit as st
import math
import scipy.stats as stat
from z_test import ztests,two_sample_z
from t_test import ttest
def inferential():
    data=["col1","col2"]
    st.header("-------HYPOTHESES TESTING-------")
    cl=st.sidebar
    cl1,cl2,cl3=st.columns((1,1,1))
    ho=cl1.text_input("Describe H0:","H0: mu1=mu2")
    h1=cl1.text_input("Describe H1:","H1: mu1<10")
    conf=cl1.slider("% CI",1,100)
    col1=cl2.text_input("column 1 [value 1] ","23,24,56,57")
    col2=cl2.text_input("column 2 [value 2] ","23,24,56,57")
    col3=cl2.text_input("column 3 [value 3]","23,24,56,57")
    sel1=cl3.selectbox("select column 1",data)
    sel2=cl3.selectbox("select column 2",data)
    sel3=cl3.selectbox("select column 3",data)
    c=st.sidebar
    c1,c2=st.columns((1,1))
    c1_rad=c1.radio("parametric tests",["Z-test","T-test","Anova","Pearson Correlation Test"])
    c2_rad=c2.radio("Non Prametric Tests",["Mann-Whitney U Test",
    "Wilcoxon Signed Rank","The Kruskal-Wallis Test","Spearman Rank Test","chi-test"])

    if c1_rad=="Z-test":
        type_rad=c1.radio("",["one sample z-test","Two sample z-test"])
        if type_rad=="one sample z-test":
            z=ztests(col1,col2,conf,ho,h1)
            z.one_sample_z()

        elif type_rad=="Two sample z-test":
            two=two_sample_z(col1,col2,conf,ho,h1)
            two.one_sample_z()




    elif c1_rad=="T-test":
        t_rad=c1.radio("",["one sample t-test","independent sample t-test","paired t-test"])
        if t_rad=="one sample t-test":
            t=ttest(col1,col2,conf,ho,h1)
            t.one_samp()
        elif t_rad=="independent sample t-test":
            t=ttest(col1,col2,conf,ho,h1)
            t.ind_2_sample()
        elif t_rad=="paired t-test":
            t=ttest(col1,col2,conf,ho,h1)
            t.paired_t_test()
