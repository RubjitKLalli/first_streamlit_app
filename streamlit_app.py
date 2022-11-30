import streamlit
import pandas

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal 🥣')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie 🥗')
streamlit.text('🐔 Hard-Boiled Free-Range Egg 🐔')
streamlit.text('🥑🍞 Avocado Toast 🥑🍞')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd

mfl = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

mfl = mfl.set_index('Fruit')

fs = streamlit.multiselect("Pick some fruits:", list(mfl.index),['Strawberries','Avocado'])
fts = mfl.loc[fs]
streamlit.dataframe(fts) 

streamlit.header("Fruityvice Fruit Advice!")

import requests

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi") 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json()) 
streamlit.dataframe(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice) 

