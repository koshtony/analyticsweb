import pandas as pd
import streamlit as st
def desc_anal(data,col1,col2):
    stat=[""]
    sel_r=col1.radio("",["calculate statistics","group statistics"])
    col2.write("------------------------------")
    col2.write("------------------------------")
    col2.write("------------------------------")
    col2.write("-------------results--------------------------------------")
    if sel_r=="calculate statistics":
        try:
            des_sel=col1.multiselect("select columns",data.columns)
            stat_sel=col1.multiselect("select statistic",["mean","median","std","kurtosis","skewness","min","count","max"])
            dic={}
            for i in des_sel:
                dic[i]=stat_sel
            col2.write(data[des_sel].agg(dic))
        except:
            expnd=col1.expander("something not right..ensure that:")
            expnd.markdown("""
            * All the fields are selected
            * Data is uploaded
            * Appropriate columns and statistic are selected.
            """)


    if sel_r=="group statistics":
        try:
            r_multi1=col1.multiselect("select columns to compute with:",data.columns)
            r_multi2=col1.multiselect("select columns to group with :",data.columns)
            r_stat=col1.multiselect("select statistics to cumpute",["mean","median","std","mode","skewness","kurtosis","count","min","max"])
            dik={}
            dik={}
            alls=[]
            for i in r_multi2:
                alls.append(i)
            for i in r_multi1:
                alls.append(i)
            for i in r_multi1:
                dik[i]=r_stat
            col2.write(dik)
            grps=data[alls].groupby(r_multi2).agg(
            dik
            )

            col2.write(grps)
        except:
            expnd=col1.expander("something not right..ensure that:")
            expnd.markdown("""
            * All the fields are selected
            * Data is uploaded
            * Appropriate columns and statistic are selected.
            """)
