import streamlit as st
from linear_reg import lin_mod
from log_reg import logit
import pandas as pd
#@st.cache(suppress_st_warning=True)
def models_(data,col1,col2,col3):
    sel_x=col2.multiselect("X",data.columns)
    sel_y=col2.selectbox("Y",data.columns)
    model_type=col1.radio("models",["Linear Regression","Logistic Regression","General Linear Models"])
    if model_type=="Linear Regression":
        mod_class=lin_mod(data[sel_x],data[sel_y])
        mod_class.model_imp()
    elif model_type=="Logistic Regression":
        log_class=logit(data[sel_x],data[sel_y])
        log_class.logit_imp()
