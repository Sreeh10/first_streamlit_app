import streamlit
import pandas
import requests

streamlit.title("My Daily Workout!!")
streamlit.text( "Run atleast 5k")
streamlit.text( "Do some basic gym things...")
streamlit.text( "Be sure to wake up early" )

streamlit.header ("What should I plan Next ? I should Eat some fruits")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits for me:" , list(my_fruit_list.index) , ["Avocado", "Strawberries"] )
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

fruityvice_response = requests.get ( "https://fruityvice.com/api/fruit/watermelon")
streamlit.text ( fruityvice_response)
