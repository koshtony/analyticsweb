from linear_reg import lin_mod
import streamlit as st
import statsmodels.api as sm
import pandas as pd
class glm(lin_mod): # General Linear models
    @st.cache
    def gamma_imp(self):
        x=sm.add_constant(self.x)
        mod=sm.GLM(self.y,x,family=sm.families.Gamma()).fit()
        return mod.summary()
    @st.cache
    def poiss_imp(self):
        x=sm.add_constant(self.x)
        mod=sm.GLM(self.y,x,family=sm.families.Poisson()).fit()
        return mod.summary()
    @st.cache
    def bino_imp(self):
        x=sm.add_constant(self.x)
        mod=sm.GLM(self.y,x,family=sm.families.Binomial()).fit()
        return mod.summary()
    @st.cache
    def negbino_imp(self):
        x=sm.add_constant(self.x)
        mod=sm.GLM(self.y,x,family=sm.families.NegativeBinomial()).fit()
        return mod.summary()
