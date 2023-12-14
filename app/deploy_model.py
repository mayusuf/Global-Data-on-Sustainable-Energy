###############################
# This program lets you       #
# - Create a dashboard        #
# - Evevry dashboard page is  #
# created in a separate file  #
###############################

# Python libraries
import streamlit as st
from PIL import Image

# User module files
from ml import ml
from eda import eda

def main():

    #############
    # Main page #
    #############

    options = ['Home','Prediction','Stop']
    choice = st.sidebar.selectbox("Menu",options, key = '1')

    if ( choice == 'Home' ):
      st.title("Welcome to the Global Data on Sustainable Energy (2000-2020) Pridiction App!!")
      st.image('./images/access_elect_2020.png')
      pass

    # elif ( choice == 'EDA' ):
    #   eda()
    #   pass

    elif ( choice == 'Prediction' ):
      ml()

    else:
      st.stop()


main()
