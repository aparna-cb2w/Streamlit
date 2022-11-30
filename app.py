import streamlit as st
import pandas as pd
import numpy as np

def main():
  st.title("Find whether the given number is odd or even")
  html_temp = """
  <div style="background-color:black;padding:10px">
  <h2 style="color:black;text-align:center;">Division of 2 Numbers</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  num = st.number_input("Number")
  
  if(num % 2 == 0):
    result = 'even'
  else:
    result= 'odd'
  
  st.success('The number is {}'.format(result))
  
if __name__=='__main__':
  main()
