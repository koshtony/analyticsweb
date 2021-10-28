from statsmodels.stats import weightstats as ws
import numpy as np
import streamlit as st
import seaborn as sb
import math
import scipy.stats as stat
from z_test import ztests,two_sample_z
from t_test import ttest
from anova_t import anova
from corr import pearson_corr
from mann_whit import mann
from wilcoxon import wilcox
from spearman import spear_corr
from chi import chi_test
def inferential(data):
    st.header("-------HYPOTHESES TESTING-------")
    cl=st.sidebar
    cl1,cl2,cl3=st.columns((1,1,1))
    ho=cl1.text_input("Describe H0:","H0: mu1=mu2")
    h1=cl1.text_input("Describe H1:","H1: mu1<10")
    conf=cl1.slider("% CI",1,100)
    col1=cl2.text_input("column 1 [value 1] ","23,24,56,57")
    col2=cl2.text_input("column 2 [value 2] ","23,24,56,57")
    col3=cl2.text_input("column 3 [value 3]","23,24,56,57")
    sel1=cl3.selectbox("select column 1",data.columns)
    sel2=cl3.selectbox("select column 2",data.columns)
    sel3=cl3.selectbox("select column 3",data.columns)
    c=st.sidebar
    c1,c2=st.columns((1,1))
    data_c1=[]
    data_c2=[]
    data_c3=[]
    if len(str(col1))==0 or len(str(col1))==0 or len(str(col1))==0:
        st.warning("upload mode")
        for i in data[sel1]:
                data_c1.append(i)
                col1=data_c1
        for i in data[sel2]:
                data_c2.append(i)
                col2=data_c2
        for i in data[sel3]:
                data_c3.append(i)
                col3=data_c3
    else:
            st.warning('input mode')
            col3,col3,col3=col3,col3,col3
    main_rad=c1.radio("",["parametric test","Non parametric tests"])
    if main_rad=="parametric test":
        c1_rad=c1.radio("parametric tests",["Z-test","T-test","Anova","Pearson Correlation Test"])
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
                st.write("section under repair")
        elif c1_rad=="Anova":
            anv_rad=c1.radio("",["one way","Two way"])
            if anv_rad=="one way":
                try:
                    test=anova(data,col1,col2,col3)
                    test.one_way()
                except Exception as e:
                    pass
                #st.error("kindly check out guidelines")


            elif anv_rad=="Two way":
                pass
        if c1_rad=='Pearson Correlation Test':
            pearson_corr(col1, col2, conf,ho,h1)
    if main_rad=="Non parametric tests":
        c2_rad=c2.radio("Non Prametric Tests",["Mann-Whitney U Test",
        "Wilcoxon Signed Rank","The Kruskal-Wallis Test","Spearman Rank Test","chi-test"])
        if c2_rad=="Mann-Whitney U Test":
            mann_t=mann(col1,col2,conf,ho,h1)
            mann_t.mann_test()
        elif c2_rad=="Wilcoxon Signed Rank":
            wilc_test=wilcox(col1,col2,conf,ho,h1)
            wilc_test.wilc_test()
        elif c2_rad=="Spearman Rank Test":
            spear_corr(col1, col2, conf, ho, h1)
        elif c2_rad=="chi-test":
            c_t=chi_test(data[sel1], data[sel2], conf, ho, h1)
            c_t.cross_chi()
