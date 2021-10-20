import pandas as pd
import numpy as np
import streamlit as st
import statsmodels.api as sm
from statsmodels.formula.api import ols
class anova: #performs anova test
    def __init__(self,data,col1,col2,col3):
        self.col1=col1
        self.col2=col2
        self.col3=col3
        self.data=data
    def one_way(self): #one way anova for three groups
        if type(self.col1)==str:
            col1=[float(val) for val in self.col1.split(",")]
            col2=[float(val) for val in self.col2.split(",")]
            col3=[float(val) for val in self.col3.split(",")]
        else:
            col1=self.col1
            col2=self.col2
            col3=self.col3
        data=pd.DataFrame({"values":[*col1,*col2,*col3],
                    "groups":np.repeat(["group1","group2","group3"],[len(col1),len(col2),len(col3)])
                    })
        model=ols('values~groups',data=data).fit()
        anv=sm.stats.anova_lm(model,typ=2)
        st.write(anv)
        st.info('Pairwise Comparison')
        st.write(model.t_test_pairwise('groups').result_frame)
    def more_one_way(self):
        formula=self.col1+"~"+self.col
        model=ols(formula,data=self.data).fit()
        anv=sm.stats.anova_lm(model,typ=2)
        st.write(anv)
        st.info('Pairwise Comparison')
        st.write(model.t_test_pairwise('groups').result_frame)
