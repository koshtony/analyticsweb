from sklearn.ensemble import RandomForestClassifier as RFC
from dec_tree import tree_class
import sklearn.metrics as met
import streamlit as st
class forest(tree_class):
    def __init__(self,x,y,xte,yte,n_est):
        super().__init__(x,y,xte,yte)
        self.n_est=n_est
    def forest_imp(self):
        return RFC(n_estimators=self.n_est,random_state=0).fit(self.x,self.y)
    def forest_clf(self):
        return met.classification_report(self.yt,self.forest_imp().predict(self.xt))
    def forest_conf_matrix(self):
        return met.confusion_matrix(self.yt,self.forest_imp().predict(self.xt))
    @st.cache
    def forest_fet_imp(self):
        return self.forest_imp().feature_importances_
