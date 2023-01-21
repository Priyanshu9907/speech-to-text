import speech_recognition as sr
Audio_file=("")  #upload your audio file in wav format inside the inverted commas
r=sr.Recognizer()   #itialise the recogniser

with sr.AudioFile(Audio_file) as source:
    audio=r.record(source)  #reads the audio file

try:
    print("audio file contains: "+ r.recognize_google(audio)) #convert audio to text
except sr.UnknownValueError:
    print("not understand language")
except sr.RequestError:
    print("could not get the result from google")
