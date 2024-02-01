import speech_recognition as sr

r = sr.Recognizer()

try:
    with sr.Microphone() as source:
        audio = r.listen(source)
        query = r.recognize_google(audio, language='en')
        # language => en or fa-IR
        with open('input.txt', 'a') as f:
            f.write(query)
            print('success')
except sr.UnknownValueError:
    print('Error: could not understand audio')


# Compare two files txt in Python
import filecmp

f1 = "output.txt"
f2 = "output.txt"

# shallow comparison
result = filecmp.cmp(f1, f2)
print(result)
# deep comparison
result = filecmp.cmp(f1, f2, shallow=False)
print(result)
