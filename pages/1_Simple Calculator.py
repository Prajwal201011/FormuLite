from streamlit import *
import streamlit as st 
from streamlit_extras.colored_header import colored_header as ch
import math 
st.set_page_config(page_title='FormuLight: Illuminate Your Calculations',
        page_icon="🧮"
    )


st.sidebar.success("Welcome! 🎉")
st.sidebar.info("FormuLight is a simple calculator that can perform basic arithmetic operations and evaluate powers, square roots, and cube roots. 🧮")
ch (label= "⁉️ Simple Calculator",
               color_name='red-70')

n1 = st.number_input("Number 1", 0.0000, 10000000000.0000)
n2 = st.number_input("Number 2", 0.0000, 10000000000.0000)

c1, c2, c3 = st.columns(3)
with c1:
    ope = st.radio("Select an Operation", ('Addition', 'Subtraction', 'Multiplication', 'Division'))

with c2:
    opp = st.radio('#',('Power', "SquareRoot", "CubeRoot"))

def calculate():
    if ope == 'Addition':
        st.write(n1,'+' , n2,'=', n1 + n2)
    elif ope=='Subtraction':
        st.write(n1,'-' , n2,'=', n1 - n2)
    elif ope=='Multiplication':
        st.write(n1,'x' , n2,'=', n1 * n2)
    elif ope == 'Division' and n2!= 0:
        st.write(n1,'/' , n2,'=', n1 / n2)
    elif ope == 'Division' and n1!= 0:
        st.warning("Division by 0 error. Please enter a non-zero number.")
    else: 
        st.warning('Please select an operation')

def evaluate():
    if opp == 'Power':
        st.write( n1, "^", n2 ,"=", n1**n2 )
    elif opp == 'SquareRoot':
        st.warning('Enter 1 number for square root', icon='🤖')
        st.write("√", n1 ,'=', math.sqrt(n1))
    elif opp == 'CubeRoot':
        st.write("3√",n1,'=', n1**1/3)

with c1:
    if st.button ('Calculate'):
        calculate()
with c2:
    if st.button ('Evaluate'):
        evaluate()



st.write("-----")