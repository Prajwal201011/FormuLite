from streamlit import *
import streamlit as st 
from streamlit_extras.colored_header import colored_header as ch
import math 
st.sidebar.success("Welcome! 🎉")
st.header ("Compund Interest")
st.sidebar.info("This app calculates the compound interest for you. Just enter the values and get the result.")

st.write("Compound interest is the interest calculated on the initial principal and also on the accumulated interest of previous periods of a deposit or loan.\n It is the result of reinvesting interest, rather than paying it out, so that interest in the next period is then earned on the principal sum plus previously accumulated interest.")
principal = st.number_input("Enter the principal amount", min_value=0.0)
rate = st.number_input("Enter the rate of interest", min_value=0.0)
time = st.number_input("Enter the time period", min_value=0.0)

def compound_interest(principal, rate, time):
    amount = principal * math.pow((1 + rate / 100), time)
    ci = amount - principal
    return ci

if st.button("Calculate"):
    ci = compound_interest(principal, rate, time)
    st.write(f"The compound interest is {ci}")
    st.write("[$Formula used: A = P(1 + r/100)^t$]")

st.sidebar.info("Thank you for using this app! 😊")
