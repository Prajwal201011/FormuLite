from streamlit import *
import streamlit as st 
from streamlit_extras.colored_header import colored_header as ch
import math 

st.sidebar.success("Welcome! 🎉")
st.header("Speed, Distance and Time")

st.write("This app calculates the speed, distance and time of an object. Please enter the values in the fields below.")
st.write("Speed: Speed is the rate at which a particular distance is covered by an object in motion.\nTime: Time is an interval separating two events.\nDistance: Distance is the extent of space between two points.")

sel = st.selectbox("Select a parameter to calculate", ("Speed", "Distance", "Time"))
if sel == "Speed":
        d = st.number_input("Distance (m)")
        t = st.number_input("Time")
        def speed():
                st.write("Speed is ", d/t , "m/s")
                st.write("[$Formula: Speed = Distance/Time$]")
        if st.button("Enumerate"):
                speed()
elif sel == "Distance":
        s = st.number_input("Speed (m/s)")
        t = st.number_input("Time")
        def dist():
                st.write("Distance is ", s*t , "m")
                st.write("[$Formula: Distance = Speed x Time$]")
        if st.button("Figure Out"):
                dist()
elif sel == "Time":
        d = st.number_input("Distance (m)")
        s = st.number_input("Speed (m/s)")
        def time():
                st.write("Time is ", d/s , "s")
                st.write("[$Formula: Time = Distance/Speed$]")
        if st.button("Put a figure On it"):
                time()


st.write('--------')