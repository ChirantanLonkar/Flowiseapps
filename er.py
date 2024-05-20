import streamlit as st
import requests

# Define the API URL
API_URL = "http://localhost:3000/api/v1/prediction/e3bb7e17-f383-4e7c-8c77-802bd31e8029"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

# Streamlit UI
st.title("Flowise Chatbot")

question = st.text_input("Ask a question:")

if st.button("Submit"):
    if question:
        output = query({"question": question})
        
        # Parse and display the output in a readable format
        if "text" in output:
            st.write("### Response")
            st.write(output["text"])
            
            st.write("### Details")
            st.write(f"- **Question**: {output.get('question', 'N/A')}")
            st.write(f"- **Chat ID**: {output.get('chatId', 'N/A')}")
            st.write(f"- **Chat Message ID**: {output.get('chatMessageId', 'N/A')}")
            st.write(f"- **Session ID**: {output.get('sessionId', 'N/A')}")
        else:
            st.write("No valid response received.")
    else:
        st.write("Please enter a question.")
