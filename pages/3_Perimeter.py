from streamlit import *
import streamlit as st 
from streamlit_extras.colored_header import colored_header as ch
import math


ch (label= "Perimeter",
               color_name='red-70')
st.sidebar.success("Welcome! 🎉")
st.sidebar.info("This is a simple web app that calculates the perimeter of a two-dimensional figure.")
st.write('The perimeter of a two-dimensional figure is the distance covered around it.\n It defines the length of shape, whether it is a triangle, square, rectangle or a circle.')

sy = st.selectbox("Choose a 2D Shape ", ("Square", "Rectangle", "Parallelogram", "Triangle", "Circle", "Trapezium"))

if sy == "Square":
                tside = st.number_input('Side')
                def evl():
                        st.write('Perimeter') 
                        st.write(4*tside, 'units') 
                        st.write('$Formula: 4 * Side$')
                if st.button("Assess"):
                                evl()


elif sy == "Rectangle":
                l = st.number_input('Length')
                b = st.number_input('Breadth')
                def ev():
                        st.write('Perimeter') 
                        st.write(2*(l+b), 'units')
                        st.write('$Formula: 2 * (Length + Breadth)$')  
                if st.button("Check"):
                                ev()

elif sy == "Parallelogram":
                b = st.number_input('Base')
                h = st.number_input('Height')
                def eva():
                        st.write('Perimeter') 
                        st.write(2*(b+h), 'units')
                        st.write('$Formula: 2 * (Base + Height)$')
                if st.button("Anticipate"):
                                eva()
elif sy == "Circle":    
                r = st.number_input('Radius')
                
                def comp():
                        st.write("Circumference :", 2*math.pi*r )
                        st.write("$Formula: 2 * π * r$")
                if st.button("Compute"):
                                comp()
        
elif sy == "Triangle":
                g = st.selectbox("Perimeter or Hypotenuse", ("Perimeter" ,"Hypotenuse"))
                if g == "Perimeter":
                      a = st.number_input('Side A')
                      b = st.number_input('Side B')
                      c = st.number_input('Side c')  
                      def pe():
                                st.write("Perimeter :", a + b + c)
                                st.write("$Formula: Side A + Side B + Side C$")
                      if st.button("Find"):
                                pe()
                
                                                        
                elif g == "Hypotenuse":
                        leg = st.number_input('Leg 1')
                        legs = st.number_input('Leg 2')
                        def hypotenuse():
                                st.write('Hypotenuse :', math.sqrt(leg**2 + legs**2))
                                st.write('$Formula: √(Leg 1^2 + Leg 2^2)')
                        if st.button("Caliberate"):
                                hypotenuse()
                                
elif sy == "Trapezium":
                s = st.number_input('Side 1')
                ss = st.number_input('Side 2')
                sss = st.number_input('Side 3')
                ssss = st.number_input('Side 4')
                def sse():
                        st.write("Perimeter :", s + ss + sss + ssss)
                        st.write("$Formula: Side 1 + Side 2 + Side 3 + Side 4$")
                if st.button("Find"):
                                sse()
