
import edge_tts

voice = "en-US-GuyNeural"  # male voice
rate = "+0%"

async def text_to_speech(text, filename):
    communicate = edge_tts.Communicate(text, voice=voice, rate=rate)
    await communicate.save(filename)
    print(f"Audio saved as {filename}")


