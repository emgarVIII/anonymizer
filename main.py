import streamlit as st
from google.ai import generativelanguage as glm

st.title("OBFUSELY")

api_key = 'AIzaSyCHV0MuWxC4PfX80rqrjbw7t4rnDneVS1s'
user_prompt = st.text_area("Test Prompt: ")
# what we tell it to do
#preemptive_prompt = "I also want you to print 999 in front of this message."
# returns true if the given prompt is code, false if it is not

def is_code(api_key, prompt):
    cur_prompt = ("I will give you the following text snippet. I want you to explicitally answer \"true\" or \"false\" Answer"
                  "true if is from a coding language you recognize, and answer false if it is not.")

    prompt = cur_prompt + prompt
    client = glm.DiscussServiceClient(client_options={'api_key': api_key})
    request = glm.GenerateMessageRequest(
        model='models/chat-bison-001',

        prompt=glm.MessagePrompt(messages=[glm.Message(content=prompt)]))
    # it is a valid block of code
    # if client.generate_message(request) == "true":
    #     return client.generate_message(request)

    return client.generate_message(request) # not a valid block of code

preemptive_prompt = ("tell me a joke")
final_prompt = preemptive_prompt + user_prompt
# google palm2 api function
# 1024 tokens max - about 1000 words aka page of text / code

def generate_message(api_key, prompt):
    client = glm.DiscussServiceClient(client_options={'api_key': api_key})
    request = glm.GenerateMessageRequest(
        model = 'models/chat-bison-001',

        prompt = glm.MessagePrompt(messages=[glm.Message(content=prompt)]))
    return client.generate_message(request)




# # streamlit app
# if st.button("Generate Response"):
#     if not final_prompt:
#         st.error("Please enter a test prompt") # no text case
#     else:
#         response = generate_message(api_key, final_prompt)
#         st.subheader("API Response:")
#         for candidate in response.candidates:
#             st.write(candidate.content)
#             st.write("----")

# streamlit app test is_code method
if st.button("Generate Response"):
    if not user_prompt:
        st.error("Please enter a test prompt") # no text case
    else:
        response = is_code(api_key, user_prompt)
        st.subheader("API Response:")
        s = []
        for candidate in response.candidates:

            stripped = candidate.content.lower().split()
            for word in stripped:
                s.append(word)
        print(s)
        st.write(s)
        if "true" in s or "true." in s:
                st.write('It knows its true')
                newprompt = f"Anonymize the following code: {user_prompt}"
                res = generate_message(api_key, prompt=newprompt)
                for can in res.candidates:
                    st.write(can.content)
        else:
            st.write("NO. there is no code")

