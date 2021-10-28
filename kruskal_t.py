class kruskal_w:
    def __init__(self,col1,col2,col3,conf,ho,h1):
        self.col1=col1
        self.col2=col2
        self.col3=col3
        self.conf=conf
        self.ho=ho
        self.h1=h1
    def kruskal_test(self):
        if type(self.col1)==str:
            col1=[c for c in self.col1.split(',')]
            col2=[c for c in self.col2.split(',')]
            col3=[c for c in self.col3.split(',')]
        st.info(self.ho)
        st.info(self.)
