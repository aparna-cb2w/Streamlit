import streamlit as st
import pandas as pd
import numpy as np

def main():
  st.title("Find whether the given number is odd or even")
  num = st.number_input("Enter a integer")
  
  if(num % 2 == 0):
    result = 'even'
  else:
    result= 'odd'
  
  st.success('The number is {}'.format(result))
  
if __name__=='__main__':
  main()
