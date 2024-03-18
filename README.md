# gemini_api
A repository containing a simple gemini api streamlit application.
The vision model is deployed here : https://visionapi.streamlit.app/
## chat_api.py is a chatbot with history and a simple interface
## vision_api.py is a using "gemini-pro-vision' to learn about the image you upload

## to run the code locally 
--first install the requirements
```bash
pip install -r requirements.txt
```
--then run the streamlit app
```bash
streamlit run chat_api.py --server.enableXsrfProtection false
```
or for the vision model :
```bash
streamlit run vision_api.py --server.enableXsrfProtection false
```
## Getting a Gemini API Key
To get a Gemini API key, follow these steps:
https://aistudio.google.com/app/apikey
![Image Description](image.png)

## Setting up the Gemini API Key
change your API key f dak .env file

Note : the same API key is used in both vision_api and chat_api

