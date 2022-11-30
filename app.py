import streamlit as st
import pandas as pd
import numpy as np

def main():
  html_temp = """
  <div style="background-color:white;padding:10px">
  <h2 style="color:black;text-align:center;">Find whether the given number is odd or even</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  num = st.number_input("Enter a number")
  
  if type(num) != 'int':
    st.sucess("Please enter an integer")
    
  else:
  
    if(num % 2 == 0):
      result = 'EVEN'
    else:
      result= 'ODD'

    st.success('The number is {}'.format(result))

if __name__=='__main__':
  main()
