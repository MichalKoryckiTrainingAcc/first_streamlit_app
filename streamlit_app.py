import streamlit
streamlit.title('🍞DUM DUM DUM MODMDOMDODMODMOD')
streamlit.header('Breakfast')
streamlit.text('🥣   DSDSDDS')
streamlit.text("🥗sidjsijsdj")
streamlit.text("🐔AEIOU")
streamlit.text("🥑JOHN MADDEN")

import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
