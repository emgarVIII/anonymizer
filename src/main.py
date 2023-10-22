import streamlit as st
from google.ai import generativelanguage as glm
import openai
import re
openai.api_key = ""
custom_css = """
<style>
.stApp{
background-color: #B2BEB5 !important;
}

.custom-title{
color: #242124;
font-size: 50px;
text-align: center;
font-weight: bold;
margin-top: -70px;
}

</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

st.markdown('<p class="custom-title">Anonymizer</p>', unsafe_allow_html=True)


st.selectbox('Select Language', ['Python','Java','C#','C++','C','Javascript'])
# chat GPT powered validation
def gpt(messages):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    return response.choices[0].message['content']

user_prompt = st.text_area("Test Prompt: ", height=300)

# google palm2 api function
def generate_message(api_key, prompt):
    client = glm.DiscussServiceClient(client_options={'api_key': api_key})
    request = glm.GenerateMessageRequest(
        model = 'models/chat-bison-001',

        prompt = glm.MessagePrompt(messages=[glm.Message(content=prompt)]))
    return client.generate_message(request)

# checks if it is code or not. returns true or false accordingly
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
        if "TRUE" in response.upper():
            newprompt = (
                f"I want you to make the following code completely different than the first version I sent you. You must:"
                f"1. do not change type of variables and 2. change variable names to others. 3. do NOT change functionality. it must function the same"
                f"as the original: {user_prompt}")
            res = generate_message(api_key, prompt=newprompt)
            output = ''
            for can in res.candidates:
                code_matches = re.findall(r'```python\n(.*?)```', can.content, re.DOTALL)
                if code_matches:
                    extracted_code = "```python\n" + code_matches[0] + "```"
                    st.write(extracted_code)
                    print(extracted_code)
                else:
                    print("No code found within triple backticks.")
        else:
            st.write("Please input code Only. What you have entered is not code from any known programming language.")
