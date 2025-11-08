import streamlit as st
import asyncio
import os
from llm_response import get_response
from male_voice import text_to_speech

st.set_page_config(page_title="Ajoy Prasad Bot", layout="centered")
st.title("Bot on behalf of Ajoy Prasad")

tab_text, tab_voice = st.tabs(["Type Your Question", "Voice Input (Coming Soon)"])

with tab_text:
    user_input = st.text_input(
        "Type your question and press Enter:",
        placeholder="Ask Ajoy anything...",
        key="text_input",
        label_visibility="collapsed"
    )

    if user_input:
        with st.spinner("Ajoy is thinking..."):
            try:
                response = asyncio.run(get_response(user_input))
                audio_file = "response.wav"
                asyncio.run(text_to_speech(response, audio_file))

                if os.path.exists(audio_file):
                    st.audio(audio_file, format="audio/wav", autoplay=True)
                else:
                    st.warning("Audio file not generated.")

                st.markdown("### **Ajoy's Answer:**")
                st.write(response)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.info("Please try again with a different question.")

with tab_voice:
    st.info("Voice input feature coming soon!")
    st.write("You'll be able to speak your question directly to Ajoy.")