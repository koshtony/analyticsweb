from splitter import split_data
import streamlit as st
import time
from dec_tree import tree_class
def t_models(data,col1,col2,col3):
    s_x=col2.multiselect("features",data.columns)
    s_y=col3.selectbox("target",data.columns)
    testsize=col1.select_slider("test size",[0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5])
    tree_type=col1.radio("models",['Decision Tree',"Random Forest"])
    x_tr,x_te,y_tr,y_te=split_data(data[s_x],data[s_y],testsize).split_imp()
    col2.info("train set length: "+str(x_tr.shape[0]))
    col3.info("test set length: "+str(x_te.shape[0]))

    if tree_type=="Decision Tree":
        st.write("--------------training------>")
        prog=st.progress(0)
        for i in range(100):
            tree=tree_class(x_tr,y_tr,x_te,y_te)
            time.sleep(0.01)
            prog.progress(i+1)
        st.write(tree.dec_tree_clfp())
        #st.balloons()
    elif tree_type=="Random Forest":
        pass
