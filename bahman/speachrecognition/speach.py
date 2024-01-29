import speech_recognition as sr

r = sr.Recognizer()

try:
    with sr.Microphone() as source:
        audio = r.listen(source)
        query = r.recognize_google(audio, language='fa-IR')
        with open('input.txt', 'a') as f:
            f.write(query)
            print('success')
except sr.UnknownValueError:
    print('Error: could not understand audio')