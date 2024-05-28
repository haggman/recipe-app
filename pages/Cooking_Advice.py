import streamlit as st
#
# Add the code you copied from your notebook below this message
#
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, Tool
import vertexai.preview.generative_models as generative_models

project_id = "YOUR_PROJECT_ID"

def start_chat_session():
  vertexai.init(project=project_id, location="us-central1")
  tools = [
      Tool.from_retrieval(
          retrieval=generative_models.grounding.Retrieval(
              source=generative_models.grounding.VertexAISearch(datastore="projects/"+project_id+"/locations/global/collections/default_collection/dataStores/old-cookbooks-id"),
              disable_attribution=False,
          )
      ),
  ]
  model = GenerativeModel(
    "gemini-1.0-pro-002",
    tools=tools,
    generation_config=generation_config,
    safety_settings=safety_settings,
  )
  chat = model.start_chat()
  return chat


generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 1,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

chat = start_chat_session()


#
# Here's the code to setup your session variables
# Uncomment this block when instructed
#

if "chat" not in st.session_state:
  st.session_state.chat = start_chat_session()
else:
  chat = st.session_state.chat

if "history" not in st.session_state:
  st.session_state.history = st.session_state.chat.history

# Setup done, let's build the page UI

st.set_page_config(page_title="AI Recipe Haven - AI Cooking Advisor", page_icon="🍲")
st.title("Your AI Cooking Advisor")

#
# Here's the code to create the chat interface
# Uncomment this block when instructed
# 

for message in st.session_state.history:
    with st.chat_message(message.role):
        st.markdown(message.parts[0].text)

if prompt := st.chat_input("How can I help you today?"):

    with st.chat_message("user"):
        st.markdown(prompt)
    
    response = chat.send_message(prompt)

    with st.chat_message("assistant"):
        st.markdown(response.candidates[0].content.parts[0].text)