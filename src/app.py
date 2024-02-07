#pip install streamlit langchain langchain-openai

#app config
import streamlit as st
st.set_page_config(page_title="Chat With Websites", page_icon="🤖👩‍💻")
st.title("Chat with websites")

#sidebar
with st.sidebar:
  st.header("Settings")
  website_url = st.text_input("Website URL")

# if website_url is None or website_url == "":
#   st.info("Please enter a website URL")

# else:
#   #session state
#   if "chat_history" not in st.session_state:
#     st.session_state.chat_history = [
#       AIMessage(content="Hello , I am a BOT. How can I help you?"),
#     ]
#   if "vector_store" not in st.session_state:
#     st.session_state.vector_store = get_vectorstore_from_url(website_url)
  print('chat_input' in dir(st))
  #st.chat_input("Please Type your input here.....")