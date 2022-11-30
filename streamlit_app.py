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

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi") 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json()) 
streamlit.dataframe(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice) 

import snowflake.connector

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.header("Hello from Snowflake:")
streamlit.dataframe(my_data_row)

my_cur.execute("select * from fruitloadlist")
my_data_rows = my_cur.fetchall()
streamlit.header("the fruit load list contains:")
streamlit.dataframe(my_data_rows)

add_my_Fruit = str(streamlit.text_input('What fruit would you like to add?'))
my_data_rows.loc[:, add_my_Fruit] = 'test values'



