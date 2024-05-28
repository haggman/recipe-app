import streamlit as st
#
# Add the code you copied from your notebook below this message
#

#
# Here's the code to setup your session variables
# Uncomment this block when instructed
#

# if "chat" not in st.session_state:
#   st.session_state.chat = start_chat_session()
# else:
#   chat = st.session_state.chat

# if "history" not in st.session_state:
#   st.session_state.history = st.session_state.chat.history



# Setup done, let's build the page UI
st.set_page_config(page_title="AI Recipe Haven - AI Cooking Advisor", page_icon="🍲")
st.title("Your AI Cooking Advisor")

#
# Here's the code to create the chat interface
# Uncomment this block when instructed
# 


# for message in st.session_state.history:
#     with st.chat_message(message.role):
#         st.markdown(message.parts[0].text)

# if prompt := st.chat_input("How can I help you today?"):

#     with st.chat_message("user"):
#         st.markdown(prompt)
    
#     response = chat.send_message(prompt)

#     with st.chat_message("assistant"):
#         st.markdown(response.candidates[0].content.parts[0].text)