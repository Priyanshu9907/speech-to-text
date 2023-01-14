import speech_recognition as sr
Audio_file=("voice.wav")
r=sr.Recognizer()
with sr.AudioFile(Audio_file) as source:
    audio=r.record(source)

try:
    print("audio file contains: "+r.recognize_google(audio))
except sr.UnknownValueError:
    print("not understand language")
except sr.RequestError:
    print("could not get the result from google")
