import streamlit as st

# Set tile 
st.title("Our First Streamlit App")

from PIL import Image 

st.subheader('Total Data Science')

image = Image.open("DataScience.jpg")
st.image(image,use_column_width=True)

st.write("This is Binu Thomas The King of Datascience")

st.markdown("This is Binu Thomas The king of Machine Learning")

st.success("Congrats You have run first App")

st.info("This is an information for you")

st.warning("Be cautious")

#st.error("Oops you run into an error, you needed to rerun the app")

