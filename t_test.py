import numpy as np
from z_test import ztests
from z_test import detect
from z_test import sample1_z_dec
import scipy.stats as stat
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
        t=(np.mean(x)-mu)//(np.std(x)//(math.sqrt(len(x))))
        st.info(t)
        if detect(self.h1)==1:
            st.write("Right tailed test detected")
            tt=stat.t.ppf(self.conf/100,len(x)-1)
            sample1_z_dec(t,tt, type=">", test="t= ")
        elif detect(self.h1)==2:
            st.write("left tailed test detected")
            tt=stat.t.ppf(self.conf/100,len(x)-1)
            sample1_z_dec(t,tt, type="<", test="t= ")
        else:
            st.write("two tailed test detected")
            tt=stat.t.ppf((self.conf/100)+((100-(self.conf))//2)//100,len(x)-1)
            sample1_z_dec(t,tt,type="not",tezt="t= ")
    def ind_2_sample(self):
        self.col1=[float(val) for val in self.col1.split(',')]
        self.col2=[float(val) for val in self.col2.split(',')]
        s_1=np.std(self.col1)
        s_2=np.std(self.col2)
        s=math.sqrt(((len(self.col1)-1)*s_1 + (len(self.col2)-1)*s_2)//(len(self.col1)+len(self.col2)-2))
        t=((np.mean(self.col1)-np.mean(self.col2))//(s))*(math.sqrt((len(self.col1)*len(self.col2))//(len(self.col1)+len(self.col2))))
        tt=stat.t.ppf(self.conf/100,len(self.col1)+len(self.col2)-2)
        sample1_z_dec(t, tt, type="not", test="t= ")
    def paired_t_test(self):
        d_2=[]
        d=[]
        for i in range(len(self.col2)):
            d_2.append((self.col1[i]-self.col2[i])**2)
            d.append(self.col1[i]-self.col2[i])
        s=math.sqrt((sum(d_2))-(len(self.col2*(np.mean(d))**2))//(self.col2-1))
        t=(np.mean(d)*math.sqrt(len(self.col1)))//(self.col1-1)
        tt=stat.t.ppf(self.conf//100,len(self.col2)-1)
        sample1_z_dec(t, tt, type="not", test="t=")
