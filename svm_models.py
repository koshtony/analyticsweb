import streamlit as st
from svm import svm_mod
import time
from splitter import split_data
def svm_gui(data,col,col2,col3,testsize):# svm user interface
        x=col2.multiselect("Features",data.columns)
        y=col2.multiselect("Target",data.columns)
        kernel=col3.selectbox("kernel",["linear","poly",
                "rbf","sigmoid"])
        c=col3.text_input("regularization parametere")
        c=float(c)
        x_tr,x_te,y_tr,y_te=split_data(data[x],data[y],testsize).split_imp()
        col2.info("train set length; "+str(x_tr.shape[0]))
        col3.info("test set lenght: "+str(x_te.shape[0]))
        st.write("-----training---->")
        prog=st.progress(0)
        for i in range(100):
            svm=svm_mod(x_tr,y_tr,x_te,y_te,kernel,c)
            time.sleep(0.01)
            prog.progress(i+1)
        st.info("performance metric")
        st.write(svm.__eval__())
