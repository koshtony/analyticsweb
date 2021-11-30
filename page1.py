import streamlit as st
from scraper_html import scraped,csv_download,scrape_pdf
from PIL import Image
from tabula import read_pdf
from googlesearch import search
def page_1():
    global col1
    colm=st.sidebar
    colm1,colm2,colm3=st.columns((1,1,1))
    img=Image.open('g.png')
    colm.image(img,width=300)
    expnd=colm1.expander("About")
    expnd.markdown("""
    * passionate data scientist
    * student at Catholic University of Eastern Africa
    """)
    expnd2=colm2.expander("contacts")
    expnd2.markdown("""
    * phone: +254 712110972
    * github:
    * Linkedin:
    * Facebook:
    * Twitter
    """)
    expnd3=colm3.expander("Services")
    expnd3.markdown("""
    * Dashboards creation/
    * Web driven websites
    * Data Analysis
    * Data Streaming
    * Model Development

    """)

    st.write("""
    **Scrapes tables from websites and pdfs** """ )
    col1=st.sidebar
    col2,col3=st.columns((1,1))
    col2.write("""
    **scrape tables from websites**
    """)
    url=col2.text_input("copy website url here")
    table_no=col2.slider("which table? [0,1,2,3....]",0,10)
    tab_no=int(table_no)
    if col2.button("scrape table"):
        df=scraped(url,tab_no)
        if True:
            col2.write("""
            **scraped table**""")
            st.write(df)
            link=csv_download(df)
            col2.markdown(link,unsafe_allow_html=True)
        else:
            col2.write("""
            no recognized table in this site!! """)
    col2.write(""" ***sites to download data***""")
    col2.write(""" [kaggle datasets](https://www.kaggle.com/datasets)""")
    col2.write(""" [socrate](https://opendata.socrata.com/)""")
    col2.write(""" [Quandl] (https://www.quandl.com/search)""")
    col2.write(""" [Academic Torrent] (https://academictorrents.com/browse.php)""")
    col3.write("""
            **scrape tables from pdf**
            """)
    sach=col2.text_input("search data")
    if col2.button("search"):
        try:
            search_results=search(sach)
            for res in search_results:
                col2.write(res)
        except Exception as e:
            col2.write(e)
            col2.write("search not found")
    upload_file=col3.file_uploader("upload pdf file",['pdf'])
    col3.write(""" **or enter pdf online url** """)
    url2=col3.text_input("copy pdf url here")
    pdf_tab_no=col3.slider("which table?[0,1,2,3...]",0,10)
    t_no=int(pdf_tab_no)
    if col3.button("scrape tables from uploaded pdf"):
        try:
                tab=scrape_pdf(str(upload_file.name),t_no)
                if True:
                    col3.write("**tables from the pdf**")
                    col3.write(tab)
                    lk=csv_download(tab)
                    col3.markdown(lk,unsafe_allow_html=True)
        except Exception as error:
                    col3.write(error)
                    col3.write("""This pdf has no recognised tables""")
    if col3.button("scrape online pdf (url)"):
        try:
            table=scrape_pdf(url2,t_no)
            if True:
                st.write(""" table scraped from pdf """)
                st.write(tab)
                d_l=col3.markdown(d_l,unsafe_allow_html=True)
        except Exception as error:
            col3.write("""Failed to scrape table: either there are no recognised table or server error""")
