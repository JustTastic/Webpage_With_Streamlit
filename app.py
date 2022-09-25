from threading import local
from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":snowflake:", layout="wide")

def load_lottie(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

# local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")

# --- load animations
animation_lottie = load_lottie("https://assets3.lottiefiles.com/packages/lf20_igvitqdp.json")
first_image = Image.open("images/god_of_war_kratos.jpg")
# --- header section ---
with st.container():
    st.subheader("Hello, My name is Abdirahman :wave:")
    st.title("A computer science student in Somalia")
    st.write("I am python programmer or hoping to be and i have a passion for python and automations.")
    st.write("[Learn More on: >](https://www.youtube.com/c/CodingIsFun)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My Info")
        st.write("##")
        st.write("""
            I am computer science student how started his journey of learning coding resently,
            and i have found a great sense of liking to python and its automations.
            I hope that one day i can proundly say i have mastered python and do what i think its appropriately.
            This have been my story..""")
        st.write("For projects i have done [Click here: >](https://github.com/JustTastic)")
    
    with right_column:
        st_lottie(animation_lottie, height=300, key="student")



with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(first_image)
    with text_column:
        st.subheader("Track people from a phone number AnyWhere, Python Script")
        st.write("""
        Creating python script to tack any phone number anywhere from just i click of a button.
        Step by step, full code well written as much as possible, have look and try creating whatever fun ideas
        you have with python scripts.""")
        st.write("The Complete Code [Phone Tracker Python Script > ](https://github.com/JustTastic/Phone-Tracker)")
        st.markdown("For Orignal Source [Watch this video >](https://www.youtube.com/watch?v=Dz3rSZHnKkM&t=708s)")


with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    # ---contact form ---
    contact_form = """
        <form action="https://formsubmit.co/practice4learning.only@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="massage" placeholder="Your Massage Here " required></textarea>
            <button type="submit">Send</button>
        </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()