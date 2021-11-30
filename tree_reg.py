from sklearn.tree import DecisionTreeRegressor,export_graphviz
from dec_tree import tree_class
import sklearn.metrics as met
from six import StringIO
import pydotplus
import streamlit as st
class tree_reg(tree_class): # implementing decision tree regression
    @st.cache
    def tree_reg_imp(self):
        return DecisionTreeRegressor().fit(self.x,self.y)
    @st.cache
    def tree_reg_fet_imp(self):
        return self.tree_reg_imp().feature_importances_
    @st.cache
    def tree_scores(self):
        return met.mean_squared_error(self.yt,self.tree_reg_imp().predict(self.xt))
    @st.cache
    def vis_tree_reg(self):
        dot_data = StringIO()
        export_graphviz(self.tree_reg_imp(), out_file=dot_data,
                 feature_names = list(self.x.columns))
        graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
        graph.write_png('tree_reg.png')
