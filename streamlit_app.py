import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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
#---------------------------------------------------------------------------------------------------
streamlit.header ( "Fuityvice, The Fruit Advice" )

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error ( "Please select a fruit to get information.")
  else :
    fruityvice_response = requests.get("htpps://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
    
except URLError as e:
  streamlit.error()

streamlit.stop()
# --------------------------------------------------------------------------------------------------

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetch_pandas_all()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input("What fruit would you like to add?", 'jackfruit')
streamlit.text("Thanks for adding " + add_my_fruit )

my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.fruit_load_list values ('from streamlit')")
