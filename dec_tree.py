import streamlit as st
from sklearn.tree import DecisionTreeClassifier
import sklearn.metrics as met
from six import StringIO
from sklearn.tree import export_graphviz
import pydotplus
import pandas as pd
class tree_class: # implements sklearn decision tree
    def __init__(self,x,y,xt,yt):
        self.x=x
        self.y=y
        self.xt=xt
        self.yt=yt
    @st.cache
    def dec_tree_imp(self):
        clf=DecisionTreeClassifier()
        clf=clf.fit(self.x,self.y)
        return clf
    @st.cache
    def dec_tree_clfp(self):
        return met.classification_report(self.yt,self.dec_tree_imp().predict(self.xt))
    @st.cache
    def feature_imp(self):
        model=self.dec_tree_imp()
        return model.feature_importances_
    @st.cache
    def conf_matrix(self):
        return met.confusion_matrix(self.yt,self.dec_tree_imp().predict(self.xt))
    @st.cache
    def vis_tree(self):
        dot_data = StringIO()
        export_graphviz(self.dec_tree_imp(), out_file=dot_data,filled=True,
                 feature_names = list(self.x.columns),class_names=[str(i) for i in pd.unique(self.y)])
        graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
        graph.write_png('tree.png')
