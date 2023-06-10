import streamlit as st
import random
import requests

st.set_page_config(page_title='DecisionMaker!', page_icon=':tada:', layout='wide')


st.title('This app is made by a 14 year old, and is my first app')
st.title('This website, will help you solve a dilemma, by choosing one of the options randomly!')

def load_lottieurl(url):
    r = requests.get(url)
    return r.json()

lottie_1 = load_lottieurl('https://assets8.lottiefiles.com/packages/lf20_F04ihok7hO.json')

st.lottie(lottie_1, height = 300)

decison_1 = st.text_input('Enter decision 1')
decison_2 = st.text_input('Enter decision 2')


options = [decison_1, decison_2]
decision = random.choice(options)

Button_1 = st.button('Click me to get result')

if Button_1:
    st.write(decision)



with st.container():
    st.write('---')
    st.header('Get in touch with me!')
    st.write('##')

    contact_form = """<form action="https://formsubmit.co/harikiran.turla@gmail.com" method="POST">
    <input type = "hidden" name= "_captcha" value ="false">
     <input type="text" name="name"placeholder = "Your name" required>
     <input type="email" name="email"Placeholder= "Your Email" required>
     <textarea name ="message" Placeholder="your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

st.write("write your message for me in that box, maybe its for an improvement.")
