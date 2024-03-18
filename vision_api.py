import google.generativeai as genai
from PIL import Image
import streamlit as st
from dotenv import load_dotenv
import os

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


# Function to give gemini a name in the UI
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


# to ADD Chat History Uncomment this
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


# Display the chatbot's title on the page
st.title("🤖 Gemini Pro VISION")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        if message.parts[0].content_type == "text":
            st.markdown(message.parts[0].text)
        elif message.parts[0].content_type == "image":
            st.image(message.parts[0].image, use_column_width=True)
# Input field for user's message
user_prompt = st.chat_input("Ask Gemini-Pro-Vision about the image ...")
# create file uploader button at the left of the send button of the chat input
img = st.file_uploader("Upload an image for the model to generate content from: ", type=["jpg", "png", "jpeg"])


if img is not None:
    image =Image.open(img)
    gemini_response = model.generate_content(["What's in this picture?", image])
    with st.chat_message("user"):
        st.image(image, use_column_width=True)
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)

if user_prompt and img:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)
    
    # Send user's message to Gemini-Pro and get the response
    gemini_response = model.generate_content([user_prompt, image])


    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)