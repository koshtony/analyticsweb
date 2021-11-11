from sklearn.model_selection import train_test_split
import streamlit as st
class split_data:# split the dataset
    def __init__(self,x,y,size):
        self.x=x
        self.y=y
        self.size=size
    @st.cache
    def split_imp(self):
        return train_test_split(self.x,self.y,test_size=self.size,random_state=1)
