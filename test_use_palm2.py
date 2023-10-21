import streamlit as st
from google.ai import generativelanguage as glm

st.title("OBFUSELY")

api_key = 'AIzaSyCHV0MuWxC4PfX80rqrjbw7t4rnDneVS1s'
message_prompt = st.text_area("Test Prompt:")

# google palm2 api function

def generate_message(api_key, prompt):
    client = glm.DiscussServiceClient(client_options={'api_key': api_key})
    request = glm.GenerateMessageRequest(
        model = 'models/chat-bison-001',
        prompt = glm.MessagePrompt(messages=[glm.Message(content=prompt)]))
    return client.generate_message(request)


# streamlit app
if st.button("Generate Response"):
    if not message_prompt:
        st.error("Please enter a test prompt")
    else:
        response = generate_message(api_key, message_prompt)
        st.subheader("API Response:")
        for candidate in response.candidates:
            st.write(candidate.content)
            st.write("----")

