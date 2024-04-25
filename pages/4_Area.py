from streamlit import *
import streamlit as st 
from streamlit_extras.colored_header import colored_header as ch
import math

st.sidebar.success("Welcome! 🎉")
st.sidebar.info("This is a simple web app that calculates the area of a 2D shape. Select a shape from the dropdown menu and enter the required values. Click the button to calculate the area.")
ch (label= "Area",
               color_name='red-70')
st.write("The area is the region bounded by the shape of an object.\n The space covered by the figure or any two-dimensional geometric shape, in a plane, is the area of the shape.")
shap = st.selectbox("Select a 2D shape:" , ('Square', "Circle", "Triangle", "Rectangle", "Parallelogram", "Trapezium"))

if shap == 'Square':
        s = st.number_input("Length of Side")
        def cal():
                st.write("Area is ", s**2 )
                st.write("$Formula: s^2$")
        if st.button("Reckon"):
                cal()

elif shap == "Circle":
        r = st.number_input("Radius of Circle:")
        def cir():
                st.write("Area is ", math.pi*r**2 )
                st.write("$Formula: πr^2$")
        if st.button("Add up"):
                cir()

elif shap == "Triangle":
        b = st.number_input("Base")
        h = st.number_input("Height")
        def com():
                st.write("Area is ", 1/2*b*h )
                st.write("$Formula: 1/2*b*h$")
        if st.button("Tally"):
                com()

elif shap == "Rectangle":
        l = st.number_input("Length")
        w = st.number_input("Width")
        def rec():
                st.write("Area is ", l*w )
                st.write("$Formula: l*w$")
        if st.button("Totalize"):
                rec()

elif shap == "Parallelogram":
        b = st.number_input("Base")
        h = st.number_input("Height")
        def coml():
                st.write("Area is ", b*h )
                st.write("$Formula: b*h$")
        if st.button("Quantify"):
                coml()

elif shap == "Trapezium":
        a = st.number_input("Base 1")
        b = st.number_input("Base 2")
        h = st.number_input("Height")
        def coml():
                st.write("Area is ", 1/2*(a+b)*h )
                st.write("$Formula: 1/2*(a+b)*h$")
        if st.button("Cast"):
                coml()
st.write("------")