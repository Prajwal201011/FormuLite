from streamlit import *
import streamlit as st 
from streamlit_extras.colored_header import colored_header as ch
import math 
st.sidebar.success("Welcome! 🎉")
ch (label= "Volume",
               color_name='red-70')

st.sidebar.info("This is a simple volume calculator for 3D shapes. Select a shape and enter the required values to calculate the volume of the shape. ")
st.write("A volume is simply defined as the amount of space occupied by any three-dimensional solid. These solids can be a cube, a cuboid, a cone, a cylinder or a sphere.")
shp = st.selectbox("Select a 3D shape:" , ('Cube', "Cuboid", "Pyramid", "Sphere", "Cylinder"))

if shp == 'Cube':
        s = st.number_input("Length of the Side")
        def co():
                st.write("Volume is ", s**3 ,"units³")
                st.write('[$Formula: s³$]')
        if st.button("Compete"):
                co()
elif shp == "Cuboid":
         w = st.number_input("Width of cuboid")
         l = st.number_input("Length of cuboid")
         h = st.number_input("Height of cuboid")
         def cub():
                 st.write("Volume:", w*l*h,"units³")
                 st.write('[$Formula: w*l*h$]')
         if st.button("Compete"):
                cub()
          
elif shp == "Pyramid":
        b = st.number_input("Base")
        h = st.number_input("Height")

        def coml():
                st.write("Volume is ", 1/3*b*h , "units³")
                st.write('[$Formula: 1/3*b*h$]')
        if st.button("Figure Out"):
                coml()

elif shp == "Sphere":
        r = st.number_input("Radius")
        def sph():
                st.write("Volume is ", 4/3*math.pi*r**3 , "units³")
                st.write('[$Formula: 4/3*π*r³$]')
        if st.button("Calibrate"):
                sph()
elif shp == "Cylinder":
        r = st.number_input("Radius")
        h = st.number_input("Height")
        def cy():
                st.write("Volume is ", math.pi*r**2*h , "units³")
                st.write('[$Formula: π*r²*h$]')
        if st.button("Complete"):
                cy()

st.write('--------')