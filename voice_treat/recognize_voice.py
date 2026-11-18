
import speech_recognition

# устройство ввода
# device_id - идентификатор устройства ввода
def setup_input_device(d_id: int):
    return speech_recognition.Microphone(device_index=d_id)

# обработка голоса
def recognize_voice(*args: tuple, d_id: int):
    microphone = setup_input_device(d_id)
    recognizer = speech_recognition.Recognizer()
    recognizer.pause_threshold = 1

    with microphone:
        recognized_data = ""
        recognizer.adjust_for_ambient_noise(microphone, duration=0.5)

        try:
            print('Слушаю...')
            audio = recognizer.listen(microphone)
        except speech_recognition.WaitTimeoutError:
            return

        try:
            print('Обрабатываю...')
            recognized_data = recognizer.recognize_google(audio, language='ru').lower()
        except speech_recognition.UnknownValueError:
            pass

    return recognized_data        