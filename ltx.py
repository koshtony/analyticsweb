import streamlit as st
def editor():
    eq=st.text_area("latex code here")
    st.latex(eq)
