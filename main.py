import streamlit as st
import requests

tabs_font_css = """
<style>
div[class*="stTextArea"] label {
  font-size: 26px;
  color: red;
}

div[class*="stTextInput"] label {
  font-size: 26px;
  color: blue;
  border: 5px solid #1C6EA4;
  
div[class*="stContainer"] label {
  border: 5px solid #1C6EA4;
}

}

}
</style>
"""

response = requests.get('https://randomuser.me/api')
st.set_page_config(
    page_title="Multipage App",
    page_icon = "S",
    layout="wide"
)
st.write(tabs_font_css, unsafe_allow_html=True)

st.title("Main Page")

st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""
my_input = st.text_area("Input a text here", st.session_state["my_input"], height = 200)

submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", response.json())

with st.container():
    st.write("THIS IS INSIDE A CONTAINER")