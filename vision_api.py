import google.generativeai as genai
from PIL import Image
import streamlit as st
from dotenv import load_dotenv
import os
from time import sleep

# Load GOOGLE_API_KEY from .env file
load_dotenv()
# Configure Streamlit page settings
st.set_page_config(
    page_title="Chatbot with Gemini-Pro!",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)


# Set up Google Gemini-Pro AI model gemini-pro for chat and gemini-pro-vision for vision
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro-vision')

# to ADD Chat History Uncomment this
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


# Display the chatbot's title on the page
st.title("🤖 Gemini Pro VISION")

# Input field for user's message
user_prompt = st.chat_input("Ask Gemini-Pro-Vision about the image ...")
# create file uploader button at the left of the send button of the chat input
img = st.file_uploader("Upload an image for the model to generate content from: ", type=["jpg", "png", "jpeg"])

if user_prompt or img:
    # Display Image
    image =Image.open(img)
    with st.chat_message("user"):
        st.image(image, use_column_width=True)
    for message in st.session_state.chat_session.history:
        with st.chat_message(message[1]):
            st.markdown(message[0])
    # Add user's message to chat and display it
    if user_prompt:
        st.chat_message("user").markdown(user_prompt)

        st.session_state.chat_session.history.append([user_prompt, "User"])
        with st.spinner('knfeker a sa7pe...'):
            gemini_response = model.generate_content([user_prompt, image])
    else:
        with st.spinner('knfeker a sa7pe...'):
            gemini_response = model.generate_content(["What's in this picture?", image])
    #display the response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
    st.session_state.chat_session.history.append([gemini_response.text, "Assistant"])