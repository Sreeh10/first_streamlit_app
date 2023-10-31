import streamlit
import pandas

streamlit.title("My Daily Workout!!")
streamlit.text( "Run atleast 5k")
streamlit.text( "Do some basic gym things...")
streamlit.text( "Be sure to wake up early" )

streamlit.header ("What should I plan Next ? I should Eat some fruits")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("Pick some fruits for me:" , list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
