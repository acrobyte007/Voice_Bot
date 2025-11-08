import streamlit as st
import asyncio
from llm_response import get_response
from male_voice import text_to_speech

st.title("🎙️ AI Interview Voice Bot")

user_input = st.text_input("Ask your question to Ajoy:")

async def main(user_input):
    response = await get_response(user_input)
    await text_to_speech(response, "response.wav")
    return response

if user_input:
    with st.spinner("Thinking..."):
        response = asyncio.run(main(user_input))
    st.audio("response.wav", format="audio/wav")
    st.success("Ajoy has answered your question!")
