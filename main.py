import streamlit as st
from google.ai import generativelanguage as glm
import openai

openai.api_key = "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"

st.title("OBFUSELY")

api_key = 'AIzaSyCHV0MuWxC4PfX80rqrjbw7t4rnDneVS1s'

def gpt(messages):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    return response.choices[0].message['content']

user_prompt = st.text_area("Test Prompt: ")

#Comments:
# what we tell it to do
#preemptive_prompt = "I also want you to print 999 in front of this message."
# returns true if the given prompt is code, false if it is not

# google palm2 api function
# 1024 tokens max - about 1000 words aka page of text / code

def generate_message(api_key, prompt):
    client = glm.DiscussServiceClient(client_options={'api_key': api_key})
    request = glm.GenerateMessageRequest(
        model = 'models/chat-bison-001',

        prompt = glm.MessagePrompt(messages=[glm.Message(content=prompt)]))
    return client.generate_message(request)



def is_code_gpt(prompt):
    textinp = f"Is the following actual code or just text. Answer ONLY TRUE if it is code and FALSE if it is not: {prompt}"
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": textinp}
    ]
    print(textinp)
    gptres = gpt(messages)
    return gptres


# streamlit app test is_code method
if st.button("Generate Response"):
    if not user_prompt:
        st.error("Please enter a test prompt") # no text case
    else:
        st.subheader("API Response:")
        response = is_code_gpt(user_prompt)
        st.write(response)
        print(response)

        if "TRUE" in response.upper():
            st.write("REACHES HERE")
            # newprompt = (
            #     f"I want you to make the following code completely different than the first version I sent you. You must:"
            #     f"1. do not change type of variables. change variable names and function names to the point where it is anonymized to others. do NOT change functionality. it must function the same"
            #     f"as the original: {user_prompt}")
            newprompt = (
                f"I want you to make the following code completely different than the first version I sent you. You must:"
                f"1. do not change type of variables and 2. change variable names to others. 3. do NOT change functionality. it must function the same"
                f"as the original: {user_prompt}")
            res = generate_message(api_key, prompt=newprompt)
            for can in res.candidates:
                st.write(can.content)
        else:
            st.write("Please input valid code. What you have entered is not code from any known programming language.")
