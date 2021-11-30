import streamlit as st
from tree_reg import tree_reg,forest_reg
from tree_models import fet_imp_plot
from splitter import split_data
from PIL import Image
import time
def t_regressor(data,col1,col2,col3,testsize): # creating tree regression model user interface
    x_val=col2.multiselect("Features",data.columns)
    y_val=col2.selectbox("Target",data.columns)
    tree_reg_type=col1.radio("models",['Decision Tree',"Random Forest"])
    x_tr,x_te,y_tr,y_te=split_data(data[x_val],data[y_val],testsize).split_imp()
    col2.info("train set length: "+str(x_tr.shape[0]))
    col3.info("test set length: "+str(x_te.shape[0]))
    if tree_reg_type=="Decision Tree":
        st.write("Training--->")
        progress=st.progress(0)
        for i in range(100):
            t_reg=tree_reg(x_tr,y_tr,x_te,y_te)
            time.sleep(0.01)
            progress.progress(i+1)
        fet_imp_plot(t_reg.tree_reg_fet_imp())
        st.info("mean squared error: "+str(t_reg.tree_scores()))
        t_reg.vis_tree_reg()
        t_reg_im=Image.open("tree_reg.png")
        st.info("regression tree diagram")
        st.image(t_reg_im,caption="regression tree")
    elif tree_reg_type=="Random Forest":
        st.write("Training--->")
        progress=st.progress(0)
        for i in range(100):
            forest=forest_reg(x_tr,y_tr,x_te,y_te)
            time.sleep(0.01)
            progress.progress(i+1)
        fet_imp_plot(forest.train_mod())
        st.info("mean squared error: "+str(forest.evaluate()))
