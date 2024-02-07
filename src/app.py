#pip install streamlit langchain langchain-openai


import streamlit as st

def get_response(user_input):
  return "I don't know"

#app config
st.set_page_config(page_title="Chat With Websites", page_icon="🤖👩‍💻")
st.title("Chat with websites")
chat_history = [
  AIMessage(content="Hello, I am chatbot! How can I help you?"),
]

#sidebar
with st.sidebar:
  st.header("Settings")
  website_url = st.text_input("Website URL")

#user_input
user_query = st.chat_input("Type your message here...")
if user_query is not None and user_query != "":
  response = get_response(user_query)
  with st.chat_message("Human"):
    st.write(user_query)

  with st.chat_message("AI"):
    st.write(response)

  


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