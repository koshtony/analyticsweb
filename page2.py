import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from PIL import Image
from stream import curr
from scraper_html import csv_download
from datetime import datetime
from datetime import datetime
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import time
from desc import desc_anal
from visuals import graphs
from infer import inferential
def page_2():
    col1=st.sidebar
    col2,col3=st.columns((1,1))
    uploads=col2.file_uploader("upload csv file",type=["csv","xlsx","xls","txt"])
    cal_radio=col1.radio("cleaning->Analysis->modelling",["check nullity","remove columns",
    "replace empty cells (na)","replace and remove empty cells (na)",
    "detect outliers","Descriptive statistics","Visualisation","Inferential statistics"])
    if cal_radio=="check nullity":
        try:
        #up_file=open("upload.txt","w")
        #up_c=up_file.write(str(uploads.name))
            null_df=check_na(uploads)
            st.write(null_df)
        except:
            col2.write("**no file uploaded**")
            col3.markdown("""
            -----------------------------------------
            -----------------------------------------
            -----------------------------------------
            -----------------------------------------

            -------plots and tables here !!----------
            -----------------------------------------
            -----------------------------------------
            -----------------------------------------
            """)

    elif cal_radio=="remove columns":
        try:
            remove_na(uploads,col2)
        except:
            col2.write("**no loaded data or inappropriate selection**")
            col3.markdown("""
                -----------------------------------------
                -----------------------------------------
                -----------------------------------------
                -----------------------------------------

                -------plots and tables here !!----------
                -----------------------------------------
                -----------------------------------------
                -----------------------------------------
            """)

    elif cal_radio=="replace empty cells (na)":
        try:
            replace_na(uploads,col2)
        except:
            col2.write("**no loaded data or inappropriate selection**")
            col3.markdown("""
                -----------------------------------------
                -----------------------------------------
                -----------------------------------------
                -----------------------------------------

                -------plots and tables here !!----------
                -----------------------------------------
                -----------------------------------------
                -----------------------------------------
            """)
    elif cal_radio=="replace and remove empty cells (na)":
        try:
            some_some(uploads,col2)
        except Exception as err:
            col2.write("no loaded data or inappropriate selection")
            col3.markdown("""
                -----------------------------------------
                -----------------------------------------
                -----------------------------------------
                -----------------------------------------

                -------plots and tables here !!----------
                -----------------------------------------
                -----------------------------------------
                -----------------------------------------
            """)

    elif cal_radio=="detect outliers":
        cleans=col2.selectbox("is your data already clean ?",["detect as it is","detect preprocessed data"])
        if cleans=="detect as it is":
            try:
                detect_outliers(upload_csv(uploads),col3)
            except Exception as e:

                col2.write("no column selected yet | the column selected is not numerical")
                col3.markdown("""
                -----------------------------------------
                -----------------------------------------
                -----------------------------------------
                -----------------------------------------

                -------plots and tables here !!----------
                -----------------------------------------
                -----------------------------------------
                -----------------------------------------
                """)

        elif cleans=="detect preprocessed data":
            try:
                detect_outliers(new_data,col3)
            except:
                col3.markdown("""
            -----------------------------------------
            -----------------------------------------
            -----------------------------------------
            -----------------------------------------

            -------plots and tables here !!----------
            -----------------------------------------
            -----------------------------------------
            -----------------------------------------
            """)

    elif cal_radio=="Descriptive statistics":
        choice=col2.selectbox("choose data",["use uploaded data as it is","use data you have preprocessed"])
        if choice=="use uploaded data as it is":
            try:
                desc_anal(upload_csv(uploads),col2,col3)
            except Exception as e:
                col2.write("no file uploaded yet")
        elif choice=="use data you have preprocessed":
            try:
                desc_anal(new_data,col2,col3)
            except:
                col2.write("no preprocessing carried out")
    elif cal_radio=="Visualisation":
        choices=col2.selectbox("choose data",["use uploaded data as it is","use data you have preprocessed"])
        if choices=="use uploaded data as it is":
            try:
                graphs(upload_csv(uploads))
            except Exception as e:
                col2.write(e)
        elif choices=="use data you have preprocessed":
            try:
                graphs(new_data)
            except Exception as e:
                col2.write(e)
    elif cal_radio=="Inferential statistics":
        inferential()







def upload_csv(uploads):
    if uploads.type=="text/csv":
        data=pd.read_csv(uploads)
        return data
    else:
        try:
            data=pd.read_excel(uploads)
            return data
        except Exception as e:
            st.write("----try loading correct file format | file not found----")
    ret_data()
def check_na(file):
            df=upload_csv(file)
            null=df.isnull().any()
            return null
def remove_na(file,col):
    global new_data
    dat=upload_csv(file)
    columns=dat.columns
    sel_col=col.multiselect('select column(s) to drop!!',columns)
    all_cols=[]
    for i in sel_col:
        all_cols.append(i)
    if col.button("drop selected columns with"):
        new_data=dat.drop(all_cols,axis=1)
        col.write(""" download the cleaned file """)
        col.markdown(csv_download(new_data),unsafe_allow_html=True)
        passer(new_data)
def replace_na(file,colu):
    global new_data
    data=upload_csv(file)
    rep_with=colu.multiselect("select columns",data.columns)
    if colu.button("replace with mean"):
        m_n=data[rep_with].mean()
        new_data=data.fillna(m_n)
        colu.markdown(csv_download(new_data),unsafe_allow_html=True)
        passer(new_data)
def some_some(file,cols):
    global new_data
    deta=upload_csv(file)
    rem_col=cols.multiselect("columns to remove",deta.columns)
    rep_col=cols.multiselect("columns to replace",deta.columns)
    remv=[]
    for i in rem_col:
        remv.append(i)
    if cols.button("remove and replace na"):
        new_da=deta.drop(remv,axis=1)
        mean_s=new_da[rep_col].mean()
        new_data=new_da.fillna(mean_s)
        cols.write("**selected columns have been successfully removed and replaced**")
        cols.markdown(csv_download(new_data),unsafe_allow_html=True)
        passer(new_data)
def detect_outliers(data,clm):
    sel_plot=clm.selectbox("select column to detect outliers",data.columns)
    clm.write(sel_plot)
    if True:
        fig=plt.figure(figsize=(5,5))
        sb.boxplot(data=data,x=str(sel_plot))
        clm.pyplot(fig)
