from sympy import *
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import sympy.plotting as pl
from sympy.parsing.sympy_parser import parse_expr
def calc():
    x,y,z,t=symbols('x y z t')
    init_printing(use_unicode=True)
    equation=st.text_input("add equation here")
    equation=str(equation).lower()
    calc1=st.sidebar
    calc2,calc3=st.columns((1,1))
    calc2.write("**Differentiation**")
    calc1.write("**video example**")
    calc1.video("instr.webm")
    with_res=calc2.text_input("Differentiate: with respect to")
    with_res=with_res.lower()
    calc3.write("**Integration**")
    int_no=calc3.slider("number of integrations",0,3)
    fst1,s2,thrd=[],[],[]
    for i in range(int_no):
        with_res_to=calc1.text_input("input "+str(i+1)+" .integrate: with respect to:")
        with_res_to=with_res_to.lower(

        )
        lower_lim=calc1.text_input("lower limit "+str(i+1))
        upper_lim=calc1.text_input("upper limit "+str(i+1))
        if i==0:
                fst1.append([with_res_to,lower_lim,upper_lim])

        elif i==1:
                s2.append([with_res_to,lower_lim,upper_lim])
        elif i==2:
                thrd.append([with_res_to,lower_lim,upper_lim])



    try:
        calc2.write("------------------------------")
        calc2.write("----------derivative----------")
        calc2.write("------------------------------")
        calc2.write("equation:>>>>>>")
        calc2.write(Derivative(equation,with_res))
        calc2.write("solution:>>>>>>")
        calc2.write(diff(equation,with_res))
        try:
            p=pl.plot(equation)
            p.save('fig.png')
            calc2.write("**corresponding equation plot**")
            ims=Image.open('fig.png')
            calc2.image(ims,width=300)
        except:
            p=pl.plot3d(equation)
            p.save('fig.png')
            calc2.write("**corresponding equation plot**")
            ims=Image.open('fig.png')
            calc2.image(ims,width=300)
    except:
        calc2.warning("The input fields are empty..if not kindly check out the guidelines.")

    try:
        calc3.write("------------------------------")
        calc3.write("----------Integral--------------")
        calc3.write("------------------------------")


        if int_no==1:
            calc3.write(Integral(equation,tuple(fst1)))
            calc3.write(integrate(equation,tuple(fst1)))
        elif int_no==2:
            calc3.write(Integral(equation,fst1,s2))
            calc3.write(integrate(equation,fst1,s2))
        elif int_no==3:
            calc3.write(Integral(equation,tuple(fst1),tuple(s2),tuple(thrd)))
            calc3.write(integrate(equation,tuple(fst1),tuple(s2),tuple(thrd)))

    except Exception as err:
        calc3.warning("The input fields are empty..if not kindly check out the guidelines.")
    calc2.write("**Limits**")
    calc3.write("**Series Expansion**")
    lim=calc2.text_input("limit equation")
    lim=lim.lower
    val=calc2.text_input("variable i.e x,y..")
    val=val.lower
    app=calc2.text_input("approaching")
    rd=calc2.radio("",["+","-"])
    if rd=="+":
        if app=="infinity":
            try:
                calc2.write(">>>>equation>>>>")
                calc2.write(Limit(lim,val,oo))
                calc2.write(">>>>solution>>>>")
                calc2.write(limit(lim,val,oo))
            except:
                calc2.warning("The input fields are empty..if not kindly check out the guidelines.")
        else:
            try:
                calc2.write(">>>>equation>>>>")
                calc2.write(Limit(lim,val,app))
                calc2.write(">>>>solution>>>>")
                calc2.write(limit(lim,val,app))
            except:
                calc2.warning("The input fields are empty..if not kindly check out the guidelines.")
    if rd=="-":
        if app=="infinity":
            try:
                calc2.write(">>>>equation>>>>")
                calc2.write(Limit(lim,val,oo,'-'))
                calc2.write(">>>>solution>>>>")
                calc2.write(limit(lim,val,oo,'-'))
            except:
                calc2.warning("The input fields are empty..if not kindly check out the guidelines.")
        else:
            try:
                calc2.write(">>>>equation>>>>")
                calc2.write(Limit(lim,val,app,'-'))
                calc2.write(">>>>solution>>>>")
                calc2.write(limit(lim,val,app,'-'))
            except:
                calc2.warning("The input fields are empty..if not kindly check out the guidelines.")
    series_eq=calc3.text_input("Initialize Series")
    val=calc3.text_input("variable:")
    from_=calc3.text_input("from:")
    to=calc3.text_input("to:")
    try:
        calc3.write(">>>>Expanded Series >>>>")
        sq=parse_expr(series_eq)
        calc3.write(sq)
        calc3.write(sq.series(val,from_,to))
    except Exception as err:
        #st.write(err)
        calc3.warning("The input fields are empty..if not kindly check out the guidelines.")
