import streamlit

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
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# write your own comment -what does the next line do? 
fruityvice_normalized = json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
