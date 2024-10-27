import streamlit as st
import google.generativeai as gen_ai
GOOGLE_API_KEY = "AIzaSyDNbLonDcxyJjvmKMQOmmU2_GyeH50hTG0"
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-1.5-flash')
text = st.text_input("Give your prompt")
st.write(model.generate_content(text).text)
