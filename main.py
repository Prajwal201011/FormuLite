from streamlit import *
import streamlit as st 
import math 

st.set_page_config(page_title='FormuLight: Illuminate Your Calculations',
        page_icon="🧮"
    )

name = st.sidebar.text_input("Enter your name:")
st.sidebar.success(f"Welcome to FormuLite {name}! 🎉")

st.title("FormuLite: Illuminate Your Calculations")
st.write('--------')
st.write("FormuLite is a simple web app that allows you to perform basic calculations. It is built using Streamlit, a popular Python library for building web apps. You can perform calculations such as addition, subtraction, multiplication, and division. You can also calculate the square root of a number and raise a number to a power. FormuLite is a great tool for students, teachers, and professionals who need to perform quick calculations.")

st.write('FormuLight is not just a calculator, it’s a comprehensive guide to mathematical formulas and their applications. \n This innovative app is designed to help you solve complex problems with ease and understand the logic behind them.')

st.write("""Key Features:\n
Comprehensive Formula Library: Access a wide range of mathematical formulas from basic arithmetic to advanced culations.\n
Single Line Explanations: Each formula comes with a concise explanation to help you understand its purpose and usage.\n
Advanced Calculator: Solve any mathematical problem using our advanced calculator that supports all mathematical operations.\n
User-Friendly Interface: Navigate through the app with ease thanks to our intuitive and user-friendly interface.\n""")


st.write("To get started, select a calculation from the sidebar on the left and enter the required inputs.\n Click the 'Calculate' button to see the result\n You can also click the 'Clear' button to clear the inputs and start over.")

st.write('--------')

