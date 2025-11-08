import streamlit as st
import asyncio
from llm_response import get_response
from male_voice import text_to_speech
from audio_text import transcribe_audio

st.title("Bot on behalf of Ajoy Prasad")


tab_text, tab_voice = st.tabs(["Type Your Question", "Speak Your Question"])


with tab_text:
    user_input = st.text_input(
        "Type your question and press Enter:",
        placeholder="Ask Ajoy anything...",
        key="text_input"
    )

    if user_input:
        with st.spinner("Ajoy is thinking..."):
            response = asyncio.run(get_response(user_input))
            asyncio.run(text_to_speech(response, "response.wav"))

        st.audio("response.wav", format="audio/wav", autoplay=True)
        st.markdown("**Ajoy's Answer:**")
        st.write(response)


with tab_voice:
    if st.button("Speak Now", type="primary", use_container_width=True):
        with st.spinner("Recording..."):
            audio_bytes = st.experimental_audio_input(
                "Speak your question... (click when done)",
                key="voice_input"
            )

        if audio_bytes:
            audio_file = "user_question.wav"
            with open(audio_file, "wb") as f:
                f.write(audio_bytes)

            with st.spinner("Ajoy is listening and answering..."):
                response_text, response_audio_path = asyncio.run(
                    transcribe_audio(audio_file)
                )

            if response_text and response_audio_path:
                st.audio(response_audio_path, format="audio/wav", autoplay=True)
                st.markdown("**Ajoy's Answer:**")
                st.write(response_text)
            else:
                st.error("Couldn't process your voice. Try again.")