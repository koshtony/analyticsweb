import streamlit as st
from sklearn.tree import DecisionTreeClassifier
import sklearn.metrics as met
class tree_class:
    def __init__(self,x,y,xt,yt):
        self.x=x
        self.y=y
        self.xt=xt
        self.yt=yt
    @st.cache
    def dec_tree_imp(self):
        clf=DecisionTreeClassifier()
        clf=clf.fit(self.x,self.y)
        return clf.predict(self.xt)
    @st.cache
    def dec_tree_clfp(self):
        return met.classification_report(self.yt,self.dec_tree_imp())
