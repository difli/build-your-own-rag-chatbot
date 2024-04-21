import streamlit as st

# TODO #1:
# 1. Copy and paste the necessary code from the langflow Python API tab.
#    Exclude the last two lines of the provided code; these will be used elsewhere.
# 2. Ensure the 'TWEAKS' dictionary is fully configured with all required customizations
#    specific to your flow needs.
# Example:
# import requests
# from typing import Optional
#
# BASE_API_URL = "http://127.0.0.1:7861/api/v1/run"
# FLOW_ID = "6e1a0080-46ee-4746-bb85-cea248f54bc0"
# # You can tweak the flow by adding a tweaks dictionary
# # e.g {"OpenAI-XXXXX": {"model_name": "gpt-4"}}
# TWEAKS = {
#     "Prompt-svuPA": {"template": """Answer the user as if you were a funny generative AI geek.
#   User: {user_input}
#
#   Answer: """},
#     "OpenAIModel-RhxsO": {"openai_api_key": st.secrets['OPENAI_API_KEY']},
#     "ChatOutput-wHG84": {},
#     "ChatInput-jLIhU": {}
# }
#
# def run_flow(message: str,
#   flow_id: str,
#   output_type: str = "chat",
#   input_type: str = "chat",
#   tweaks: Optional[dict] = None,
#   api_key: Optional[str] = None) -> dict:
#     """
#     Run a flow with a given message and optional tweaks.
#
#     :param message: The message to send to the flow
#     :param flow_id: The ID of the flow to run
#     :param tweaks: Optional tweaks to customize the flow
#     :return: The JSON response from the flow
#     """
#     api_url = f"{BASE_API_URL}/{flow_id}"
#
#     payload = {
#         "input_value": message,
#         "output_type": output_type,
#         "input_type": input_type,
#     }
#     headers = None
#     if tweaks:
#         payload["tweaks"] = tweaks
#     if api_key:
#         headers = {"x-api-key": api_key}
#     response = requests.post(api_url, json=payload, headers=headers)
#     return response.json()
#

# Start with empty messages, stored in session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Draw a title and some markdown
st.title("Your personal Efficiency Booster")
st.markdown("""Generative AI is considered to bring the next Industrial Revolution.  
Why? Studies show a **37% efficiency boost** in day to day work activities!""")

# Draw all messages, both user and bot so far (every time the app reruns)
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

# Draw the chat input box
if question := st.chat_input("What's up?"):
    # Store the user's question in a session object for redrawing next time
    st.session_state.messages.append({"role": "human", "content": question})

    # Draw the user's question
    with st.chat_message('human'):
        st.markdown(question)

# TODO #2:
# 1. Invoke the run_flow function using the provided question, flow_id, and tweaks.
# 2. Capture and process the output to extract the desired result.
# Example:
#     output = run_flow(message=question, flow_id=FLOW_ID, tweaks=TWEAKS)
#     answer = output['outputs'][0]['outputs'][0]['results']['result']

    # REPLACE THE FOLLOWING LINE
    answer = "You asked: " + question

    # Store the bot's answer in a session object for redrawing next time
    st.session_state.messages.append({"role": "ai", "content": answer})

    # Draw the bot's answer
    with st.chat_message('assistant'):
        st.markdown(answer)