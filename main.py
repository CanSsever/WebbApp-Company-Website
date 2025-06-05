import streamlit as st
import pandas


st.set_page_config(layout="wide")

st.header("The Best Company")

st.write("""
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed sit amet sem vitae lacus vulputate suscipit. Nullam euismod, urna in commodo feugiat, 
arcu augue fermentum nulla, in luctus justo enim ut odio. 
Curabitur at elit id sapien tincidunt luctus. Vivamus a facilisis mauris. Suspendisse potenti. 
In hac habitasse platea dictumst. Aenean convallis sapien vitae magna fermentum, 
ut malesuada orci cursus.
""")

st.subheader("Our Team")
df = pandas.read_csv("data (1).csv", sep=",")

col1, col2, col3 = st.columns([5.0, 5.0, 5.0])

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("imagescompany/" + row["image"])


with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("imagescompany/" + row["image"])


with col3:
    for index, row in df[8:12].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("imagescompany/" + row["image"])

