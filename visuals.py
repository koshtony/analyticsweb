import streamlit as st
import seaborn as sb
import matplotlib.pyplot as plt
def graphs(data):
    v=st.sidebar
    v1,v2,v3=st.columns((1,1,1))
    v2.write("--------------------------------------")
    v2.write("--------------------------------------")
    v3.write("--------------------------------------")
    v3.write("--------------------------------------")

    major_rad=v1.radio("",["unvariate plots","Bivariate plots","Multivariate plots"])
    #v1.write("--------------------------------------")
    selects=v1.selectbox("x",data.columns)
    select_y=v1.selectbox("y",data.columns)
    by=v1.multiselect("group by",data.columns)
    if len(by)==1:
        by=by[0]
    elif len(by)==0:
        by=by
    else:
        v3.warning("only one selection is permitted")
    col=v1.multiselect("group also by",data.columns)
    if len(col)==1:
        col=col[0]
    elif len(by)==0:
        col=col
    else:
        v3.warning("only one selection is permitted")

    width=v3.slider("set plot height",1,10)
    height=v3.slider("set plot width",1,10)
    xlab=v2.text_input("x label title")
    ylab=v2.text_input("y label title")
    title=v2.text_input("main title")
    v3.write("--------------------------------------")
    v3.write("--------------------------------------")
    v3.write("--------------------------------------")
    v2.write("--------------------------------------")
    v2.write("--------------------------------------")
    if major_rad=="unvariate plots":
        m1_rad=v2.radio("",["Categorical","Quantitative"])
        if m1_rad=="Categorical":

            trad=v3.radio("",["Frequency","Percentage"])
            if trad=="Frequency":
                cat=categorical(data,selects,xlab,title,width,height)
                cat.countplots_f()
                #cat.countplots_per()
            elif trad=="Percentage":
                pass
                #cat=categorical(data,selects,xlab,title,width,height)
                #cat.countplots_per()

                #cat2=categorical(data,selects,xlab,title)
                #cat2.catplots_per()
        elif m1_rad=="Quantitative":
            q=quants(data,selects,xlab,title,width,height)
            q.distribution()
    elif major_rad=="Bivariate plots":
        type_rad=v2.radio("",["scatterplots","distribution plots","categorical plots"])
        if type_rad=="scatterplots":
            try:
                scat=biva(data,selects,select_y,by,xlab,ylab,title,width,height)
                scat.scatter_plot()

            except Exception as e:
                st.warning("Encountered Error..kindly check our guidelines")
        elif type_rad=="categorical plots":
            scats=biva(data,selects,select_y,by,xlab,ylab,title,width,height)
            scats.categorical_biv()
    elif major_rad=="Multivariate plots":
        multiple=multi(data,selects,select_y,by,col,title,width,height)
        multiple.facet()
        multiple.pairplot()




class categorical(object):
    def __init__(self,data,x,xlab,title,width,height):
        self.data=data
        self.x=x
        self.xlab=xlab
        self.title=title
        self.height=height
        self.width=width
    def countplots_f(self):
        fig=plt.figure(figsize=(self.height,self.width))
        sb.countplot(x=self.x,data=self.data)
        plt.xlabel(self.xlab)
        plt.title(self.title)
        st.pyplot(fig)
    def countplots_per(self):
        fig2=plt.figure()
        self.x = self.data.x.apply(lambda x: (x/sum(data.x))*100)
        sb.countplot(x=self.x)
        plt.xlabel(self.xlab)
        plt.title(self.title)
        st.pyplot(fig2)
class quants(categorical):
    def distribution(self):
        fg=plt.figure(figsize=(self.height,self.width))
        sb.distplot(x=self.data[self.x],hist=True,kde=True)
        plt.xlabel(self.xlab)
        plt.title(self.title)
        st.pyplot(fg)
class biva(object):
    def __init__(self,data,x,y,hue,xlab,ylab,title,width,height):
        self.data=data
        self.x=x
        self.y=y
        self.hue=hue
        self.xlab=xlab
        self.ylab=ylab
        self.title=title
        self.width=width
        self.height=height
    def scatter_plot(self):
        if self.hue:
            scat=plt.figure(figsize=(self.height,self.width))
            sb.scatterplot(x=self.x,y=self.y,hue=self.hue,data=self.data)
            plt.xlabel(self.xlab)
            plt.ylabel(self.ylab)
            plt.title(self.title)
            st.pyplot(scat)
        else:
            scat=plt.figure(figsize=(self.height,self.width))
            sb.scatterplot(x=self.x,y=self.y,data=self.data)
            plt.xlabel(self.xlab)
            plt.ylabel(self.ylab)
            plt.title(self.title)
            st.pyplot(scat)
    def categorical_biv(self):
        if self.hue:
            cat,ax=plt.subplots(2,2,figsize=(self.height,self.width))
            sb.swarmplot(ax=ax[0,0],x=self.x,y=self.y,hue=self.hue,data=self.data)
            sb.boxplot(ax=ax[0,1],x=self.x,y=self.y,hue=self.hue,data=self.data)
            sb.catplot(ax=ax[1,0],x=self.x,y=self.y,hue=self.hue,data=self.data)
            sb.catplot(ax=ax[1,1],x=self.x,y=self.y,hue=self.hue,data=self.data)
            plt.xlabel(self.xlab)
            plt.ylabel(self.ylab)
            plt.title(self.title)
            st.pyplot(cat)
        else:
            cat,ax=plt.subplots(2,2,figsize=(self.height,self.width))
            sb.swarmplot(ax=ax[0,0],x=self.x,y=self.y,data=self.data)
            sb.boxplot(ax=ax[0,1],x=self.x,y=self.y,data=self.data)
            sb.violinplot(ax=ax[1,0],x=self.x,y=self.y,data=self.data)
            sb.pointplot(ax=ax[1,1],x=self.x,y=self.y,data=self.data)
            plt.xlabel(self.xlab)
            plt.ylabel(self.ylab)
            plt.title(self.title)
            st.pyplot(cat)
class multi(object):
    def __init__(self,data,x,y,hue,col,title,width,height):
        self.data=data
        self.x=x
        self.y=y
        self.col=col
        self.hue=hue
        self.title=title
        self.width=width
        self.height=height
    def pairplot(self):
        if self.hue:
            fig=plt.figure(figsize=(self.height,self.width))
            sb.pairplot(self.data,hue=self.hue,palette="set2")
            plt.title(self.title)
            st.pyplot(fig)
        else:
            fig=plt.figure(figsize=(self.height,self.width))
            sb.pairplot(self.data,palette="set2")
            plt.title(self.title)
            st.pyplot(fig)
    def facet(self):
            fg=sb.FacetGrid(self.data,col=self.col,hue=self.hue,height=self.height)
            fg.map_dataframe(plt.scatter,x=self.x,y=self.y,alpha=.7)
            fg.add_legend()
            st.pyplot(fg)
            fg=sb.FacetGrid(self.data,col=self.col,hue=self.hue,height=self.height)
            fg.map(sb.barplot,self.x,self.y,alpha=.7)
            fg.add_legend()
            st.pyplot(fg)
            fg=sb.FacetGrid(self.data,col=self.col,hue=self.hue,height=self.height)
            fg.map(sb.histplot,self.x,alpha=.7)
            fg.add_legend()
            st.pyplot(fg)
