import streamlit as st
from src.math_utils import add,sqr
st.write("Simple application to add two numbers and square them")
a = st.number_input("Enter the first number",min_value = 1,max_value = 100)
b = st.number_input("Enter the second number",min_value = 1,max_value = 100)
if st.button('calculate'):
    c = add(a,b)
    d = sqr(c)
    st.write(f"Sum of two numbers {a} and {b} is: {c}")
    st.write(f"Square of added two numbers {c} is: {d}")
else:
    st.write("click on calculate")


