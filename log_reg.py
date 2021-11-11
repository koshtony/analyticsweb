from linear_reg import lin_mod
import pandas as pd
import statsmodels.api as sm
import streamlit as st
class logit(lin_mod): # logistic regression using statsmodel
    def logit_imp(self):
        st.info("conversion to dummie")
        st.write(pd.get_dummies(self.y).head())
        st.write("selecting first column ---->")
        mod=sm.Logit(pd.get_dummies(self.y).iloc[:,0],self.x).fit()
        st.write(mod.summary())
