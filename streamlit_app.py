import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Pick list
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

if (len(fruits_selected) != 0):
    fruits_to_show = my_fruit_list.loc[fruits_selected]
else:
    fruits_to_show = my_fruit_list
# Display the table on the page
streamlit.dataframe(fruits_to_show)