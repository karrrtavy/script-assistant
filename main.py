
from voice_engine.silero_tts import TTS
from voice_treat.recognize_voice import recognize_voice
from tasks.YM import greeting, play_music

def main():
    tts = TTS()
    # tts.text2speech("привет")

    while True:
        query = recognize_voice(d_id=1)
        print('Твой запрос:', query)

        if query == "привет":
            tts.text2speech(text=greeting())
        elif query == "включи музыку":
            tts.text2speech(text=play_music())
            play_music()

if __name__ == "__main__":
    main()