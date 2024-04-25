from streamlit import *
import streamlit as st 
import math
st.sidebar.success("Welcome! 🎉")
st.header("Simple Interest")

st.sidebar.info("This is a simple interest calculator. You can calculate the simple interest and the amount by providing the principal, rate and term. \n You can provide the input either by using the slider or by typing the value in the text box.")
st.write('Simple Interest is an easy method of calculating the interest for a loan/principal amount.\n Simple interest is a concept that is used in many sectors such as banking, finance, automobile, and so on.')
st.write('$Simple Interest = (Principal * Rate * Term) / 100 \n Amount = Principal + Simple Interest$')
sl = st.selectbox("Input Type", ("Slider", "Text"))
if sl == "Slider":
        p1 = st.slider('Principal',100,10000)
        t1 = st.slider('Term',100,10000)
        r1= st.slider('Rate',0, 100)
        
        btn = st.button("Workout")
        def calculate():
                si = st.write("Simple Interest Is: " , (p1*t1*r1)/100)
                amt = st.write("Amount is: " , si + p1)
        if btn :
                calculate()
        
elif sl == 'Text':
        p = st.text_input('Principal',100)
        t = st.text_input('Term',100)
        r = st.text_input('Rate',0, 100)

        btn2 = st.button("Cast")
        def calculate():
                st.write("Simple Interest Is: " , p*t*r/100)
                st.write("Amount is: " , p+p*t*r/100)
                
        if btn2 :
                 calculate()



st.write('--------')
