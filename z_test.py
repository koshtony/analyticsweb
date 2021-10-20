import numpy as np
import streamlit as st
import math
import scipy.stats as stat
class ztests:
    def __init__(self,col1,col2,conf,ho,h1):
        self.col1=col1
        self.col2=col2
        self.conf=conf
        self.ho=ho
        self.h1=h1
    def one_sample_z(self):
            if type(self.col1)==str:
                mu=self.col1.split(',')
                mu=[float(mu) for mu in mu]
                if len(mu)==1:
                    mu=mu[0]
                    st.info("one sample z-test")
                elif len(mu)>1:
                    mu=np.mean(mu)
                    st.info("two sample z-test")
                else:
                    info.warning("no inputs yet..having trouble! check guidelines")
            else:
                try:
                    mu=np.mean(self.col1)
                    st.info("two sample z-test")
                except:
                    st.warning("The data selected is not numerical")
            if type(self.col2)==str:
                x=self.col2.split(',')
                x=[float(x) for x in x]
            else:
                x=self.col2
            try:
                sd_x=np.std(x)
                x_bar=np.mean(x)
                z_score=(x_bar-mu)/(sd_x/math.sqrt(len(x)))
                st.info("Result")
                st.write(self.ho)
                st.write(self.h1)
                st.write("-----------------------------------")
                st.info("Z-score= "+str(z_score))
                st.write("-----------------------------------")
                if detect(self.h1)==1:
                    st.info("Right tailed test detected")
                    z_tab=stat.norm.ppf(self.conf/100)
                    sample1_z_dec(z_score, z_tab,type=">",test="z-score=")
                elif detect(self.h1)==2:
                    st.info("Left tailed test detected")
                    z_tab=stat.norm.ppf(self.conf/100)
                    sample1_z_dec(z_score, z_tab, type="<",test="z-score=")
                elif detect(self.h1)==3:
                    st.info("two tailed test detected")
                    alpha=(self.conf/100)+((100-(self.conf))//2)//100
                    z_tab=stat.norm.ppf(alpha)
                    sample1_z_dec(z_score, z_tab,type="not",test="z-score=")
            except:
                st.error("error encountered kindly check out the above warning, guideline")
class two_sample_z(ztests):
    def __init__(self,col1,col2,conf,ho,h1):
        super().__init__(col1,col2,conf,ho,h1)


def sample1_z_dec(z_score,z_tab,type,test):
    if type==">" or type=="not":
        if z_score >= z_tab:
            deci=test+str(z_score)+" > "+" critical value= "+str(z_tab)
            st.info(deci)
            st.info("Reject the Ho")
            st.write("-----------------------------------")
        else:
            deci=test+str(z_score)+" < "+" critical value= "+str(z_tab)
            st.info(deci)
            st.info("Fail to Reject the Ho")
            st.write("-----------------------------------")
    elif type=="<":
        if z_score <= z_tab:
            deci=test+str(z_score)+" < "+" critical value= "+str(z_tab)
            st.info(deci)
            st.info("Reject the Ho")
            st.write("-----------------------------------")
        else:
            deci=test+str(z_score)+" > "+" critical value= "+str(z_tab)
            st.info(deci)
            st.info("Fail to Reject the Ho")
            st.write("- ----------------------------------")


def detect(sent):
    if sent.find(">")>=0 or sent.find("greater")>=0:
        return 1
    elif sent.find("<")>=0 or sent.find("less")>=0:
        return 2
    elif sent.find("not")>=0:
        return 3
    else:
        st.write("use key words in describing the hypotheses")
