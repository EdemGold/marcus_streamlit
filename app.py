import streamlit as st
import google.generativeai as genai
import textwrap

# Configure Google's generative AI
genai.configure(api_key='AIzaSyBvQsBVbiJEkv8mwk1-p9FzTpjm6h7IA7c')  # Replace with your actual API key

class GeminiChat:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])

    def get_response(self, user_message):
        response = self.chat.send_message(user_message)
        formatted_response = self.to_markdown(response.text)
        return formatted_response

    def to_markdown(self, text):
        text = text.replace('•', '  *')
        return textwrap.indent(text, '> ', predicate=lambda _: True)

def main():
    st.title("Gemini Chat Bot")

    user_input = st.text_input("Type your message:")
    gemini_chat = st.session_state.get("gemini_chat", None)

    if gemini_chat is None:
        gemini_chat = GeminiChat()
        st.session_state.gemini_chat = gemini_chat

    if st.button("Send"):
        # Get response from Gemini API
        bot_response = gemini_chat.get_response(user_input)

        # Display the response
        st.markdown(f"User: {user_input}")
        st.markdown(f"Bot: {bot_response}")

if __name__ == "__main__":
    main()
