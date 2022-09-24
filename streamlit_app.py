import streamlit
streamlit.title('🍞DUM DUM DUM MODMDOMDODMODMOD')
streamlit.header('Breakfast')
streamlit.text('🥣   DSDSDDS')
streamlit.text("🥗sidjsijsdj")
streamlit.text("🐔AEIOU")
streamlit.text("🥑JOHN MADDEN")

import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ["Avocado", "Strawberries"])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
