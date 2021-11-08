import streamlit as st
import statsmodels.api as s_api
import matplotlib.pyplot as plt
class lin_mod: #perform linear regression using sklearn and stamodels
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def model_imp(self):
        x=s_api.add_constant(self.x)
        y=self.y
        mod=s_api.OLS(y,x).fit()
        preds=mod.predict(x)
        st.write(mod.summary())
        mod_plots(preds-y)
        hetero(y,y-preds)
def mod_plots(res): # create a qqplot
    fig=s_api.qqplot(res,line='45')
    st.pyplot(fig)
def hetero(x,y): #check heteroscekedacity
    fig=plt.figure(figsize=(5,3))
    plt.scatter(x,y,alpha=0.5)
    plt.xlabel("response")
    plt.ylabel("residuals")
    plt.title("response vs residuals")
    st.pyplot(fig)
