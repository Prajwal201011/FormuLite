from streamlit import *
import streamlit as st 
import math 

st.sidebar.success("Welcome! 🎉")
st.header ( "Surface Area")
st.write("This is a simple web app that calculates the surface area of a 3D shape. You can select a 3D shape from the dropdown menu and enter the required values to calculate the surface area of the shape. The app can calculate the surface area of a Cube, Cuboid, Pyramid, and Sphere. The formulas used to calculate the surface area of each shape are also displayed. Click the button below to get started!")
st.write("The total area occupied by the surfaces of an object is called its surface area. ")
cu = st.selectbox("Select a 3D shape to calculate Surface Area:" , ('Cube', "Cuboid", "Pyramid", "Sphere"))
if cu == 'Cube':
        s = st.number_input("Length of the Side of the Cube")
        def co():
                st.write("Surface Area is ", 6*s**2 )
                st.write("[$Formula: 6 * s²$]")
        if st.button("Compute"):
                co()

elif cu == "Cuboid":
        w = st.number_input("Width of  3D cuboid")
        l = st.number_input("Length of 3D cuboid")
        h = st.number_input("Height of  3D scuboid")
        def cub():
                st.write("Surface Area:", 2*(w*l + l*h + h*w),"units²")
                st.write("[$Formula: 2 * (w*l + l*h + h*w)$]")
        if st.button("Tabulate"):
                cub()

elif cu == "Pyramid":
        b = st.number_input("Base")
        h = st.number_input("Height")
        def coml():
                st.write("Surface Area is ", b**2 + 2*b*(math.sqrt((b**2)/4 + h**2)) , "units²")
                st.write("[$Formula: b² + 2b√(b²/4 + h²)$]")
        if st.button("Check out"):
                coml()

elif cu == "Sphere":
        r = st.number_input("Radius")
        def sph():
                st.write("Surface Area is ", 4*math.pi*r**2 , "units²")
                st.write("[$Formula: 4πr²$]")
        if st.button("Make Out"):
                sph()
